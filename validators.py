# TODO: This should be provided by configuration
allowed_domains = ['fyndiq']
allowed_channels = ['friendly-pr-reviewers', 'backend_hub', 'directmessage']


async def validate_request(request):
    body = await request.post()

    team_domain = body.get('team_domain')
    if team_domain not in allowed_domains:
        return {}, f'Your domain {team_domain} is not allowed to use this command'

    channel_id = body.get('channel_id')
    channel_name = body.get('channel_name')
    if channel_name not in allowed_channels:
        return {}, f'The channel {channel_name} is not allowed to use this command'

    user_id = body.get('user_id')
    text = body.get('text')
    if not text.startswith("<http"):
        return {}, f'You need to provide a pull request link'

    return {
        'text': text,
        'user': user_id,
        'channel': channel_id
    }, None
