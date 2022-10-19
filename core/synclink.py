
import asyncio
from typing import List

from utils.decide_majority_checkpoint import decide_majority_checkpoint

from core.node import Node
from utils.list import async_filter


class SynclinkClient():
    def __init__(self, nodes: List[str]) -> None:
        self.nodes = [Node(n) for n in set(nodes)]
        self.ready_nodes: List[Node] = []

    async def select_ready_nodes(self) -> List[Node]:
        async def check_is_ready(node: Node):
            health = await node.is_working()

            if (not health):
                return False

            syncing = await node.is_syncing()

            if (syncing):
                return False

            return True

        ready_nodes = [i async for i in async_filter(check_is_ready, self.nodes)]

        self.ready_nodes = ready_nodes.copy()

    async def start(self):
        await self.select_ready_nodes()

        if (not len(self.ready_nodes)):
            raise Exception('TODO: Loop searching for ready_nodes')

        checkpoints = []

        for node in self.ready_nodes:
            checkpoint = await node.api.beacon.state_finality_checkpoints('head')
            checkpoints.append(checkpoint['data'])

        final_checkpoint = decide_majority_checkpoint(checkpoints)

        print('Final checkpoint: ', final_checkpoint)
