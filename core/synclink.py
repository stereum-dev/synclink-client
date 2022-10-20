
import random
from typing import List
from config.config import read

from models.get_state_finality_checkpoints_response_data import \
    GetStateFinalityCheckpointsResponseData
from utils.decide_majority_checkpoint import decide_majority_checkpoint

from core.nodes import Nodes


class SynclinkClient():
    def __init__(self, nodes: List[str]) -> None:
        self.nodes: Nodes = Nodes(nodes)

        self.head: GetStateFinalityCheckpointsResponseData = GetStateFinalityCheckpointsResponseData()
        self.syncpoint: GetStateFinalityCheckpointsResponseData = GetStateFinalityCheckpointsResponseData()

        self.selected_ready_finalized_node = None

    async def get_head_finality(self):
        checkpoints = []

        ready_nodes = await self.nodes.get_readies()

        for node in ready_nodes:
            checkpoint = await node.api.beacon.state_finality_checkpoints('head')
            checkpoints.append(checkpoint.data)

        final_head_checkpoint = decide_majority_checkpoint(checkpoints)

        if (not self.head or (not self.head.finalized) or (self.head.finalized.root != final_head_checkpoint.finalized.root)):
            self.head = final_head_checkpoint.copy()

    async def check_final_checkpoint(self):
        checkpoint = self.head

        ready_nodes = await self.nodes.get_readies()
        finalized_nodes = await self.nodes.get_finalizes(nodes=ready_nodes, checkpoint=checkpoint)
        self.selected_ready_finalized_node = random.choice(finalized_nodes)

        block = await self.selected_ready_finalized_node.api.beacon.block(checkpoint.finalized.root)
        spec = await self.selected_ready_finalized_node.api.config.spec()

        if (int(block.data.message.slot) % int(spec.data['SLOTS_PER_EPOCH']) != 0):
            if (not len(ready_nodes)):
                raise Exception('TODO: validate error block is not finalized')

        self.syncpoint = checkpoint

    async def start(self):
        ready_nodes = await self.nodes.get_readies()

        if (not len(ready_nodes)):
            raise Exception('TODO: Loop searching for ready_nodes')

        await self.get_head_finality()
        await self.check_final_checkpoint()

        print("-----CHECKPOINT RECOGNIZED-------")
        print('------ROOT: ', self.syncpoint.finalized.root)
        print('------EPOCH: ', self.syncpoint.finalized.epoch)


config = read('config.yaml')

slc = SynclinkClient(config['nodes'])
