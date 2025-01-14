import logging

from fastapi import HTTPException, APIRouter

from shortener.dto import Create


logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/app/create")
def create(body: Create):
    url = body.url

    # TODO should the DTO logic from pydantic be responsible for raising errors and 
    # then being caught by a fastapi handler? DTO serialization failure logic should
    # return HTTP422 to be more description. Using 400 for now.
    # https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers
    if not url:
        logger.error('URL passed as empty')
        raise HTTPException(
            status_code=400,
            detail='URL cannot be empty',
        )

    logger.debug(f'Received {url=}')
