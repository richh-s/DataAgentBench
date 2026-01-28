code = """import json, pandas as pd
rows = var_call_ESYDTW6PGKrr1Q6vADuIeshc
# pick month with max count; if tie, earliest? question asks significantly exceeds others; use max.
df = pd.DataFrame(rows)
df['case_count']=df['case_count'].astype(int)
df['month_start']=pd.to_datetime(df['month_start'])
max_row = df.sort_values(['case_count','month_start'], ascending=[False, True]).iloc[0]
month_name = max_row['month_start'].strftime('%B')
print('__RESULT__:')
print(json.dumps(month_name))"""

env_args = {'var_call_Ylczao0mfg71dwWPikwZbwf7': [], 'var_call_l6SmSS447IFsFmSNDJw7mEHH': [], 'var_call_6pvorehAv6e4rzqUytb1NWsL': [{'cnt': '0'}], 'var_call_Je837l9SRBUcUA6QMiPGcNWa': [{'cnt': '5'}], 'var_call_ESYDTW6PGKrr1Q6vADuIeshc': [{'month_start': '2020-11-01', 'case_count': '2'}, {'month_start': '2021-03-01', 'case_count': '1'}, {'month_start': '2021-01-01', 'case_count': '1'}, {'month_start': '2020-09-01', 'case_count': '1'}]}

exec(code, env_args)
