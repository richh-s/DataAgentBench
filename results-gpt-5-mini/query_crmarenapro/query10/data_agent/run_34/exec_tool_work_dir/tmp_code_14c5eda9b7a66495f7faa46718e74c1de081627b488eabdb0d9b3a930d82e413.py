code = """import json
import pandas as pd
from datetime import datetime

# Load large owner assignment data from file path variable
owner_assignments_path = var_call_miPtpuiGlCi6TkRFSNIZbKej
with open(owner_assignments_path, 'r', encoding='utf-8') as f:
    owner_assignments = json.load(f)

cases_closed = var_call_oV7MtJHO6JOKKdeXdTLuAcDZ

# Build DataFrames
df_oa = pd.DataFrame(owner_assignments)
df_cases = pd.DataFrame(cases_closed)

# Clean ID-like fields: strip whitespace and leading '#'
for col in ['caseid__c', 'oldvalue__c', 'newvalue__c']:
    if col in df_oa.columns:
        df_oa[col] = df_oa[col].astype(str).str.strip().str.lstrip('#')

for col in ['id', 'ownerid']:
    if col in df_cases.columns:
        df_cases[col] = df_cases[col].astype(str).str.strip().str.lstrip('#')

# Parse datetimes
if 'createddate' in df_oa.columns:
    df_oa['createddate'] = pd.to_datetime(df_oa['createddate'], errors='coerce')
if 'createddate' in df_cases.columns:
    df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], errors='coerce')
if 'closeddate' in df_cases.columns:
    df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'], errors='coerce')

# Define window
window_start = pd.to_datetime('2023-05-02')
window_end = pd.to_datetime('2023-09-02')

# Agent case counts in the window (count assignments where agent was assigned in window)
mask_window_oa = (df_oa['createddate'] >= window_start) & (df_oa['createddate'] <= window_end)
df_oa_window = df_oa[mask_window_oa].copy()

agent_case_counts = df_oa_window.groupby('newvalue__c')['caseid__c'].nunique()
agents_more_than_one = set(agent_case_counts[agent_case_counts > 1].index.dropna().tolist())

# Determine which cases were transferred overall (more than one Owner Assignment)
case_assignment_counts = df_oa.groupby('caseid__c').size()
non_transferred_cases = set(case_assignment_counts[case_assignment_counts == 1].index.tolist())

# Filter cases closed in the window
mask_cases_window = (df_cases['closeddate'] >= window_start) & (df_cases['closeddate'] <= window_end)
df_cases_window = df_cases[mask_cases_window].copy()

# Clean case ids in df_cases as well (they may have '#')
df_cases_window['id'] = df_cases_window['id'].astype(str).str.strip().str.lstrip('#')

# Keep only non-transferred cases
df_cases_nt = df_cases_window[df_cases_window['id'].isin(non_transferred_cases)].copy()

# Compute handle time in seconds
df_cases_nt['handle_seconds'] = (df_cases_nt['closeddate'] - df_cases_nt['createddate']).dt.total_seconds()

# Clean ownerid
df_cases_nt['ownerid'] = df_cases_nt['ownerid'].astype(str).str.strip().str.lstrip('#')

# Group by owner and compute average handle time
avg_handle = df_cases_nt.groupby('ownerid')['handle_seconds'].mean()

# Filter to agents with >1 cases processed in window
# Note: the agent ids in agents_more_than_one were extracted from owner assignment newvalue__c (cleaned)
candidates = [aid for aid in avg_handle.index if aid in agents_more_than_one]

result_agent = None
if candidates:
    # find agent with lowest average handle time
    subset = avg_handle.loc[candidates]
    # In case of tie, choose smallest id lexicographically
    min_val = subset.min()
    mins = subset[subset == min_val].index.tolist()
    mins_sorted = sorted(mins)
    result_agent = mins_sorted[0]

# Prepare output
import json as _json
output = result_agent if result_agent is not None else None
print("__RESULT__:")
print(_json.dumps(output))"""

env_args = {'var_call_kKDDJ0nFmfD4qlW34hRJ19oA': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_Jfwgyl5W4QQ93Zw9iDe9TGPm': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_miPtpuiGlCi6TkRFSNIZbKej': 'file_storage/call_miPtpuiGlCi6TkRFSNIZbKej.json', 'var_call_oV7MtJHO6JOKKdeXdTLuAcDZ': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}]}

exec(code, env_args)
