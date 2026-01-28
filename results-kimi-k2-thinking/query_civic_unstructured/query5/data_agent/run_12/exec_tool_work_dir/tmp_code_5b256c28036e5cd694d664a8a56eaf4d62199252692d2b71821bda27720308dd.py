code = """import json
import pandas as pd
import re

# Load data
f = open(locals()['var_functions.query_db:5'], 'r')
funding_data = json.load(f)
f.close()

f = open(locals()['var_functions.query_db:0'], 'r')
civic_data = json.load(f)
f.close()

# Process DataFrames
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Find disaster projects
disaster_mask = funding_df['Project_Name'].str.contains('FEMA|Cal.OES|CalJPIA|disaster|recovery', case=False, na=False)
disaster_projects = funding_df[disaster_mask]

# Find 2022 projects from civic documents
projects_2022_list = []
for doc in civic_data:
    text = doc.get('text', '')
    if '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) < 100 and not line.startswith('('):
                if any(kw in line.lower() for kw in ['project', 'repair', 'improvement']):
                    projects_2022_list.append(line.split('(')[0].strip())

# Match funding
funding_2022 = disaster_projects[disaster_projects['Project_Name'].str.contains('2022', case=False, na=False)]
total_funding = funding_2022['Amount'].sum()

result = {'total_funding_2022': int(total_funding), 'projects_found': len(funding_2022)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'total_funding_2022': 0, 'total_disaster_funding': 1410000, 'disaster_2022_projects_count': 0}}

exec(code, env_args)
