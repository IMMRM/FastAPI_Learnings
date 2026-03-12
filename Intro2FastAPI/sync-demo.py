import time
from timeit import default_timer as timer


# by default the function is synchronous and will block the execution of the code until it finishes
def task(name, seconds, start_time):
    elapsed = timer() - start_time
    print(f"Task {name} started at {elapsed:.2f} seconds")
    time.sleep(seconds)  # Simulate a time-consuming task
    elapsed = timer() - start_time
    print(f"Task {name} completed at {elapsed:.2f} seconds")


start = timer()
task("A", 2, start)
task("B", 1, start)
task("C", 3, start)
end = timer()
print(f"Total time taken: {end-start:.2f} seconds")
