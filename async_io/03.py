import asyncio


async def fetch_task(id, delay):
    print(f"working for id:{id}")
    await asyncio.sleep(delay)
    data = f"data for id:{id}"
    return {f"response for id:{id}":f"data for id:{id}"}

async def main():
    results = await asyncio.gather(fetch_task(1,2), fetch_task(2,1), fetch_task(3,3))

    for result in results:
        print(result)
asyncio.run(main())