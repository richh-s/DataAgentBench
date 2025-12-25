code = """import pandas as pd, json
order_items = pd.DataFrame(var_call_RS0NqMwBOGmHAIbLeznJzC5F)
cases = pd.DataFrame(var_call_MnhXjJZEVc3cHPjzE3SDBNAN)
order_items['clean_id'] = order_items['Id'].str.replace('#','', regex=False)
cases['clean_orderitemid'] = cases['orderitemid__c'].str.replace('#','', regex=False)
merged = cases.merge(order_items, left_on='clean_orderitemid', right_on='clean_id', how='inner')
if merged.empty:
    result = None
else:
    merged['month'] = pd.to_datetime(merged['created_date']).dt.to_period('M')
    counts = merged.groupby('month').size().reset_index(name='case_count')
    counts['z'] = (counts['case_count'] - counts['case_count'].mean())/counts['case_count'].std(ddof=0) if len(counts)>1 else 0
    max_row = counts.loc[counts['case_count'].idxmax()]
    if len(counts)>1 and max_row['z']>2:
        month_name = max_row['month'].strftime('%B')
    else:
        month_name = None
    result = month_name
res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_RS0NqMwBOGmHAIbLeznJzC5F': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_MnhXjJZEVc3cHPjzE3SDBNAN': [{'created_date': '2020-12-29', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'created_date': '2020-09-01', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'created_date': '2021-01-10', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'created_date': '2020-09-05', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'created_date': '2021-03-31', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'created_date': '2020-07-05', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'created_date': '2020-07-01', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'created_date': '2021-03-24', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'created_date': '2021-03-05', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'created_date': '2020-11-05', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'created_date': '2021-02-01', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'created_date': '2021-01-25', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'created_date': '2020-11-05', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'created_date': '2020-10-01', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'created_date': '2020-09-03', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'created_date': '2020-10-22', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'created_date': '2021-02-20', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'created_date': '2020-09-29', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'created_date': '2021-01-03', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'created_date': '2021-03-07', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'created_date': '2020-11-10', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'created_date': '2020-11-09', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'created_date': '2021-03-10', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}]}

exec(code, env_args)
