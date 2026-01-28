code = """import json
import re
import pandas as pd

# Read the civic documents from file
civic_docs_path = var_functions.query_db:2
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Total civic documents: {len(civic_docs)}")

# Read the funding data from file
funding_path = var_functions.query_db:5
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Total funding records: {len(funding_data)}")

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

print(f"Funding data loaded: {funding_df.shape}")

# Simple print format to check initial data
print("__RESULT__:")
print(f"Civic docs count: {len(civic_docs)}, Funding count: {len(funding_data)}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
