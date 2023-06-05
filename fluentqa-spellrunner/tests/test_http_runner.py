from spell.clients.http_clients import HttpRequestSpec

from spell.core.containers import providers
from spell.runner.runners import runner
from qpydao.client import Databases, DatabaseConfig

dao = Databases.default_client(DatabaseConfig(
    url="postgresql://root:qwerasdf@pg-dev.sh.hwc.cew.host:5432/qa"
))


def load_data():
    result = dao.query_for_objects(
        "select request_url as url, method,request_headers as headers, request_body as body from api_monitor_record \
             where record_name = :record_name", HttpRequestSpec,
        record_name='record-api-for-test'
    )

    return result


def test_api_runner():
    providers.register(dao, "dao")
    runner.add_spells(providers, "providers")
    runner.run_script(load_data())
    runner.run()
