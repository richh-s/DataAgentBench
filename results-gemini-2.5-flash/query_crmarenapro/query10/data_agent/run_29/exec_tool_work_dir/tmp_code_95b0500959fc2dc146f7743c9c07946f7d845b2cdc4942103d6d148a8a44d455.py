code = """import pandas as pd
from datetime import datetime

case_data = locals()['var_function-call-17675603725989747493']['results']

df = pd.DataFrame(case_data)
df['createddate'] = pd.to_datetime(df['createddate'])
df['closeddate'] = pd.to_datetime(df['closeddate'])

df['handle_time'] = (df['closeddate'] - df['createddate']).dt.total_seconds() / 60  # in minutes

agent_case_counts = df['ownerid'].value_counts()
agents_more_than_one_case = agent_case_counts[agent_case_counts > 1].index

df_filtered = df[df['ownerid'].isin(agents_more_than_one_case)]

average_handle_time = df_filtered.groupby('ownerid')['handle_time'].mean()

if not average_handle_time.empty:
    lowest_handle_time_agent = average_handle_time.idxmin()
    result = lowest_handle_time_agent
else:
    result = None

print('__RESULT__:')
print(pd.json_normalize(result).to_json(orient='records'))"""

env_args = {'var_function-call-8484619367196463445': [], 'var_function-call-17675603725989747493': [{'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}]}

exec(code, env_args)
