"""DTOs for the create endpoint."""
from pydantic import BaseModel


class Create(BaseModel):
    """Defines the request JSON body for the POST /app/create endpoint."""
    url: str


class Response(BaseModel):
    """Defines the response JSON body for the POST /app/create endpoint."""
    original: str
    shortened: str
