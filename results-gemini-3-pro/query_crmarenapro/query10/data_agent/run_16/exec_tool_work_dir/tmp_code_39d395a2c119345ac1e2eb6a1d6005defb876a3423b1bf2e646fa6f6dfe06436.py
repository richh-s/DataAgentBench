code = """import json
import pandas as pd

cases_data = locals()['var_function-call-5445523109931077059']
history_path = locals()['var_function-call-17191194624287533228']
with open(history_path, 'r') as f:
    history_data = json.load(f)

def clean_id(i):
    if not i: return i
    return i.lstrip('#')

cases_df = pd.DataFrame(cases_data)
cases_df['id'] = cases_df['id'].apply(clean_id)
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'])

history_df = pd.DataFrame(history_data)
history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)
history_df['newvalue__c'] = history_df['newvalue__c'].apply(clean_id)

# 1. Calculate Total Processed Count per Agent (from full history)
# "Processing" = being an owner (newvalue__c in Owner Assignment)
total_processed = history_df.groupby('newvalue__c')['caseid__c'].nunique().reset_index(name='total_count')

# 2. Calculate Handle Time for the 7 closed cases
# We established all 7 are single owner (assign_count=1 for these 7).
# So we can just use the cases_df directly.
cases_df['handle_time'] = (cases_df['closeddate'] - cases_df['createddate']).dt.total_seconds()
# We need to assign each case to its agent.
# Since they are single owner, the current 'ownerid' in cases_df is the agent.
cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)

# 3. Join with Total Processed Count
# We care about the agents in cases_df
metric_df = cases_df[['ownerid', 'handle_time']].copy()
# Merge with processed counts
metric_df = pd.merge(metric_df, total_processed, left_on='ownerid', right_on='newvalue__c', how='left')

# 4. Filter for agents with total_count > 1
filtered_df = metric_df[metric_df['total_count'] > 1].copy()

# 5. Find lowest average handle time
# Note: In this specific dataset (7 cases, 7 agents), each agent has 1 case.
# So "Average" is just the handle time of that 1 case.
# But we only consider agents who processed > 1 case *total* (in history).

if filtered_df.empty:
    result = "No agents met the criteria (total > 1)"
else:
    # Sort by handle_time (ascending)
    # If multiple cases per agent, we would groupby and mean. Here it's 1-to-1.
    # But for safety:
    avg_df = filtered_df.groupby('ownerid')['handle_time'].mean().reset_index()
    min_row = avg_df.loc[avg_df['handle_time'].idxmin()]
    result = min_row['ownerid']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-18262003565180936915': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5445523109931077059': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-15917723063401705946': [], 'var_function-call-18379950216490017826': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-9205801986047596649': [{'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4'}, {'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG'}, {'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW'}, {'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG'}, {'caseid__c': '500Wt00000DE0NGIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG'}, {'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDfYxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG'}], 'var_function-call-9805771422527820542': [{'count': '7'}], 'var_function-call-17615445584445883886': [{'count': '165'}], 'var_function-call-4850416943357918028': 'Need to fetch history', 'var_function-call-17191194624287533228': 'file_storage/function-call-17191194624287533228.json', 'var_function-call-440547325235926189': 'No agents met the criteria', 'var_function-call-3099379707628599216': 'Debug info printed', 'var_function-call-15982900317457714271': {'total_cases': 7, 'cases_with_history': 7, 'assignment_counts': [{'caseid__c': '500Wt00000DDepmIAD', 'assign_count': 1}, {'caseid__c': '500Wt00000DDyzpIAD', 'assign_count': 1}, {'caseid__c': '500Wt00000DDzUPIA1', 'assign_count': 1}, {'caseid__c': '500Wt00000DDzsbIAD', 'assign_count': 1}, {'caseid__c': '500Wt00000DDzscIAD', 'assign_count': 1}, {'caseid__c': '500Wt00000DDzuEIAT', 'assign_count': 1}, {'caseid__c': '500Wt00000DE02HIAT', 'assign_count': 1}], 'processed_counts': [{'newvalue__c': '005Wt000003NDqDIAW', 'processed_count': 1}, {'newvalue__c': '005Wt000003NEtOIAW', 'processed_count': 1}, {'newvalue__c': '005Wt000003NIddIAG', 'processed_count': 1}, {'newvalue__c': '005Wt000003NJD9IAO', 'processed_count': 1}, {'newvalue__c': '005Wt000003NJGLIA4', 'processed_count': 1}, {'newvalue__c': '005Wt000003NJJaIAO', 'processed_count': 1}, {'newvalue__c': '005Wt000003NJufIAG', 'processed_count': 1}], 'single_owner_cases': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD', '500Wt00000DDzuEIAT', '500Wt00000DE02HIAT'], 'single_owner_agents': ['005Wt000003NEtOIAW', '005Wt000003NJufIAG', '005Wt000003NDqDIAW', '005Wt000003NJJaIAO', '005Wt000003NJGLIA4', '005Wt000003NJD9IAO', '005Wt000003NIddIAG']}}

exec(code, env_args)
