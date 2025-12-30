code = """import re, json
import pandas as pd

# load funding data
with open(var_call_3kTvWOoxh8m1tGrpZQqhV9eX, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)

# Disaster-related projects: names containing FEMA, CalOES, CalJPIA
mask_disaster = funding_df['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, regex=True)

# 2022 projects: names containing '2022'
mask_2022 = funding_df['Project_Name'].str.contains('2022', case=False, regex=False)

filtered = funding_df[mask_disaster & mask_2022].copy()

# convert Amount to int
filtered['Amount'] = filtered['Amount'].astype(int)

total = int(filtered['Amount'].sum())

result = {"total_disaster_funding_2022": total, "matching_projects": filtered[['Funding_ID','Project_Name','Amount']].to_dict(orient='records')}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_L0EK6EZ4bhOie1wj99oXoxPO': 'file_storage/call_L0EK6EZ4bhOie1wj99oXoxPO.json', 'var_call_3kTvWOoxh8m1tGrpZQqhV9eX': 'file_storage/call_3kTvWOoxh8m1tGrpZQqhV9eX.json'}

exec(code, env_args)
