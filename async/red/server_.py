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
MSG_CONNECT = 'Client {} connected'
MSG_DISCONNECT = 'Client {} disconnected'

""" 
create_redis - вызывается дважды для публикации и подписки 
"""


class Connections:
    connections = set()


class Session(Connections):
    def __init__(self, ws):
        self.name = str(uuid.uuid4())
        self.socket = ws

    def __enter__(self):
        print('Client %s connected' % self.name)
        self.connections.add(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Client %s disconnected' % self.name)
        self.connections.remove(self)


@asyncio.coroutine
def channel_reader(channel):
    while (yield from channel.wait_message()):
        msg = yield from channel.get(encoding="utf-*")
        print('Message: {} from {}'.format(msg, channel.name))
        for session in Connections.connections:
            yield from session.socket.send(msg)


@asyncio.coroutine
def start_listener():
    redis_sub = yield from aioredis.create_redis((RHOST, RPORT))
    redis_sub.delete(CHANNEL)

    ch = yield from redis_sub.subscribe(CHANNEL)
    yield from channel_reader(ch[0])


@asyncio.coroutine
def connect(ws, path, **kwargs):
    rpub = kwargs['redis_pub']
    with Session(ws) as session:
        rpub.publish(CHANNEL, MSG_CONNECT.format(session.name))
        while True:
            try:
                data = yield from ws.recv()
                msg = '{}> {}'.format(session.name, data)
                rpub.publish(CHANNEL, msg)
            except websockets.ConnectionClosed:
                rpub.publish(CHANNEL, MSG_DISCONNECT.format(session.name))
                break


@asyncio.coroutine
def start_server():
    redis_pub = yield from aioredis.create_redis((RHOST, RPORT))
    yield from websockets.serve(functools.partial(connect, redis_pub=redis_pub), WSHOST, WSPORT)
    yield from start_listener()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()
