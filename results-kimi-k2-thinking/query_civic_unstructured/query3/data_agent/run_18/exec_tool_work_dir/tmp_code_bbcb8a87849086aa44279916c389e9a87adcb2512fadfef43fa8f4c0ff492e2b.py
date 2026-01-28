code = """import json
import re

# Load the funding data
with open('var_functions.query_db:2', 'r') as f:
    funding_data = json.load(f)

# Load the civic documents data
with open('var_functions.query_db:0', 'r') as f:
    civic_docs = json.load(f)

print(f"Number of funding records: {len(funding_data)}")
print(f"Number of civic documents: {len(civic_docs)}")
print(f"Sample funding record: {funding_data[0]}")
print(f"Sample civic document keys: {list(civic_docs[0].keys())}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
