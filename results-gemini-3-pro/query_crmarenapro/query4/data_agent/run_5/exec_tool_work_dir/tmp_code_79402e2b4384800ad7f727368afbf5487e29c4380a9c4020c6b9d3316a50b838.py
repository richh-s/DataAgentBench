code = """import json
import pandas as pd
from datetime import datetime

# Load Order Item IDs
order_items_raw = locals()['var_function-call-3903120554950776209']
# Normalize IDs: remove leading '#'
order_item_ids = set()
for item in order_items_raw:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    order_item_ids.add(oid)

# Load Cases
cases_file = locals()['var_function-call-3593888098400294967']
with open(cases_file, 'r') as f:
    cases_data = json.load(f)

# Process Cases
filtered_cases = []
current_date = pd.to_datetime('2021-04-10').tz_localize('UTC') # Ensure UTC timezone for comparison if createddate is TZ-aware
start_date = current_date - pd.DateOffset(months=10)

print(f"Filtering cases from {start_date} to {current_date}")

for case in cases_data:
    # Clean orderitemid__c
    oid_c = case.get('orderitemid__c')
    if not oid_c:
        continue
    if oid_c.startswith('#'):
        oid_c = oid_c[1:]
    
    # Check match
    if oid_c in order_item_ids:
        # Check date
        cdate_str = case.get('createddate')
        if not cdate_str:
            continue
        try:
            # createddate format: "2023-07-02T11:00:00.000+0000"
            c_date = pd.to_datetime(cdate_str)
            if c_date.tzinfo is None:
                 c_date = c_date.tz_localize('UTC')
            
            # Check range
            if c_date >= start_date and c_date <= current_date:
                filtered_cases.append({
                    'id': case['id'],
                    'month': c_date.strftime('%Y-%m'),
                    'month_name': c_date.strftime('%B')
                })
        except Exception as e:
            continue

df = pd.DataFrame(filtered_cases)
if not df.empty:
    counts = df['month_name'].value_counts()
    print("__RESULT__:")
    print(counts.to_json())
else:
    print("__RESULT__:")
    print(json.dumps({}))"""

env_args = {'var_function-call-3903120554950776209': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-8688839653892335344': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-3593888098400294967': 'file_storage/function-call-3593888098400294967.json'}

exec(code, env_args)
