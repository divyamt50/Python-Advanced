import asyncio
import time


async def fetch_task(id, delay):
    print(f"fetching data for task{id}")
    await asyncio.sleep(delay)
    data = f"data for id = {id}"
    return {"id":id, "task":data}

async def main():
    start_time = time.time()
    task_1 = asyncio.create_task(fetch_task(1,2))
    task_2 = asyncio.create_task(fetch_task(2,2))
    task_3 = asyncio.create_task(fetch_task(3,2))
    task_4 = asyncio.create_task(fetch_task(4,2))

    result_1 = await(task_1)
    result_2 = await(task_2)
    print(result_1)
    print(result_2)
    result_4 = await(task_4)
    print(result_4)
    result_3 = await(task_3)
    print(result_3)
    end_time = time.time()
    print("total time taken", end_time-start_time)

asyncio.run(main())