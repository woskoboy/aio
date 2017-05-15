import os
import asyncio
import aiohttp

# BASE_URL = 'https://iqsha.ru/upload/lib/counting/tsifry'
# path = '{base_url}/{cc}_150.png'
BASE_URL = 'http://flupy.org/data/flags'
path = '{base_url}/{cc}/{cc}.gif'
CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.lower().split()
DIR = 'downloads/'


class NameException(Exception):
    def __init__(self, name):
        self.name = name


def save_img(img, cc):
    local_path = os.path.join(DIR, '{}.gif'.format(cc))
    print(cc,'file save as', local_path)
    with open(local_path, 'wb') as f:
        f.write(img)


@asyncio.coroutine
def get_file(cc):
    url = path.format(base_url=BASE_URL, cc=cc)
    resp = yield from aiohttp.request('GET', url=url)
    if resp.status == 200:
        print(cc, 'status 200 ok')
        img = yield from resp.read()
        return img
    else:
        raise NameException(cc)


@asyncio.coroutine
def download_one(cc, semaphore):
    try:
        with (yield from semaphore):
            img = yield from get_file(cc)
    except Exception as ex:
        raise NameException(cc) from ex
    else:
        save_img(img, cc)
        return cc


@asyncio.coroutine
def prepare(semaphore):
    result = []
    tasks = [download_one(cc, semaphore) for cc in CC]
    for task in asyncio.as_completed(tasks):
        try:
            fname = yield from task
            result.append(fname)
        except NameException as ex:
            print('Exception by download file %s.png' % ex.name)
        else:
            print('Task %s completed' % fname)
    return result

semaphore = asyncio.Semaphore(5)
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(prepare(semaphore))
# except asyncio.CancelledError:
#     print('Tasks has been canceled')
except Exception as e:
    print(repr(e))
finally:
    loop.close()
