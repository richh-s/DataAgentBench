code = """import json
import pandas as pd
import re

# Load funding data
f = open(locals()['var_functions.query_db:5'], 'r')
funding_data = json.load(f)
f.close()

# Load civic documents
f = open(locals()['var_functions.query_db:0'], 'r')
civic_data = json.load(f)
f.close()

# Process funding dataframe
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Identify disaster-related projects
pattern = r'FEMA|Cal.?OES|CalJPIA|disaster|recovery'
disaster_mask = funding_df['Project_Name'].str.contains(pattern, case=False, na=False)
disaster_df = funding_df[disaster_mask].copy()

# Sum all disaster funding first
total_disaster_funding = disaster_df['Amount'].sum()

# Check for explicit 2022 in project names
has_2022 = disaster_df['Project_Name'].str.contains('2022', case=False, na=False)
disaster_2022_df = disaster_df[has_2022].copy()
total_funding_2022 = disaster_2022_df['Amount'].sum()

# Simple result without problematic strings
result = {
    'total_funding_2022': int(total_funding_2022),
    'total_disaster_funding': int(total_disaster_funding),
    'disaster_2022_projects_count': len(disaster_2022_df)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
