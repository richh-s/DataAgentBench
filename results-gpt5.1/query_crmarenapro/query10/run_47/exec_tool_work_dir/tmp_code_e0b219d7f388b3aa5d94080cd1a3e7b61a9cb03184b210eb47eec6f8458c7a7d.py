code = """import pandas as pd, json
cases = pd.DataFrame(var_call_ePDovRDkyO5zuBN1DgN8EtdP)
cases['createddate'] = pd.to_datetime(cases['createddate'])
cases['closeddate'] = pd.to_datetime(cases['closeddate'])
cases['handle_hours'] = (cases['closeddate'] - cases['createddate']).dt.total_seconds() / 3600.0
agg = cases.groupby('agent_id').agg(case_count=('case_id','count'), avg_handle=('handle_hours','mean')).reset_index()
agg = agg[agg['case_count'] > 1]
if not agg.empty:
    result_id = agg.sort_values(['avg_handle','agent_id']).iloc[0]['agent_id']
else:
    result_id = None
out = json.dumps(result_id)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ePDovRDkyO5zuBN1DgN8EtdP': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'case_id': '500Wt00000DDepmIAD'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'case_id': '500Wt00000DDyzpIAD'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'case_id': '500Wt00000DDzUPIA1'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'case_id': '500Wt00000DDzsbIAD'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'case_id': '#500Wt00000DDzscIAD'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'case_id': '500Wt00000DDzuEIAT'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'case_id': '#500Wt00000DE02HIAT'}], 'var_call_RPoSmAqdLtZgBHz5LOt9GXHa': []}

exec(code, env_args)
