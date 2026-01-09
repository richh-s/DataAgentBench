code = """import json, pandas as pd

df = pd.DataFrame(var_call_82bO5G0N6uJ3EnUq2JZNQVlm)
if df.empty:
    out = None
else:
    df['case_count'] = df['case_count'].astype(int)
    df['month_start'] = pd.to_datetime(df['month_start'])
    # determine if any month significantly exceeds others: use > mean + 2*std heuristic
    mean = df['case_count'].mean()
    std = df['case_count'].std(ddof=0)
    thresh = mean + 2*std
    sig = df[df['case_count'] > thresh].sort_values('case_count', ascending=False)
    if sig.empty:
        # fallback to max month if uniquely highest
        maxc = df['case_count'].max()
        top = df[df['case_count']==maxc]
        if len(top)==1 and (maxc > df['case_count'].median()):
            sig = top
    if sig.empty:
        out = None
    else:
        out = sig.iloc[0]['month_start'].strftime('%B')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NVXWMhXf6akwBfsDKt3wPiyS': [], 'var_call_Io7Hwtf71oy8U4hg1RbeoYwk': [], 'var_call_82bO5G0N6uJ3EnUq2JZNQVlm': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
