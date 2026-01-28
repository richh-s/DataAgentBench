code = """import json, pandas as pd
rows = var_call_y0AER2oCfIbzjomYuOyavgKz
df = pd.DataFrame(rows)
df['case_count'] = df['case_count'].astype(int)
df['month_start'] = pd.to_datetime(df['month_start'])
max_count = df['case_count'].max()
# significance: max > mean + 1*std (simple heuristic); else pick max month anyway
mean = df['case_count'].mean()
std = df['case_count'].std(ddof=0)
max_rows = df[df['case_count']==max_count].sort_values('month_start')
month = max_rows.iloc[-1]['month_start'].strftime('%B')
print('__RESULT__:')
print(json.dumps({'month': month, 'max_count': int(max_count), 'mean': float(mean), 'std': float(std)}))"""

env_args = {'var_call_xcshrAkDU6ULEDnEWsk9PKw4': [], 'var_call_kSevAx2NvbBZaGCQddWWlqxT': [], 'var_call_6ZebMNvJXA0FQRDXRvcgUUHz': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_kpWEi6PayVHUBwhx93zyv1zr': [{'createddate': '2023-07-02T11:00:00.000+0000', 'orderitemid__c': '802Wt00000797r4IAA', 'subject': 'Feature Update Notifications Lack'}, {'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ', 'subject': 'Missing Feature Update Alerts'}, {'createddate': '2023-09-30T11:30:00.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'subject': 'Delayed Support Response '}, {'createddate': '2022-08-05T14:30:00.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'subject': 'AI Feature Malfunction'}, {'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'subject': 'Access Issues with Training Module'}], 'var_call_dhosv2e9ZYl5QSCnU2aprLPY': [{'Id': '#01tWt000006hVJdIAM'}], 'var_call_y4OEMVQOxQaZi2AkJYihBoi5': [{'orderitem_id': '802Wt0000078yuGIAQ'}, {'orderitem_id': '802Wt00000790mOIAQ'}, {'orderitem_id': '802Wt00000790zGIAQ'}, {'orderitem_id': '802Wt00000794F2IAI'}, {'orderitem_id': '802Wt000007968eIAA'}, {'orderitem_id': '802Wt00000796bfIAA'}, {'orderitem_id': '802Wt00000796qFIAQ'}, {'orderitem_id': '802Wt0000079734IAA'}, {'orderitem_id': '802Wt00000797W5IAI'}, {'orderitem_id': '802Wt00000797awIAA'}, {'orderitem_id': '802Wt00000797z7IAA'}, {'orderitem_id': '802Wt00000798VPIAY'}, {'orderitem_id': '802Wt00000798YdIAI'}, {'orderitem_id': '802Wt00000798okIAA'}, {'orderitem_id': '802Wt00000799o1IAA'}, {'orderitem_id': '802Wt0000079A2bIAE'}, {'orderitem_id': '802Wt0000079ACGIA2'}, {'orderitem_id': '802Wt0000079B0EIAU'}, {'orderitem_id': '802Wt0000079B6gIAE'}], 'var_call_y0AER2oCfIbzjomYuOyavgKz': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
