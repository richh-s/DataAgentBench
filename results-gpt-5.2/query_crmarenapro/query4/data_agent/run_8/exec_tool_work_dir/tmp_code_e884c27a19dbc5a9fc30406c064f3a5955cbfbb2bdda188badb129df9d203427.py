code = """import json, pandas as pd

df = pd.DataFrame(var_call_X5A8MIN9qAzwFKYTOLMAXpo3)
if df.empty:
    out = None
else:
    df['case_count'] = df['case_count'].astype(int)
    df['month_start'] = pd.to_datetime(df['month_start'])
    top = df.sort_values(['case_count','month_start'], ascending=[False, True]).iloc[0]
    out = top['month_start'].strftime('%B')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QjYh3ueXNCARch38JQtJprEm': [], 'var_call_xWFW3cx5hzz3TbZCKWJpx6Z9': [], 'var_call_oPJ3PkB7qg9dkkqE6vyrqrZv': [{'orderitemid__c': '802Wt00000796qFIAQ', 'c': '3'}, {'orderitemid__c': '802Wt00000798aDIAQ', 'c': '3'}, {'orderitemid__c': '802Wt00000797r5IAA', 'c': '3'}, {'orderitemid__c': '802Wt0000079A2ZIAU', 'c': '2'}, {'orderitemid__c': '802Wt00000797foIAA', 'c': '2'}, {'orderitemid__c': '802Wt00000796bfIAA', 'c': '1'}, {'orderitemid__c': '802Wt00000797axIAA', 'c': '1'}, {'orderitemid__c': '802Wt00000794bTIAQ', 'c': '1'}, {'orderitemid__c': '802Wt00000796JtIAI', 'c': '1'}, {'orderitemid__c': '802Wt00000798OvIAI', 'c': '1'}, {'orderitemid__c': '802Wt00000795XwIAI', 'c': '1'}, {'orderitemid__c': '802Wt00000799b7IAA', 'c': '1'}, {'orderitemid__c': '802Wt00000799o1IAA', 'c': '1'}, {'orderitemid__c': '802Wt00000799uTIAQ', 'c': '1'}, {'orderitemid__c': '802Wt00000796dGIAQ', 'c': '1'}], 'var_call_dYQmCEH8mDNC3OIZlKnz8Caj': [{'month_start': '2020-11-01', 'case_count': '2'}, {'month_start': '2021-03-01', 'case_count': '1'}], 'var_call_ae2y7UNFOPOOiHU5QRFxYqAb': [{'n': '19'}], 'var_call_NxedSuiFzX5ngJS1YBTsOm8J': [{'orderitem_id': '#802Wt0000078yuGIAQ'}, {'orderitem_id': '802Wt00000790mOIAQ'}, {'orderitem_id': '802Wt00000790zGIAQ'}, {'orderitem_id': '802Wt00000794F2IAI'}, {'orderitem_id': '802Wt000007968eIAA'}, {'orderitem_id': '802Wt00000796bfIAA'}, {'orderitem_id': '802Wt00000796qFIAQ'}, {'orderitem_id': '802Wt0000079734IAA'}, {'orderitem_id': '802Wt00000797W5IAI'}, {'orderitem_id': '802Wt00000797awIAA'}, {'orderitem_id': '802Wt00000797z7IAA'}, {'orderitem_id': '#802Wt00000798VPIAY'}, {'orderitem_id': '802Wt00000798YdIAI'}, {'orderitem_id': '802Wt00000798okIAA'}, {'orderitem_id': '#802Wt00000799o1IAA'}, {'orderitem_id': '802Wt0000079A2bIAE'}, {'orderitem_id': '802Wt0000079ACGIA2'}, {'orderitem_id': '802Wt0000079B0EIAU'}, {'orderitem_id': '802Wt0000079B6gIAE'}], 'var_call_X5A8MIN9qAzwFKYTOLMAXpo3': [{'month_start': '2020-09-01', 'case_count': '1'}, {'month_start': '2020-11-01', 'case_count': '2'}, {'month_start': '2021-01-01', 'case_count': '1'}, {'month_start': '2021-03-01', 'case_count': '1'}]}

exec(code, env_args)
