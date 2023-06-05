from spell.clients.http_clients import HttpProcessor
from spell.core.containers import providers


def test_provider_container():
    http_processor = providers.get(HttpProcessor)
    print(http_processor)
