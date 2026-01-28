code = """import json
import os

# Read the query results from the file path stored in the variable
file_path = 'var_functions.query_db:6'

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        mongo_results = json.load(f)
else:
    # Fall back to reading from the variable directly
    mongo_results = locals().get('var_functions.query_db:6', [])

print(f"Found {len(mongo_results)} documents")

# Let's examine the first document to understand structure
if mongo_results:
    print(f"First document keys: {list(mongo_results[0].keys())}")
    print(f"Sample text preview: {mongo_results[0].get('text', '')[:500]}")

print('__RESULT__:')
print(json.dumps({'count': len(mongo_results), 'sample': mongo_results[0] if mongo_results else None}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
