code = """import json
import pandas as pd
from datetime import datetime, timedelta

# Load OrderItem IDs
order_items = locals()['var_function-call-3420856295872642531']
# Normalize OrderItem Ids
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

# Filter and Count
case_counts = {}
start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10)

filtered_cases = []

for case in cases:
    # Clean OrderItemId
    oid_c = case.get('orderitemid__c')
    if not oid_c:
        continue
    if oid_c.startswith('#'):
        oid_c = oid_c[1:]
    
    # Check if related to target product
    if oid_c in target_order_item_ids:
        # Check date
        cdate_str = case['createddate']
        # format 2023-07-02T11:00:00.000+0000
        # parse
        try:
            # We only need date part
            cdate_dt = datetime.strptime(cdate_str[:10], "%Y-%m-%d")
            if start_date <= cdate_dt <= end_date:
                month_name = cdate_dt.strftime("%B")
                case_counts[month_name] = case_counts.get(month_name, 0) + 1
                filtered_cases.append(case)
        except ValueError:
            continue

print("__RESULT__:")
print(json.dumps(case_counts))"""

env_args = {'var_function-call-530338849428747900': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-530338849428749193': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-3420856295872642531': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-3420856295872639120': 'file_storage/function-call-3420856295872639120.json'}

exec(code, env_args)
