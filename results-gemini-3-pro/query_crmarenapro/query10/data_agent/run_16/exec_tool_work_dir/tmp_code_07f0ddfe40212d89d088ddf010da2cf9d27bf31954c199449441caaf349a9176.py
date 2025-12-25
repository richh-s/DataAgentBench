code = """import json
import pandas as pd
from datetime import datetime

# Load Cases
cases_data = locals()['var_function-call-5445523109931077059']
# cases_data is a list of dicts.
# [{"id": "...", "ownerid": "...", "createddate": "...", "closeddate": "..."}]

# Load History
history_path = locals()['var_function-call-17191194624287533228']
with open(history_path, 'r') as f:
    history_data = json.load(f)

# Helper to clean IDs
def clean_id(i):
    if not i: return i
    return i.lstrip('#')

# Prepare DataFrames
cases_df = pd.DataFrame(cases_data)
cases_df['id'] = cases_df['id'].apply(clean_id)
cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)
# Parse dates
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'])

history_df = pd.DataFrame(history_data)
history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)
history_df['newvalue__c'] = history_df['newvalue__c'].apply(clean_id)

# Filter history to only relevant cases
relevant_case_ids = set(cases_df['id'].unique())
history_filtered = history_df[history_df['caseid__c'].isin(relevant_case_ids)].copy()

# Determine Single Owner Cases
# Group by CaseId, count entries
assignment_counts = history_filtered.groupby('caseid__c').size().reset_index(name='assign_count')
# Cases with exactly 1 assignment
single_owner_case_ids = set(assignment_counts[assignment_counts['assign_count'] == 1]['caseid__c'])

# Calculate Handle Time for Single Owner Cases
# Handle Time = Closed - Created
single_owner_cases = cases_df[cases_df['id'].isin(single_owner_case_ids)].copy()
single_owner_cases['handle_time_seconds'] = (single_owner_cases['closeddate'] - single_owner_cases['createddate']).dt.total_seconds()

# Map Case -> Agent for Single Owner Cases
# We can use 'ownerid' from cases_df since they are single owner
# Verify with history? History 'newvalue__c' should match 'ownerid'.
# We'll trust 'ownerid' or merge with history.
# Let's merge with history to be sure we get the correct "assigned" agent from the "Owner Assignment" event.
# Actually, for single owner, the history has 1 row. newvalue is the agent.
single_owner_history = history_filtered[history_filtered['caseid__c'].isin(single_owner_case_ids)]
# Merge single_owner_cases with single_owner_history on caseid
# Note: history might have multiple rows if my logic is wrong? No, we filtered count==1.
single_owner_merged = pd.merge(single_owner_cases, single_owner_history, left_on='id', right_on='caseid__c')
# Agent is newvalue__c
single_owner_merged['agent_id'] = single_owner_merged['newvalue__c']

# Calculate Processed Count per Agent
# Agent "processed" a case if they appear in history newvalue__c for that case.
# (This includes initial assignment and transfers).
# Use history_filtered (all assignments for these cases)
processed_counts = history_filtered.groupby('newvalue__c')['caseid__c'].nunique().reset_index(name='processed_count')

# Filter Agents with > 1 Processed Case
eligible_agents = set(processed_counts[processed_counts['processed_count'] > 1]['newvalue__c'])

# Calculate Average Handle Time for Eligible Agents
# Using only single_owner_merged data
eligible_single_owner = single_owner_merged[single_owner_merged['agent_id'].isin(eligible_agents)]

if eligible_single_owner.empty:
    result = "No agents met the criteria"
else:
    avg_handle_time = eligible_single_owner.groupby('agent_id')['handle_time_seconds'].mean().reset_index()
    # Find min
    min_row = avg_handle_time.loc[avg_handle_time['handle_time_seconds'].idxmin()]
    result = min_row['agent_id']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-18262003565180936915': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5445523109931077059': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-15917723063401705946': [], 'var_function-call-18379950216490017826': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-9205801986047596649': [{'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4'}, {'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG'}, {'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW'}, {'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG'}, {'caseid__c': '500Wt00000DE0NGIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG'}, {'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDfYxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG'}], 'var_function-call-9805771422527820542': [{'count': '7'}], 'var_function-call-17615445584445883886': [{'count': '165'}], 'var_function-call-4850416943357918028': 'Need to fetch history', 'var_function-call-17191194624287533228': 'file_storage/function-call-17191194624287533228.json'}

exec(code, env_args)
