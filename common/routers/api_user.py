import yaml

from fastapi import APIRouter
import logging.config

from common.models import (
    Payment
)
from support.http_status_codes import (
    CODE_201_CREATED,
    CODE_202_ACCEPTED,
    CODE_501_NOT_IMPLEMENTED
)
from support.local_paths import (
    LOGGING_CONFIG_FILEPATH
)

if LOGGING_CONFIG_FILEPATH:
    with open(LOGGING_CONFIG_FILEPATH) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))

router = APIRouter()
logger = logging.getLogger("api_user")


@router.post("/api/open/login", status_code=CODE_202_ACCEPTED)
async def sign_in(token: str):
    logger.debug("received token: %s", token)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.get("/api/open/initiatives")
async def get_initiatives():
    logger.debug("get all initiatives request")
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.get("/api/open/initiatives/{id}")
async def get_initiative(id: int):
    logger.debug("received ID: %s", id)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.post("/api/open/payment", status_code=CODE_201_CREATED)
async def add_payment(payment: Payment):
    logger.debug("received payment: %s", payment)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.get("/api/open/payment/{id}")
async def get_payment(id: int):
    logger.debug("received ID: %s", id)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.get("/api/open/{id}")
async def get_user(id: int):
    logger.debug("received ID: %s", id)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.get("/api/open/blog/{id}")
async def get_blog_item(id: int):
    logger.debug("received ID: %s", id)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED
