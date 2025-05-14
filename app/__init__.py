from aiohttp import web
from app.routes.ad_routes import routes

def create_app():
    app = web.Application()
    app.add_routes(routes)
    return app
