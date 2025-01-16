"""Creates the sqlmodel engine object and provides a FastAPI dependency for use within HTTP routes."""

import logging
from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from shortener.settings import settings

logger = logging.getLogger(__name__)


def init_engine():
    """Reads the shortener.settings.settings object for the database_uri to pass to the engine.
    TODO how to import the Engine object from sqlmodel as the return type."""
    logger.info(f"Connecting to {settings.database_uri=}")
    return create_engine(settings.database_uri)


engine = init_engine()


def create_db_and_tables() -> None:
    """Creates the database and tables for all required models."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """FastAPI dependency for accessing the database within the context of a route function."""
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
