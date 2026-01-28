code = """import json
import re

# Access the data from variables
funding_var = locals()['var_functions.query_db:5']
civic_var = locals()['var_functions.query_db:2']

print(f"Funding variable type: {type(funding_var)}")
print(f"Civic variable type: {type(civic_var)}")

# Load data based on whether it's a file path or direct data
if isinstance(funding_var, str) and '.json' in funding_var:
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_var
    
if isinstance(civic_var, str) and '.json' in civic_var:
    with open(civic_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_var

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Show sample data
print(f"\nFunding sample keys: {list(funding_data[0].keys()) if funding_data else 'N/A'}")
print(f"Civic sample keys: {list(civic_docs[0].keys()) if civic_docs else 'N/A'}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
