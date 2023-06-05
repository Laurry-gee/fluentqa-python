import abc
from typing import Any


class SpellService(metaclass=abc.ABCMeta):
    pass


class HttpInvokerService(SpellService):

    def invoke(self, request: Any):
        print("http invoke service")


class DatabaseInvokerService(SpellService):

    def invoke(self, request: Any):
        print("database invoke service")
