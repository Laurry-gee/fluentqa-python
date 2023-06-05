import functools
import inspect
from typing import Callable, List

from pydantic.main import BaseModel

print(spell_model.json())
s = MatrixService()

t = inspect.signature(s.get_unit)
print(t)
# print(t.parameters['x'])
# print(t.parameters['y'].annotation)
print(s.get_unit.__code__.co_varnames)

service_caller = getattr(s, "get_unit")
print(service_caller)


class SpellModel(BaseModel):
    name: str
    caller: str
    args: List[str]


class RequestDemo(BaseModel):
    x: str
    y: SpellModel


class MatrixService:
    def get_unit(self, x: str, y: SpellModel):
        pass


spell_model = SpellModel(name="name", caller=12, args=[])
request_demo = RequestDemo(x="x", y=spell_model)

url_path = "matrixService/get_unit"


def dynamic_call_func(func, http_json_model):
    t = inspect.signature(func)
    args = []
    for item in t.parameters.items():
        args.append(getattr(http_json_model, item[0]))
    func(*args)


def call_service_method(url_path, request_data):
    service, method = url_path.split("/")
    print(service, method)
    if service == "matrixService":  ## 此处只是进行演示,可以通过module import获取所有的service
        s = MatrixService()
    func = getattr(s, method)  # 获取调用参数
    dynamic_call_func(func, request_data)


call_service_method(url_path, request_demo)
