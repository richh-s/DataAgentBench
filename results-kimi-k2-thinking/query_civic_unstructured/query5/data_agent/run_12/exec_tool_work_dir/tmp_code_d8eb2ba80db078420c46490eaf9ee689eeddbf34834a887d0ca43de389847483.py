code = """import json
import pandas as pd

# Load data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:0'], 'r') as f:
    civic_data = json.load(f)

# Process funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Find disaster projects
disaster_df = funding_df[funding_df['Project_Name'].str.contains('FEMA|Cal.OES|CalJPIA', case=False, na=False)]

# Find projects with 2022 in their names
projects_2022 = disaster_df[disaster_df['Project_Name'].str.contains('2022', case=False, na=False)]

total = int(projects_2022['Amount'].sum())
count = len(projects_2022)

# Look for more matches in civic docs
additional_funding = 0
for _, fund_row in disaster_df.iterrows():
    fund_name = fund_row['Project_Name']
    
    # Check if this project appears in civic docs with 2022
    for doc in civic_data:
        text = doc.get('text', '')
        if '2022' in text:
            clean_fund = fund_name.lower().split('(')[0].strip()
            if clean_fund in text.lower():
                additional_funding += fund_row['Amount']
                break

result = {'total_funding_2022': total + additional_funding}

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'total_funding_2022': 0, 'total_disaster_funding': 1410000, 'disaster_2022_projects_count': 0}, 'var_functions.execute_python:22': {'total_funding_2022': 0, 'project_count': 0}, 'var_functions.execute_python:26': 0}

exec(code, env_args)
