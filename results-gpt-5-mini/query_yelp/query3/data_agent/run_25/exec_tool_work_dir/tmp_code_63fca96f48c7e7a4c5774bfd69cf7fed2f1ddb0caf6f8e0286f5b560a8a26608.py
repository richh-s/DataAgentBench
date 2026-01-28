code = """import json, ast

# Load data from previous tool calls
# var_call_9NxVzh6kHvi9Vo0PSsDHGOnL is a filepath to the business attributes JSON
with open(var_call_9NxVzh6kHvi9Vo0PSsDHGOnL, 'r') as f:
    businesses = json.load(f)

# var_call_8B1z7or13yVfqHJGbjV2BpuO is a list of dicts from the review query
reviews = var_call_8B1z7or13yVfqHJGbjV2BpuO

# Build set of business_ids that had reviews in 2018
review_business_ids = set()
for r in reviews:
    ref = r.get('business_ref')
    if not ref:
        continue
    # convert prefix businessref_X -> businessid_X
    if ref.startswith('businessref_'):
        num = ref.split('businessref_')[1]
        review_business_ids.add('businessid_' + num)
    else:
        # fallback
        review_business_ids.add(ref)

count = 0
matched_businesses = []

for b in businesses:
    bid = b.get('business_id')
    if bid not in review_business_ids:
        continue
    attrs = b.get('attributes')
    if not attrs:
        continue

    bike_flag = False
    parking_flag = False

    # Check BikeParking
    bike_val = attrs.get('BikeParking') if isinstance(attrs, dict) else None
    if bike_val is not None:
        if isinstance(bike_val, bool):
            bike_flag = bike_val is True
        else:
            if 'true' in str(bike_val).lower():
                bike_flag = True

    # Check BusinessParking
    bp_val = attrs.get('BusinessParking') if isinstance(attrs, dict) else None
    if bp_val is not None:
        # If it's already a dict
        if isinstance(bp_val, dict):
            for v in bp_val.values():
                if v is True or (isinstance(v, str) and v.lower() == 'true') or v == 1:
                    parking_flag = True
                    break
        else:
            s = str(bp_val)
            if s.lower() != 'none':
                # Try to parse dict-like string
                try:
                    parsed = ast.literal_eval(s.replace("u'", "'"))
                    if isinstance(parsed, dict):
                        for v in parsed.values():
                            if v is True or (isinstance(v, str) and v.lower() == 'true') or v == 1:
                                parking_flag = True
                                break
                except Exception:
                    # fallback: look for the literal 'true' in the string
                    if 'true' in s.lower():
                        parking_flag = True

    if bike_flag or parking_flag:
        count += 1
        matched_businesses.append(bid)

# Print result in required format
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_UUYBreg6m1MNmvinAl2RK5HI': ['business', 'checkin'], 'var_call_DjiysTbZPCOOgk3Ubc4CB2k5': ['review', 'tip', 'user'], 'var_call_9NxVzh6kHvi9Vo0PSsDHGOnL': 'file_storage/call_9NxVzh6kHvi9Vo0PSsDHGOnL.json', 'var_call_8B1z7or13yVfqHJGbjV2BpuO': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}]}

exec(code, env_args)
