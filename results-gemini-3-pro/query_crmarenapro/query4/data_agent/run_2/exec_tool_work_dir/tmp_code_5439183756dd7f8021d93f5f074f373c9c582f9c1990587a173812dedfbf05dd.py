code = """import pandas as pd
import json

path_orders = locals()['var_function-call-17653216939775560679']
with open(path_orders, 'r') as f:
    order_items = json.load(f)

path_cases = locals()['var_function-call-8848634664430094508']
with open(path_cases, 'r') as f:
    cases = json.load(f)

target_product_id = '01tWt000006hVJdIAM'
valid_order_ids = set()
debug_pids = []

for item in order_items:
    pid = item.get('Product2Id')
    oid = item.get('Id')
    if pid:
        pid_clean = pid.strip().lstrip('#')
        if pid_clean == target_product_id:
            if oid:
                oid_clean = oid.strip().lstrip('#')
                valid_order_ids.add(oid_clean)
        # Collect some PIDs for debug
        if len(debug_pids) < 5:
            debug_pids.append(pid)

print(f"DEBUG: Found {len(valid_order_ids)} OrderItems for product {target_product_id}")
print(f"DEBUG: Sample PIDs in DB: {debug_pids}")

case_count_total = 0
case_match_count = 0
case_date_match_count = 0

end_date = pd.Timestamp('2021-04-10').replace(tzinfo=None)
start_date = end_date - pd.DateOffset(months=10)

debug_case_dates = []

for case in cases:
    case_count_total += 1
    cdate_str = case.get('createddate')
    oid = case.get('orderitemid__c')
    
    if oid:
        oid_clean = oid.strip().lstrip('#')
        if oid_clean in valid_order_ids:
            case_match_count += 1
            if cdate_str:
                try:
                    cdate = pd.to_datetime(cdate_str).tz_localize(None)
                    if start_date <= cdate <= end_date:
                        case_date_match_count += 1
                    # Debug date distribution for matches
                    if len(debug_case_dates) < 20:
                        debug_case_dates.append(cdate_str)
                except:
                    pass

print(f"DEBUG: Total cases: {case_count_total}")
print(f"DEBUG: Cases matching product: {case_match_count}")
print(f"DEBUG: Cases matching product and date: {case_date_match_count}")
print(f"DEBUG: Sample match dates: {debug_case_dates}")

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-17653216939775560679': 'file_storage/function-call-17653216939775560679.json', 'var_function-call-8848634664430094508': 'file_storage/function-call-8848634664430094508.json', 'var_function-call-14765431148327615615': {'2021-January': 1, '2020-November': 2, '2020-September': 1, '2021-March': 1}}

exec(code, env_args)
