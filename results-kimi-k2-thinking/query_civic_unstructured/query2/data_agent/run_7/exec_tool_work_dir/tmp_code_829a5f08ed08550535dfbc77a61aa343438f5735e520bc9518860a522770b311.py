code = """import json
# Read the full MongoDB result
with open('var_functions.query_db:2') as f:
    result = json.load(f)

print(f"Number of documents: {len(result)}")
print("Document structure:")
print(json.dumps(result[0], indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
