from pymongo import MongoClient
import pandas as pd
from common_scaffold.config import MONGO_URI

def get_mongo_client():
    return MongoClient(MONGO_URI)

def mongo_query(db_name, collection_name, query={}, projection=None):
    client = get_mongo_client()
    db = client[db_name]
    cursor = db[collection_name].find(query, projection)
    df = pd.DataFrame(list(cursor))
    return df
