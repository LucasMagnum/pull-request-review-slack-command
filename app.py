import functools
import random

from aiohttp import web

from reviewers import get as get_reviewers
from validators import validate_request

# TODO: This should be provided by configuration
number_of_reviewers = 3


async def handle_command(request):
    data, error = await validate_request(request)

    if not error:
        text = data['text']
        reviewers_list = await get_reviewers(
            channel_name=data['channel_name'],
            exclude=data['user']
        )
        random.shuffle(reviewers_list)

        reviewers = ', '.join(
            f"<@{reviewer}>" for reviewer in reviewers_list[:number_of_reviewers]
        )

        return web.json_response({
            "text": f"Hey {reviewers} could you review this Pull Request?",
            "response_type": "in_channel",
            "attachments": [
                {
                    "text": f"Pull request {text}"
                }
            ]
        })

    return web.json_response({
        "response_type": "ephemeral",
        "text": error
    })


app = web.Application()
app.add_routes([
    web.post('/', handle_command)
])

web.run_app(app, port=8000)
