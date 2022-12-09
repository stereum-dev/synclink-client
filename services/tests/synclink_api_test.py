import asyncio

import pytest

from services.synclink_api import SyncLink

syncLink = SyncLink('http://localhost:8000')


@pytest.mark.asyncio
async def test_synclink_server_is_ready():
    is_ready = await syncLink.server.is_ready()

    assert is_ready.status_code == 200


@pytest.mark.asyncio
async def test_synclink_server_get_config():
    config = await syncLink.server.config()

    assert config.spec and config.fork_epochs and config.deposit_contract


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
