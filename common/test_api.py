import pytest
from fastapi.testclient import TestClient

from api import (
    app as dvor_app
)
from support.http_status_codes import (
    CODE_200_OK
)


@pytest.fixture
def client():
    with TestClient(dvor_app) as client:
        yield client


def test_root(client):
    app_response = client.get("/")
    code = app_response.status_code
    assert CODE_200_OK == code, (
        f"Expected: {CODE_200_OK}. Received: {code}"
    )
    expected = {"Server is running": "1"}
    received = app_response.json()
    assert expected == received, (
        f"Expected {expected}. Received {received}"
    )
