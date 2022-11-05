import core.synclink
from config.config import get_app_config
from loguru import logger

config = get_app_config()


async def startup():
    await core.synclink.client.start()

    docs_addr = config.addr if config.addr != "0.0.0.0" else "127.0.0.1"
    docs_port = config.port

    logger.success(
        f"Server starting, find API docs at http://{docs_addr}:{docs_port}/docs")
