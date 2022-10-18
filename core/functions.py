from config.config import read
from core.node import Node


async def startup():
    config = read('config.yaml')

    n = Node(config['nodes'][0])
    s = await n.is_syncing()

    print(s)
