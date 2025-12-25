code = """import pandas as pd, json
cases = pd.DataFrame(var_call_8TYwQTQ8duLGsvaqH7a3tKm9)
history = pd.DataFrame(var_call_9bPkbnAZfAxChPe0KqMNbzIu)
# Normalize IDs by stripping leading '#'
cases['norm_id'] = cases['id'].str.lstrip('#')
history['norm_caseid'] = history['caseid__c'].str.lstrip('#')
# Count owner assignment records per case to identify transfers
owner_assign_counts = history.groupby('norm_caseid').size().rename('assign_count').reset_index()
cases = cases.merge(owner_assign_counts, left_on='norm_id', right_on='norm_caseid', how='left')
cases['assign_count'] = cases['assign_count'].fillna(0).astype(int)
# Keep only cases with exactly one owner assignment (no transfer)
no_transfer = cases[cases['assign_count'] == 1].copy()
# Parse datetimes and compute handle time in seconds
no_transfer['created_ts'] = pd.to_datetime(no_transfer['createddate'])
no_transfer['closed_ts'] = pd.to_datetime(no_transfer['closeddate'])
no_transfer['handle_seconds'] = (no_transfer['closed_ts'] - no_transfer['created_ts']).dt.total_seconds()
# Aggregate by agent
agent_stats = no_transfer.groupby('ownerid').agg(cases_handled=('id','count'), avg_handle=('handle_seconds','mean')).reset_index()
# Filter to agents who processed more than one case
eligible = agent_stats[agent_stats['cases_handled'] > 1]
if eligible.empty:
    result = None
else:
    best = eligible.sort_values(['avg_handle','ownerid']).iloc[0]['ownerid']
    result = best
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mLSVuZYY3NCaCZfK2rpNqEAI': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_9bPkbnAZfAxChPe0KqMNbzIu': [{'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDsG3IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzivIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000'}], 'var_call_8TYwQTQ8duLGsvaqH7a3tKm9': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}]}

exec(code, env_args)
