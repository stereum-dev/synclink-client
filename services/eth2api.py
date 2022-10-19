from http import client
from urllib.parse import urljoin

import httpx
from models.get_state_finality_checkpoints_response import \
    GetStateFinalityCheckpointsResponse
from models.get_syncing_status_response import GetSyncingStatusResponse
from validators.content_type import ContentTypeSSZ


class API:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.__client = httpx.AsyncClient(base_url=apiUrl)

    async def request(self, url_path):
        try:
            response = await self.__client.get(url_path)
            response.raise_for_status()

            return response.json()
        except Exception as exc:
            print("ERROR: ", exc)


class BeaconAPI(API):
    async def genesis(self):
        return await self.request('/eth/v1/beacon/genesis')

    async def block_root(self, block_id):
        return await self.request(f"/eth/v1/beacon/blocks/{block_id}/root")

    async def state_finality_checkpoints(self, state_id) -> GetStateFinalityCheckpointsResponse:
        res = await self.request(f"/eth/v1/beacon/states/{state_id}/finality_checkpoints")

        return GetStateFinalityCheckpointsResponse(**res)

    async def block(self, block_id):
        return await self.request(f"/eth/v2/beacon/blocks/{block_id}")


class ConfigAPI(API):
    async def spec(self):
        return await self.request('/eth/v1/config/spec')

    async def deposit_contract(self):
        return await self.request('/eth/v1/config/deposit_contract')

    async def fork_schedule(self):
        return await self.request('/eth/v1/config/fork_schedule')


class NodeAPI(API):
    async def syncing(self) -> GetSyncingStatusResponse:
        return await self.request('/eth/v1/node/syncing')

    async def version(self):
        return await self.request('/eth/v1/node/version')

    async def peers(self):
        return await self.request('/eth/v1/node/peers')

    async def peer_count(self):
        return await self.request('/eth/v1/node/peer_count')


class DebugAPI(API):
    def bacon_state(self, state_id):
        with httpx.stream("GET", urljoin(self.apiUrl, f"/eth/v2/debug/beacon/states/{state_id}")) as r:
            for chunk in r.iter_bytes():
                yield chunk


class ETH2API:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.beacon = BeaconAPI(self.apiUrl)
        self.config = ConfigAPI(self.apiUrl)
        self.node = NodeAPI(self.apiUrl)
        self.debug = DebugAPI(self.apiUrl)
