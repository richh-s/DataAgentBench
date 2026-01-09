code = """import json, pandas as pd
orderitems = pd.DataFrame(var_call_UvpkqTVQ95Gu162jl3qE1X1G)
ids = orderitems['Id'].astype(str).str.replace('#','', regex=False).unique().tolist()
chunks = [ids[i:i+500] for i in range(0, len(ids), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'" + x + "'" for x in ch])
    q = "SELECT date_trunc('month', createddate::timestamp)::date AS month_start, COUNT(*)::int AS case_count FROM \"Case\" WHERE replace(orderitemid__c,'#','') IN (" + in_list + ") AND createddate::date >= (DATE '2021-04-10' - INTERVAL '10 months') AND createddate::date < DATE '2021-04-10' GROUP BY 1"
    queries.append(q)
print('__RESULT__:')
print(json.dumps({'queries': queries}))"""

env_args = {'var_call_M3zG3I8pLBeBPWtSbRmfeh1S': [], 'var_call_T91IpmjrA2YouM2RgSPF0hES': [], 'var_call_fquvyvw3IGf57p6izizRIhnn': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}], 'var_call_Cy1F8UCr0R7NMEPbh7kVNPAv': [{'month_start': '2020-12-01', 'case_count': '1'}, {'month_start': '2021-02-01', 'case_count': '1'}, {'month_start': '2021-03-01', 'case_count': '1'}], 'var_call_UvpkqTVQ95Gu162jl3qE1X1G': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PGdVHIA1'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PHQuGIAX'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGc9QIAT'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PHLzOIAX'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PH4FLIA1'}]}

exec(code, env_args)
