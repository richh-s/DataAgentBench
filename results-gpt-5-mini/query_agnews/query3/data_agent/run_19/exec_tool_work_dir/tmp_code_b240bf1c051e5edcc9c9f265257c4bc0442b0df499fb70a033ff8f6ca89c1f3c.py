code = """import json
# var_call_FptZsboUs5IwWU1JjmsLWqRS is provided by previous query_db and contains the filepath to the full JSON result
path = var_call_FptZsboUs5IwWU1JjmsLWqRS
with open(path, 'r') as f:
    data = json.load(f)
# extract article_ids and convert to integers
article_ids = [int(item['article_id']) for item in data]
# produce a MongoDB filter JSON string with $in list
mongo_query = {"collection": "articles", "filter": {"article_id": {"$in": article_ids}}, "projection": {"article_id": 1, "title": 1, "description": 1}, "limit": 0}
import json
print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_call_FptZsboUs5IwWU1JjmsLWqRS': 'file_storage/call_FptZsboUs5IwWU1JjmsLWqRS.json'}

exec(code, env_args)
