code = """import json, pandas as pd
rows = var_call_8lgrP7uu3QA5aipumuwM5cK1
# build full 10-month window: 2020-07..2021-04
months = pd.date_range('2020-07-01','2021-04-01',freq='MS')
df = pd.DataFrame(rows)
if not df.empty:
    df['month_start']=pd.to_datetime(df['month_start'])
    df['case_count']=df['case_count'].astype(int)
else:
    df = pd.DataFrame({'month_start':[], 'case_count':[]})
full = pd.DataFrame({'month_start':months})
full = full.merge(df, on='month_start', how='left').fillna({'case_count':0})
full['case_count']=full['case_count'].astype(int)
# identify month with max cases
max_count = full['case_count'].max()
max_months = full.loc[full['case_count']==max_count,'month_start'].tolist()
# choose earliest if tie
chosen = min(max_months) if max_months else None
month_name = chosen.strftime('%B') if chosen is not None else None
print('__RESULT__:')
print(json.dumps(month_name))"""

env_args = {'var_call_89iRFkJK8YrGjCfiIMvHoSUl': [], 'var_call_o2d6Rsqdvj3RLxgiIWFmNt5m': [], 'var_call_T36rWG4HuuRJMUSSdzxz0lxu': [{'n': '153'}], 'var_call_5Y3NFWaKJ3lsqypj8BieN8TG': [{'orderitemid__c': '802Wt00000797r4IAA', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'orderitemid__c': '802Wt00000792tiIAA', 'createddate': '2023-09-30T11:30:00.000+0000'}, {'orderitemid__c': '802Wt00000797r3IAA', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}], 'var_call_nY5lyQPUuR06AaWB2vKPeCAO': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}], 'var_call_BV1Dq1oxfTkk6ocMgzVAK4hu': [{'orderitem_id_clean': '802Wt0000078yuGIAQ'}, {'orderitem_id_clean': '802Wt00000790mOIAQ'}, {'orderitem_id_clean': '802Wt00000790zGIAQ'}, {'orderitem_id_clean': '802Wt00000794F2IAI'}, {'orderitem_id_clean': '802Wt000007968eIAA'}, {'orderitem_id_clean': '802Wt00000796bfIAA'}, {'orderitem_id_clean': '802Wt00000796qFIAQ'}, {'orderitem_id_clean': '802Wt0000079734IAA'}, {'orderitem_id_clean': '802Wt00000797W5IAI'}, {'orderitem_id_clean': '802Wt00000797awIAA'}, {'orderitem_id_clean': '802Wt00000797z7IAA'}, {'orderitem_id_clean': '802Wt00000798VPIAY'}, {'orderitem_id_clean': '802Wt00000798YdIAI'}, {'orderitem_id_clean': '802Wt00000798okIAA'}, {'orderitem_id_clean': '802Wt00000799o1IAA'}, {'orderitem_id_clean': '802Wt0000079A2bIAE'}, {'orderitem_id_clean': '802Wt0000079ACGIA2'}, {'orderitem_id_clean': '802Wt0000079B0EIAU'}, {'orderitem_id_clean': '802Wt0000079B6gIAE'}], 'var_call_8lgrP7uu3QA5aipumuwM5cK1': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
