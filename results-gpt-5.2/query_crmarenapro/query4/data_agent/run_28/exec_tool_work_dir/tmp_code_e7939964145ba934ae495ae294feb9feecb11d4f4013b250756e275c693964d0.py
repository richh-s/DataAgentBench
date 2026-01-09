code = """import json, pandas as pd

orderitems = pd.DataFrame(var_call_R7vTcVvwpjZt4ACx88givNvs)
cases = pd.DataFrame(var_call_12LDRbbFPckQTPj2XMAdhtDh)

orderitem_set = set(orderitems['orderitem_id'].astype(str))

cases['orderitem_clean'] = cases['orderitemid__c'].astype(str).str.replace('#','', regex=False)
cases = cases[cases['orderitem_clean'].isin(orderitem_set)].copy()

cases['created_ts'] = pd.to_datetime(cases['created_ts'])
cases['month'] = cases['created_ts'].dt.to_period('M').dt.to_timestamp()
counts = cases.groupby('month').size().sort_index()

# restrict to past 10 months inclusive ending 2021-04
start = pd.Timestamp('2020-07-01')
end = pd.Timestamp('2021-04-01')
counts = counts[(counts.index>=start) & (counts.index<=end)]

# find significant exceed: use z-score threshold 1.5; if none, take max
if len(counts)==0:
    out = None
else:
    mean = counts.mean()
    std = counts.std(ddof=0)
    if std == 0:
        best_month = counts.idxmax()
    else:
        z = (counts - mean) / std
        sig = z[z >= 1.5]
        best_month = (sig if len(sig)>0 else counts).idxmax()
    out = best_month.strftime('%B')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_b0QFZb2rwu0t1XOQZH9GMX4N': [], 'var_call_mDfjxn1UfZbbglMTCSCsLRv1': [], 'var_call_HGztwb3dVjnujjAe7aHcl1LC': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_mxClCuwicCtVXw0JmL28V6DO': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}], 'var_call_R7vTcVvwpjZt4ACx88givNvs': [{'orderitem_id': '802Wt0000078yuGIAQ'}, {'orderitem_id': '802Wt00000790mOIAQ'}, {'orderitem_id': '802Wt00000790zGIAQ'}, {'orderitem_id': '802Wt00000794F2IAI'}, {'orderitem_id': '802Wt000007968eIAA'}, {'orderitem_id': '802Wt00000796bfIAA'}, {'orderitem_id': '802Wt00000796qFIAQ'}, {'orderitem_id': '802Wt0000079734IAA'}, {'orderitem_id': '802Wt00000797W5IAI'}, {'orderitem_id': '802Wt00000797awIAA'}, {'orderitem_id': '802Wt00000797z7IAA'}, {'orderitem_id': '802Wt00000798VPIAY'}, {'orderitem_id': '802Wt00000798YdIAI'}, {'orderitem_id': '802Wt00000798okIAA'}, {'orderitem_id': '802Wt00000799o1IAA'}, {'orderitem_id': '802Wt0000079A2bIAE'}, {'orderitem_id': '802Wt0000079ACGIA2'}, {'orderitem_id': '802Wt0000079B0EIAU'}, {'orderitem_id': '802Wt0000079B6gIAE'}], 'var_call_12LDRbbFPckQTPj2XMAdhtDh': [{'id': '500Wt00000DDDtTIAX', 'created_ts': '2020-12-29 08:36:00', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'created_ts': '2020-09-01 10:30:00', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'created_ts': '2021-01-10 09:30:00', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'created_ts': '2020-09-05 09:15:00', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'created_ts': '2021-03-31 11:41:00', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'created_ts': '2020-07-05 09:45:00', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'created_ts': '2020-07-01 15:30:00', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'created_ts': '2021-03-24 18:04:00', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'created_ts': '2021-03-05 09:45:00', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'created_ts': '2020-11-05 11:00:00', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'created_ts': '2021-02-01 10:30:00', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'created_ts': '2021-01-25 09:30:00', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'created_ts': '2020-11-05 08:19:00', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'created_ts': '2020-10-01 14:30:00', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'created_ts': '2020-09-03 14:45:00', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'created_ts': '2020-10-22 03:55:00', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'created_ts': '2021-02-20 14:30:00', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'created_ts': '2020-09-29 01:59:00', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'created_ts': '2021-01-03 15:30:00', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'created_ts': '2021-03-07 11:25:00', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'created_ts': '2020-11-10 22:14:00', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'created_ts': '2020-11-09 19:02:00', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'created_ts': '2021-03-10 15:45:00', 'orderitemid__c': '802Wt00000797foIAA'}]}

exec(code, env_args)
