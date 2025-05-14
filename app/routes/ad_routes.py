from aiohttp import web
from app.models.ad import Ad
from app.db import AsyncSessionLocal
from sqlalchemy.future import select

routes = web.RouteTableDef()

@routes.post("/ads/")
async def create_ad(request):
    data = await request.json()
    async with AsyncSessionLocal() as session:
        ad = Ad(
            title=data["title"],
            description=data.get("description", ""),
            owner=data["owner"]
        )
        session.add(ad)
        await session.commit()
        await session.refresh(ad)
        return web.json_response({"id": ad.id}, status=201)

@routes.get("/ads/{ad_id}")
async def get_ad(request):
    ad_id = int(request.match_info["ad_id"])
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Ad).where(Ad.id == ad_id))
        ad = result.scalar_one_or_none()
        if ad is None:
            return web.json_response({"error": "Not found"}, status=404)
        return web.json_response({
            "id": ad.id,
            "title": ad.title,
            "description": ad.description,
            "created_at": ad.created_at.isoformat(),
            "owner": ad.owner
        })

@routes.delete("/ads/{ad_id}")
async def delete_ad(request):
    ad_id = int(request.match_info["ad_id"])
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Ad).where(Ad.id == ad_id))
        ad = result.scalar_one_or_none()
        if ad is None:
            return web.json_response({"error": "Not found"}, status=404)
        await session.delete(ad)
        await session.commit()
        return web.json_response({"message": "Ad deleted"})
