code = """import json
import pandas as pd
from datetime import datetime

# Load OrderItem IDs
order_items = locals()['var_function-call-11019259640815089045']
# Clean OrderItem IDs
valid_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    valid_order_item_ids.add(oid)

# Load Case data
with open(locals()['var_function-call-4384810770770684280'], 'r') as f:
    cases = json.load(f)

# Filter and count
case_counts = {}
relevant_cases = []

start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10)

for case in cases:
    # Check date first
    cdate_str = case['createddate']
    # Format: "2023-07-02T11:00:00.000+0000"
    # We only care about YYYY-MM-DD
    try:
        cdate = datetime.strptime(cdate_str[:10], "%Y-%m-%d")
    except:
        continue

    if start_date <= cdate <= end_date:
        # Check product
        oid = case.get('orderitemid__c')
        if oid:
            if oid.startswith('#'):
                oid = oid[1:]
            
            if oid in valid_order_item_ids:
                month_key = cdate.strftime("%B %Y")
                case_counts[month_key] = case_counts.get(month_key, 0) + 1
                relevant_cases.append(case)

print("__RESULT__:")
print(json.dumps(case_counts))"""

env_args = {'var_function-call-11019259640815089045': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-4384810770770684280': 'file_storage/function-call-4384810770770684280.json'}

exec(code, env_args)
