code = """import json
import re

# Read the MongoDB query results
with open('/tmp/tmp4b1e1x7g.json', 'r') as f:
    mongo_results = json.load(f)

print(f"Number of documents: {len(mongo_results)}")
print("First document preview:")
print(mongo_results[0]['text'][:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
