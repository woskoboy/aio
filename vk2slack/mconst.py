TOKEN_VK = 'd4c469b1d4c469b1d4c469b18dd4984f49dd4c4d4c469b18ddb404ee3cf5d2e72933b4b'
GIDS = 30666517, 142410745, 54530371
METHOD = 'wall.get'
URL = 'https://api.vk.com/method/{method}?owner_id=-{gid}&v=5.64&access_token={token}'
POST = '<https://vk.com/public{gid}?w=wall-{gid}_{item_id}>'

SLACK_URL = 'https://hooks.slack.com/services/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'

# LAST_COUNTS = {30666517: 18820, 142410745: 45, 54530371: 5500}
URL_WITH_OFFSET = 'https://api.vk.com/method/{method}?owner_id=-{gid}&v=5.64&access_token={token}' \
                  '&count={count}&offset={offset}'
