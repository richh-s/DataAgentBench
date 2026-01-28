code = """import json
import re

# Read the full result from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")

# Let's explore the structure
print(f"First document keys: {list(civic_docs[0].keys())}")
print(f"Sample filename: {civic_docs[0]['filename']}")
print(f"Sample text (first 500 chars): {civic_docs[0]['text'][:500]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
