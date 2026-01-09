code = """import json, pandas as pd
from datetime import datetime

orderitems = pd.DataFrame(var_call_A5GZWFvPtUQwet4iCDtvOdwi)
cases = pd.DataFrame(var_call_bBHPyaDZeUDen8JG8KpFGT4s)

orderitem_set = set(orderitems['orderitem_id'].dropna().astype(str))
sc = cases[cases['orderitem_id'].isin(orderitem_set)].copy()

sc['created_dt'] = pd.to_datetime(sc['createddate'], errors='coerce', utc=True)
sc['month'] = sc['created_dt'].dt.month
sc['month_name'] = sc['created_dt'].dt.strftime('%B')

counts = sc.groupby(['month','month_name']).size().reset_index(name='n').sort_values('n', ascending=False)
# determine if a particular month significantly exceeds others: pick max if strictly greater than second max by >=2 cases (simple heuristic)
if counts.empty:
    ans = None
else:
    top = counts.iloc[0]
    if len(counts) == 1:
        ans = top['month_name']
    else:
        second = counts.iloc[1]
        ans = top['month_name'] if top['n'] >= second['n'] + 2 else top['month_name']

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_A5GZWFvPtUQwet4iCDtvOdwi': [{'orderitem_id': '802Wt0000078yuGIAQ'}, {'orderitem_id': '802Wt00000790mOIAQ'}, {'orderitem_id': '802Wt00000790zGIAQ'}, {'orderitem_id': '802Wt00000794F2IAI'}, {'orderitem_id': '802Wt000007968eIAA'}, {'orderitem_id': '802Wt00000796bfIAA'}, {'orderitem_id': '802Wt00000796qFIAQ'}, {'orderitem_id': '802Wt0000079734IAA'}, {'orderitem_id': '802Wt00000797W5IAI'}, {'orderitem_id': '802Wt00000797awIAA'}, {'orderitem_id': '802Wt00000797z7IAA'}, {'orderitem_id': '802Wt00000798VPIAY'}, {'orderitem_id': '802Wt00000798YdIAI'}, {'orderitem_id': '802Wt00000798okIAA'}, {'orderitem_id': '802Wt00000799o1IAA'}, {'orderitem_id': '802Wt0000079A2bIAE'}, {'orderitem_id': '802Wt0000079ACGIA2'}, {'orderitem_id': '802Wt0000079B0EIAU'}, {'orderitem_id': '802Wt0000079B6gIAE'}], 'var_call_bBHPyaDZeUDen8JG8KpFGT4s': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitem_id': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitem_id': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitem_id': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitem_id': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitem_id': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitem_id': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitem_id': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitem_id': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitem_id': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitem_id': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitem_id': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitem_id': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitem_id': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitem_id': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitem_id': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitem_id': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitem_id': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitem_id': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitem_id': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitem_id': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitem_id': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitem_id': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitem_id': '802Wt00000797foIAA'}]}

exec(code, env_args)
