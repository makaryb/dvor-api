import logging.config
import yaml

from fastapi import FastAPI

from common.routers import (
    api_user,
    api_author
)
from support.local_paths import (
    LOGGING_CONFIG_FILEPATH
)

if LOGGING_CONFIG_FILEPATH:
    with open(LOGGING_CONFIG_FILEPATH) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))

app = FastAPI()
app.include_router(api_user.router)
app.include_router(api_author.router)
logger = logging.getLogger("api")


@app.get("/")
async def root():
    return {"Server is running": "1"}
