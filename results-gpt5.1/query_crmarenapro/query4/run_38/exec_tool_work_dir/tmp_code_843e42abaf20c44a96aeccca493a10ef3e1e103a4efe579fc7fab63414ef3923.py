code = """import pandas as pd, json
order_items = pd.DataFrame(var_call_vDlVAhiM12KHMn8uLpGjwnn4)
cases = pd.DataFrame(var_call_6kPLInpXUYJzgnsrn6d96lSd)
order_items['clean_id'] = order_items['Id'].str.lstrip('#')
cases['clean_orderitemid'] = cases['orderitemid__c'].str.lstrip('#')
merged = cases.merge(order_items, left_on='clean_orderitemid', right_on='clean_id', how='inner')
merged['createddate'] = pd.to_datetime(merged['createddate'])
merged = merged[(merged['createddate'] >= '2020-06-10') & (merged['createddate'] < '2021-04-11')]
merged['month'] = merged['createddate'].dt.to_period('M')
counts = merged.groupby('month').size().reset_index(name='case_count')
if counts.empty:
    result = None
else:
    counts = counts.sort_values('case_count', ascending=False)
    top = counts.iloc[0]
    if len(counts) > 1 and counts.iloc[1]['case_count'] == top['case_count']:
        result = None
    else:
        month_str = str(top['month']) + "-01"
        month_name = pd.to_datetime(month_str).strftime('%B')
        result = month_name
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_vDlVAhiM12KHMn8uLpGjwnn4': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_call_ESA1HCadZfDrs3BqeGIpEBnv': [{'createddate': '2020-12-29T08:36:00.000+0000'}, {'createddate': '2020-09-01T10:30:00.000+0000'}, {'createddate': '2021-01-10T09:30:00.000+0000'}, {'createddate': '2020-09-05T09:15:00.000+0000'}, {'createddate': '2021-03-31T11:41:00.000+0000'}, {'createddate': '2020-07-05T09:45:00.000+0000'}, {'createddate': '2020-07-01T15:30:00.000+0000'}, {'createddate': '2021-03-24T18:04:00.000+0000'}, {'createddate': '2021-03-05T09:45:00.000+0000'}, {'createddate': '2020-11-05T11:00:00.000+0000'}, {'createddate': '2021-02-01T10:30:00.000+0000'}, {'createddate': '2021-01-25T09:30:00.000+0000'}, {'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2020-10-01T14:30:00.000+0000'}, {'createddate': '2020-09-03T14:45:00.000+0000'}, {'createddate': '2020-10-22T03:55:00.000+0000'}, {'createddate': '2021-02-20T14:30:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-01-03T15:30:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-10T22:14:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}, {'createddate': '2021-03-10T15:45:00.000+0000'}], 'var_call_6kPLInpXUYJzgnsrn6d96lSd': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}]}

exec(code, env_args)
