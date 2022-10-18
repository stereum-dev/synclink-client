import logging

from config.config import read
from core.node import Node


async def startup():
    config = read('config.yaml')

    n = Node(config['nodes'][0])
    w = await n.is_working()
    s = await n.is_not_syncing()

    print(w, s)
