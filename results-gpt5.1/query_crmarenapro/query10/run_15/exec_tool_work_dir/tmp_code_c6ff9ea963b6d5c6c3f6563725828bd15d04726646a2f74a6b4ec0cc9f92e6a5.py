code = """import pandas as pd, json
cases = pd.DataFrame(var_call_OO1qiX6VEAjQqprgudDGGFZS)
cases['createddate'] = pd.to_datetime(cases['createddate'])
cases['closeddate'] = pd.to_datetime(cases['closeddate'])
cases['handle_time_hours'] = (cases['closeddate'] - cases['createddate']).dt.total_seconds() / 3600.0
avg_handle = cases.groupby('agent_id').agg(cases_handled=('case_id','nunique'), avg_handle_time_hours=('handle_time_hours','mean')).reset_index()
eligible = avg_handle[avg_handle['cases_handled'] > 1]
if not eligible.empty:
    min_row = eligible.sort_values('avg_handle_time_hours', ascending=True).iloc[0]
    result = min_row['agent_id']
else:
    result = None
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OO1qiX6VEAjQqprgudDGGFZS': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'case_id': '500Wt00000DDepmIAD'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'case_id': '500Wt00000DDyzpIAD'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'case_id': '500Wt00000DDzUPIA1'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'case_id': '500Wt00000DDzsbIAD'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'case_id': '#500Wt00000DDzscIAD'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'case_id': '500Wt00000DDzuEIAT'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'case_id': '#500Wt00000DE02HIAT'}], 'var_call_SLFsB7r6R8DhYtbd7HFecV4X': []}

exec(code, env_args)
