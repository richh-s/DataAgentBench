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
        # Clean Product2Id
        clean_pid = pid.strip()
        if clean_pid.startswith('#'):
            clean_pid = clean_pid[1:]
            
        if clean_pid == target_product_id:
            # Clean OrderItem Id
            clean_oid = oid.strip()
            if clean_oid.startswith('#'):
                clean_oid = clean_oid[1:]
            valid_ids.add(clean_oid)

# Process cases
case_data = []
for c in cases:
    oid = c.get('orderitemid__c')
    cdate = c.get('createddate')
    if oid and cdate:
        # Clean oid
        if oid.startswith('#'):
            oid = oid[1:]
        oid = oid.strip()
        
        if oid in valid_ids:
            case_data.append({'createddate': cdate})

df = pd.DataFrame(case_data)
if not df.empty:
    df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce')
    df['createddate'] = df['createddate'].dt.tz_convert(None) # Convert to naive

    # Filter for past 10 months from 2021-04-10
    end_date = pd.Timestamp('2021-04-10')
    start_date = end_date - pd.DateOffset(months=10)
    
    df = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]
    
    # Extract month name
    df['month_name'] = df['createddate'].dt.month_name()
    df['year_month'] = df['createddate'].dt.to_period('M')
    
    counts = df.groupby('year_month').size()
    counts_named = df.groupby('month_name').size()
    
    print("__RESULT__:")
    print(json.dumps({
        "counts_by_period": {str(k): v for k, v in counts.items()},
        "counts_by_name": counts_named.to_dict()
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"message": "No matching cases found"}))"""

env_args = {'var_function-call-10158223557989843011': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-8293248890011068619': 'file_storage/function-call-8293248890011068619.json', 'var_function-call-14906054330457365788': {'counts_by_period': {'2020-09': 1, '2020-11': 2, '2021-03': 1}, 'counts_by_name': {'March': 1, 'November': 2, 'September': 1}}, 'var_function-call-9437586672348318743': 'file_storage/function-call-9437586672348318743.json'}

exec(code, env_args)
