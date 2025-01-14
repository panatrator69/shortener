import pytest
from fastapi.testclient import TestClient

from shortener.app import app


@pytest.fixture
def test_client():
    with TestClient(app) as test_client:
        yield test_client
