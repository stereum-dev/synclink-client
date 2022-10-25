import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

import core.synclink


class SchedulerService:
    async def test_interval(self):
        print('Interval check...')

    def start(self):
        print('Starting scheduler service.')

        self.queue = asyncio.Queue()
        self.sch = AsyncIOScheduler()
        self.sch.start()

        self.sch.add_job(self.test_interval, 'interval',
                         seconds=5, max_instances=1)


async def startup():
    sch_srv = SchedulerService()
    sch_srv.start()
    await core.synclink.slc.start()
