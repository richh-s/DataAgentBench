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

case_match_count = 0
matched_dates = []

end_date = pd.Timestamp('2021-04-10').replace(tzinfo=None)
start_date = end_date - pd.DateOffset(months=10)

for case in cases:
    cdate_str = case.get('createddate')
    oid = case.get('orderitemid__c')
    
    if oid:
        oid_clean = oid.strip().lstrip('#')
        if oid_clean in valid_order_ids:
            case_match_count += 1
            if cdate_str:
                matched_dates.append(cdate_str)

result = {
    "valid_order_ids_count": len(valid_order_ids),
    "case_match_count": case_match_count,
    "matched_dates_sample": matched_dates[:20],
    "all_matched_dates": matched_dates
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17653216939775560679': 'file_storage/function-call-17653216939775560679.json', 'var_function-call-8848634664430094508': 'file_storage/function-call-8848634664430094508.json', 'var_function-call-14765431148327615615': {'2021-January': 1, '2020-November': 2, '2020-September': 1, '2021-March': 1}, 'var_function-call-17298362015042363489': 'Done'}

exec(code, env_args)
