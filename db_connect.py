import motor.motor_asyncio


def init(db, collection):
    client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    db = client[db]
    collection = db[collection]
    return collection, db, client


async def do_find_one(db, collection, params):
    collection, *args = init(db, collection)
    document = await collection.find_one(params)
    return document

async def do_find_many(db, collection, params=None):
    collection, *args = init(db, collection)
    result_list =[]
    async for document in collection.find(params):
        result_list.append(document)
    return result_list

