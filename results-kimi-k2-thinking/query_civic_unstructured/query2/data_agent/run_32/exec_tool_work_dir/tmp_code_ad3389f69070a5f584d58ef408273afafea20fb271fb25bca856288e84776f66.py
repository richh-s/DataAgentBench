code = """import json
import pandas as pd

# Load funding data
funding_path = locals()['var_functions.query_db:4']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
civic_path = locals()['var_functions.query_db:5']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Process funding data
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

print('Funding records count:', len(df_funding))
print('Civic documents count:', len(civic_docs))
print('Funding columns:', df_funding.columns.tolist())

# Find park-related projects in funding data
park_keywords = ['park', 'playground', 'bluff']
park_mask = df_funding['Project_Name'].str.contains('|'.join(park_keywords), case=False, na=False)
park_projects = df_funding[park_mask]

print('Park-related funding projects:', len(park_projects))
print(park_projects[['Project_Name', 'Amount']].head(10).to_string())"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
