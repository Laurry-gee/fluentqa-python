#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
covert yaml to object or object to yaml string or file
"""
from typing import Any
from typing import Dict
from typing import Union

from pydantic.config import Extra
from pydantic_yaml import YamlModel


class YamlGenericModel(YamlModel, extra=Extra.allow):

    def to_yaml_file(self, file_path: str):
        to_yaml_file(file_path, self.dict(by_alias=True))


def load_yaml(file_path: str) -> Any:
    return YamlGenericModel.parse_file(file_path).dict()


def load_yaml_to_object(model: type[YamlGenericModel], file_path: str):
    return model.parse_file(file_path)


def to_yaml_file(file_path: str, data: Union[YamlGenericModel, Dict]):
    if isinstance(data, YamlGenericModel):
        yaml_str = data.yaml()
    else:
        yaml_str = YamlGenericModel.parse_obj(data).yaml()
    with open(file_path, "w") as f:
        f.write(yaml_str)
