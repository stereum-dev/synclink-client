from apiclient_pydantic import serialize_all_methods

from core.config import Config

from .base_api import API


@serialize_all_methods()
class SynclinkServerAPI(API):
    async def config(self) -> Config:
        return await self.request('/synclink/v1/config')

    async def is_ready(self):
        return await self.client.get('/synclink/v1/ready')


class SyncLink:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.server = SynclinkServerAPI(self.apiUrl)
