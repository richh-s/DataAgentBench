code = """import json
from datetime import datetime

# Load OrderItem IDs
order_items = locals()['var_function-call-3420856295872642531']
target_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_order_item_ids.add(oid)

# Load Cases
cases_file = locals()['var_function-call-3420856295872639120']
with open(cases_file, 'r') as f:
    cases = json.load(f)

# Count all matches
all_matches = []
for case in cases:
    oid_c = case.get('orderitemid__c')
    if not oid_c:
        continue
    if oid_c.startswith('#'):
        oid_c = oid_c[1:]
    
    if oid_c in target_order_item_ids:
        all_matches.append(case['createddate'])

print("__RESULT__:")
print(json.dumps(all_matches))"""

env_args = {'var_function-call-530338849428747900': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-530338849428749193': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-3420856295872642531': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-3420856295872639120': 'file_storage/function-call-3420856295872639120.json', 'var_function-call-14800394706308198195': {'January': 1, 'November': 2, 'September': 1, 'March': 1}, 'var_function-call-13992762942569951089': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'External_ID__c': 'Data Analytics Platforms,Security and Compliance Modules_13'}]}

exec(code, env_args)
