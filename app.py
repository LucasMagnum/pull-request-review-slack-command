import functools
import random

from aiohttp import web

from members import get as get_members
from validators import validate_request

# TODO: This should be provided by configuration
number_of_reviewers = 3
ignore_list = [
    'U0EPUDKRA'  # Hans
]


async def handle_command(request):
    data, error = await validate_request(request)

    if not error:
        text = data['text']
        members = await get_members(channel_id=data['channel'])

        if members:
            reviewers = get_random_reviewers(members, exclude=[data['user']])
            reviewers_text = ', '.join(
                f"<@{reviewer}>" for reviewer in reviewers[:number_of_reviewers]
            )

            return web.json_response({
                "text": f"Hey {reviewers_text} could you review this Pull Request?",
                "response_type": "ephemeral",
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

    exclude += ignore_list
    for user in exclude:
        users.remove(user)

    random.shuffle(users)
    return users[:number_of_reviewers]


app = web.Application()
app.add_routes([
    web.post('/', handle_command)
])

web.run_app(app, port=8000)
