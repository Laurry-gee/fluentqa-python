import json
import time

from functools import partial
import random
from typing import List, Dict, Any

import httpx
from pydantic.main import BaseModel


class HttpRequestSpec(BaseModel):
    url: str = None
    method: str = None
    headers: str | Dict = None
    body: Any = None
    files: Any = None


def new_request_id() -> str:
    plain = "".join(
        random.choices("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz", k=16)
    )
    timestamp_ms = int(round(time.time()))
    return f"{plain}.{timestamp_ms}"


def get_http_caller(method: str):
    return getattr(httpx, method.lower())


import requests


class HttpProcessor:

    def invoke(self, req: HttpRequestSpec):
        caller = get_http_caller(req.method)
        if isinstance(req.headers, str):
            req.headers = json.loads(req.headers)
            req.headers.pop("content-length")
            req.headers["cookie"] = req.headers['cookie'].replace(",", ";")

        http_partial_func = partial(caller, url=req.url, headers=req.headers)
        if req.method.upper() in ["GET", "DELETE"]:
            response = http_partial_func()
        elif req.files:
            response = http_partial_func(data=req.body, files=req.files)
        else:
            if isinstance(req.body, dict):
                req.body = json.dumps(req.body)
            response = http_partial_func(data=req.body)
        return response
