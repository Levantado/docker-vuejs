from aiohttp import web
import aioredis
CLI = None


async def init_redis():
    redis = await aioredis.create_redis_pool('redis://redis-server')
    await redis.set('visitors', 0)
    return await redis
routes = web.RouteTableDef()

@routes.get('/get')
async def visitors(request):
    global CLI
    if not CLI:
        CLI = await init_redis()
    visitors = await CLI.incr('visitors')
    body = {'visitors': visitors}
    return web.json_response(body)

app = web.Application()
app.add_routes(routes)

web.run_app(app)