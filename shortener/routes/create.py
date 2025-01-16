import logging

from fastapi import APIRouter, HTTPException

from shortener import b62, models
from shortener.db import SessionDep
from shortener.dto import Create, Response

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/app/create", status_code=201)
def create(body: Create, session: SessionDep) -> Response:
    url = body.url
    logger.debug(f"Received {url=}")

    # TODO what to do when url already exists in the system?

    link = models.Link(original=str(url), shortened="")
    session.add(link)
    session.flush()
    session.refresh(link)

    link.shortened = b62.encode(link.id)

    session.commit()

    return link
