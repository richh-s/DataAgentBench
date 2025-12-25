code = """import pandas as pd
import json

# Load OrderItems
path_orders = locals()['var_function-call-17653216939775560679']
with open(path_orders, 'r') as f:
    order_items = json.load(f)

# Load Cases
path_cases = locals()['var_function-call-8848634664430094508']
with open(path_cases, 'r') as f:
    cases = json.load(f)

# Process OrderItems
target_product_id = '01tWt000006hVJdIAM'
valid_order_ids = set()

for item in order_items:
    pid = item.get('Product2Id')
    oid = item.get('Id')
    if pid and oid:
        # Clean PID
        pid_clean = pid.strip().lstrip('#')
        if pid_clean == target_product_id:
            # Clean OID
            oid_clean = oid.strip().lstrip('#')
            valid_order_ids.add(oid_clean)

# Process Cases
case_counts = {}
# Time range: Past 10 months from 2021-04-10
# So roughly 2020-06-10 to 2021-04-10
end_date = pd.Timestamp('2021-04-10').replace(tzinfo=None)
start_date = end_date - pd.DateOffset(months=10)

for case in cases:
    cdate_str = case.get('createddate')
    oid = case.get('orderitemid__c')
    
    if cdate_str and oid:
        # Clean OID
        oid_clean = oid.strip().lstrip('#')
        
        if oid_clean in valid_order_ids:
            try:
                # Parse Date, handle timezone by converting to utc then removing tz or just naive
                cdate = pd.to_datetime(cdate_str).tz_localize(None)
            except:
                continue
            
            if start_date <= cdate <= end_date:
                month_key = cdate.strftime('%Y-%B')
                case_counts[month_key] = case_counts.get(month_key, 0) + 1

print("__RESULT__:")
print(json.dumps(case_counts))"""

env_args = {'var_function-call-17653216939775560679': 'file_storage/function-call-17653216939775560679.json', 'var_function-call-8848634664430094508': 'file_storage/function-call-8848634664430094508.json'}

exec(code, env_args)
