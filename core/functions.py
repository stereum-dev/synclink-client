import logging

from config.config import read

from core.node import Node
from core.synclink import SynclinkClient


async def startup():
    config = read('config.yaml')

    slc = SynclinkClient(config['nodes'])

    await slc.start()
