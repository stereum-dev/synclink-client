import core.synclink

from config.config import read

from core.node import Node
from core.synclink import SynclinkClient


async def startup():
    await core.synclink.slc.start()
