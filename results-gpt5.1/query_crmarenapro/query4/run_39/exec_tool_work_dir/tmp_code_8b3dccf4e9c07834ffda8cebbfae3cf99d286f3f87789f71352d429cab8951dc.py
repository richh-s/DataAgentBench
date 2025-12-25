code = """import json, pandas as pd
from datetime import datetime

orderitems = var_call_qpd8JOmlih0idQpaPYO38j1e
with open(var_call_bKgRwBvh7ceZhC7zVqOIiDKB) as f:
    cases = json.load(f)

oi_df = pd.DataFrame(orderitems)
oi_df['clean_id'] = oi_df['Id'].str.replace('#','', regex=False)

cases_df = pd.DataFrame(cases)
cases_df['orderitemid__c_clean'] = cases_df['orderitemid__c'].str.replace('#','', regex=False)

merged = cases_df.merge(oi_df, left_on='orderitemid__c_clean', right_on='clean_id', how='inner')

merged['created_dt'] = pd.to_datetime(merged['createddate'], utc=True)
start = pd.Timestamp('2020-06-10', tz='UTC')
end = pd.Timestamp('2021-04-11', tz='UTC')
mask = (merged['created_dt'] >= start) & (merged['created_dt'] < end)
filtered = merged.loc[mask].copy()

filtered['month'] = filtered['created_dt'].dt.to_period('M')
counts = filtered.groupby('month').size().sort_values(ascending=False)

if counts.empty:
    result = None
else:
    top_month = counts.index[0]
    if len(counts) > 1:
        second = counts.iloc[1]
    else:
        second = 0
    if counts.iloc[0] >= second + 2:
        dt = top_month.to_timestamp()
        month_name = dt.strftime('%B')
        result = month_name
    else:
        result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_qpd8JOmlih0idQpaPYO38j1e': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_call_bKgRwBvh7ceZhC7zVqOIiDKB': 'file_storage/call_bKgRwBvh7ceZhC7zVqOIiDKB.json'}

exec(code, env_args)
