from services.eth2api import ETH2API

from core.config import Config


class Node():
    def __init__(self, url) -> None:
        self.api = ETH2API(url)
        self.config = Config()

    async def is_ready(self) -> bool:
        try:
            r = await self.api.synclink_server.is_ready()
            r.raise_for_status()

            return True
        except:
            return False

    async def get_config(self) -> bool:
        config = await self.api.synclink_server.config()
        self.config = config

    async def is_syncing(self) -> bool:
        r = await self.api.node.syncing()

        return bool(r.data.is_syncing)
