code = """import pandas as pd, json

cases = pd.DataFrame(var_call_VYx7pqQdZJbbUkUhD0nfIECO)

cases['createddate'] = pd.to_datetime(cases['createddate'])
cases['closeddate'] = pd.to_datetime(cases['closeddate'])

cases['handle_time_hours'] = (cases['closeddate'] - cases['createddate']).dt.total_seconds() / 3600.0

agent_stats = cases.groupby('agent_id').agg(
    cases_processed=('case_id', 'count'),
    avg_handle_time_hours=('handle_time_hours', 'mean')
).reset_index()

eligible = agent_stats[agent_stats['cases_processed'] > 1]

if eligible.empty:
    result = None
else:
    best_agent_id = eligible.sort_values('avg_handle_time_hours').iloc[0]['agent_id']
    result = best_agent_id

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VYx7pqQdZJbbUkUhD0nfIECO': [{'agent_id': '005Wt000003NJufIAG', 'case_id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'agent_id': '005Wt000003NJGLIA4', 'case_id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'agent_id': '005Wt000003NDqDIAW', 'case_id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'agent_id': '005Wt000003NJD9IAO', 'case_id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'case_id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'agent_id': '005Wt000003NJJaIAO', 'case_id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'agent_id': '005Wt000003NIddIAG', 'case_id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_fz9R4ukjaJjqKRoXoujJYkOq': []}

exec(code, env_args)
