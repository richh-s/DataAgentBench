code = """import json
import pandas as pd
import os

# Load funding data
funding_file = "/tmp/tmp4g9x7lxn.json"
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        content = f.read().strip()
        funding_data = json.loads(content) if content.startswith('[') else []
else:
    funding_data = []

funding_df = pd.DataFrame(funding_data)
if not funding_df.empty:
    funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Get park-related funding projects
park_funding = funding_df[funding_df['Project_Name'].str.contains('park', case=False, na=False)]

# Simple approach: sum up park project funding
if not park_funding.empty:
    total_funding = park_funding['Amount'].sum()
    project_count = len(park_funding)
    
    result = {
        'total_funding': int(total_funding),
        'project_count': int(project_count),
        'projects': park_funding[['Project_Name', 'Amount', 'Funding_Source']].to_dict('records')
    }
else:
    result = {'total_funding': 0, 'project_count': 0, 'projects': []}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
