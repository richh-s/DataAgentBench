code = """import pandas as pd
import json

with open(locals()['var_function-call-2126214902618498647'], 'r') as f:
    article_metadata_2015 = json.load(f)

article_ids_2015 = [article['article_id'] for article in article_metadata_2015]

# Prepare the query for MongoDB
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids_2015}},
    "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-2126214902618498647': 'file_storage/function-call-2126214902618498647.json'}

exec(code, env_args)
