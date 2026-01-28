code = """import json
import re

# Read the civic documents from the file
with open('var_functions.query_db:0', 'r') as f:
    civic_docs = json.load(f)

# Read the funding data from the file
with open('var_functions.query_db:5', 'r') as f:
    funding_data = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")
print(f"Number of funding records: {len(funding_data)}")
print("\nFirst civic doc preview:")
print(civic_docs[0]['text'][:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
