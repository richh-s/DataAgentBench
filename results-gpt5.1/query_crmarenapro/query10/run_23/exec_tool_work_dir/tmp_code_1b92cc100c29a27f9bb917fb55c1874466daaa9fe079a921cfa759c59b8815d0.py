code = """import json, pandas as pd
from datetime import datetime

cases = var_call_1FXyfMqy8Ifchowo9hAAZfcQ

df = pd.DataFrame(cases)

for col in ['createddate','closeddate']:
    df[col] = pd.to_datetime(df[col])

# handle time in seconds
df['handle_seconds'] = (df['closeddate'] - df['createddate']).dt.total_seconds()

# all these cases have only one owner assignment since transfer history is empty
# group by agent and compute avg handle time and count of cases
agg = df.groupby('agent_id').agg(case_count=('agent_id','size'), avg_handle=('handle_seconds','mean')).reset_index()

# filter agents with more than one case
eligible = agg[agg['case_count'] > 1]

if eligible.empty:
    result = None
else:
    best_agent = eligible.sort_values(['avg_handle','agent_id']).iloc[0]['agent_id']
    result = best_agent

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1FXyfMqy8Ifchowo9hAAZfcQ': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_Ry3Bq7fr7Tn1ezeCKSKRoPnb': []}

exec(code, env_args)
