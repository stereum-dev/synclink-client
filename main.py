import uvicorn
from fastapi import FastAPI
from loguru import logger

from config.config import get_app_config
from config.logger import LOG_LEVEL, UVICORN_LOGGING_CONFIG, setup_logging
from core.functions import startup
from routes.eth_handler import eth_router

app = FastAPI(
    title="SyncLink Client API",
    description="Specification of the SyncLink Client API",
    version="0.1.0",
)

setup_logging(LOG_LEVEL, False)

app.include_router(eth_router, prefix='/eth')


@app.on_event("startup")
async def startup_event():
    await startup()


if __name__ == "__main__":
    config = get_app_config()

    docs_addr = config.addr if config.addr != "0.0.0.0" else "127.0.0.1"
    docs_port = config.port

    uvicorn.run("main:app", host=config.addr,
                port=config.port, reload=True, log_config=UVICORN_LOGGING_CONFIG)
