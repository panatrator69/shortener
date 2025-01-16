"""DTOs for the create endpoint."""

import datetime

from pydantic import BaseModel
from pydantic.networks import HttpUrl


class Create(BaseModel):
    """Defines the request JSON body for the POST /app/create endpoint."""

    url: HttpUrl


class Link(BaseModel):
    """Defines the response JSON body for the POST /app/create endpoint."""

    original: str
    shortened: str
    created_at: datetime.datetime
