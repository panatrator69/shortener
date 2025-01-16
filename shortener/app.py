from fastapi import FastAPI

from shortener.db import create_db_and_tables
from shortener.routes import create, redirect

app = FastAPI()
app.include_router(create.router)
app.include_router(redirect.router)


@app.on_event("startup")
def on_startup() -> None:
    """Initialize db and tables on app startup.
    TODO is this idempotent?
    """
    create_db_and_tables()

