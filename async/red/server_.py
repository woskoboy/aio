import asyncio
import functools
import html

import aioredis
import websockets
import uuid

# connected = set()
CHANNEL = 'chanel_A'
RHOST = 'localhost'
RPORT = 6379
WSHOST = 'localhost'
WSPORT = 8765

""" 
create_redis - вызывается дважды для публикации и подписки 
глобальная перем-я connected - хранит список активных подключений
"""


class Session:
    def __init__(self):
        # global connected
        # self.connected = connected
        self.connected = set()

    def __enter__(self, ws):
        self.name = str(uuid.uuid4())
        print('Client %s connected' % self.name)
        self.connected.add(ws)
        self.socket = ws
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Client disconnected')
        self.connected.remove(self.socket)


@asyncio.coroutine
def channel_reader(channel, session):
    while (yield from channel.wait_message()):
        msg = yield from channel.get(encoding="utf-*")
        print('Message: {} from {}'.format(msg, channel.name))
        for ws in session.connected:
            yield from ws.send(msg)


@asyncio.coroutine
def start_listener(session):
    redis_sub = yield from aioredis.create_redis((RHOST, RPORT))
    redis_sub.delete(CHANNEL)

    ch = yield from redis_sub.subscribe(CHANNEL)
    yield from channel_reader(ch[0], session)


@asyncio.coroutine
def connect(ws, path, **kwargs):

    with kwargs['session'](ws) as session:
        while True:
            try:
                data = yield from ws.recv()
                msg = '{} > {}'.format(session.name, data)
                kwargs['redis_pub'].publish(CHANNEL, msg)
            except websockets.ConnectionClosed:
                break


@asyncio.coroutine
def start_server():
    redis_pub = yield from aioredis.create_redis((RHOST, RPORT))
    s = Session()
    yield from websockets.serve(functools.partial(connect, redis_pub=redis_pub, session=s), WSHOST, WSPORT)
    yield from start_listener(s)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()
