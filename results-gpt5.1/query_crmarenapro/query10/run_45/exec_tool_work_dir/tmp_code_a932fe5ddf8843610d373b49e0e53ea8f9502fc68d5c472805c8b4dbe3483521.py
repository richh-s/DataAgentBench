code = """import json, pandas as pd
cases = pd.DataFrame(var_call_WpYmxPzcAn8EW8pZnbuFHaBH)
all_cases_path = var_call_ZUiWiA5E1dQpRUHAidBEhaEa
with open(all_cases_path, 'r') as f:
    all_cases = pd.DataFrame(json.load(f))

# Normalize IDs by stripping leading '#'
for df in (cases, all_cases):
    df['case_id'] = df['case_id'].astype(str).str.lstrip('#')
    if 'initial_owner_id' in df.columns:
        df['initial_owner_id'] = df['initial_owner_id'].astype(str).str.lstrip('#')
    if 'agent_id' in df.columns:
        df['agent_id'] = df['agent_id'].astype(str).str.lstrip('#')

# Merge to get initial owner (for transfer logic handle time policy; here all handle time on initial owner)
merged = cases.merge(all_cases[['case_id','initial_owner_id']], on='case_id', how='left')

# Compute handle time in hours
for col in ['createddate','closeddate']:
    merged[col] = pd.to_datetime(merged[col])
merged['handle_hours'] = (merged['closeddate'] - merged['createddate']).dt.total_seconds() / 3600.0

# We treat handle time against the initial owner only
merged['owner_for_ht'] = merged['initial_owner_id']

# Aggregate per agent
agg = merged.groupby('owner_for_ht').agg(cases_handled=('case_id','nunique'), avg_handle_hours=('handle_hours','mean')).reset_index()
# Filter agents who processed more than one case
filtered = agg[agg['cases_handled'] > 1]

if filtered.empty:
    result = None
else:
    # Lowest average handle time
    best = filtered.sort_values(['avg_handle_hours','owner_for_ht']).iloc[0]
    result = best['owner_for_ht']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_WpYmxPzcAn8EW8pZnbuFHaBH': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'case_id': '500Wt00000DDepmIAD'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'case_id': '500Wt00000DDyzpIAD'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'case_id': '500Wt00000DDzUPIA1'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'case_id': '500Wt00000DDzsbIAD'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'case_id': '#500Wt00000DDzscIAD'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'case_id': '500Wt00000DDzuEIAT'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'case_id': '#500Wt00000DE02HIAT'}], 'var_call_ooRK0qlMfpgLTcjJkvER37C8': [], 'var_call_ZUiWiA5E1dQpRUHAidBEhaEa': 'file_storage/call_ZUiWiA5E1dQpRUHAidBEhaEa.json'}

exec(code, env_args)
