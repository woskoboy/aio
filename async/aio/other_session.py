import aiohttp
import asyncio
import os


@asyncio.coroutine
def download_coroutine(session_, url):
    response = yield from session_.get(url)
    with open(os.path.basename(url), 'wb') as file:
        while True:
            chunk = yield from response.content.read()
            if not chunk:
                break
            file.write(chunk)
    yield from response.release()


@asyncio.coroutine
def main(loop):
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

    with aiohttp.ClientSession(loop=loop) as session:
        tasks = [download_coroutine(session, url) for url in urls]
        yield from asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
