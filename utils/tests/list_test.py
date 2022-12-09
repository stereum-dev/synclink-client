import pytest
import asyncio
from utils.list import async_filter


@pytest.mark.asyncio
async def test_async_list_filter():
    original_list = [1, 2, 3]
    without_one_list = []

    async def not_one(item):
        if item == 1:
            await asyncio.sleep(1)
            return False

        return True

    for item in original_list:
        is_one = await not_one(item)
        if is_one:
            without_one_list.append(item)

    without_one_list_async = [i async for i in async_filter(not_one, original_list)]

    assert without_one_list_async == without_one_list
