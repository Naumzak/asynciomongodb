import routes as routes
from aiohttp import web
from db_connect import *

routes = web.RouteTableDef()

@routes.post('/do_find_many/')
async def find_manyq(request):
    params_for_connection_to_db = await request.json()
    db = params_for_connection_to_db.get('db', 'test')
    collections = params_for_connection_to_db.get('collections', 'test')
    params = params_for_connection_to_db.get('params', None)
    result = await do_find_many(db, collections, params)
    return web.json_response({"info": result})


@routes.post('/do_find_one/')
async def find_one(request):
    params_for_connection_to_db= await request.json()
    db = params_for_connection_to_db.get('db', 'test')
    collections = params_for_connection_to_db.get('collections', 'test')
    params = params_for_connection_to_db.get('params', None)
    result = await do_find_one(collections, db, params)
    return web.json_response(result)

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)