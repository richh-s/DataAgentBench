code = """import json, re
import pandas as pd

# load funding totals
with open(var_call_gnR6FFAxlLSWHKytbV5kC9xe, 'r', encoding='utf-8') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
# coerce total_amount to int
if not df_f.empty:
    df_f['total_amount'] = df_f['total_amount'].astype(int)

# disaster-related heuristic: FEMA/CalOES/CalJPIA or 'Disaster' in name
mask_disaster = df_f['Project_Name'].str.contains(r'FEMA|CalOES|CalJPIA|Disaster', case=False, regex=True, na=False)
df_dis = df_f[mask_disaster].copy()

# started in 2022: use project name containing '2022' (since start dates extraction failed)
mask_2022 = df_dis['Project_Name'].str.contains(r'2022', na=False)
df_2022 = df_dis[mask_2022]

total = int(df_2022['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding_disaster_projects_started_2022': total, 'projects_count': int(df_2022.shape[0]), 'projects': df_2022['Project_Name'].tolist()}))"""

env_args = {'var_call_BeorDsx8JrPIuB2mlCATPqZZ': ['Funding'], 'var_call_OADTgr7Ub1LCEk7c1kButQGv': ['civic_docs'], 'var_call_K2hwlcqqTZL2gfcVFExZ9mfr': 'file_storage/call_K2hwlcqqTZL2gfcVFExZ9mfr.json', 'var_call_EWFTxgYkLzCvdzSftlUYarES': {'disaster_projects_started_2022': [], 'count': 0}, 'var_call_gnR6FFAxlLSWHKytbV5kC9xe': 'file_storage/call_gnR6FFAxlLSWHKytbV5kC9xe.json'}

exec(code, env_args)
