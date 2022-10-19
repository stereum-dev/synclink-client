from typing import List

from utils.list import async_filter

from core.node import Node


class Nodes:
    def __init__(self, nodes: List[str]) -> None:
        self.nodes = [Node(n) for n in set(nodes)]

    async def get_readies(self) -> List[Node]:
        async def check_is_ready(node: Node):
            health = await node.is_working()

            if (not health):
                return False

            syncing = await node.is_syncing()

            if (syncing):
                return False

            return True

        ready_nodes = [i async for i in async_filter(check_is_ready, self.nodes)]

        return ready_nodes
