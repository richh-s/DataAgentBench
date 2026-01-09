code = """import pandas as pd, json
orderitems = pd.DataFrame(var_call_JQo4fdWnDoqAfY0DkMjCc0SO)
cases = pd.DataFrame(var_call_PQzcUDOGQ54jqx6dAMfJmaBP)
# normalize ids by stripping leading '#'
orderitems['oid'] = orderitems['Id'].astype(str).str.replace('#','', regex=False).str.strip()
cases['orderitem_norm'] = cases['orderitemid__c'].astype(str).str.replace('#','', regex=False).str.strip()
# filter cases for this product's orderitems
product_oids = set(orderitems['oid'].tolist())
fc = cases[cases['orderitem_norm'].isin(product_oids)].copy()
# parse createddate and limit to past 10 months relative to 2021-04-10 => from 2020-06-10
fc['created_ts'] = pd.to_datetime(fc['createddate'], errors='coerce', utc=True)
fc = fc[(fc['created_ts'] >= pd.Timestamp('2020-06-10', tz='UTC')) & (fc['created_ts'] < pd.Timestamp('2021-04-11', tz='UTC'))]
fc['month'] = fc['created_ts'].dt.strftime('%B')
counts = fc.groupby(fc['created_ts'].dt.to_period('M')).size().sort_index()
# find month that significantly exceeds others: pick max; require at least 2 higher than second max
if counts.empty:
    ans = None
else:
    top = counts.max()
    second = counts.sort_values(ascending=False).iloc[1] if len(counts)>1 else 0
    peak_period = counts.idxmax()
    ans = peak_period.to_timestamp().strftime('%B')
print('__RESULT__:')
print(json.dumps({'answer': ans, 'counts': {str(k): int(v) for k,v in counts.items()}, 'top': int(top) if not counts.empty else None, 'second': int(second) if not counts.empty else None}))"""

env_args = {'var_call_JQo4fdWnDoqAfY0DkMjCc0SO': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_call_PQzcUDOGQ54jqx6dAMfJmaBP': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}]}

exec(code, env_args)
