# TODO: This should be provided by configuration
allowed_domains = ['fyndiq']
allowed_channels = ['friendly-pr-reviewers', 'backend_hub', 'directmessage']


def validate(data):
    """
    Validate data payload.

    Args:
        data = {
            'team_domain': 'Co AB',
            'channel_id': 'UX12312',
            'channel_name': 'mychannel',
            'user_id': 'UXASD1231',
            'text': '<http://github.com/fyndiq/>'
        }

    Rules:
        - Team domain should be in the allowed domains
        - Channel name should be in the allowed channels
        - Text should start with an url

    Response:
        Return relevant data and the error response if it's invalid

    """
    team_domain = data.get('team_domain')
    if team_domain not in allowed_domains:
        return {}, f'Your domain {team_domain} is not allowed to use this command'

    channel_name = data.get('channel_name')
    if channel_name not in allowed_channels:
        return {}, f'The channel {channel_name} is not allowed to use this command'

    text = data.get('text')
    if not text.startswith("<http"):
        return {}, f'You need to provide a pull request link'

    channel_id = data.get('channel_id')
    user_id = data.get('user_id')

    return {
        'text': text,
        'user': user_id,
        'channel': channel_id
    }, None
