from engines import invoker_service
from spell.core.containers import  services


class TestSpellContainer:

    def test_register_spell(self):
        services.register(invoker_service, "invoker_service")
        print(services)
        result = services.get_spell("DatabaseInvokerService.invoke")
        print(result("request"))
        print(services.get("invoker_service"))
