code = """import json
import pandas as pd
from datetime import datetime, timedelta

order_items = locals()['var_function-call-10888803579691069025']
cases_file = locals()['var_function-call-2174225455058142858']

with open(cases_file, 'r') as f:
    cases = json.load(f)

# Helper to clean IDs
def clean_id(val):
    if not val:
        return ""
    s = str(val).strip()
    if s.startswith("#"):
        s = s[1:]
    return s

target_product_id = "01tWt000006hVJdIAM"
target_order_item_ids = set()

# Filter Order Items
for oi in order_items:
    pid = clean_id(oi.get("Product2Id"))
    oid = clean_id(oi.get("Id"))
    if pid == target_product_id:
        target_order_item_ids.add(oid)

print(f"Found {len(target_order_item_ids)} target OrderItem IDs.")

# Filter Cases
# Date range: 2020-06-10 to 2021-04-10
start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10, 23, 59, 59)

monthly_counts = {}

for c in cases:
    # Check Order Item
    c_oid = clean_id(c.get("orderitemid__c"))
    if c_oid not in target_order_item_ids:
        continue
    
    # Check Date
    c_date_str = c.get("createddate")
    if not c_date_str:
        continue
    
    try:
        # Format: 2023-07-02T11:00:00.000+0000
        # Parsing with simple approach or strptime
        # 2023-07-02T11:00:00.000+0000
        # We can take first 10 chars for YYYY-MM-DD if we ignore time/timezone slightly or parse properly
        # Ideally use datetime.fromisoformat if python version allows, but the +0000 might need handling
        # Using pandas to_datetime is easier if we had a dataframe, but loop is fine
        dt = datetime.strptime(c_date_str[:19], "%Y-%m-%dT%H:%M:%S")
        # Assume UTC or close enough for day resolution
        
        if start_date <= dt <= end_date:
            month_key = dt.strftime("%B") # Full month name
            year_month = dt.strftime("%Y-%m")
            
            if year_month not in monthly_counts:
                monthly_counts[year_month] = 0
            monthly_counts[year_month] += 1
            
    except ValueError:
        pass

print("__RESULT__:")
print(json.dumps(monthly_counts))"""

env_args = {'var_function-call-10888803579691069025': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-10888803579691066634': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2174225455058142858': 'file_storage/function-call-2174225455058142858.json'}

exec(code, env_args)
