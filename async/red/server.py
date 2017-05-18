import asyncio
import functools

import aioredis
import websockets
# many_ws = []
#
# # @asyncio.coroutine
# # def html_handler(ws, path):
# #     while True:
# #         now = datetime.datetime.utcnow().isoformat() + 'Z'
# #         yield from ws.send(now)
# #         yield from asyncio.sleep(1)
#
#
# @asyncio.coroutine
# def handler(ws, path):
#     global many_ws
#     many_ws.append(ws)
#     data = yield from ws.recv()
#     for ind, ws in enumerate(many_ws):
#         try:
#             yield from ws.send('echo: %s' % data)
#         except websockets.ConnectionClosed:
#             pass
#     print(len(many_ws))


# @asyncio.coroutine
# def handler(ws, path, **kwargs):
#     que = kwargs['que']
#     while que:
#         data = yield from que.get()
#         try:
#             yield from asyncio.sleep(2)
#             yield from ws.send('echo: %s' % data)
#         except websockets.ConnectionClosed:
#             print('ConnectionClosed')
#             ws.close()
#             pass
#
#
# @asyncio.coroutine
# def prepare(que):
#     for data in 'Hello ', 'my', 'best', 'friend!', 'How', 'are', 'you?':
#         yield from que.put(data)
#     yield from websockets.serve(functools.partial(handler, que=que), 'localhost', 8765)


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
    tasks = [websockets.serve(functools.partial(connect, conn=conn), 'localhost', 8765)]
    asyncio.gather(*tasks)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()