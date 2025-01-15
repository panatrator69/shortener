from fastapi import FastAPI

from shortener.db import create_db_and_tables
from shortener.routes import create

app = FastAPI()
app.include_router(create.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

