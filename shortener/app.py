from fastapi import FastAPI

from shortener.routes import create

app = FastAPI()
app.include_router(create.router)
