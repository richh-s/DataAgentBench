code = """import pandas as pd
import json
from datetime import datetime

# Load previous tool results from storage variables
cases = var_call_QY5GYcbXuAYT3pSP4XKMF8gC
casehistory_path = var_call_CQU3KMJO31XZasyoGwebQjNl

# Read the large casehistory JSON file
with open(casehistory_path, 'r', encoding='utf-8') as f:
    casehistory = json.load(f)

# Create DataFrames
df_cases = pd.DataFrame(cases)
df_ch = pd.DataFrame(casehistory)

# Normalization function for IDs
def normalize_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Normalize IDs in both dataframes
if not df_cases.empty:
    df_cases['id_norm'] = df_cases['id'].apply(normalize_id)
    df_cases['ownerid_norm'] = df_cases['ownerid'].apply(normalize_id)
else:
    df_cases['id_norm'] = pd.Series(dtype=str)
    df_cases['ownerid_norm'] = pd.Series(dtype=str)

if not df_ch.empty:
    df_ch['caseid_norm'] = df_ch['caseid__c'].apply(normalize_id)
    df_ch['newvalue_norm'] = df_ch['newvalue__c'].apply(normalize_id)
else:
    df_ch['caseid_norm'] = pd.Series(dtype=str)
    df_ch['newvalue_norm'] = pd.Series(dtype=str)

# Consider only Owner Assignment entries already filtered in query
# Count owner assignment events per case for cases closed in the window
closed_case_ids = set(df_cases['id_norm'].dropna().unique())

df_ch_in_window = df_ch[df_ch['caseid_norm'].isin(closed_case_ids)].copy()
owner_counts = df_ch_in_window.groupby('caseid_norm').size().rename('owner_assignment_count')

# Merge counts back to cases
df_cases = df_cases.merge(owner_counts, left_on='id_norm', right_on='caseid_norm', how='left')
# If no history entries, owner_assignment_count is NaN -> treat as 0
df_cases['owner_assignment_count'] = df_cases['owner_assignment_count'].fillna(0).astype(int)

# We only compute handle time for cases that have NOT been transferred to other agents
# According to policy, transferred cases have more than one Owner Assignment
df_cases['transferred'] = df_cases['owner_assignment_count'] > 1

# Keep only non-transferred cases
df_non_transferred = df_cases[~df_cases['transferred']].copy()

# If no non-transferred cases, return empty
if df_non_transferred.empty:
    result = json.dumps("")
    print("__RESULT__:")
    print(result)
else:
    # Compute handle time in seconds
    df_non_transferred['created_dt'] = pd.to_datetime(df_non_transferred['createddate'], utc=True, errors='coerce')
    df_non_transferred['closed_dt'] = pd.to_datetime(df_non_transferred['closeddate'], utc=True, errors='coerce')
    df_non_transferred['handle_seconds'] = (df_non_transferred['closed_dt'] - df_non_transferred['created_dt']).dt.total_seconds()

    # Remove rows with invalid times
    df_non_transferred = df_non_transferred[df_non_transferred['handle_seconds'].notna()]

    # Group by owner and compute average handle time and count of cases processed
    grp = df_non_transferred.groupby('ownerid_norm').agg(
        case_count=('id', 'count'),
        avg_handle_seconds=('handle_seconds', 'mean')
    ).reset_index()

    # Filter agents who processed more than one case
    grp = grp[grp['case_count'] > 1]

    if grp.empty:
        result = json.dumps("")
        print("__RESULT__:")
        print(result)
    else:
        # Find agent with lowest average handle time
        grp_sorted = grp.sort_values(['avg_handle_seconds', 'ownerid_norm'])
        best_agent = grp_sorted.iloc[0]['ownerid_norm']
        result = json.dumps(str(best_agent))
        print("__RESULT__:")
        print(result)"""

env_args = {'var_call_gXVnXPqOfYv599kVpjrLbnLR': [{'field__c': 'Owner Assignment'}, {'field__c': 'Case Closed'}, {'field__c': 'Case Creation'}], 'var_call_AE41nAhrDAX2Edva1zVfNaRE': [{'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}], 'var_call_QY5GYcbXuAYT3pSP4XKMF8gC': [{'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}], 'var_call_CQU3KMJO31XZasyoGwebQjNl': 'file_storage/call_CQU3KMJO31XZasyoGwebQjNl.json'}

exec(code, env_args)
