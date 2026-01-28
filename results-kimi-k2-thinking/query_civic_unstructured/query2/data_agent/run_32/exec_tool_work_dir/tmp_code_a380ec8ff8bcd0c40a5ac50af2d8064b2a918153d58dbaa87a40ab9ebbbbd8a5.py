code = """import json
import pandas as pd
import re

# Load funding data
funding_file_path = locals()['var_functions.query_db:4']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file_path = locals()['var_functions.query_db:5']
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")

# Convert funding data to DataFrame
df_funding = pd.DataFrame(funding_data)
print(f"Funding DataFrame shape: {df_funding.shape}")
print(f"Funding columns: {df_funding.columns.tolist()}")
print("\nSample funding data:")
print(df_funding.head(3))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
