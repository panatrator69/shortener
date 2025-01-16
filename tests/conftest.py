"""Provides mock objects for use within the pytest suite."""

import os
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import text

TEST_DATABASE_URI = "postgresql://user:pass@127.0.0.1:5432/test_shortener"


def create_test_database() -> None:
    db_create_engine = create_engine("postgresql://user:pass@127.0.0.1:5432/postgres")
    connection = db_create_engine.connect()
    connection.execute(text("commit"))
    connection.execute(text("CREATE DATABASE test_shortener"))
    db_create_engine.dispose(close=True)


def drop_test_database() -> None:
    db_create_engine = create_engine("postgresql://user:pass@127.0.0.1:5432/postgres")
    connection = db_create_engine.connect()
    # Drop all active connections to the test database
    connection.execute(
        text("""
        SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE pg_stat_activity.datname = 'test_shortener'
          AND pid <> pg_backend_pid();
        """)
    )
    connection.execute(text("commit"))
    connection.execute(text("DROP DATABASE test_shortener"))
    db_create_engine.dispose(close=True)


@pytest.fixture(scope="session")
def patch_database_uri() -> None:
    os.environ["DATABASE_URI"] = TEST_DATABASE_URI


@pytest.fixture(scope="session", autouse=True)
def create_and_drop_test_database(patch_database_uri) -> None:
    create_test_database()
    yield
    drop_test_database()


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(TEST_DATABASE_URI)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

        session.execute(text("DROP TABLE link CASCADE;"))
        session.commit()


@pytest.fixture
def test_client(session: Session) -> Generator[TestClient, None, None]:
    """Provides a mocked HTTP client to test endpoints against."""
    from shortener.app import app
    from shortener.db import get_session

    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    with TestClient(app) as test_client:
        yield test_client
