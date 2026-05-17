import asyncio
import time

async def fetch_data(id, delay):
    await asyncio.sleep(delay)
    return {"id":id, "data":f"data for id = {id}"}
    

async def main():
    res_list = []
    start_time = time.time()
    async with asyncio.TaskGroup() as tg:
        for id, delay in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data(id, delay))
            res_list.append(task)

    end_time = time.time()

    print("time", end_time-start_time)
    
    res_final = []

    for res in res_list:
        res_task = res.result()
        res_final.append(res_task)
    
    for res in res_final:
        print("received result", res)

asyncio.run(main())