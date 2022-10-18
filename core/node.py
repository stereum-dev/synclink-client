from cmath import log
from xmlrpc.client import Boolean
from services.eth2api import ETH2API


class Node():
    def __init__(self, url) -> None:
        self.api = ETH2API(url)

    async def is_working(self) -> bool:
        r = await self.api.node.syncing()

        return Boolean(r)

    async def is_syncing(self) -> bool:
        r = await self.api.node.syncing()

        return Boolean(r and r['data']['is_syncing'])

    async def is_not_syncing(self) -> bool:
        syncing = await self.is_syncing()

        return not syncing
