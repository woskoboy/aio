import os
import asyncio
import aiohttp

DIR = 'downloads/'
URL = 'http://flupy.org/data/flags/{name}/{name}.gif'
CC = 'CN IN US ID BR PK NG BD RU JP MX ' \
     'PH VN ET EG DE IR TR CD FR'.lower().split()


class FlagException(Exception):
    def __init__(self, cc):
        self.name = cc


def save_img(img, cc):
    local_path = os.path.join(DIR, '%s.gif' % cc)
    with open(local_path, 'wb') as f:
        f.write(img)


@asyncio.coroutine
def get_file(cc):
    url = URL.format(name=cc)
    with aiohttp.ClientSession() as session:
        resp = yield from session.request('GET', url=url)
        if resp.status == 200:
            # data = yield from resp.read()
            return (yield from resp.read())  # data
        else:
            raise FlagException(cc)


@asyncio.coroutine
def download_one(cc, semaphore):
    try:
        with (yield from semaphore):
            img = yield from get_file(cc)
    except FlagException as fe:
        return "Flag %s do not download" % fe.name
    else:
        save_img(img, cc)
        return 'File %s was saved' % cc


@asyncio.coroutine
def prepare(semaphore):
    tasks = [download_one(cc, semaphore) for cc in sorted(CC)]
    gen_completed = asyncio.as_completed(tasks)
    for task in gen_completed:
        result = yield from task
        print(result)

semaphore_ = asyncio.Semaphore(5)
loop = asyncio.get_event_loop()
loop.run_until_complete(prepare(semaphore_))
loop.close()
# BASE_URL = 'http://127.0.0.1:8000/static'
# path = '{base_url}/{file_name}.jpg'
# DIR = 'downloads/'
# BASE_URL = 'https://iqsha.ru/upload/lib/counting/tsifry'
# url_img = '{url}/{cc}_150.png'
# # except asyncio.CancelledError:
# #     print('Tasks has been canceled')
# except Exception as e:
#     print(repr(e))
# finally:
