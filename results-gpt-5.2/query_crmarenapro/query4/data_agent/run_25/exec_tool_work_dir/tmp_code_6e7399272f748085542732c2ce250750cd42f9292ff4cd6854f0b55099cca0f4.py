code = """import json, pandas as pd
from datetime import datetime

data = var_call_Macv2zDzWgQBkUJFQ8qgGtSB

df = pd.DataFrame(data)
df['case_count'] = df['case_count'].astype(int)
df['month_start'] = pd.to_datetime(df['month_start'])
# define significant as strictly greater than all other months (max unique)
max_count = df['case_count'].max()
max_rows = df[df['case_count']==max_count].sort_values('month_start')
# if tie, pick earliest max month
month_name = max_rows.iloc[0]['month_start'].strftime('%B')
print('__RESULT__:')
print(json.dumps(month_name))"""

env_args = {'var_call_DblMzJiP6kLh05Nrcn6MRAHa': [], 'var_call_hmQ7i5pPilFAmoW9xYiP0lXi': [{'total_cases': '0', 'min_createddate': 'None', 'max_createddate': 'None'}], 'var_call_9G5i6f7hgoqeWlzQplIZVkh1': [{'total_cases': '0'}], 'var_call_aMJpHoe1i9scvXolWy2tMmi2': [{'total_cases': '5'}], 'var_call_Macv2zDzWgQBkUJFQ8qgGtSB': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
