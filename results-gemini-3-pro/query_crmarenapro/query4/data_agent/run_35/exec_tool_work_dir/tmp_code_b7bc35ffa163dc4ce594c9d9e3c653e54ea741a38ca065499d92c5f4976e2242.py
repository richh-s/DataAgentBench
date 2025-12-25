code = """import pandas as pd
import json
from datetime import datetime

# Load OrderItems (previous result)
order_items_data = locals()['var_function-call-2626624589572009612']
# Load Cases (previous result file)
with open(locals()['var_function-call-2626624589572007461'], 'r') as f:
    cases_data = json.load(f)

def normalize(s):
    if not s: return ""
    return str(s).strip().lstrip('#')

# Set of target OrderItem IDs
target_oids = set()
for item in order_items_data:
    target_oids.add(normalize(item['Id']))

print(f"DEBUG: Found {len(target_oids)} target OrderItem IDs.")
print(f"DEBUG: Sample target IDs: {list(target_oids)[:5]}")

# Check matches
matched_cases = []
for case in cases_data:
    case_oid = normalize(case.get('orderitemid__c'))
    if case_oid in target_oids:
        matched_cases.append(case)

print(f"DEBUG: Found {len(matched_cases)} matched cases.")

# Analyze dates of matched cases
date_counts = {}
for c in matched_cases:
    d_str = c.get('createddate')
    if d_str:
        ym = d_str[:7] # YYYY-MM
        date_counts[ym] = date_counts.get(ym, 0) + 1

print("__RESULT__:")
print(json.dumps(date_counts))"""

env_args = {'var_function-call-9876070469168569295': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9876070469168567712': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-2626624589572009612': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-2626624589572007461': 'file_storage/function-call-2626624589572007461.json', 'var_function-call-5659416735711038722': {'2021-01': 1, '2020-11': 2, '2020-09': 1, '2021-03': 1}}

exec(code, env_args)
