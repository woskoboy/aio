import json
from collections import defaultdict
import asyncio
from vk2slack.test import save_counts, read_counts
from vk2slack.mconst import *
import aiohttp


SLACK_PAYLOADS = defaultdict()

CONST = 10

LAST_COUNTS = read_counts()


def counter(gid, dif_count):
    print('{} has {} new posts'.format(gid, dif_count))
    cos = []
    if dif_count < CONST:
        cos.append((dif_count, 0))
    else:
        k, ost = divmod(dif_count, CONST)
        for offset in range(k):
            cos.append((CONST, CONST * offset))
        cos.append((ost, CONST*k))
    return cos


@asyncio.coroutine
def get_posts(gid):
    start_count = LAST_COUNTS[gid]
    with aiohttp.ClientSession() as session:
        res = yield from session.get(URL_WITH_OFFSET.format(method=METHOD, gid=gid, token=TOKEN_VK, count=1, offset=0))
        if res.status == 200:
            content = yield from res.json()
            last_count = content['response']['count']
            res.close()

            dif = last_count-start_count
            if not dif:
                print(gid, 'no have new posts')
                return

            cos = counter(gid, dif)
            for c, o in cos:
                res = yield from session.get(URL_WITH_OFFSET.format(method=METHOD, gid=gid, token=TOKEN_VK, count=c, offset=o))
                content = yield from res.json()
                for item in content['response']['items']:
                    link = POST.format(gid=gid, item_id=item['id'])
                    SLACK_PAYLOADS['text'] = '{}\n{}'.format(link, item['text'])
                    print(link)
                    res = yield from session.post(SLACK_URL, data=json.dumps(SLACK_PAYLOADS))
                    res.close()

            LAST_COUNTS[gid] = last_count
            save_counts(LAST_COUNTS)


@asyncio.coroutine
def prepare():
    tasks = [get_posts(gid) for gid in GIDS]
    yield from asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(prepare())
finally:
    loop.close()
