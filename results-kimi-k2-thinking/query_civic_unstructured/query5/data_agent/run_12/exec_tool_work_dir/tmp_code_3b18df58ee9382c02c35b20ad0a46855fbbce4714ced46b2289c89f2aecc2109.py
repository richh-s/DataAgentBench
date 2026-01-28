code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    funding_data = json.load(f)

# Load civic documents  
with open(locals()['var_functions.query_db:0'], 'r') as f:
    civic_data = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Find disaster projects by funding source
fema_mask = funding_df['Project_Name'].str.contains('FEMA', case=False, na=False)
caloes_mask = funding_df['Project_Name'].str.contains('Cal.OES', case=False, na=False)
caljpia_mask = funding_df['Project_Name'].str.contains('CalJPIA', case=False, na=False)

combined_mask = fema_mask | caloes_mask | caljpia_mask

disaster_df = funding_df[combined_mask].copy()

# Find projects with 2022 in the name
twenty22_mask = disaster_df['Project_Name'].str.contains('2022', case=False, na=False)
twenty22_df = disaster_df[twenty22_mask]

total_funding = twenty22_df['Amount'].sum()
count = len(twenty22_df)

result = str(total_funding)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'total_funding_2022': 0, 'total_disaster_funding': 1410000, 'disaster_2022_projects_count': 0}, 'var_functions.execute_python:22': {'total_funding_2022': 0, 'project_count': 0}}

exec(code, env_args)
