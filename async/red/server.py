import asyncio
import functools
import aioredis
import websockets
import uuid

connected = set()
CHANNEL = 'chanel_A'
RHOST = 'localhost'
RPORT = 6379
WSHOST = 'localhost'


class Session:
    def __init__(self, ws):
        global connected
        self.socket = ws
        self.connected = connected
        self.name = str(uuid.uuid4())

    def __enter__(self):
        print('Client %s connected' % self.name)
        self.connected.add(self.socket)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Client disconnected')
        self.connected.remove(self.socket)


@asyncio.coroutine
def listner(channel):
    while (yield from channel.wait_message()):
        msg = yield from channel.get(encoding="utf-*")
        print('Message: {} from {}'.format(msg, channel.name))
        global connected
        for ws in connected:
            yield from ws.send(msg)


@asyncio.coroutine
def subscribe():
    redis_sub = yield from aioredis.create_redis((RHOST, RPORT))
    redis_sub.delete(CHANNEL)

    ch = yield from redis_sub.subscribe(CHANNEL)
    yield from listner(ch[0])


@asyncio.coroutine
def connect(ws, path, **kwargs):
    # print(path)
    session = Session(ws)
    with session:
        while True:
            try:
                data = yield from ws.recv()
                kwargs['redis_pub'].publish(CHANNEL, '{} > \t\n{}'.format(session.name, data))
            except websockets.ConnectionClosed:
                break


@asyncio.coroutine
def start_server():
    redis_pub = yield from aioredis.create_redis((RHOST, RPORT))
    yield from websockets.serve(functools.partial(connect, redis_pub=redis_pub), WSHOST, 8765)

    yield from subscribe()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()
