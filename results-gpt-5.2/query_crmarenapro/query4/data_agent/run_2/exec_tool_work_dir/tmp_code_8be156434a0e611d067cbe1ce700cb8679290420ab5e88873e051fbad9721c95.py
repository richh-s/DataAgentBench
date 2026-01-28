code = """import json, pandas as pd
rows = var_call_uGyARuxqhZNnJ5ha0DGdVilD
# case_count may be str
for r in rows:
    r['case_count'] = int(r['case_count'])
df = pd.DataFrame(rows)
df['month_start'] = pd.to_datetime(df['month_start'])
# pick month with max count
max_row = df.loc[df['case_count'].idxmax()]
month_name = max_row['month_start'].strftime('%B')
print('__RESULT__:')
print(json.dumps(month_name))"""

env_args = {'var_call_2MWPUoZGF7Y6RxAESiC7krmx': [], 'var_call_CRx9oa5DPm8vfEfuOAMagdZw': [], 'var_call_uGyARuxqhZNnJ5ha0DGdVilD': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
