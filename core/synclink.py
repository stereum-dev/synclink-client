
from typing import List

from utils.decide_majority_checkpoint import decide_majority_checkpoint

from core.node import Node


class SynclinkClient():
    def __init__(self, nodes: List[str]) -> None:
        self.nodes = map(lambda n: Node(n), nodes)
        self.ready_nodes: List[Node] = []

    async def select_ready_nodes(self) -> List[str]:
        for node in self.nodes:
            health = await node.is_working()

            if (not health):
                break

            syncing = await node.is_syncing()

            if (syncing):
                break

            self.ready_nodes.append(node)

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
