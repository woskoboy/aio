import json
from collections import defaultdict
import asyncio
from vk2slack.test import save_counts, read_counts
import aiohttp

TOKEN_VK = 'd4c469b1d4c469b1d4c469b18dd4984f49dd4c4d4c469b18ddb404ee3cf5d2e72933b4b'
GIDS = 30666517,  142410745, 54530371
# LAST_COUNTS = {30666517: 18820, 142410745: 45, 54530371: 5500}
METHOD = 'wall.get'
URL = 'https://api.vk.com/method/{method}?owner_id=-{gid}&v=5.64&access_token={token}&count={count}&offset={offset}'
POST = '<https://vk.com/public{gid}?w=wall-{gid}_{item_id}>'
SLACK_URL = 'https://hooks.slack.com/services/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'
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
        res = yield from session.get(URL.format(method=METHOD, gid=gid, token=TOKEN_VK, count=1, offset=0))
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
                res = yield from session.get(URL.format(method=METHOD, gid=gid, token=TOKEN_VK, count=c, offset=o))
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
