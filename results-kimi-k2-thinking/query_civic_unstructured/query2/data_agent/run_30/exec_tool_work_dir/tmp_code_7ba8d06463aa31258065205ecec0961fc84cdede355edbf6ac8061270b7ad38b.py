code = """import json
import re

# Load the full civic documents data
civic_docs_file = var_functions.query_db:2
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load the full funding data
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Debug: Show a sample
print(f"Sample civic doc: {civic_docs[0]['filename']}")
print(f"Sample funding: {funding_data[0]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
