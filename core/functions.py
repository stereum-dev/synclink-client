import core.synclink


async def startup():
    await core.synclink.client.start()
