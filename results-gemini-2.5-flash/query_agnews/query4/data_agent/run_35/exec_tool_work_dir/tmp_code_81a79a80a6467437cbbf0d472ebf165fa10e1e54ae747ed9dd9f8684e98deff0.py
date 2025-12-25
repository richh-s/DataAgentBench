code = """import pandas as pd
import json

with open(locals()['var_function-call-3584800626798106583'], 'r') as f:
    articles_2015_metadata = json.load(f)

article_ids_2015 = [article['article_id'] for article in articles_2015_metadata]

# Convert article_ids to integers for the MongoDB query
article_ids_2015_int = [int(article_id) for article_id in article_ids_2015]

# Prepare the query for MongoDB
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids_2015_int}},
    "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-3584800626798106583': 'file_storage/function-call-3584800626798106583.json'}

exec(code, env_args)
