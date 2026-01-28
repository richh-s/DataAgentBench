code = """import json
import re

# Load MongoDB results - this is a list of documents
mongo_docs_path = locals()['var_functions.query_db:0']

# The variable is a string path to the JSON file, not the actual data
# Let's read the file
with open(mongo_docs_path, 'r') as f:
    mongo_docs = json.load(f)

print(f"Number of MongoDB documents: {len(mongo_docs)}")

# Let's examine the structure of one document
if mongo_docs:
    print(f"First document keys: {mongo_docs[0].keys()}")
    print(f"Sample text (first 500 chars): {mongo_docs[0]['text'][:500]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
