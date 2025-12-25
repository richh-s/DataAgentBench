code = """import json

# Read the metadata result
with open(locals()['var_function-call-3168952214730479894'], 'r') as f:
    metadata_records = json.load(f)

# Extract article IDs
article_ids = [record['article_id'] for record in metadata_records]

# Just to be safe, convert to int if they are strings in the file but ints in Mongo, or vice-versa.
# The preview shows "article_id": "13", so they are strings in the JSON result from SQLite?
# Wait, SQLite query_db returns a list of records. If the column type is int, it might be returned as int or str depending on the tool implementation.
# The preview shows strings: "article_id": "13". 
# The DB description says `article_id` (int). 
# I will prepare a list of integers, because usually Mongo stores ints as ints.
# But I will also keep the mapping of article_id -> region.

article_id_to_region = {int(r['article_id']): r['region'] for r in metadata_records}
article_ids_int = list(article_id_to_region.keys())

print("__RESULT__:")
print(json.dumps(article_ids_int))"""

env_args = {'var_function-call-3168952214730479894': 'file_storage/function-call-3168952214730479894.json'}

exec(code, env_args)
