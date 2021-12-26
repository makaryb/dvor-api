import yaml

from fastapi import APIRouter
import logging.config

from common.models import (
    Initiative,
    EditInitiative,
    BlogItem,
    EditBlogItem
)
from support.http_status_codes import (
    CODE_200_OK,
    CODE_201_CREATED,
    CODE_204_NO_CONTENT,
    CODE_501_NOT_IMPLEMENTED
)
from support.local_paths import (
    LOGGING_CONFIG_FILEPATH
)


if LOGGING_CONFIG_FILEPATH:
    with open(LOGGING_CONFIG_FILEPATH) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))

router = APIRouter()
logger = logging.getLogger("api_author")


@router.post("/api/active/initiatives", status_code=CODE_201_CREATED)
async def add_initiative(initiative: Initiative):
    logger.debug("received Initiative: %s", initiative.dict())
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.put("/api/active/initiatives/{id}", status_code=CODE_200_OK)
async def update_initiative(initiative: EditInitiative):
    logger.debug("received Initiative: %s", initiative.dict())
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.delete("/api/active/initiatives/{id}", status_code=CODE_204_NO_CONTENT)
async def delete_initiative(id: int):
    logger.debug("received ID: %s", id)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.get("/api/active/favourites")
async def get_favourites(token: str):
    logger.debug("received token: %s", token)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.delete("/api/active/favourites/{id}", status_code=CODE_204_NO_CONTENT)
async def delete_from_favourites(id: int):
    logger.debug("received ID: %s", id)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.post("/api/active/report/{id}", status_code=CODE_201_CREATED)
async def create_report(id: str):
    logger.debug("received ID: %s", id)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.post("/api/active/blog/{id}", status_code=CODE_201_CREATED)
async def add_blog_item(blog_item: BlogItem, id: int):
    logger.debug("received blog item: %s", blog_item.dict())
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.put("/api/active/blog/{id}", status_code=CODE_200_OK)
async def add_blog_item(blog_item: EditBlogItem, id: int):
    logger.debug("received blog item: %s", blog_item.dict())
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED


@router.delete("/api/active/blog/{id}", status_code=CODE_204_NO_CONTENT)
async def add_blog_item(id: int):
    logger.debug("received ID %s", id)
    return "Not implemented yet", CODE_501_NOT_IMPLEMENTED
