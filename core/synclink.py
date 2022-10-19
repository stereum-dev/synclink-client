
from typing import List

from models.get_state_finality_checkpoints_response_data import \
    GetStateFinalityCheckpointsResponseData
from utils.decide_majority_checkpoint import decide_majority_checkpoint

from core.nodes import Nodes


class SynclinkClient():
    def __init__(self, nodes: List[str]) -> None:
        self.nodes = Nodes(nodes)

        self.head = GetStateFinalityCheckpointsResponseData()

    async def get_head_finality(self):
        checkpoints = []

        ready_nodes = await self.nodes.get_readies()

        for node in ready_nodes:
            checkpoint = await node.api.beacon.state_finality_checkpoints('head')
            checkpoints.append(checkpoint.data)

        final_head_checkpoint = decide_majority_checkpoint(checkpoints)

        if (not self.head or (not self.head.finalized) or (self.head.finalized.root != final_head_checkpoint.finalized.root)):
            self.head = final_head_checkpoint.copy()

    async def start(self):
        ready_nodes = await self.nodes.get_readies()

        if (not len(ready_nodes)):
            raise Exception('TODO: Loop searching for ready_nodes')

        await self.get_head_finality()

        print('Final checkpoint: ', self.head)
