from aiohttp import web

from app import config, views


service = web.Application()
service.add_routes([
    web.post('/', views.handle_command)
])


if __name__ == '__main__':
    web.run_app(service, port=config.PORT)
