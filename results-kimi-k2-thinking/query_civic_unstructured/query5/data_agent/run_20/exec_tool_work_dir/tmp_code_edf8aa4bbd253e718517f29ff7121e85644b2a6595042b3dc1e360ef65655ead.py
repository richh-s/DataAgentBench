code = """import json
import re

# Load civic docs data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# Preview first doc structure
print("\nFirst doc keys:", list(civic_docs[0].keys()))
print("\nFirst doc filename:", civic_docs[0]['filename'])
print("\nFirst doc text sample:", civic_docs[0]['text'][:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
