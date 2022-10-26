from cmath import log
from xmlrpc.client import Boolean
from services.eth2api import ETH2API


class Node():
    def __init__(self, url) -> None:
        self.api = ETH2API(url)

    async def is_working(self) -> bool:
        try:
            r = await self.api.node.health()
            r.raise_for_status()

            return True
        except:
            return False

    async def is_syncing(self) -> bool:
        r = await self.api.node.syncing()

        return Boolean(r.data.is_syncing)
