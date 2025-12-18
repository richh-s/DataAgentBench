code = """import pandas as pd
from datetime import datetime

cases_data = locals()['var_function-call-7153037534315772368']['results']

df_cases = pd.DataFrame(cases_data)

# Clean 'case_id' and 'agent_id' columns by stripping leading/trailing whitespace and '#' character
df_cases['case_id'] = df_cases['case_id'].str.strip().str.lstrip('#')
df_cases['agent_id'] = df_cases['agent_id'].str.strip().str.lstrip('#')

# Convert date columns to datetime objects
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

# Calculate handle time in minutes
df_cases['handle_time_minutes'] = (df_cases['closeddate'] - df_cases['createddate']).dt.total_seconds() / 60

# Filter for agents who processed more than one case
agent_case_counts = df_cases.groupby('agent_id').size().reset_index(name='case_count')
agents_with_multiple_cases = agent_case_counts[agent_case_counts['case_count'] > 1]

# Merge back to get the handle times for these agents
df_filtered_cases = df_cases[df_cases['agent_id'].isin(agents_with_multiple_cases['agent_id'])]

# Calculate average handle time for these agents
average_handle_time = df_filtered_cases.groupby('agent_id')['handle_time_minutes'].mean().reset_index()

# Find the agent with the lowest average handle time
lowest_avg_handle_time_agent = average_handle_time.sort_values(by='handle_time_minutes', ascending=True).iloc[0]

print('__RESULT__:')
print(lowest_avg_handle_time_agent['agent_id']))"""

env_args = {'var_function-call-7153037534315772368': [{'case_id': '500Wt00000DDepmIAD', 'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'case_id': '500Wt00000DDyzpIAD', 'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'case_id': '500Wt00000DDzUPIA1', 'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'case_id': '500Wt00000DDzsbIAD', 'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'case_id': '#500Wt00000DDzscIAD', 'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'case_id': '500Wt00000DDzuEIAT', 'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'case_id': '#500Wt00000DE02HIAT', 'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-15040405172988116327': []}

exec(code, env_args)
