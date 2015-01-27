#!/usr/bin/env python
"""
Count the number of unique users.
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient()
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [
        {"$group": {"_id": "$created.user"},
                    "count": {"$sum": 1}}]

    return pipeline

def aggregate(db, pipeline):
    result = db.map.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('map')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)
