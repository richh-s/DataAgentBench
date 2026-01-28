code = """import json
import pandas as pd

df = pd.DataFrame(var_call_KcPe61h6PuKYwyzO0aKtPEcs)
if df.empty:
    ans = None
else:
    df['case_count'] = df['case_count'].astype(int)
    df['month_start'] = pd.to_datetime(df['month_start'])
    # past 10 months relative to 2021-04-10 => 2020-07-01 through 2021-04-01 month buckets
    start = pd.Timestamp('2020-07-01')
    end = pd.Timestamp('2021-04-01')
    df = df[(df['month_start']>=start) & (df['month_start']<=end)]
    # find max
    df = df.sort_values(['case_count','month_start'], ascending=[False, False])
    top = df.iloc[0]
    ans = top['month_start'].strftime('%B')

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_3m8vQ8OGnOU2qlCACIbJuTii': [], 'var_call_KcPe61h6PuKYwyzO0aKtPEcs': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
