import os
import asyncio
import aiohttp

DIR = 'downloads/'
BASE_URL = 'http://flupy.org/data/flags'
url_img = '{url}/{cc}/{cc}.gif'
CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ' \
     'ET EG DE IR TR CD FR'.lower().split()


def save_img(img, name):
    path = os.path.join(DIR, '{}.gif'.format(name))
    with open(path, 'wb') as f:
        f.write(img)


@asyncio.coroutine
def get_flag(code):

    url = url_img.format(url=BASE_URL, cc=code)

    with aiohttp.ClientSession() as session:
        resp = yield from session.request('GET', url=url)
        # resp = yield from aiohttp.request('GET', url=url)
        if resp.status == 200:
            print(code, 'status 200 ok')
            img = yield from resp.read()
            return img


@asyncio.coroutine
def download(cc):
    img = yield from get_flag(cc)
    save_img(img, cc)

loop = asyncio.get_event_loop()
coros = [download(cc) for cc in CC]
loop.run_until_complete(asyncio.wait(coros))
loop.close()
