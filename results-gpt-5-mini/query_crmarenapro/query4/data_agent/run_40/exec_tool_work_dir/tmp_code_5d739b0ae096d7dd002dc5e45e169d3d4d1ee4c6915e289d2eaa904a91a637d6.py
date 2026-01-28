code = """import pandas as pd
import json

df = pd.DataFrame(var_call_Wkn23I3tGPPt7bC9xuLtOeV0)
if df.empty:
    result = None
else:
    df['month_name'] = df['month_name'].str.strip()
    df['cnt'] = df['cnt'].astype(int)
    mean = df['cnt'].mean()
    std = df['cnt'].std(ddof=0)
    threshold = mean + std
    max_row = df.loc[df['cnt'].idxmax()]
    if max_row['cnt'] > threshold:
        result = max_row['month_name']
    else:
        result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eYcwqYk0M2TrbSpbzu273mFz': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_Wkn23I3tGPPt7bC9xuLtOeV0': [{'month_start': '2020-09-01 00:00:00', 'month_name': 'September', 'cnt': '1'}, {'month_start': '2020-11-01 00:00:00', 'month_name': 'November ', 'cnt': '2'}, {'month_start': '2021-01-01 00:00:00', 'month_name': 'January  ', 'cnt': '1'}, {'month_start': '2021-03-01 00:00:00', 'month_name': 'March    ', 'cnt': '1'}]}

exec(code, env_args)
