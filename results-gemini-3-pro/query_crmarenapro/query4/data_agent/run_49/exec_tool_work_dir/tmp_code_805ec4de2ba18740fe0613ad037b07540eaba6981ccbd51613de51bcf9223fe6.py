code = """import json
import pandas as pd

# Load OrderItem IDs
order_items = locals()['var_function-call-10023800480704351753']
target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_ids.add(oid)

# Load Cases
with open(locals()['var_function-call-708752942025156642'], 'r') as f:
    cases = json.load(f)

# Count matches
match_count = 0
dates = []
for case in cases:
    oid = case.get('orderitemid__c')
    if not oid:
        continue
    if oid.startswith('#'):
        oid = oid[1:]
    
    if oid in target_ids:
        match_count += 1
        dates.append(case.get('createddate'))

print("__RESULT__:")
print(f"Total Matches: {match_count}")
print(f"Sample Dates: {dates[:10]}")"""

env_args = {'var_function-call-10023800480704351753': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-13331700831189368373': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-708752942025156642': 'file_storage/function-call-708752942025156642.json', 'var_function-call-9034528603292838690': {'2021-01': 1, '2020-11': 2, '2020-09': 1, '2021-03': 1}, 'var_function-call-6207247607094848795': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'Description': 'Data analytics platform with enhanced focus on security and compliance.', 'IsActive': '1', 'External_ID__c': 'Data Analytics Platforms,Security and Compliance Modules_13'}]}

exec(code, env_args)
