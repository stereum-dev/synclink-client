from distutils import core
from typing import Union

import core.synclink
from fastapi import APIRouter, Header, Query, Response
from fastapi.responses import JSONResponse, StreamingResponse
from models.get_block_root_response import GetBlockRootResponse
from models.get_block_v2_response import GetBlockV2Response
from models.get_deposit_contract_response import GetDepositContractResponse
from models.get_fork_schedule_response import GetForkScheduleResponse
from models.get_genesis_response import GetGenesisResponse
from models.get_peer_count_response import GetPeerCountResponse
from models.get_peers_response import GetPeersResponse
from models.get_spec_response import GetSpecResponse
from models.get_state_finality_checkpoints_response import \
    GetStateFinalityCheckpointsResponse
from models.get_state_v2_response import GetStateV2Response
from models.get_syncing_status_response import GetSyncingStatusResponse
from models.get_version_response import GetVersionResponse
from services.eth2api import ETH2API
from validators.content_type import (ContentTypeJSON, ContentTypeSSZ,
                                     validate_content_type)

api = ETH2API('http://localhost:5051')

eth_router = APIRouter()


@eth_router.get("/v1/beacon/genesis", tags=["Beacon"], response_model=GetGenesisResponse)
async def handle_eth_v1_beacon_genesis(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.beacon.genesis()

    return r


@eth_router.get("/v1/beacon/blocks/{block_id}/root", tags=["Beacon"], response_model=GetBlockRootResponse)
async def handle_eth_v1_beacon_blocks_root(block_id, content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.beacon.block_root(block_id)

    return JSONResponse(r)


@eth_router.get("/v1/beacon/states/{state_id}/finality_checkpoints", tags=["Beacon"], response_model=GetStateFinalityCheckpointsResponse)
async def handle_eth_v1_beacon_blocks_root(state_id, content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.beacon.state_finality_checkpoints(state_id)

    return JSONResponse(r)


@eth_router.get("/v2/beacon/blocks/{block_id}", tags=["Beacon"], response_model=GetBlockV2Response)
async def handle_eth_v2_beacon_block(block_id, content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON, ContentTypeSSZ])

    r = await api.beacon.block(block_id)

    return JSONResponse(r)


@eth_router.get("/v1/config/spec", tags=["Config"], response_model=GetSpecResponse)
async def handle_eth_v1_config_spec(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.config.spec()

    return JSONResponse(r)


@eth_router.get("/v1/config/deposit_contract", tags=["Config"], response_model=GetDepositContractResponse)
async def handle_eth_v1_config_deposit_contract(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.config.deposit_contract()

    return JSONResponse(r)


@eth_router.get("/v1/config/fork_schedule", tags=["Config"], response_model=GetForkScheduleResponse)
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.config.fork_schedule()

    return JSONResponse(r)


@eth_router.get("/v1/node/health/", tags=["Node"])
async def handle_eth_v1_config_fork_schedule(
    syncing_status: Union[str, None] = Query(
        "206", description="Customize syncing status instead of default status code (206)",
    ),
):

    r = await api.node.health(syncing_status)

    return Response(status_code=r.status_code)


@eth_router.get("/v1/node/syncing", tags=["Node"], response_model=GetSyncingStatusResponse)
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.node.syncing()

    return JSONResponse(r)


@eth_router.get("/v1/node/version", tags=["Node"], response_model=GetVersionResponse)
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.node.version()

    return JSONResponse(r)


@eth_router.get("/v1/node/peers", tags=["Node"], response_model=GetPeersResponse)
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.node.peers()

    return JSONResponse(r)


@eth_router.get("/v1/node/peer_count", tags=["Node"], response_model=GetPeerCountResponse)
async def handle_eth_v1_config_fork_schedule(content_type: str = Header(default=ContentTypeJSON)):
    validate_content_type(content_type, [ContentTypeJSON])

    r = await api.node.peer_count()

    return JSONResponse(r)


@eth_router.get("/v2/debug/beacon/states/{state_id}", tags=["Debug"], response_model=GetStateV2Response)
async def handle_eth_v2_debug_beacon_state(state_id, content_type: str = Header(default=ContentTypeSSZ)):
    validate_content_type(content_type, [ContentTypeSSZ])

    if (state_id == 'finalized'):
        syncpoint = core.synclink.client.syncpoint
        api = core.synclink.client.selected_ready_finalized_node.api

        syncpoint_block = await api.beacon.block(syncpoint.finalized.root)

        return StreamingResponse(api.debug.bacon_state(state_id=syncpoint_block.data.message.slot), headers={"Content-Type": "application/json"})
