import asyncio
import aiohttp
# import vk
# import json
# import slacker
# import requests
from collections import defaultdict

TOKEN_VK = 'd4c469b1d4c469b1d4c469b18dd4984f49dd4c4d4c469b18ddb404ee3cf5d2e72933b4b'
GIDS = 30666517, 142410745, 54530371
METHOD = 'wall.get'
URL = 'https://api.vk.com/method/{method}?owner_id=-{gid}&v=5.64&access_token={token}'
POST = '<https://vk.com/public{gid}?w=wall-{gid}_{item_id}>'

SLACK_URL = 'https://hooks.slack.com/services/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'
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
