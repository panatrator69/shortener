"""Provides mock objects for use within the pytest suite."""
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from shortener.app import app


@pytest.fixture
def test_client() -> Generator[TestClient]:
    """Provides a mocked HTTP client to test endpoints against."""
    with TestClient(app) as test_client:
        yield test_client
