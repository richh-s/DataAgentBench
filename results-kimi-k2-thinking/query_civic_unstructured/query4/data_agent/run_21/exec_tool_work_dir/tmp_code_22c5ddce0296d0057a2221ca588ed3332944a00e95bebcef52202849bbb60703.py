code = """import json
import re

# Read the full civic_docs result from the file
with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")
print("\nFirst document structure:")
print(json.dumps(civic_docs[0], indent=2)[:2000])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
