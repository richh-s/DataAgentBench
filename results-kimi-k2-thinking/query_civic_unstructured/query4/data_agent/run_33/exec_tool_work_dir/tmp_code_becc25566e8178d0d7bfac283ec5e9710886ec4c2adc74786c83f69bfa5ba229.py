code = """import json

# Read the query result
with open('var_functions.query_db:8.json', 'r') as f:
    results = json.load(f)

print(f"Number of documents: {len(results)}")
print(f"First document keys: {list(results[0].keys())}")
print(f"Filename: {results[0]['filename']}")
print("\nText preview (first 500 chars):")
print(results[0]['text'][:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
