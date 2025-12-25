code = """import pandas as pd, json

cases = pd.DataFrame(var_call_X3spUN4kCY1bBKWc8Vc7KLgd)

for col in ['createddate','closeddate']:
    cases[col] = pd.to_datetime(cases[col])

cases['handle_time_hours'] = (cases['closeddate'] - cases['createddate']).dt.total_seconds() / 3600.0

agent_stats = cases.groupby('agent_id').agg(
    cases_handled=('agent_id','size'),
    avg_hrs=('handle_time_hours','mean')
).reset_index()

eligible = agent_stats[agent_stats['cases_handled'] > 1]

if eligible.empty:
    result = None
else:
    min_avg = eligible['avg_hrs'].min()
    best_agents = eligible[eligible['avg_hrs'] == min_avg]['agent_id'].tolist()
    result = best_agents[0]

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_X3spUN4kCY1bBKWc8Vc7KLgd': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_e54b2Nxv4g6Ad1IXboahIalL': []}

exec(code, env_args)
