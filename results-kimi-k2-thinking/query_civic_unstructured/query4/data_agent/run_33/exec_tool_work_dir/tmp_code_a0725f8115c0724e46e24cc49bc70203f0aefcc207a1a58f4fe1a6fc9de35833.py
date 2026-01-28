code = """import json
import re

# Read both query results
with open('var_functions.query_db:2.json', 'r') as f:
    result_all = json.load(f)

with open('var_functions.query_db:5.json', 'r') as f:
    result_spring = json.load(f)

print(f"Total documents in first query: {len(result_all)}")
print(f"Total documents in second query: {len(result_spring)}")

# Show first few documents to understand structure
if result_all:
    print(f"Sample document structure: {list(result_all[0].keys())}")
    print(f"Sample filename: {result_all[0]['filename']}")
    print(f"Sample text preview: {result_all[0]['text'][:200]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
