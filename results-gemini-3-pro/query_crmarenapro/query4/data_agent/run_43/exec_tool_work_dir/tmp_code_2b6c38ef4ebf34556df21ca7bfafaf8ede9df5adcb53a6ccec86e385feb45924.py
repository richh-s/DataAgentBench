code = """import json
import pandas as pd
from datetime import datetime, timedelta

# Load data
with open(locals()['var_function-call-9021888379879792617'], 'r') as f:
    order_items = json.load(f)

with open(locals()['var_function-call-2036162275247155383'], 'r') as f:
    cases = json.load(f)

# Helper to clean IDs
def clean_id(i):
    if i:
        return i.strip().lstrip('#')
    return ''

target_product_id = '01tWt000006hVJdIAM'
clean_target = clean_id(target_product_id)

# Find matching OrderItem IDs
matching_order_item_ids = set()
for item in order_items:
    pid = clean_id(item.get('Product2Id'))
    if pid == clean_target:
        matching_order_item_ids.add(clean_id(item.get('Id')))

print(f"DEBUG: Found {len(matching_order_item_ids)} matching OrderItems.")

# Process Cases
case_dates = []
ref_date = datetime(2021, 4, 10)
start_date = ref_date - timedelta(days=30*10) # Approx 10 months

debug_matches = []

for c in cases:
    oid = clean_id(c.get('orderitemid__c'))
    cdate_str = c.get('createddate')
    if oid in matching_order_item_ids and cdate_str:
        try:
            # Parse date. Format: "2021-01-25T09:30:00.000+0000"
            # Python 3.12 handles isoformat better, but let's be safe
            # removing +0000 might be easiest if we assume UTC
            dt = datetime.strptime(cdate_str[:19], "%Y-%m-%dT%H:%M:%S")
            
            if start_date <= dt <= ref_date:
                month_key = dt.strftime("%Y-%B") # e.g. 2020-November
                case_dates.append(month_key)
                debug_matches.append(cdate_str)
        except ValueError as e:
            pass

# Count by month
from collections import Counter
counts = Counter(case_dates)

print("__RESULT__:")
print(json.dumps(counts))"""

env_args = {'var_function-call-8128570514379634743': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-11721698262061313310': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-4512183450764435327': ['802Wt00000797awIAA', '802Wt00000794F2IAI', '802Wt00000798YdIAI', '802Wt000007968eIAA', '802Wt0000079B6gIAE', '802Wt0000079A2bIAE', '802Wt00000790zGIAQ', '802Wt00000796qFIAQ', '802Wt00000797z7IAA', '802Wt0000079ACGIA2', '802Wt0000079B0EIAU', '802Wt00000798okIAA', '802Wt00000798VPIAY', '802Wt00000799o1IAA', '802Wt00000796bfIAA', '802Wt0000079734IAA', '802Wt00000790mOIAQ', '802Wt00000797W5IAI', '802Wt0000078yuGIAQ'], 'var_function-call-592931264969697146': "SELECT createddate FROM Case WHERE REPLACE(orderitemid__c, '#', '') IN ('802Wt00000797awIAA', '802Wt00000794F2IAI', '802Wt00000798YdIAI', '802Wt000007968eIAA', '802Wt0000079B6gIAE', '802Wt0000079A2bIAE', '802Wt00000790zGIAQ', '802Wt00000796qFIAQ', '802Wt00000797z7IAA', '802Wt0000079ACGIA2', '802Wt0000079B0EIAU', '802Wt00000798okIAA', '802Wt00000798VPIAY', '802Wt00000799o1IAA', '802Wt00000796bfIAA', '802Wt0000079734IAA', '802Wt00000790mOIAQ', '802Wt00000797W5IAI', '802Wt0000078yuGIAQ')", 'var_function-call-15789657828664171327': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9052905423854056100': [{'createddate': '2021-01-25T09:30:00.000+0000'}, {'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2023-06-30T13:03:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_function-call-16424016131220522002': [{'orderitemid__c': '802Wt00000797r4IAA'}, {'orderitemid__c': '802Wt00000798aDIAQ'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt00000797r3IAA'}, {'orderitemid__c': '802Wt00000797r5IAA'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt0000078xAFIAY'}, {'orderitemid__c': '802Wt0000079ATyIAM'}, {'orderitemid__c': '802Wt00000794bXIAQ'}, {'orderitemid__c': '802Wt00000796yFIAQ'}, {'orderitemid__c': '802Wt000007988nIAA'}, {'orderitemid__c': '802Wt00000797axIAA'}, {'orderitemid__c': '802Wt00000797r5IAA'}, {'orderitemid__c': '802Wt0000079As9IAE'}, {'orderitemid__c': '802Wt000007983xIAA'}, {'orderitemid__c': '802Wt0000079ADpIAM'}, {'orderitemid__c': '802Wt000007928FIAQ'}, {'orderitemid__c': '802Wt0000079ATxIAM'}, {'orderitemid__c': '802Wt00000799EZIAY'}, {'orderitemid__c': '802Wt0000079ATxIAM'}], 'var_function-call-2356987768373831129': [{'Count(*)': '689'}], 'var_function-call-16150683284823236420': [{'count': '153'}], 'var_function-call-9021888379879792617': 'file_storage/function-call-9021888379879792617.json', 'var_function-call-2036162275247155383': 'file_storage/function-call-2036162275247155383.json'}

exec(code, env_args)
