code = """import json
import pandas as pd
import re

# Let's check what variables are available
available_vars = [k for k in locals().keys() if 'var_functions' in k]
print("Available variables:", available_vars)

# Check the values
civic_docs_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

print("\nCivic docs path type:", type(civic_docs_path))
print("Funding path type:", type(funding_path))

# Check if they're strings (file paths) or already loaded data
if isinstance(civic_docs_path, str):
    print("Civic docs is a file path:", civic_docs_path[:100])
    # Load from file
    with open(civic_docs_path, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = civic_docs_path
    print("Civic docs is already loaded")

if isinstance(funding_path, str):
    print("Funding is a file path:", funding_path[:100])
    # Load from file
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_path
    print("Funding is already loaded")

print("\nLoaded data:")
print("Civic docs length:", len(civic_docs_data) if isinstance(civic_docs_data, list) else "Not a list")
print("Funding data length:", len(funding_data) if isinstance(funding_data, list) else "Not a list")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
