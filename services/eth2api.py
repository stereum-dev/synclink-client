from typing import Union
from urllib.parse import urljoin

import httpx
from apiclient_pydantic import response_serializer, serialize_all_methods
from loguru import logger
from models.get_block_v2_response import GetBlockV2Response
from models.get_spec_response import GetSpecResponse
from models.get_state_finality_checkpoints_response import \
    GetStateFinalityCheckpointsResponse
from models.get_syncing_status_response import GetSyncingStatusResponse


class API:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.client = httpx.AsyncClient(base_url=apiUrl)

    async def request(self, url_path):
        try:
            response = await self.client.get(url_path)
            response.raise_for_status()

            return response.json()
        except Exception as exc:
            logger.error(f"ERROR: {exc}")


@serialize_all_methods()
class BeaconAPI(API):
    async def genesis(self):
        return await self.request('/eth/v1/beacon/genesis')

    async def block_root(self, block_id):
        return await self.request(f"/eth/v1/beacon/blocks/{block_id}/root")

    async def state_finality_checkpoints(self, state_id) -> GetStateFinalityCheckpointsResponse:
        return await self.request(f"/eth/v1/beacon/states/{state_id}/finality_checkpoints")

    async def block(self, block_id) -> GetBlockV2Response:
        return await self.request(f"/eth/v2/beacon/blocks/{block_id}")


@serialize_all_methods()
class ConfigAPI(API):
    async def spec(self) -> GetSpecResponse:
        return await self.request('/eth/v1/config/spec')

    async def deposit_contract(self):
        return await self.request('/eth/v1/config/deposit_contract')

    async def fork_schedule(self):
        return await self.request('/eth/v1/config/fork_schedule')


@serialize_all_methods()
class NodeAPI(API):
    async def health(self):
        return await self.client.get('/eth/v1/node/health')

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
        with httpx.stream("GET", urljoin(self.apiUrl, f"/eth/v2/debug/beacon/states/{state_id}"), headers={'Accept': 'application/octet-stream'}) as r:
            for chunk in r.iter_bytes():
                yield chunk


class ETH2API:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.beacon = BeaconAPI(self.apiUrl)
        self.config = ConfigAPI(self.apiUrl)
        self.node = NodeAPI(self.apiUrl)
        self.debug = DebugAPI(self.apiUrl)
