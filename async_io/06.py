import asyncio

async def access_resource(semaphore, i):
    async with semaphore:
        print(f"Accessing resource {i}")
        await asyncio.sleep(2)
        print(f"releasing resource {i}")

async def main():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))


asyncio.run(main())