from typing import List
from models.get_state_finality_checkpoints_response_data import GetStateFinalityCheckpointsResponseData

from utils.list import async_filter

from core.node import Node


class Nodes:
    def __init__(self, nodes: List[str]) -> None:
        self.nodes = [Node(n) for n in set(nodes)]

    async def get_readies(self) -> List[Node]:
        async def check_is_ready(node: Node):
            is_ready = await node.is_ready()

            return is_ready

        ready_nodes = [i async for i in async_filter(check_is_ready, self.nodes)]

        return ready_nodes

    async def get_finalizes(self, checkpoint: GetStateFinalityCheckpointsResponseData, nodes: List[Node]) -> List[Node]:
        nodes = nodes or self.nodes

        async def is_finalized(node: Node):
            finality_state = await node.api.beacon.state_finality_checkpoints('head')

            if (not finality_state or (finality_state.data.finalized.epoch < checkpoint.finalized.epoch)):
                return False

            return True

        ready_nodes = [i async for i in async_filter(is_finalized, nodes)]

        return ready_nodes
