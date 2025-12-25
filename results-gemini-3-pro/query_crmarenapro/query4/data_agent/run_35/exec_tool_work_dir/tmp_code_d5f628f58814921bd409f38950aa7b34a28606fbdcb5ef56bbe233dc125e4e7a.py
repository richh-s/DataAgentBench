code = """import pandas as pd
import json
from datetime import datetime, timedelta

# Load OrderItems
order_items_data = locals()['var_function-call-2626624589572009612']
# order_items_data is a list of dicts: [{'Id': '...'}, ...]

# Load Cases
# It is in a file
with open(locals()['var_function-call-2626624589572007461'], 'r') as f:
    cases_data = json.load(f)

# Normalize ID function
def normalize_id(oid):
    if not oid:
        return ""
    oid = str(oid).strip()
    if oid.startswith('#'):
        oid = oid[1:]
    return oid

# specific product OrderItem IDs
target_order_item_ids = set()
for item in order_items_data:
    target_order_item_ids.add(normalize_id(item['Id']))

# Filter cases
filtered_cases = []
current_date = datetime(2021, 4, 10)
start_date = current_date - timedelta(days=30*10) # Approx 10 months. Or use exact calculation. 
# "past 10 months" usually means the window [2020-06-10, 2021-04-10].

valid_cases = []
for case in cases_data:
    oid = normalize_id(case.get('orderitemid__c'))
    if oid in target_order_item_ids:
        cdate_str = case.get('createddate')
        if cdate_str:
            # Format: "2023-07-02T11:00:00.000+0000"
            # We can parse the first 10 chars "YYYY-MM-DD"
            try:
                cdate = datetime.strptime(cdate_str[:10], '%Y-%m-%d')
                if start_date <= cdate <= current_date:
                    valid_cases.append(cdate)
            except:
                pass

# Count by month
month_counts = {}
for d in valid_cases:
    month_name = d.strftime('%B') # Full month name
    # month_key = d.strftime('%Y-%m') # Year-Month to separate if needed, but 10 months implies unique months.
    # However, if range is e.g. June 2020 to April 2021, April 2021 is partial?
    # Actually, June 2020 to April 2021 is 10 months. June, July, Aug, Sep, Oct, Nov, Dec, Jan, Feb, Mar, Apr. That's 11 months span.
    # "past 10 months" creates a window.
    # Let's count by Year-Month first to be precise.
    ym = d.strftime('%Y-%m')
    month_counts[ym] = month_counts.get(ym, 0) + 1

print("__RESULT__:")
print(json.dumps(month_counts))"""

env_args = {'var_function-call-9876070469168569295': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9876070469168567712': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-2626624589572009612': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-2626624589572007461': 'file_storage/function-call-2626624589572007461.json'}

exec(code, env_args)
