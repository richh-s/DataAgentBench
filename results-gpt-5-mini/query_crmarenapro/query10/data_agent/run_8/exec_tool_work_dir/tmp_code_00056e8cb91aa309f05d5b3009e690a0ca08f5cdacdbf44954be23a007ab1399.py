code = """import json
import pandas as pd
from datetime import datetime

# Load variables from storage
cases = var_call_v1JeZzBrneohF5xKMgBfaNPy
owner_history_path = var_call_T5T9uIWA8DnUKGvBBj55OhvV

# owner_history_path is a file path to JSON
with open(owner_history_path, 'r', encoding='utf-8') as f:
    owner_history = json.load(f)

# Create DataFrames
cases_df = pd.DataFrame(cases)
owner_df = pd.DataFrame(owner_history)

# Normalize case ids by stripping whitespace and leading '#'
def normalize_id(x):
    if pd.isna(x):
        return x
    return str(x).strip().lstrip('#').strip()

cases_df['case_id_norm'] = cases_df['id'].apply(normalize_id)
owner_df['case_id_norm'] = owner_df['caseid__c'].apply(normalize_id)

# Filter owner assignments to only those cases closed in the window
owner_for_closed = owner_df[owner_df['case_id_norm'].isin(cases_df['case_id_norm'].unique())].copy()

# Count owner assignment entries per case
owner_counts = owner_for_closed.groupby('case_id_norm').size().reset_index(name='owner_assign_count')

# Merge counts back to cases
cases_df = cases_df.merge(owner_counts, left_on='case_id_norm', right_on='case_id_norm', how='left')
cases_df['owner_assign_count'] = cases_df['owner_assign_count'].fillna(0).astype(int)

# Keep only cases with exactly one owner assignment (not transferred)
single_owner_cases = cases_df[cases_df['owner_assign_count'] == 1].copy()

# For these cases, find the single owner id from owner_for_closed
# There should be exactly one record per case in owner_for_closed
owner_single = owner_for_closed[owner_for_closed['case_id_norm'].isin(single_owner_cases['case_id_norm'])].copy()
# Normalize owner id
owner_single['owner_id_norm'] = owner_single['newvalue__c'].apply(normalize_id)

# Merge owner into single_owner_cases
single_owner_cases = single_owner_cases.merge(owner_single[['case_id_norm', 'owner_id_norm']], on='case_id_norm', how='left')

# Compute handle time (in seconds) as closeddate - createddate
# Parse datetimes
single_owner_cases['created_dt'] = pd.to_datetime(single_owner_cases['createddate'], errors='coerce')
single_owner_cases['closed_dt'] = pd.to_datetime(single_owner_cases['closeddate'], errors='coerce')
single_owner_cases['handle_seconds'] = (single_owner_cases['closed_dt'] - single_owner_cases['created_dt']).dt.total_seconds()

# Drop rows with null handle_seconds or owner
single_owner_cases = single_owner_cases.dropna(subset=['handle_seconds', 'owner_id_norm'])

# Compute per-agent stats: count and average handle time
agent_stats = single_owner_cases.groupby('owner_id_norm').agg(count_cases=('case_id_norm', 'nunique'), avg_handle_seconds=('handle_seconds', 'mean')).reset_index()

# Filter agents who processed more than one case
eligible_agents = agent_stats[agent_stats['count_cases'] > 1].copy()

# If no eligible agents, return empty string
if eligible_agents.empty:
    result = json.dumps("")
else:
    # Find agent with lowest average handle time
    min_row = eligible_agents.sort_values(['avg_handle_seconds', 'owner_id_norm']).iloc[0]
    agent_id = min_row['owner_id_norm']
    result = json.dumps(agent_id)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_aPtlTsGgp7u1BQYiedAJSw2l': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_YPXW7wDx1AXbUoQouJlVOdkj': [{'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDsG3IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzivIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000'}], 'var_call_T5T9uIWA8DnUKGvBBj55OhvV': 'file_storage/call_T5T9uIWA8DnUKGvBBj55OhvV.json', 'var_call_v1JeZzBrneohF5xKMgBfaNPy': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}]}

exec(code, env_args)
