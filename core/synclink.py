import asyncio
import random
from typing import List

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger
from models.get_state_finality_checkpoints_response_data import \
    GetStateFinalityCheckpointsResponseData
from utils.decide_majority_checkpoint import decide_majority_checkpoint

from config.config import config
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

        if final_head_checkpoint:
            if (not self.head or (not self.head.finalized) or (self.head.finalized.root != final_head_checkpoint.finalized.root)):
                self.head = final_head_checkpoint.copy()

    async def check_final_checkpoint(self):
        if not self.head or not self.head.finalized:
            return

        if (self.syncpoint.finalized != None and self.head.finalized.epoch == self.syncpoint.finalized.epoch):
            return

        checkpoint = self.head

        ready_nodes = await self.nodes.get_readies()
        finalized_nodes = await self.nodes.get_finalizes(nodes=ready_nodes, checkpoint=checkpoint)

        self.selected_ready_finalized_node = random.choice(finalized_nodes)

        block = await self.selected_ready_finalized_node.api.beacon.block(checkpoint.finalized.root)

        await self.selected_ready_finalized_node.get_config()
        spec = self.selected_ready_finalized_node.config.spec

        if (int(block.data.message.slot) % int(spec.SLOTS_PER_EPOCH) != 0):
            if (not len(ready_nodes)):
                logger.error('Validate error block is not finalized.')

        self.syncpoint = checkpoint

        logger.success(f"ROOT: {self.syncpoint.finalized.root}")
        logger.success(f"EPOCH: {self.syncpoint.finalized.epoch}")

    async def start(self):
        logger.info('Searching for at least one ready node...')
        ready_nodes = await self.nodes.get_readies()
        while not len(ready_nodes):
            logger.warning('No ready node found! Will try in 5 sec..')
            ready_nodes = await self.nodes.get_readies()
            await asyncio.sleep(5)

        logger.success(f"{str(len(ready_nodes))} ready node(s) found.")

        await self.get_head_finality()
        await self.check_final_checkpoint()
        while not self.syncpoint.finalized:
            logger.warning('Not ready yet, searching for finality...')
            await self.get_head_finality()
            await self.check_final_checkpoint()
            await asyncio.sleep(10)

        self.scheduler = AsyncIOScheduler()

        self.scheduler.add_job(self.get_head_finality, 'interval', seconds=10)

        self.scheduler.add_job(self.check_final_checkpoint,
                               'interval', seconds=30, max_instances=1)

        self.scheduler.start()


client = SynclinkClient(config.nodes)
