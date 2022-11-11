async def async_filter(async_pred, iterable):
    for item in iterable:
        should_yield = await async_pred(item)
        if should_yield:
            yield item
