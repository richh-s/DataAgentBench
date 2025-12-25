code = """import pandas as pd, json
cases = pd.DataFrame(var_call_2NTbTrZg10Y4uPx3LU2taxm1)
# parse dates
cases['createddate'] = pd.to_datetime(cases['createddate'])
cases['closeddate'] = pd.to_datetime(cases['closeddate'])
# handle time in seconds (no transfers in this dataset, so all count)
cases['handle_seconds'] = (cases['closeddate'] - cases['createddate']).dt.total_seconds()
# agents with more than one case
agent_stats = cases.groupby('agent_id').agg(cases_count=('agent_id','size'), avg_handle=('handle_seconds','mean')).reset_index()
eligible = agent_stats[agent_stats['cases_count'] > 1]
result_id = None
if not eligible.empty:
    result_id = eligible.sort_values(['avg_handle','agent_id']).iloc[0]['agent_id']
result = json.dumps(result_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_2NTbTrZg10Y4uPx3LU2taxm1': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_zMotuctASFPRvtgfeYLHAeit': []}

exec(code, env_args)
