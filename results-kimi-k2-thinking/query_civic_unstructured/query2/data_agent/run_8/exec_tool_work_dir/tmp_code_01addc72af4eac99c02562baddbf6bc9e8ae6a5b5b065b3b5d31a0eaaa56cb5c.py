code = """import json
import pandas as pd
import re

# Get the file paths from storage variables
civic_docs_path = locals().get('var_functions.query_db:0')
funding_path = locals().get('var_functions.query_db:1')

print("Paths from variables:")
print("Civic docs:", civic_docs_path)
print("Funding:", funding_path)

# Read the data files
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"\nSuccessfully loaded data:")
print(f"Number of civic documents: {len(civic_docs_data)}")
print(f"Number of funding records: {len(funding_data)}")

# Show sample of data
print("\nFirst civic doc keys:")
print(list(civic_docs_data[0].keys()))

print("\nFirst funding record:")
print(funding_data[0])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
