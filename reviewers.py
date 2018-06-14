from async_lru import alru_cache

reviewers = [
    'Viktor',
    'Ghassen',
    'Lucas',
    'Simon',
    'Dildar',
]


async def get(channel_name=None, exclude=None):
    if channel_name is not None:
        return await _get_reviews_from_channel(channel_name)
    return reviewers


@alru_cache(maxsize=None)
async def _get_reviews_from_channel(channel_name):
    return reviewers
