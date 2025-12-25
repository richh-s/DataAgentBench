code = """import pandas as pd
from datetime import datetime
import json

cases = locals()['var_function-call-1841987621623620202']

df_cases = pd.DataFrame(cases)

# Convert datetime strings to datetime objects
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

# Calculate handle time in seconds
df_cases['handle_time'] = (df_cases['closeddate'] - df_cases['createddate']).dt.total_seconds()

# Group by ownerid, count cases, and calculate average handle time
agent_stats = df_cases.groupby('ownerid').agg(
    case_count=('id', 'count'),
    avg_handle_time=('handle_time', 'mean')
).reset_index()

# Filter agents who processed more than one case
filtered_agents = agent_stats[agent_stats['case_count'] > 1]

# Find the agent with the lowest average handle time
if not filtered_agents.empty:
    lowest_avg_handle_time_agent = filtered_agents.loc[filtered_agents['avg_handle_time'].idxmin()]
    result_agent_id = lowest_avg_handle_time_agent['ownerid']
else:
    result_agent_id = None 


print('__RESULT__:')
print(json.dumps(result_agent_id))"""

env_args = {'var_function-call-1841987621623620202': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-12233347763171719886': []}

exec(code, env_args)
