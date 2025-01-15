import logging
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from shortener.settings import settings


logger = logging.getLogger(__name__)


def init_engine():
    logger.info(f'Connecting to {settings.database_uri=}')
    return create_engine(settings.database_uri)


engine = init_engine()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
    
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
