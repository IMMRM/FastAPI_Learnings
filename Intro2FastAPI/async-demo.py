import time
import asyncio
from timeit import default_timer as timer


# on the other hand, the function is asynchronous and will not block the execution of the code while it is running
async def task(name,seconds,start_time):
    elapsed=timer()-start_time
    print(f"Task {name} started at {elapsed:.2f} seconds")
    await asyncio.sleep(seconds) # Simulate a time-consuming task
    elapsed=timer()-start_time
    print(f"Task {name} completed at {elapsed:.2f} seconds")
    
async def main():
    start=timer()
    await asyncio.gather(
        task("A",2,start),
        task("B",1,start),
        task("C",3,start)
    )
    end=timer()
    print(f"Total time taken: {end-start:.2f} seconds")
    
asyncio.run(main())