code = """import pandas as pd
import json

with open(locals()['var_function-call-16912545030574088445']) as f:
    order_items = json.load(f)

with open(locals()['var_function-call-5257925918374328330']) as f:
    cases = json.load(f)

target_product_id = '01tWt000006hVJdIAM'

# Get valid OIDs
valid_oids_clean = set()
for item in order_items:
    pid = item.get('Product2Id', '')
    oid = item.get('Id', '')
    if pid and oid:
        pid_clean = pid.strip().lstrip('#')
        oid_clean = oid.strip().lstrip('#')
        if pid_clean == target_product_id:
            valid_oids_clean.add(oid_clean)

# Check Cases
matched_count = 0
total_cases_in_range = 0
ref_date = pd.Timestamp('2021-04-10', tz='UTC')
start_date = ref_date - pd.DateOffset(months=10)

matched_dates = []

for c in cases:
    oid = c.get('orderitemid__c', '')
    cdate_str = c.get('createddate')
    if cdate_str:
        cdate = pd.to_datetime(cdate_str, utc=True)
        if start_date <= cdate <= ref_date:
            total_cases_in_range += 1
            if oid:
                oid_clean = oid.strip().lstrip('#')
                if oid_clean in valid_oids_clean:
                    matched_count += 1
                    matched_dates.append(cdate_str)

debug_info = {
    "valid_oids_count": len(valid_oids_clean),
    "total_cases_in_range": total_cases_in_range,
    "matched_count": matched_count,
    "matched_dates": matched_dates
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-16912545030574088445': 'file_storage/function-call-16912545030574088445.json', 'var_function-call-5257925918374328330': 'file_storage/function-call-5257925918374328330.json', 'var_function-call-9538537814195956863': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'var_function-call-10024308654147359115': 'Done debug'}

exec(code, env_args)
