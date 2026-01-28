code = """import json
import pandas as pd

# Load funding data
f = open(locals()['var_functions.query_db:5'], 'r')
funding_data = json.load(f)
f.close()

# Load civic documents
f = open(locals()['var_functions.query_db:0'], 'r')
civic_data = json.load(f)
f.close()

# Process funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Find disaster projects
disaster_df = funding_df[funding_df['Project_Name'].str.contains('FEMA|Cal.OES|CalJPIA|disaster', case=False, na=False)]

# Find projects with 2022 in their name
projects_2022 = disaster_df[disaster_df['Project_Name'].str.contains('2022', case=False, na=False)]

# Sum funding
total_funding = projects_2022['Amount'].sum()

result = {'total_funding_2022': int(total_funding), 'project_count': len(projects_2022)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'total_funding_2022': 0, 'total_disaster_funding': 1410000, 'disaster_2022_projects_count': 0}}

exec(code, env_args)
