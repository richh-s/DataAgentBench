code = """import json
import pandas as pd
from datetime import datetime

# Load tool results from storage variables
case_history_path = var_call_OmCyf9lowp4kvNuAk25PyX9E  # large JSON file path
cases_closed = var_call_c3MRxQohLBBkzZDi2O2JHfbZ  # list of dicts

# Read the full casehistory JSON from file
with open(case_history_path, 'r') as f:
    casehistory = json.load(f)

# Convert to DataFrame
ch = pd.DataFrame(casehistory)
cases_closed_df = pd.DataFrame(cases_closed)

# Normalize IDs: strip whitespace and remove leading '#'
def norm_id(x):
    if pd.isna(x):
        return x
    x = x.strip()
    if x.startswith('#'):
        x = x[1:]
    return x

for col in ['caseid__c','oldvalue__c','newvalue__c']:
    if col in ch.columns:
        ch[col] = ch[col].astype(str).apply(norm_id)

cases_closed_df['id'] = cases_closed_df['id'].astype(str).apply(norm_id)

# Parse dates
ch['createddate'] = pd.to_datetime(ch['createddate'], utc=True, errors='coerce')
cases_closed_df['createddate'] = pd.to_datetime(cases_closed_df['createddate'], utc=True, errors='coerce')
cases_closed_df['closeddate'] = pd.to_datetime(cases_closed_df['closeddate'], utc=True, errors='coerce')

# Define window
start = pd.to_datetime('2023-05-02T00:00:00Z')
end = pd.to_datetime('2023-09-02T23:59:59Z')

# Count owner assignment events per case overall to detect transfers
owner_ch = ch[ch['field__c']=='Owner Assignment'].copy()
owner_ch['caseid__c'] = owner_ch['caseid__c'].astype(str).apply(norm_id)

case_assign_counts = owner_ch.groupby('caseid__c').size().rename('assign_count')

# For counting agents processed >1 case in the window: filter owner_ch by createddate in window
owner_ch_in_window = owner_ch[(owner_ch['createddate'] >= start) & (owner_ch['createddate'] <= end)].copy()

# Count distinct cases per agent in window
owner_ch_in_window['newvalue__c'] = owner_ch_in_window['newvalue__c'].astype(str).apply(norm_id)
agent_case_counts = owner_ch_in_window.groupby('newvalue__c')['caseid__c'].nunique().rename('cases_processed_in_window')

# Now for handle time: consider cases closed in window and not transferred (assign_count == 1)
# Merge counts into cases_closed_df
cases_closed_df['norm_id'] = cases_closed_df['id']
cases_closed_df = cases_closed_df.merge(case_assign_counts.rename('assign_count'), left_on='norm_id', right_index=True, how='left')
cases_closed_df['assign_count'] = cases_closed_df['assign_count'].fillna(0).astype(int)

# Filter to only cases with assign_count == 1 (not transferred) and closed within window (already selected)
non_transferred_closed = cases_closed_df[cases_closed_df['assign_count']==1].copy()

# For each such case, find the owner (the single Owner Assignment event's newvalue)
# Get owner assignments for these cases
owners_for_non_transferred = owner_ch[owner_ch['caseid__c'].isin(non_transferred_closed['norm_id'])].copy()
# For safety, pick the earliest owner assignment per case (should be only one)
owners_for_non_transferred = owners_for_non_transferred.sort_values(['caseid__c','createddate']).groupby('caseid__c').first().reset_index()
owners_for_non_transferred['newvalue__c'] = owners_for_non_transferred['newvalue__c'].astype(str).apply(norm_id)

# Merge owner into non_transferred_closed
non_transferred_closed = non_transferred_closed.merge(owners_for_non_transferred[['caseid__c','newvalue__c']], left_on='norm_id', right_on='caseid__c', how='left')

# Compute handle time in seconds
non_transferred_closed['handle_seconds'] = (non_transferred_closed['closeddate'] - non_transferred_closed['createddate']).dt.total_seconds()

# Compute average handle time per agent (newvalue__c)
agent_avg = non_transferred_closed.groupby('newvalue__c')['handle_seconds'].mean().rename('avg_handle_seconds')
agent_avg = agent_avg.reset_index()

# Now filter agents who processed more than one case in window
agent_avg = agent_avg.merge(agent_case_counts.reset_index(), left_on='newvalue__c', right_on='newvalue__c', how='left')
agent_avg['cases_processed_in_window'] = agent_avg['cases_processed_in_window'].fillna(0).astype(int)

eligible = agent_avg[agent_avg['cases_processed_in_window']>1].copy()

# Identify agent with lowest average handle time
result_agent = None
if not eligible.empty:
    eligible_sorted = eligible.sort_values('avg_handle_seconds')
    result_agent = eligible_sorted.iloc[0]['newvalue__c']

# Prepare output
output = {'agent_id_with_lowest_avg_handle_time': None}
if result_agent is not None and str(result_agent).strip()!='nan':
    output['agent_id_with_lowest_avg_handle_time'] = str(result_agent)

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_cVk6AdPnWwivzL9gTmFbLum5': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_0K1PT3Ff39xC9iZ8Uv0goN4z': [{'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzivIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDsG3IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000'}], 'var_call_c3MRxQohLBBkzZDi2O2JHfbZ': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_OmCyf9lowp4kvNuAk25PyX9E': 'file_storage/call_OmCyf9lowp4kvNuAk25PyX9E.json'}

exec(code, env_args)
