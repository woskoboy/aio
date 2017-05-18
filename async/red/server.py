import asyncio
import functools
import aioredis
import websockets


@asyncio.coroutine
def listner(channel):
    while (yield from channel.wait_message()):
        msg = yield from channel.get()
        print(msg)


@asyncio.coroutine
def subscribe():
    redis_sub = yield from aioredis.create_redis(('localhost', 6379))
    redis_sub.delete('all')

    ch = yield from redis_sub.subscribe('all')
    yield from listner(ch[0])


@asyncio.coroutine
def connect(ws, path, **kwargs):
    print('Connected')
    while True:
        data = yield from ws.recv()
        kwargs['redis'].publish('all', data)


@asyncio.coroutine
def start_server():
    redis_pub = yield from aioredis.create_redis(('localhost', 6379))
    yield from websockets.serve(functools.partial(connect, redis=redis_pub), 'localhost', 8765)

    yield from subscribe()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()
