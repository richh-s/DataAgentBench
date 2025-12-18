code = """import pandas as pd
import json
from datetime import datetime

cases = locals()['var_function-call-16886252841350397161']

df = pd.DataFrame(cases)

df['createddate'] = pd.to_datetime(df['createddate'])
df['closeddate'] = pd.to_datetime(df['closeddate'])

df['handle_time'] = (df['closeddate'] - df['createddate']).dt.total_seconds() / 3600  # in hours

agent_case_count = df.groupby('ownerid')['id'].count()
agents_more_than_one_case = agent_case_count[agent_case_count > 1].index

if not agents_more_than_one_case.empty:
    df_filtered = df[df['ownerid'].isin(agents_more_than_one_case)]
    average_handle_time = df_filtered.groupby('ownerid')['handle_time'].mean()
    lowest_avg_handle_time_agent = average_handle_time.idxmin()
    result = {'agent_id': lowest_avg_handle_time_agent}
else:
    result = {'message': "No agents processed more than one case in the past four months."}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-16886252841350397161': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-295332720156216484': [], 'var_function-call-9168988524274589370': []}

exec(code, env_args)
