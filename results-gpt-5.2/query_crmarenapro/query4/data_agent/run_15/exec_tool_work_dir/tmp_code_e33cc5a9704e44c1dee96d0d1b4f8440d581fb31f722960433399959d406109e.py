code = """import json, pandas as pd

df = pd.DataFrame(var_call_RfM27AnUMVRP8EMPSASrlNyY)
if df.empty:
    out = None
else:
    df['case_count'] = df['case_count'].astype(int)
    df['month_start'] = pd.to_datetime(df['month_start'])
    # define significant as strictly greater than all other months (unique max)
    max_cnt = df['case_count'].max()
    if (df['case_count'] == max_cnt).sum() == 1 and max_cnt > df['case_count'].median():
        month = df.loc[df['case_count'].idxmax(), 'month_start'].strftime('%B')
    else:
        # if no unique significant spike, still return the month with max count
        month = df.loc[df['case_count'].idxmax(), 'month_start'].strftime('%B')
    out = month

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_phrgB6JWIMCOCNfEjEQdG0e5': [], 'var_call_mf6RZb6xRNR8W2Gn3zIHytfR': [], 'var_call_hXT10KloE2Ks7D1nantfqZVo': [{'orderitemid__c': '802Wt00000792zUIAQ', 'cnt': '4'}, {'orderitemid__c': '802Wt0000078ypPIAQ', 'cnt': '3'}, {'orderitemid__c': '802Wt0000078xAFIAY', 'cnt': '3'}, {'orderitemid__c': '802Wt00000798aDIAQ', 'cnt': '3'}, {'orderitemid__c': '802Wt00000797CjIAI', 'cnt': '3'}, {'orderitemid__c': '802Wt00000796qFIAQ', 'cnt': '3'}, {'orderitemid__c': '802Wt00000799EZIAY', 'cnt': '3'}, {'orderitemid__c': '802Wt00000797r5IAA', 'cnt': '3'}, {'orderitemid__c': '802Wt0000079A2ZIAU', 'cnt': '3'}, {'orderitemid__c': '802Wt00000798S9IAI', 'cnt': '3'}, {'orderitemid__c': '802Wt000007928FIAQ', 'cnt': '3'}, {'orderitemid__c': '802Wt00000792tiIAA', 'cnt': '3'}, {'orderitemid__c': '802Wt00000798olIAA', 'cnt': '3'}, {'orderitemid__c': '802Wt00000796jiIAA', 'cnt': '2'}, {'orderitemid__c': '802Wt00000798iIIAQ', 'cnt': '2'}, {'orderitemid__c': '802Wt00000798NMIAY', 'cnt': '2'}, {'orderitemid__c': '802Wt00000797foIAA', 'cnt': '2'}, {'orderitemid__c': '802Wt00000797pRIAQ', 'cnt': '2'}, {'orderitemid__c': '802Wt00000798dRIAQ', 'cnt': '2'}, {'orderitemid__c': '802Wt00000799UfIAI', 'cnt': '2'}], 'var_call_xliIEiJ34KtCIVcSNSypojHC': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'closeddate': '2021-01-25T15:27:34.000+0000', 'subject': 'ROI Metrics Clarification  ', 'status': 'Closed'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'closeddate': '2020-11-05T08:50:10.000+0000', 'subject': 'Update Alerts Absent', 'status': 'Closed'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None', 'subject': 'SecureAnalytics Compliance Concern', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'closeddate': '2021-03-07T17:46:52.000+0000', 'subject': 'No Feature Update Notices', 'status': 'Closed'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'closeddate': '2020-11-10T09:47:54.000+0000', 'subject': 'Missing Feature Notifications', 'status': 'Closed'}], 'var_call_RfM27AnUMVRP8EMPSASrlNyY': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
