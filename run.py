import asyncio
from aiohttp import web
from app import create_app
from app.db import Base, engine
from app.models.ad import Ad

async def init_app():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return create_app()

if __name__ == "__main__":
    web.run_app(init_app(), port=5000, host="0.0.0.0")
