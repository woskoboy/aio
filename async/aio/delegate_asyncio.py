import asyncio

DIGIT = 10, 30, 50, None  # 30
DIGIT1 = 50, 20, 50, None  # 40
DIGIT2 = 10, 20, 10, 20, None  # 15


@asyncio.coroutine
def producer(queue, data):
    yield from asyncio.sleep(1)
    for val in data:
        yield from queue.put(val)


@asyncio.coroutine
def sub_gen(queue):
    total = 0
    avg = None
    ind = 0
    while True:
        val = yield from queue.get()
        if val is None:
            break
        total += val
        ind += 1
        avg = total / ind
    return avg
# @asyncio.coroutine
# def delegate_gen(queue):
#     # yield from проглотит StopIteration
#     #  и достанет из него value
#     avg = yield from sub_gen(queue)
#     print('Final result = ', avg)


# декоратор не занимается инициализацией,но нужен для цикла обработки,
# к примеру цикл проглотит StopIteration и сделает прочие штуки
# @asyncio.coroutine
# def main(values):
#     dg = delegate_gen()
#     next(dg)
#     for d in values:
#         dg.send(d)
#     dg.send(None)

@asyncio.coroutine
def prepare(data):
    queue = asyncio.Queue()
    yield from producer(queue, data)
    avg = yield from sub_gen(queue)
    return avg


@asyncio.coroutine
def run():
    prepares = [prepare(DIGIT), prepare(DIGIT1), prepare(DIGIT2)]

    for prepare_ in asyncio.as_completed(prepares):
        avg = yield from prepare_
        print(avg)

loop = asyncio.get_event_loop()

loop.run_until_complete(run())
loop.close()
