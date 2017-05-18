import aioredis
import asyncio


@asyncio.coroutine
def listner(channel):
    print(channel)
    while (yield from channel.wait_message()):
        msg = yield from channel.get()
        print(msg)


@asyncio.coroutine
def prepare():
    conn = yield from aioredis.create_redis(('localhost', 6379))
    conn.delete('all')

    ch = yield from conn.subscribe('all')
    yield from listner(ch[0])


asyncio.get_event_loop().run_until_complete(prepare())
# tasks = [producer, subscriber]
#
# try:
#     loop.run_until_complete(asyncio.gather(*tasks))
#     loop.run_forever()
# except Exception:
#     conn.delete('all')
#     loop.close()
