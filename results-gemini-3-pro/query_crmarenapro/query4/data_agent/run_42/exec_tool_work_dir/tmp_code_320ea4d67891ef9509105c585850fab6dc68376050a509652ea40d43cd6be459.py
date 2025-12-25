code = """import json
from datetime import datetime

order_items = locals()['var_function-call-6910042798964273375']
target_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_order_item_ids.add(oid)

case_file_path = locals()['var_function-call-2116088526863280977']
with open(case_file_path, 'r') as f:
    cases = json.load(f)

month_counts = {}

for case in cases:
    cid = case.get('orderitemid__c')
    if not cid:
        continue
    if cid.startswith('#'):
        cid = cid[1:]
    
    if cid in target_order_item_ids:
        cdate_str = case['createddate']
        try:
            cdate = datetime.strptime(cdate_str[:10], "%Y-%m-%d")
            # Key by YYYY-MM to see distribution
            month_key = cdate.strftime("%Y-%m")
            month_counts[month_key] = month_counts.get(month_key, 0) + 1
        except:
            continue

print("__RESULT__:")
print(json.dumps(month_counts))"""

env_args = {'var_function-call-6910042798964273375': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-2116088526863280977': 'file_storage/function-call-2116088526863280977.json', 'var_function-call-14017992284809479758': {'January': 1, 'November': 2, 'September': 1, 'March': 1}}

exec(code, env_args)
