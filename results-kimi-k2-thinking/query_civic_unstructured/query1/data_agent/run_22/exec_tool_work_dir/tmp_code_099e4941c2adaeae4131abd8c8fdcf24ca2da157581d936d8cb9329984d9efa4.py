code = """import json
import re

# Read the funding data from the file
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Read the civic documents data from the file
with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

# Print info about the data
print(f"Total funding records: {len(funding_data)}")
print(f"Total civic documents: {len(civic_docs)}")

# Extract the first few records to see structure
print(f"\nFirst funding record: {funding_data[0]}")
print(f"\nFirst civic doc (keys): {list(civic_docs[0].keys())}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
