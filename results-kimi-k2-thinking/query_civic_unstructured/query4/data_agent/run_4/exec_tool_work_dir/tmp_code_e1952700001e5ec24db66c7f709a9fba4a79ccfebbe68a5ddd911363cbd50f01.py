code = """import json
import re
from datetime import datetime

# Load the full MongoDB results from the file
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Load the full Funding data from the file
with open('var_functions.query_db:4', 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# Let's examine the structure of the data
print(f"\nFirst civic document keys: {list(civic_docs[0].keys()) if civic_docs else 'No documents'}")
print(f"First funding record keys: {list(funding_data[0].keys()) if funding_data else 'No funding'}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
