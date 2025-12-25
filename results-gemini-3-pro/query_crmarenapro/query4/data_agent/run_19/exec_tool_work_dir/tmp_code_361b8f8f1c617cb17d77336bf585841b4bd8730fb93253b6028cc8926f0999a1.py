code = """import json
import pandas as pd
from collections import Counter
from datetime import datetime

# Load OrderItems
order_items_data = locals()['var_function-call-6182685443246565004']
# Extract Ids and clean them (remove leading #)
target_order_item_ids = set()
for item in order_items_data:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_order_item_ids.add(oid)

# Load Cases
with open(locals()['var_function-call-6182685443246566889'], 'r') as f:
    cases_data = json.load(f)

# Process Cases
relevant_cases = []
current_date = datetime(2021, 4, 10)
cutoff_date = datetime(2020, 6, 1) # broad range, will refine
months_count = Counter()

for case in cases_data:
    # Clean orderitemid__c
    oid = case.get('orderitemid__c')
    if not oid:
        continue
    if oid.startswith('#'):
        oid = oid[1:]
    
    if oid in target_order_item_ids:
        # Check date
        cdate_str = case['createddate']
        # Format usually: "2023-07-02T11:00:00.000+0000"
        # We only need Year-Month
        try:
            # Simple parse since format is consistent ISO-like
            dt = datetime.strptime(cdate_str[:10], "%Y-%m-%d")
            
            # Filter past 10 months: June 2020 to April 2021 (inclusive)
            # 10 months back from April 2021 is June 2020.
            if datetime(2020, 6, 1) <= dt <= datetime(2021, 4, 10):
                month_key = dt.strftime("%B") # Month name
                months_count[month_key] += 1
                relevant_cases.append(case)
        except Exception as e:
            continue

print("__RESULT__:")
print(json.dumps(months_count))"""

env_args = {'var_function-call-5668392397130027000': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-5668392397130026911': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6182685443246565004': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-6182685443246566889': 'file_storage/function-call-6182685443246566889.json'}

exec(code, env_args)
