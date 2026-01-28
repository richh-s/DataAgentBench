code = """import json
import re

# Load the MongoDB query result - preview shows it's a list of documents
# The full result is stored in a JSON file, let's read it
with open('var_functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

print(f"Number of civic documents retrieved: {len(civic_docs)}")
print("\nFirst document preview:")
print(json.dumps(civic_docs[0], indent=2)[:2000])"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
