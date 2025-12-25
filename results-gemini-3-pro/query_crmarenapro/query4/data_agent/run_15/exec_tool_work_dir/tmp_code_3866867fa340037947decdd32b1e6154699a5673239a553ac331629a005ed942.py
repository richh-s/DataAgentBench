code = """import json
from collections import Counter

with open(locals()['var_function-call-8702892083309368303'], 'r') as f:
    cases = json.load(f)

total_cases = len(cases)
populated_oid = [c.get('orderitemid__c') for c in cases if c.get('orderitemid__c')]
num_populated = len(populated_oid)

sample_oids = populated_oid[:10]

# Check valid IDs again
order_items = locals()['var_function-call-16064184842318411823']
valid_ids = [str(item['Id']).strip().lstrip('#') for item in order_items]

# Check for partial matches or overlap
matches = []
for oid in populated_oid:
    clean = str(oid).strip().lstrip('#')
    if clean in valid_ids:
        matches.append(clean)

print("__RESULT__:")
print(json.dumps({
    "total_cases": total_cases,
    "num_populated_oid": num_populated,
    "sample_oids": sample_oids,
    "num_matches": len(matches),
    "unique_matches": list(set(matches)),
    "valid_ids_sample": valid_ids[:5]
}))"""

env_args = {'var_function-call-16064184842318411823': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-8702892083309368303': 'file_storage/function-call-8702892083309368303.json', 'var_function-call-7519533941935195638': {'January 2021': 1, 'November 2020': 2, 'September 2020': 1, 'March 2021': 1}, 'var_function-call-2303119916940098335': {'num_order_items': 19, 'total_matches': 6, 'all_month_counts': {'January 2021': 1, 'November 2020': 2, 'June 2023': 1, 'September 2020': 1, 'March 2021': 1}}, 'var_function-call-3892015857153050438': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-14753483501253137550': [], 'var_function-call-6369002579201554899': [{'id': '500Wt00000DE00gIAD', 'priority': 'High', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqscWIAR', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000796bfIAA', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'accountid': '#001Wt00000PFsjOIAT', 'ownerid': '005Wt000003NJWTIA4'}], 'var_function-call-4190302696212677617': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}]}

exec(code, env_args)
