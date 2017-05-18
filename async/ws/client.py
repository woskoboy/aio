import asyncio
import websockets


@asyncio.coroutine
def main():
    ws = yield from websockets.connect('ws://localhost:8765')
    try:
        while True:
            name = input("Type message: ")
            yield from ws.send(name)
            response = yield from ws.recv()
            print("{}".format(response))
    finally:
        yield from ws.close()

asyncio.get_event_loop().run_until_complete(main())