code = """import pandas as pd
from datetime import datetime

cases_data = locals()['var_function-call-12105220215537794408']

df_cases = pd.DataFrame(cases_data)

df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

df_cases['handle_time'] = (df_cases['closeddate'] - df_cases['createddate']).dt.total_seconds()

agent_case_counts = df_cases.groupby('ownerid')['id'].count()
agents_with_multiple_cases = agent_case_counts[agent_case_counts > 1].index

df_filtered_cases = df_cases[df_cases['ownerid'].isin(agents_with_multiple_cases)]

average_handle_time = df_filtered_cases.groupby('ownerid')['handle_time'].mean()

if not average_handle_time.empty:
    lowest_avg_handle_time_agent = average_handle_time.idxmin()
else:
    lowest_avg_handle_time_agent = None


print('__RESULT__:')
print(lowest_avg_handle_time_agent)"""

env_args = {'var_function-call-12105220215537794408': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-6948644783581481028': []}

exec(code, env_args)
