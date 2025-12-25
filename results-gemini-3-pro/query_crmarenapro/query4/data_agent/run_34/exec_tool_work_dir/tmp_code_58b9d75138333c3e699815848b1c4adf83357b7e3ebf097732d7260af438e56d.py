code = """import json
from datetime import datetime

# Load Case data
with open(locals()['var_function-call-5866975110549239295'], 'r') as f:
    cases = json.load(f)

# Load OrderItem data
order_items = locals()['var_function-call-5866975110549240888']

target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        cleaned = oid.strip().lstrip('#')
        target_ids.add(cleaned)

print(f"Target IDs: {target_ids}")

matches = []
for case in cases:
    raw_oid = case.get('orderitemid__c')
    if not raw_oid:
        continue
    cleaned_oid = raw_oid.strip().lstrip('#')
    
    if cleaned_oid in target_ids:
        matches.append({
            'case_id': case['id'],
            'createddate': case['createddate'],
            'oid': cleaned_oid
        })

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-2761220900479506085': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2761220900479505406': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-5866975110549239295': 'file_storage/function-call-5866975110549239295.json', 'var_function-call-5866975110549240888': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-7575201057824002274': {'counts_by_ym': {'2020-09': 1, '2020-11': 2, '2021-03': 1}, 'counts_by_name': {'November': 2, 'September': 1, 'March': 1}}}

exec(code, env_args)
