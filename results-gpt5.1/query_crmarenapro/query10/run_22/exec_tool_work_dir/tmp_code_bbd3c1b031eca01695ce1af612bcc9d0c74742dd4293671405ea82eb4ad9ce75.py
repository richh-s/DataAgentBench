code = """import pandas as pd, json
cases = pd.DataFrame(var_call_ZbE2M1vorLMp7vVX9MhLk5wA)
# Handle time in seconds
cases['createddate'] = pd.to_datetime(cases['createddate'])
cases['closeddate'] = pd.to_datetime(cases['closeddate'])
cases['handle_time_sec'] = (cases['closeddate'] - cases['createddate']).dt.total_seconds()
# Count cases handled (including transferred-in, per policy, but we have only owner at closure; assume each listed case counts once per agent)
agent_stats = cases.groupby('agent_id').agg(avg_handle_time_sec=('handle_time_sec','mean'), case_count=('case_id','nunique')).reset_index()
# Filter agents with more than one case
agent_stats = agent_stats[agent_stats['case_count'] > 1]
if agent_stats.empty:
    result = None
else:
    best = agent_stats.sort_values(['avg_handle_time_sec','agent_id']).iloc[0]
    result = best['agent_id']
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ZbE2M1vorLMp7vVX9MhLk5wA': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'case_id': '500Wt00000DDepmIAD'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'case_id': '500Wt00000DDyzpIAD'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'case_id': '500Wt00000DDzUPIA1'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'case_id': '500Wt00000DDzsbIAD'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'case_id': '#500Wt00000DDzscIAD'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'case_id': '500Wt00000DDzuEIAT'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'case_id': '#500Wt00000DE02HIAT'}], 'var_call_J2Tv1aielLqTyRfigozhCR2J': []}

exec(code, env_args)
