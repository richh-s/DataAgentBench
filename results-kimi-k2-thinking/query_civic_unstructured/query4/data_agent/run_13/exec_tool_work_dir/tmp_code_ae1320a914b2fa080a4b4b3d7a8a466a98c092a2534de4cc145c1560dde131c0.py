code = """import json
import re
from datetime import datetime

# Load civic documents data
civic_docs_file = var_functions.query_db:4
with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

# Load funding data
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} civic documents")
print(f"Loaded {len(funding_data)} funding records")

# Preview the structure
print("\nFirst civic doc preview:")
print(json.dumps(civic_docs_data[0], indent=2)[:1000])

print("\nFirst funding record:")
print(json.dumps(funding_data[0], indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
