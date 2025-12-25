code = """import json
import pandas as pd

# 1. Get closed cases info (Single Owner cases)
cases_data = locals()['var_function-call-5445523109931077059']
# Clean IDs
def clean_id(i):
    if not i: return i
    return i.lstrip('#')

cases_df = pd.DataFrame(cases_data)
cases_df['id'] = cases_df['id'].apply(clean_id)
cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'])
cases_df['handle_time'] = (cases_df['closeddate'] - cases_df['createddate']).dt.total_seconds()

# Map Agent -> Handle Time
# Since 1 case per agent in this set
agent_metrics = cases_df[['ownerid', 'handle_time']].set_index('ownerid')

# 2. Get Recent Assignments
recent_history_data = locals()['var_function-call-108059554407770968']
recent_history_df = pd.DataFrame(recent_history_data)
recent_history_df['caseid__c'] = recent_history_df['caseid__c'].apply(clean_id)
recent_history_df['newvalue__c'] = recent_history_df['newvalue__c'].apply(clean_id)

# Count processed cases per agent
processed_counts = recent_history_df.groupby('newvalue__c')['caseid__c'].nunique().reset_index(name='processed_count')
processed_counts = processed_counts.set_index('newvalue__c')

# 3. Combine
# We only care about agents in agent_metrics
combined = agent_metrics.join(processed_counts, how='left')
# Fill NaN with 0 (though if they closed a case, they must have at least 1 assignment)
combined['processed_count'] = combined['processed_count'].fillna(0)

# Filter > 1
filtered = combined[combined['processed_count'] > 1]

# 4. Find min
if filtered.empty:
    result = "No agents met the criteria"
    debug = combined.to_dict()
else:
    min_agent = filtered['handle_time'].idxmin()
    result = min_agent
    debug = "Found"

print("__RESULT__:")
print(json.dumps({"result": result, "debug": debug if isinstance(debug, str) else str(debug)}))"""

env_args = {'var_function-call-18262003565180936915': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5445523109931077059': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-15917723063401705946': [], 'var_function-call-18379950216490017826': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-9205801986047596649': [{'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4'}, {'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG'}, {'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW'}, {'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG'}, {'caseid__c': '500Wt00000DE0NGIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG'}, {'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDfYxIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'caseid__c': '500Wt00000DDZtLIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG'}], 'var_function-call-9805771422527820542': [{'count': '7'}], 'var_function-call-17615445584445883886': [{'count': '165'}], 'var_function-call-4850416943357918028': 'Need to fetch history', 'var_function-call-17191194624287533228': 'file_storage/function-call-17191194624287533228.json', 'var_function-call-440547325235926189': 'No agents met the criteria', 'var_function-call-3099379707628599216': 'Debug info printed', 'var_function-call-15982900317457714271': {'total_cases': 7, 'cases_with_history': 7, 'assignment_counts': [{'caseid__c': '500Wt00000DDepmIAD', 'assign_count': 1}, {'caseid__c': '500Wt00000DDyzpIAD', 'assign_count': 1}, {'caseid__c': '500Wt00000DDzUPIA1', 'assign_count': 1}, {'caseid__c': '500Wt00000DDzsbIAD', 'assign_count': 1}, {'caseid__c': '500Wt00000DDzscIAD', 'assign_count': 1}, {'caseid__c': '500Wt00000DDzuEIAT', 'assign_count': 1}, {'caseid__c': '500Wt00000DE02HIAT', 'assign_count': 1}], 'processed_counts': [{'newvalue__c': '005Wt000003NDqDIAW', 'processed_count': 1}, {'newvalue__c': '005Wt000003NEtOIAW', 'processed_count': 1}, {'newvalue__c': '005Wt000003NIddIAG', 'processed_count': 1}, {'newvalue__c': '005Wt000003NJD9IAO', 'processed_count': 1}, {'newvalue__c': '005Wt000003NJGLIA4', 'processed_count': 1}, {'newvalue__c': '005Wt000003NJJaIAO', 'processed_count': 1}, {'newvalue__c': '005Wt000003NJufIAG', 'processed_count': 1}], 'single_owner_cases': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD', '500Wt00000DDzuEIAT', '500Wt00000DE02HIAT'], 'single_owner_agents': ['005Wt000003NEtOIAW', '005Wt000003NJufIAG', '005Wt000003NDqDIAW', '005Wt000003NJJaIAO', '005Wt000003NJGLIA4', '005Wt000003NJD9IAO', '005Wt000003NIddIAG']}, 'var_function-call-16443856319180761931': '005Wt000003NDqDIAW', 'var_function-call-15341516833122954799': ['005Wt000003NJufIAG', '005Wt000003NDqDIAW', '005Wt000003NEtOIAW', '005Wt000003NIddIAG', '005Wt000003NJGLIA4', '005Wt000003NJJaIAO', '005Wt000003NJD9IAO'], 'var_function-call-108059554407770968': [{'newvalue__c': '005Wt000003NEtOIAW', 'caseid__c': '500Wt00000DDzscIAD'}, {'newvalue__c': '005Wt000003NDqDIAW', 'caseid__c': '500Wt00000DDzZHIA1'}, {'newvalue__c': '005Wt000003NJufIAG', 'caseid__c': '500Wt00000DDepmIAD'}, {'newvalue__c': '005Wt000003NJppIAG', 'caseid__c': '500Wt00000DDflsIAD'}, {'newvalue__c': '005Wt000003NJcvIAG', 'caseid__c': '500Wt00000DDzr0IAD'}, {'newvalue__c': '005Wt000003NDqDIAW', 'caseid__c': '500Wt00000DDzUPIA1'}, {'newvalue__c': '005Wt000003NJUrIAO', 'caseid__c': '500Wt00000DDzXdIAL'}, {'newvalue__c': '005Wt000003NI5mIAG', 'caseid__c': '500Wt00000DDsG3IAL'}, {'newvalue__c': '005Wt000003NH3GIAW', 'caseid__c': '500Wt00000DDDfwIAH'}, {'newvalue__c': '005Wt000003NIfFIAW', 'caseid__c': '500Wt00000DDTxbIAH'}, {'newvalue__c': '005Wt000003NINVIA4', 'caseid__c': '500Wt00000DDzkXIAT'}, {'newvalue__c': '005Wt000003NJJaIAO', 'caseid__c': '500Wt00000DDzuEIAT'}, {'newvalue__c': '005Wt000003NF1SIAW', 'caseid__c': '500Wt00000DDflsIAD'}, {'newvalue__c': '005Wt000003NDqDIAW', 'caseid__c': '500Wt00000DDzivIAD'}, {'newvalue__c': '005Wt000003NJGLIA4', 'caseid__c': '500Wt00000DDyzpIAD'}, {'newvalue__c': '005Wt000003NJD9IAO', 'caseid__c': '500Wt00000DDzsbIAD'}, {'newvalue__c': '005Wt000003NIddIAG', 'caseid__c': '500Wt00000DE02HIAT'}, {'newvalue__c': '005Wt000003NJ0DIAW', 'caseid__c': '500Wt00000DDDfwIAH'}]}

exec(code, env_args)
