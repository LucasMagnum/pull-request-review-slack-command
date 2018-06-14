import os
import random

from aiohttp import web

from app import config, members, validators


async def handle_command(request):
    body = await request.post()
    data, error = validators.validate(body)

    if not error:
        text = data['text']
        members_list = await members.get(channel_id=data['channel'])

        if members_list:
            reviewers = get_random_reviewers(members_list, exclude=[data['user']])
            reviewers_text = ', '.join(
                f"<@{reviewer}>" for reviewer in reviewers
            )

            return web.json_response({
                "text": f"Hey {reviewers_text} could you review this Pull Request?",
                "response_type": "in_channel",
                "attachments": [
                    {
                        "text": f"Pull request {text}"
                    }
                ]
            })
        else:
            error = f"Failed to get the reviewers. Try again"

    return web.json_response({
        "response_type": "ephemeral",
        "text": error
    })


def get_random_reviewers(users, exclude=None):
    users = users[:]

    if exclude is None:
        exclude = []

    exclude += config.BLACKLIST_REVIEWERS
    for user in exclude:
        users.remove(user)

    random.shuffle(users)
    return users[:config.NUMBER_OF_REVIEWERS]
