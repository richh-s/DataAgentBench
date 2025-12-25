code = """import json
import pandas as pd
from datetime import datetime

# Load OrderItem IDs
order_items = locals()['var_function-call-11019259640815089045']
valid_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    # Clean: remove leading # and whitespace
    oid = oid.lstrip('#').strip()
    valid_order_item_ids.add(oid)

# Load Case data
with open(locals()['var_function-call-4384810770770684280'], 'r') as f:
    cases = json.load(f)

case_counts = {}

for case in cases:
    oid = case.get('orderitemid__c')
    if oid:
        # Clean: remove leading # and whitespace
        oid_clean = oid.lstrip('#').strip()
        
        if oid_clean in valid_order_item_ids:
            cdate_str = case['createddate']
            try:
                cdate = datetime.strptime(cdate_str[:10], "%Y-%m-%d")
                month_key = cdate.strftime("%Y-%m")
                case_counts[month_key] = case_counts.get(month_key, 0) + 1
            except:
                pass

print("__RESULT__:")
print(json.dumps(case_counts))"""

env_args = {'var_function-call-11019259640815089045': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-4384810770770684280': 'file_storage/function-call-4384810770770684280.json', 'var_function-call-11248319469521269189': {'January 2021': 1, 'November 2020': 2, 'September 2020': 1, 'March 2021': 1}, 'var_function-call-12550173827314784534': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
