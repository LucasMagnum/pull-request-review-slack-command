import os

import aiohttp
from async_lru import alru_cache


async def get(channel_id):
    members = []

    try:
        members = await _get_members_from_channel(channel_id)
    except Exception:
        pass

    return members


@alru_cache(maxsize=None)
async def _get_members_from_channel(channel_id):
    channel_info_url = 'https://slack.com/api/channels.info'
    token = os.getenv('SLACK_OAUTH_TOKEN')

    params = {
        'token': token,
        'channel': channel_id
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(channel_info_url, params=params) as resp:
            channel = await resp.json()

    return channel['channel']['members'] if 'channel' in channel else None
