import asyncio

@asyncio.coroutine
def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        yield from asyncio.sleep(1)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
tasks = [
    asyncio.gather(factorial("A", 2)),
    asyncio.gather(factorial("B", 3)),
    asyncio.gather(factorial("C", 4))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()