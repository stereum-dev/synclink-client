
import asyncio
from typing import List
from models.get_state_finality_checkpoints_response_data import GetStateFinalityCheckpointsResponseData

from utils.decide_majority_checkpoint import decide_majority_checkpoint

from core.node import Node
from utils.list import async_filter


class SynclinkClient():
    def __init__(self, nodes: List[str]) -> None:
        self.nodes = [Node(n) for n in set(nodes)]
        self.ready_nodes: List[Node] = []

        self.head = GetStateFinalityCheckpointsResponseData()

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

    async def get_head_finality(self):
        checkpoints = []

        for node in self.ready_nodes:
            checkpoint = await node.api.beacon.state_finality_checkpoints('head')
            checkpoints.append(checkpoint.data)

        final_head_checkpoint = decide_majority_checkpoint(checkpoints)

        if (not self.head or (not self.head.finalized) or (self.head.finalized.root != final_head_checkpoint.finalized.root)):
            self.head = final_head_checkpoint.copy()

    async def start(self):
        await self.select_ready_nodes()

        if (not len(self.ready_nodes)):
            raise Exception('TODO: Loop searching for ready_nodes')

        await self.get_head_finality()

        print(self.head)

        print('Final checkpoint: ')
