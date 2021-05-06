import asyncio
async def async_func1():
    print("Hello")


loop = asyncio.get_event_loop()
loop.run_until_compleate(async_func1())
loop.close()