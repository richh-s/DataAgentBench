code = """import pandas as pd
from datetime import datetime

cases_data = locals()['var_function-call-9326911787075994329']['results']
case_history_data = locals()['var_function-call-10181549449180025158']['results']

cases_df = pd.DataFrame(cases_data)
case_history_df = pd.DataFrame(case_history_data)

# Clean Id field in cases_df
cases_df['id'] = cases_df['id'].str.replace('#', '')

# Filter for owner assignment history
owner_assignment_history = case_history_df[case_history_df['field__c'] == 'Owner Assignment']

# Count distinct owner assignments for each case
owner_assignment_counts = owner_assignment_history.groupby('caseid__c')['newvalue__c'].nunique().reset_index()
owner_assignment_counts.rename(columns={'caseid__c': 'id', 'newvalue__c': 'owner_assignment_count'}, inplace=True)

# Merge with cases_df to get owner assignment count for each case
cases_with_owner_counts = pd.merge(cases_df, owner_assignment_counts, on='id', how='left')
cases_with_owner_counts['owner_assignment_count'] = cases_with_owner_counts['owner_assignment_count'].fillna(1).astype(int)

# Filter out transferred cases (owner_assignment_count > 1)
non_transferred_cases = cases_with_owner_counts[cases_with_owner_counts['owner_assignment_count'] == 1]

# Convert datetime strings to datetime objects
non_transferred_cases['createddate'] = pd.to_datetime(non_transferred_cases['createddate'])
non_transferred_cases['closeddate'] = pd.to_datetime(non_transferred_cases['closeddate'])

# Calculate handle time in seconds
non_transferred_cases['handle_time'] = (non_transferred_cases['closeddate'] - non_transferred_cases['createddate']).dt.total_seconds()

# Group by ownerid, count cases, and calculate average handle time
agent_stats = non_transferred_cases.groupby('ownerid').agg(
    case_count=('id', 'count'),
    avg_handle_time=('handle_time', 'mean')
).reset_index()

# Filter agents who processed more than one case
agents_more_than_one_case = agent_stats[agent_stats['case_count'] > 1]

if not agents_more_than_one_case.empty:
    # Find the agent with the lowest average handle time
    lowest_avg_handle_time_agent = agents_more_than_one_case.loc[agents_more_than_one_case['avg_handle_time'].idxmin()]
    result = lowest_avg_handle_time_agent['ownerid']
else:
    result = "No agents processed more than one case."

print('__RESULT__:')
print(pd.json_normalize({"result": result}).to_json(orient='records'))"""

env_args = {'var_function-call-9326911787075994329': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_function-call-15016906831191566863': [], 'var_function-call-10181549449180025158': [{'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Creation', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Closed', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJufIAG'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Case Creation', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Creation', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Case Closed', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJJaIAO'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJGLIA4'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJD9IAO'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Closed', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NIddIAG'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None'}]}

exec(code, env_args)
