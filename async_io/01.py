import time
import asyncio


async def fetch_data(delay):
    print("inside fetch data function")
    data = "some data"
    await asyncio.sleep(delay)
    return {data:data}

async def main():
    result = await fetch_data(2)
    print(result)

asyncio.run(main())