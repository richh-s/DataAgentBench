code = """import pandas as pd
from datetime import datetime

cases_data = locals()['var_function-call-3536210292843516054']
df_cases = pd.DataFrame(cases_data)

# Clean Id and OwnerId
df_cases['id'] = df_cases['id'].str.replace('#', '').str.strip()
df_cases['ownerid'] = df_cases['ownerid'].str.replace('#', '').str.strip()

# Filter out cases that are not closed (closeddate is not 'None')
df_cases_closed = df_cases[df_cases['closeddate'] != 'None'].copy()

# Convert dates to datetime objects
df_cases_closed['createddate'] = pd.to_datetime(df_cases_closed['createddate'])
df_cases_closed['closeddate'] = pd.to_datetime(df_cases_closed['closeddate'])

# Calculate handle time in seconds
df_cases_closed['handle_time'] = (df_cases_closed['closeddate'] - df_cases_closed['createddate']).dt.total_seconds()

# Group by ownerid and calculate average handle time and count of cases
agent_stats = df_cases_closed.groupby('ownerid').agg(
    average_handle_time=('handle_time', 'mean'),
    case_count=('id', 'count')
).reset_index()

# Filter for agents who processed more than one case
eligible_agents = agent_stats[agent_stats['case_count'] > 1]

if not eligible_agents.empty:
    # Find the agent with the lowest average handle time
    lowest_avg_handle_time_agent = eligible_agents.sort_values(by='average_handle_time').iloc[0]
    result = lowest_avg_handle_time_agent['ownerid']
else:
    result = "No agents processed more than one case in the given period."

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-3536210292843516054': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-7523304426336004592': []}

exec(code, env_args)
