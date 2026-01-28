code = """import json, pandas as pd

df = pd.DataFrame(var_call_zadFKOTQtRBRn4dqo21mxlOE)
if df.empty:
    month_name = None
else:
    df['case_count'] = df['case_count'].astype(int)
    df['month_start'] = pd.to_datetime(df['month_start'])
    # Determine if a month significantly exceeds others: use mean + 2*std heuristic.
    mean = df['case_count'].mean()
    std = df['case_count'].std(ddof=0)
    threshold = mean + 2*std
    top = df.sort_values('case_count', ascending=False).iloc[0]
    if top['case_count'] > threshold:
        month_name = top['month_start'].strftime('%B')
    else:
        # if no significant outlier, return the max month anyway per question intent
        month_name = top['month_start'].strftime('%B')

print('__RESULT__:')
print(json.dumps(month_name))"""

env_args = {'var_call_vDzYbcVbO74MQY6HK00rlqdV': [], 'var_call_qG2Nu2fA5LnUmVNE3bbkIakn': [{'column_name': 'id', 'data_type': 'text'}, {'column_name': 'priority', 'data_type': 'text'}, {'column_name': 'subject', 'data_type': 'text'}, {'column_name': 'description', 'data_type': 'text'}, {'column_name': 'status', 'data_type': 'text'}, {'column_name': 'contactid', 'data_type': 'text'}, {'column_name': 'createddate', 'data_type': 'text'}, {'column_name': 'closeddate', 'data_type': 'text'}, {'column_name': 'orderitemid__c', 'data_type': 'text'}, {'column_name': 'issueid__c', 'data_type': 'text'}, {'column_name': 'accountid', 'data_type': 'text'}, {'column_name': 'ownerid', 'data_type': 'text'}], 'var_call_Eo0CFbDkrDY2BEpYirhAgVAa': [], 'var_call_YF2vrHikzg4QPQdfFzNg8PVW': [{'id': '500Wt00000DDDtTIAX', 'subject': 'Missing Feature Update Alerts', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'subject': 'Access Issues with Training Module', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'subject': 'AI Cirku-Tech Workflow Lag', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'subject': 'Training Portal Login Problem', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'subject': 'Workflow Integration Lag  ', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}], 'var_call_u81JbLuFE0V8JnkgV2qeGGYw': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}], 'var_call_LOwQl3oIjjntfipNYgm4Ep0g': [{'orderitem_id': '802Wt0000078yuGIAQ'}, {'orderitem_id': '802Wt00000790mOIAQ'}, {'orderitem_id': '802Wt00000790zGIAQ'}, {'orderitem_id': '802Wt00000794F2IAI'}, {'orderitem_id': '802Wt000007968eIAA'}, {'orderitem_id': '802Wt00000796bfIAA'}, {'orderitem_id': '802Wt00000796qFIAQ'}, {'orderitem_id': '802Wt0000079734IAA'}, {'orderitem_id': '802Wt00000797W5IAI'}, {'orderitem_id': '802Wt00000797awIAA'}, {'orderitem_id': '802Wt00000797z7IAA'}, {'orderitem_id': '802Wt00000798VPIAY'}, {'orderitem_id': '802Wt00000798YdIAI'}, {'orderitem_id': '802Wt00000798okIAA'}, {'orderitem_id': '802Wt00000799o1IAA'}, {'orderitem_id': '802Wt0000079A2bIAE'}, {'orderitem_id': '802Wt0000079ACGIA2'}, {'orderitem_id': '802Wt0000079B0EIAU'}, {'orderitem_id': '802Wt0000079B6gIAE'}], 'var_call_NMA7RydmhKaMoLBRJ3eGYIlt': [{'month_start': '2020-07-01 00:00:00', 'case_count': '2'}, {'month_start': '2020-09-01 00:00:00', 'case_count': '4'}, {'month_start': '2020-10-01 00:00:00', 'case_count': '2'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '4'}, {'month_start': '2020-12-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '3'}, {'month_start': '2021-02-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '5'}], 'var_call_zadFKOTQtRBRn4dqo21mxlOE': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
