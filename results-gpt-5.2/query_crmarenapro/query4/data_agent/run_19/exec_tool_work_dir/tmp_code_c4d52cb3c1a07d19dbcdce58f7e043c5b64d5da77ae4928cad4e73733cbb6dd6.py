code = """import json, pandas as pd
orderitems = var_call_y4OEMVQOxQaZi2AkJYihBoi5
ids = [r['orderitem_id'] for r in orderitems]
# chunk into groups of 500 for SQL IN
chunks = [ids[i:i+500] for i in range(0, len(ids), 500)]
queries=[]
for ch in chunks:
    in_list = ','.join(["'%s'"%x for x in ch])
    queries.append(f"SELECT date_trunc('month', createddate::timestamp) AS month_start, COUNT(*) AS case_count FROM \"Case\" WHERE createddate::date >= DATE '2020-06-10' AND createddate::date <= DATE '2021-04-10' AND replace(btrim(orderitemid__c),'#','') IN ({in_list}) GROUP BY 1 ORDER BY 1;")
print('__RESULT__:')
print(json.dumps({'queries':queries}))"""

env_args = {'var_call_xcshrAkDU6ULEDnEWsk9PKw4': [], 'var_call_kSevAx2NvbBZaGCQddWWlqxT': [], 'var_call_6ZebMNvJXA0FQRDXRvcgUUHz': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_kpWEi6PayVHUBwhx93zyv1zr': [{'createddate': '2023-07-02T11:00:00.000+0000', 'orderitemid__c': '802Wt00000797r4IAA', 'subject': 'Feature Update Notifications Lack'}, {'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ', 'subject': 'Missing Feature Update Alerts'}, {'createddate': '2023-09-30T11:30:00.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'subject': 'Delayed Support Response '}, {'createddate': '2022-08-05T14:30:00.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'subject': 'AI Feature Malfunction'}, {'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'subject': 'Access Issues with Training Module'}], 'var_call_dhosv2e9ZYl5QSCnU2aprLPY': [{'Id': '#01tWt000006hVJdIAM'}], 'var_call_y4OEMVQOxQaZi2AkJYihBoi5': [{'orderitem_id': '802Wt0000078yuGIAQ'}, {'orderitem_id': '802Wt00000790mOIAQ'}, {'orderitem_id': '802Wt00000790zGIAQ'}, {'orderitem_id': '802Wt00000794F2IAI'}, {'orderitem_id': '802Wt000007968eIAA'}, {'orderitem_id': '802Wt00000796bfIAA'}, {'orderitem_id': '802Wt00000796qFIAQ'}, {'orderitem_id': '802Wt0000079734IAA'}, {'orderitem_id': '802Wt00000797W5IAI'}, {'orderitem_id': '802Wt00000797awIAA'}, {'orderitem_id': '802Wt00000797z7IAA'}, {'orderitem_id': '802Wt00000798VPIAY'}, {'orderitem_id': '802Wt00000798YdIAI'}, {'orderitem_id': '802Wt00000798okIAA'}, {'orderitem_id': '802Wt00000799o1IAA'}, {'orderitem_id': '802Wt0000079A2bIAE'}, {'orderitem_id': '802Wt0000079ACGIA2'}, {'orderitem_id': '802Wt0000079B0EIAU'}, {'orderitem_id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
