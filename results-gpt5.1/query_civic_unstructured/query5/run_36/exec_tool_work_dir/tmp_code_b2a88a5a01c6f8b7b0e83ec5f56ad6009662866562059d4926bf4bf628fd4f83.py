code = """import json, re, pandas as pd

# Load full funding data
path = var_call_mBKTNmg99B2e9tFZMzW17jch
with open(path, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Disaster-related projects: names containing FEMA, CalOES, CalJPIA, or explicitly 'Disaster' if present
pattern = re.compile(r'(FEMA|CalOES|CalJPIA)', re.IGNORECASE)
disaster_df = funding_df[funding_df['Project_Name'].str.contains(pattern)]

# For start year 2022, infer from project name if it starts with '2022 ' or contains ' 2022 ' etc.
starts_2022 = disaster_df['Project_Name'].str.contains(r'2022', regex=True)

total_2022_disaster = int(disaster_df[starts_2022]['Amount'].sum())

result = {"total_2022_disaster_funding": total_2022_disaster}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_yujtWhihEr9gOMvX9ITHVmPr': 'file_storage/call_yujtWhihEr9gOMvX9ITHVmPr.json', 'var_call_mBKTNmg99B2e9tFZMzW17jch': 'file_storage/call_mBKTNmg99B2e9tFZMzW17jch.json'}

exec(code, env_args)
