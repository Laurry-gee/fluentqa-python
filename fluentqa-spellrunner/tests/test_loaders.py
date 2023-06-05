import importlib
import inspect
from pathlib import Path

from engines import HttpInvokerService
from spell import utils


class TestLoaders:

    def test_to_package_format(self):
        result = utils.to_package_format(Path("spell/utils"))
        print(result)

    def test_load_services(self):
        service_module = importlib.import_module("engines")
        print(inspect.ismodule(service_module))
        print(service_module)
        #
        # utils.discover(Path("service"),"spell")

        invocable_service = []
        for member in dir(service_module):
            member_instance = getattr(service_module, member)
            if isinstance(member_instance, type):
                if not inspect.isabstract(member_instance):
                    invocable_service.append(member_instance)

        print(invocable_service)

    def test_load_class_lookup_method(self):
        result = utils.load_class_to_method_lookup_table(HttpInvokerService)
        print(result)
