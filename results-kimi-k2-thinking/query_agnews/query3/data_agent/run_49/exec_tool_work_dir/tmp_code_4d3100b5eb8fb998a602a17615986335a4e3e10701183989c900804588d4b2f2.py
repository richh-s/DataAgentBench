code = """import json

# Load the MongoDB query that was generated
var_name = 'var_functions.execute_python:12'
mongo_query_path = locals()[var_name]

with open(mongo_query_path, 'r') as f:
    mongo_query_json = f.read()

# Parse it
mongo_query = json.loads(mongo_query_json)

# Get the article IDs
article_ids = mongo_query['filter']['article_id']['$in']

print(f"Total article IDs to query: {len(article_ids)}")
print(f"First 10: {article_ids[:10]}")
print(f"Last 10: {article_ids[-10:]}")

# Define batching
batch_size = 500
num_batches = (len(article_ids) + batch_size - 1) // batch_size

print(f"Will process in {num_batches} batches of {batch_size}")

# Import needed function
def batch_list(lst, n):
    """Yield successive n-sized chunks from list."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

for batch_num, article_ids_batch in enumerate(batch_list(article_ids, batch_size)):
    print(f"Batch {batch_num+1}/{num_batches}: {len(article_ids_batch)} articles")

print('__RESULT__:')
print(json.dumps({'total_articles': len(article_ids), 'batches': num_batches}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': '14860', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {}, 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
