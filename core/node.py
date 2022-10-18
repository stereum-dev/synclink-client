from services.eth2api import ETH2API


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Node():
    def __init__(self, url) -> None:
        self.api = ETH2API(url)

    async def is_syncing(self) -> bool:
        r = await self.api.node.syncing()

        return r['data']['is_syncing']
