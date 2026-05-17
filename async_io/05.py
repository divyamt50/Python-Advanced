import asyncio


shared_resource = 0

lock = asyncio.Lock()

async def work_on_shared_resource():
    global shared_resource
    async with lock:
        print("resource before modification", shared_resource)
        shared_resource += 1
        await asyncio.sleep(2)
        print("resource after modification", shared_resource)
    
async def main():
    await asyncio.gather(*(work_on_shared_resource() for _ in range(5)))

asyncio.run(main())