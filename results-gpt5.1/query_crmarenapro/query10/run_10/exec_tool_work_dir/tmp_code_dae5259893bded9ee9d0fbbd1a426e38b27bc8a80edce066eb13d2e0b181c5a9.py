code = """import pandas as pd, json

df = pd.DataFrame(var_call_QPoEgfBrGq8cyloJ45HOwyZs)
# Filter to closed cases only (handle time defined) and those without transfer (no history rows)
closed = df[(df['closeddate'] != 'None') & (df['history_id'] == 'None')].copy()
# Parse datetimes
closed['createddate'] = pd.to_datetime(closed['createddate'])
closed['closeddate'] = pd.to_datetime(closed['closeddate'])
# Handle time in seconds
closed['handle_seconds'] = (closed['closeddate'] - closed['createddate']).dt.total_seconds()
# Normalize ownerid by stripping leading '#'
closed['owner_norm'] = closed['ownerid'].str.lstrip('#')
# Aggregate per agent
agg = closed.groupby('owner_norm').agg(cases=('case_id','nunique'), avg_handle=('handle_seconds','mean')).reset_index()
# Only agents managing more than one case (including transferred) - we only have current owner counts here, but no transfer history in sample; assume counts by ownerid across all cases
# For total handled cases (including transfers), count all rows by owner_norm in full df
all_cases = df.copy()
all_cases['owner_norm'] = all_cases['ownerid'].str.lstrip('#')
handled_counts = all_cases.groupby('owner_norm')['case_id'].nunique().reset_index(name='handled_cases')
res = pd.merge(agg, handled_counts, on='owner_norm', how='left')
res = res[res['handled_cases'] > 1]
if res.empty:
    answer = None
else:
    # Find agent with lowest average handle time
    best = res.sort_values('avg_handle').iloc[0]['owner_norm']
    answer = best

result = json.dumps(answer)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_QPoEgfBrGq8cyloJ45HOwyZs': [{'case_id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}, {'case_id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'history_id': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'history_createddate': 'None'}]}

exec(code, env_args)
