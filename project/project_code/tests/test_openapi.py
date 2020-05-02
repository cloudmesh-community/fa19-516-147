
import requests
###############################################################
# pytest -v --capture=no tests/test_openapi.py
# pytest -v  tests/test_openapi.py
# pytest -v --capture=no  tests/test_openapi..py::test_openapi::<METHODNAME>
###############################################################


from pprint import pprint

import pytest
from cloudmesh.common.Printer import Printer
from cloudmesh.common.util import HEADING
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.configuration.Config import Config
from pprint import pprint

Benchmark.debug()

cloud = "local"


@pytest.mark.incremental
class TestName:

    def test_status(self):
        HEADING()

        Benchmark.Start()

        r = requests.get('http://localhost:8080/cloudmesh/v3/status/')

        assert r.status_code == 200

        assert r.headers['content-type'] == "application/json"

        d = r.json()
        pprint (d)
        assert d['status'] == 'ok'

        Benchmark.Stop()

    def test_home(self):
        HEADING()

        Benchmark.Start()

        r = requests.get('http://localhost:8080/')

        assert r.status_code == 200

        assert r.headers['content-type'] == "application/json"

        d = r.json()
        pprint(d)
        assert d['status'] == 'ok'

        Benchmark.Stop()

    def test_ui(self):
        HEADING()

        Benchmark.Start()

        r = requests.get('http://localhost:8080/cloudmesh/v3/ui')

        assert r.status_code == 200

        #assert r.headers['content-type'] == "application/json"

        d = r.text()
        pprint(d)
        assert d['status'] == 'ok'

        Benchmark.Stop()

    def test_benchmark(self):
        HEADING()
        Benchmark.print(csv=True, sysinfo=True, tag=cloud)

    def test_get_database():
        url = 'http://127.0.0.1:8080/cloudmesh/v3/database/all'
        response = requests.get(url)
        assert response.status_code == 200
        print(response.content)

    def test_put_database():
        url = 'http://127.0.0.1:8080/cloudmesh/v3/database/mytestdb'
        response = requests.put(url)
        # validate response code
        assert response.status_code == 200

    def test_put_collection():
        url = 'http://127.0.0.1:8080/cloudmesh/v3/database/mytestdb/collection/all,'
        response = requests.put(url)
        # validate response code
        assert response.status_code == 200
