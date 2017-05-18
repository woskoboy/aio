import asyncio
import functools
import aioredis
import websockets


@asyncio.coroutine
def connect(ws, path, **kwargs):
    print('Connected')
    while True:
        data = yield from ws.recv()
        print(data)
        kwargs['conn'].publish('all', data)


@asyncio.coroutine
def start_server():
    conn = yield from aioredis.create_redis(('localhost', 6379))
    yield from websockets.serve(functools.partial(connect, conn=conn), 'localhost', 8765)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()