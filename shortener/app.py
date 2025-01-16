from contextlib import asynccontextmanager

from fastapi import FastAPI

from shortener.db import create_db_and_tables
from shortener.routes import create, redirect


@asynccontextmanager
async def lifespan(current_app: FastAPI) -> None:
    """Initialize db and tables on app startup."""
    # TODO is this idempotent?
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(create.router)
app.include_router(redirect.router)
