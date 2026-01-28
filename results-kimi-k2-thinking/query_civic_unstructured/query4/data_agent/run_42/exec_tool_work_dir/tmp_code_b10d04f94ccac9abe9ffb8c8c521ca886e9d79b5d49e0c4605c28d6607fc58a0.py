code = """import json
import re
import os

# Try to access the MongoDB results
mongo_result = var_functions.query_db:2

# Check if it's a file path or direct data
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        mongo_docs = json.load(f)
elif isinstance(mongo_result, list):
    mongo_docs = mongo_result
else:
    print(f"Unexpected type: {type(mongo_result)}")
    mongo_docs = []

print(f"Number of documents: {len(mongo_docs)}")

# Let's examine the first document to understand the structure
if mongo_docs:
    print("First document keys:", list(mongo_docs[0].keys()))
    print("First document filename:", mongo_docs[0].get('filename'))
    # Print a snippet of the text
    text_snippet = mongo_docs[0].get('text', '')[:500]
    print("Text snippet:", text_snippet[:200])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
