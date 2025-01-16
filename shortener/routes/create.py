import logging

from fastapi import HTTPException, APIRouter

from shortener.dto import Create, Response
from shortener import models
from shortener.db import SessionDep
from shortener import b62


logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/app/create", status_code=201)
def create(body: Create, session: SessionDep) -> Response:
    url = body.url

    if not url:
        logger.error("URL passed as empty")
        raise HTTPException(
            status_code=400,
            detail="URL cannot be empty",
        )

    logger.debug(f"Received {url=}")

    # TODO what to do when url already exists in the system?

    link = models.Link(original=url, shortened="")
    session.add(link)
    session.flush()
    session.refresh(link)

    link.shortened = b62.encode(link.id)

    session.commit()

    return link
