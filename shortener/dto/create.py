from pydantic import BaseModel


class Create(BaseModel):
    url: str


class Response(BaseModel):
    shortened: str