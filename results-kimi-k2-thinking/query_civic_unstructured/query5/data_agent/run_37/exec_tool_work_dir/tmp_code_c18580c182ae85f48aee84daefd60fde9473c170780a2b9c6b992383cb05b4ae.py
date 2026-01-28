code = """import json
import pandas as pd
import re

# Load data
f_file = locals()['var_functions.query_db:9']
with open(f_file, 'r') as f:
    funding_data = json.load(f)

c_file = locals()['var_functions.query_db:5']
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Identify disaster projects from funding data
keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster']
mask = funding_df['Project_Name'].str.contains('|'.join(keywords), case=False, na=False)
disaster_funding = funding_df[mask].copy()

result = {
    'total_disaster_funding': int(disaster_funding['Amount'].sum()),
    'disaster_project_count': len(disaster_funding),
    'sample_projects': disaster_funding[['Project_Name', 'Amount']].head(5).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
