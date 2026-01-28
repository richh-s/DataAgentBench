code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:0'], 'r') as f:
    civic_data = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Get disaster projects
disaster_df = funding_df[funding_df['Project_Name'].str.contains('FEMA|Cal\.?OES|CalJPIA', case=False, na=False)]

# Look for 2022 mentions in civic docs for each disaster project
matched_funding = 0
matched_names = []

for _, fund_row in disaster_df.iterrows():
    fund_name = fund_row['Project_Name']
    fund_amount = fund_row['Amount']
    
    clean_fund_name = fund_name.lower().split('(')[0].strip()
    
    # Search in civic docs
    for doc in civic_data:
        text = doc.get('text', '').lower()
        if '2022' in text and clean_fund_name in text:
            matched_funding += fund_amount
            matched_names.append(fund_name)
            break

# Also include projects with 2022 in their name
twenty22_direct = disaster_df[disaster_df['Project_Name'].str.contains('2022', case=False, na=False)]
for _, row in twenty22_direct.iterrows():
    if row['Project_Name'] not in matched_names:
        matched_funding += row['Amount']
        matched_names.append(row['Project_Name'])

result_dict = {
    'total_funding': int(matched_funding),
    'project_count': len(matched_names)
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'total_funding_2022': 0, 'total_disaster_funding': 1410000, 'disaster_2022_projects_count': 0}, 'var_functions.execute_python:22': {'total_funding_2022': 0, 'project_count': 0}, 'var_functions.execute_python:26': 0}

exec(code, env_args)
