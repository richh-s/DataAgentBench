code = """import json
import pandas as pd

# Load full order items
order_items_path = locals()['var_function-call-9437586672348318743']
with open(order_items_path, 'r') as f:
    order_items = json.load(f)

# Load cases
cases_path = locals()['var_function-call-8293248890011068619']
with open(cases_path, 'r') as f:
    cases = json.load(f)

target_product_id = "01tWt000006hVJdIAM"

# Find valid OrderItem IDs
valid_ids = set()
for item in order_items:
    pid = item.get('Product2Id')
    oid = item.get('Id')
    
    if pid and oid:
        clean_pid = pid.strip()
        if clean_pid.startswith('#'):
            clean_pid = clean_pid[1:]
            
        if clean_pid == target_product_id:
            clean_oid = oid.strip()
            if clean_oid.startswith('#'):
                clean_oid = clean_oid[1:]
            valid_ids.add(clean_oid)

# Process cases
case_data = []
dropped_date_count = 0
for c in cases:
    oid = c.get('orderitemid__c')
    cdate = c.get('createddate')
    if oid:
        # Clean oid
        if oid.startswith('#'):
            oid = oid[1:]
        oid = oid.strip()
        
        if oid in valid_ids:
            case_data.append({'createddate': cdate})

df = pd.DataFrame(case_data)
if not df.empty:
    print(f"Total matching cases: {len(df)}")
    df['createddate_dt'] = pd.to_datetime(df['createddate'], errors='coerce')
    print(f"Valid dates: {df['createddate_dt'].notna().sum()}")
    
    # Show distribution of all dates
    df['createddate_dt'] = df['createddate_dt'].dt.tz_convert(None)
    df['year_month'] = df['createddate_dt'].dt.to_period('M')
    counts = df.groupby('year_month').size().sort_index()
    
    print("__RESULT__:")
    print(json.dumps({
        "all_counts": {str(k): v for k, v in counts.items()}
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"message": "No matching cases found"}))"""

env_args = {'var_function-call-10158223557989843011': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-8293248890011068619': 'file_storage/function-call-8293248890011068619.json', 'var_function-call-14906054330457365788': {'counts_by_period': {'2020-09': 1, '2020-11': 2, '2021-03': 1}, 'counts_by_name': {'March': 1, 'November': 2, 'September': 1}}, 'var_function-call-9437586672348318743': 'file_storage/function-call-9437586672348318743.json', 'var_function-call-4375419799180957679': {'counts_by_period': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'counts_by_name': {'January': 1, 'March': 1, 'November': 2, 'September': 1}}, 'var_function-call-14975631221601847366': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
