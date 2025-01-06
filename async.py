import time
import timeit
import asyncio

# Simulate GET requests - Synchronous
get_1 = lambda: time.sleep(2)
get_2 = lambda: time.sleep(2)
get_3 = lambda: time.sleep(2)

# Simulate GET requests - Asynchronous
async def async_get_1():
    await asyncio.sleep(2)

async def async_get_2():
    await asyncio.sleep(2)

async def async_get_3():
    await asyncio.sleep(2)

# Synchronous version
def main_sync(get_1, get_2, get_3):
    get_1()
    get_2()
    get_3()

# Asynchronous version
async def main_async():
    await asyncio.gather(
        async_get_1(),
        async_get_2(),
        async_get_3(),
    )

# Timing synchronous execution
start = timeit.default_timer()
main_sync(get_1, get_2, get_3)
print("Synchronous time taken: ", timeit.default_timer() - start)

# Timing asynchronous execution
start = timeit.default_timer()
asyncio.run(main_async())
print("Asynchronous time taken: ", timeit.default_timer() - start)