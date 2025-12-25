code = """import pandas as pd
import json

with open(locals()['var_function-call-16912545030574088445']) as f:
    order_items = json.load(f)

with open(locals()['var_function-call-5257925918374328330']) as f:
    cases = json.load(f)

target_product_id = '01tWt000006hVJdIAM'

# Get valid OIDs
valid_oids_raw = []
valid_oids_clean = set()

for item in order_items:
    pid = item.get('Product2Id', '')
    oid = item.get('Id', '')
    if pid and oid:
        pid_clean = pid.strip().lstrip('#')
        oid_clean = oid.strip().lstrip('#')
        if pid_clean == target_product_id:
            valid_oids_raw.append(oid)
            valid_oids_clean.add(oid_clean)

print(f"DEBUG: Found {len(valid_oids_clean)} unique OrderItem Ids for target product.")
print(f"DEBUG: Sample valid OIDs: {list(valid_oids_clean)[:5]}")

# Check Cases
matched_count = 0
unmatched_sample = []
total_cases_in_range = 0
ref_date = pd.Timestamp('2021-04-10', tz='UTC')
start_date = ref_date - pd.DateOffset(months=10)

case_oid_sample = []

for c in cases:
    oid = c.get('orderitemid__c', '')
    cdate_str = c.get('createddate')
    if cdate_str:
        cdate = pd.to_datetime(cdate_str, utc=True)
        if start_date <= cdate <= ref_date:
            total_cases_in_range += 1
            if oid:
                oid_clean = oid.strip().lstrip('#')
                case_oid_sample.append(oid_clean)
                if oid_clean in valid_oids_clean:
                    matched_count += 1
                else:
                    if len(unmatched_sample) < 5:
                        unmatched_sample.append(oid_clean)

print(f"DEBUG: Total cases in 10-month range: {total_cases_in_range}")
print(f"DEBUG: Matched cases in range: {matched_count}")
print(f"DEBUG: Sample unmatched case OIDs in range: {unmatched_sample}")

# Let's check if any unmatched OIDs look like valid OIDs (e.g. truncated or close)
# Or if valid OIDs are in the unmatched list
intersection = set(case_oid_sample).intersection(valid_oids_clean)
print(f"DEBUG: Intersection of all case OIDs in range and valid OIDs: {len(intersection)}")

print("__RESULT__:")
print(json.dumps("Done debug"))"""

env_args = {'var_function-call-16912545030574088445': 'file_storage/function-call-16912545030574088445.json', 'var_function-call-5257925918374328330': 'file_storage/function-call-5257925918374328330.json', 'var_function-call-9538537814195956863': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}}

exec(code, env_args)
