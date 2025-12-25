code = """import json, pandas as pd
from datetime import datetime

orderitems = var_call_8I6pD8cyVsezWSrTEH687aHj
case_file = var_call_j0hqDw7K0IPcYnLRGxO5LsFC

with open(case_file) as f:
    cases = json.load(f)

oi_ids = {r['Id'].lstrip('#') for r in orderitems}

filtered = [c for c in cases if c['orderitemid__c'].lstrip('#') in oi_ids]

df = pd.DataFrame(filtered)

if df.empty:
    result = None
else:
    df['created_ts'] = pd.to_datetime(df['created_ts'])
    cutoff_start = pd.Timestamp('2020-06-10')
    cutoff_end = pd.Timestamp('2021-04-11')
    df = df[(df['created_ts']>=cutoff_start) & (df['created_ts']<cutoff_end)]
    if df.empty:
        result = None
    else:
        counts = df.groupby(df['created_ts'].dt.to_period('M')).size().sort_index()
        if counts.empty:
            result = None
        else:
            max_month = counts.idxmax().to_timestamp()
            result = max_month.strftime('%B')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8I6pD8cyVsezWSrTEH687aHj': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_call_htefsdXovrlXPBKNieJH6ni7': [{'createddate': '2023-07-02T11:00:00.000+0000'}], 'var_call_ur7jxJpg3BL7J8zOXKY0eq5t': [{'created_date': '2023-07-02'}], 'var_call_j0hqDw7K0IPcYnLRGxO5LsFC': 'file_storage/call_j0hqDw7K0IPcYnLRGxO5LsFC.json'}

exec(code, env_args)
