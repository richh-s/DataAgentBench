code = """import json
import pandas as pd
import re

# Get file paths
funding_path = locals()['var_functions.query_db:4']
civic_path = locals()['var_functions.query_db:5']

# Load and process funding data
with open(funding_path, 'r') as f:
    funding_raw = json.load(f)

df_funding = pd.DataFrame(funding_raw)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Load civic documents
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(df_funding)}")
print(f"Civic documents: {len(civic_docs)}")
print(f"Funding columns: {df_funding.columns.tolist()}")
print("\nSample funding data:")
print(df_funding.head())

# Look for park-related projects in funding data
park_projects = df_funding[df_funding['Project_Name'].str.contains('park', case=False, na=False)]
print(f"\nPark-related projects in funding data: {len(park_projects)}")
print(park_projects[['Project_Name', 'Amount']].head(10))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
