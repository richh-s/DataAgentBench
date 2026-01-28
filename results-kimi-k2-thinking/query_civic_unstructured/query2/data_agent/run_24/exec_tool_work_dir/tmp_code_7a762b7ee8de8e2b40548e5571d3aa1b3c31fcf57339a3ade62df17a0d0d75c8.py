code = """import json
import re

# Load the civic documents data from the file path
with open('/tmp/tmpw8a01a0z.json', 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")
print(f"\nFirst document structure:")
print(json.dumps(civic_docs[0], indent=2)[:2000])  # Print first 2000 chars"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
