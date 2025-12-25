code = """import pandas as pd
import json

case_data = locals()['var_function-call-7204162997623596997']

df_cases = pd.DataFrame(case_data)

# Cleanse Id and ownerid
df_cases['id'] = df_cases['id'].str.replace('#', '').str.strip()
df_cases['ownerid'] = df_cases['ownerid'].str.replace('#', '').str.strip()

# Convert dates to datetime objects
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

# Calculate handle time in minutes
df_cases['handle_time'] = (df_cases['closeddate'] - df_cases['createddate']).dt.total_seconds() / 60

# Filter out cases with non-positive handle time, though the initial query already handles createddate < closeddate
df_cases = df_cases[df_cases['handle_time'] > 0]

# Group by ownerid to count cases and calculate average handle time
agent_stats = df_cases.groupby('ownerid').agg(
    case_count=('id', 'count'),
    avg_handle_time=('handle_time', 'mean')
).reset_index()

# Filter for agents who processed more than one case
agents_more_than_one_case = agent_stats[agent_stats['case_count'] > 1]

if not agents_more_than_one_case.empty:
    # Find the agent with the lowest average handle time
    lowest_handle_time_agent = agents_more_than_one_case.loc[agents_more_than_one_case['avg_handle_time'].idxmin()]
    result_agent_id = lowest_handle_time_agent['ownerid']
else:
    result_agent_id = None

print("__RESULT__:")
print(json.dumps(result_agent_id))"""

env_args = {'var_function-call-7204162997623596997': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-12163430094501281139': []}

exec(code, env_args)
