code = """import json
import pandas as pd
from datetime import datetime, timedelta

# Load OrderItem IDs
order_items = locals()['var_function-call-6910042798964273375']
# Clean IDs
target_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_order_item_ids.add(oid)

# Load Cases
case_file_path = locals()['var_function-call-2116088526863280977']
with open(case_file_path, 'r') as f:
    cases = json.load(f)

# Filter Cases
valid_cases = []
current_date = datetime(2021, 4, 10)
start_date = current_date - timedelta(days=30*10) # Approx 300 days

# Adjust start_date more precisely if needed, typically "past 10 months" implies from June 2020.
# Let's say June 1st 2020 to be safe, filtering strictly later.

month_counts = {}

for case in cases:
    # Clean OrderItemId
    cid = case.get('orderitemid__c')
    if not cid:
        continue
    if cid.startswith('#'):
        cid = cid[1:]
    
    if cid in target_order_item_ids:
        # Check date
        cdate_str = case['createddate']
        # Format: 2023-07-02T11:00:00.000+0000
        # We need to parse this. 
        # Using pandas to parse might be easier or strptime
        try:
            # Parse YYYY-MM-DD
            cdate = datetime.strptime(cdate_str[:10], "%Y-%m-%d")
            
            if start_date <= cdate <= current_date:
                month_name = cdate.strftime("%B")
                month_counts[month_name] = month_counts.get(month_name, 0) + 1
        except Exception as e:
            continue

print("__RESULT__:")
print(json.dumps(month_counts))"""

env_args = {'var_function-call-6910042798964273375': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-2116088526863280977': 'file_storage/function-call-2116088526863280977.json'}

exec(code, env_args)
