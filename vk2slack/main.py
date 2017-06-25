import asyncio
import aiohttp
from vk2slack.mconst import *
# import vk
# import json
# import slacker
# import requests
from collections import defaultdict


SLACK_PAYLOADS = defaultdict()


@asyncio.coroutine
def get_posts(gid):
    with aiohttp.ClientSession() as session:
        res = yield from session.get(URL.format(method=METHOD, gid=gid, token=TOKEN_VK))
        if res.status == 200:
            content = yield from res.json()
            res.close()
            for item in content['response']['items']:
                link = POST.format(gid=gid, item_id=item['id'])
                SLACK_PAYLOADS['text'] = '{}\n{}'.format(link, item['text'])
                print(link)
                # res = yield from session.post(SLACK_URL, data=json.dumps(SLACK_PAYLOADS))
                # res.close()


@asyncio.coroutine
def prepare():
    tasks = [get_posts(gid) for gid in GIDS]
    yield from asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(prepare())
loop.close()
