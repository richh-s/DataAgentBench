code = """import json

# Load the MongoDB query that was generated
var_name = 'var_functions.execute_python:8'
mongo_query_path = locals()[var_name]

with open(mongo_query_path, 'r') as f:
    mongo_query_json = f.read()

# Parse it
mongo_query = json.loads(mongo_query_json)

# Get the article IDs and convert them to integers
raw_article_ids = mongo_query['filter']['article_id']['$in']
article_ids = [int(id_str) for id_str in raw_article_ids]

# Update the query with integer IDs
mongo_query['filter']['article_id']['$in'] = article_ids

print(f"Converting {len(raw_article_ids)} string IDs to integers")
print(f"First 5: {article_ids[:5]}")

# Create a new query string
mongo_query_str = json.dumps(mongo_query)

print('__RESULT__:')
print(mongo_query_str)"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': '14860', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {}}

exec(code, env_args)
