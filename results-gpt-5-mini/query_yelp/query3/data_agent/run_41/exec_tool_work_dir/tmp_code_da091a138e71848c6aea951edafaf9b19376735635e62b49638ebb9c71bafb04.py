code = """import json
# Load the list of business_refs from reviews in 2018
business_refs = var_call_OKOFLknvXKVr7XHjvD9dM65K
# Map to business_ids by replacing prefix
business_ids = set()
for r in business_refs:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        business_ids.add('businessid_' + br.split('businessref_')[1])

# Load full business collection from the provided JSON file path
business_file = var_call_9DkSLS2Y7nBguytVwKnHhoRZ
with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

count = 0
matched_ids = []
for b in businesses:
    bid = b.get('business_id')
    if bid not in business_ids:
        continue
    attrs = b.get('attributes')
    has_parking = False
    if attrs and attrs != 'None':
        # attrs may be a dict or a string representation
        if isinstance(attrs, dict):
            # Check BikeParking
            bp = attrs.get('BikeParking')
            if bp is not None and isinstance(bp, bool):
                if bp:
                    has_parking = True
            elif bp is not None:
                # string like 'True' or "True"
                if 'True' in str(bp) or 'true' in str(bp).lower() or 'yes' in str(bp).lower():
                    has_parking = True
            # Check BusinessParking
            bpark = attrs.get('BusinessParking')
            if not has_parking and bpark is not None:
                s = str(bpark)
                if 'True' in s or 'true' in s.lower() or "'yes'" in s.lower():
                    has_parking = True
        else:
            # attrs is a string, check substrings
            s = str(attrs)
            # Check BikeParking pattern
            if 'BikeParking' in s and 'True' in s:
                has_parking = True
            # Check BusinessParking pattern
            if not has_parking and 'BusinessParking' in s and 'True' in s:
                has_parking = True
    if has_parking:
        count += 1
        matched_ids.append(bid)

# Prepare result
result = {'count': count, 'business_ids': sorted(list(matched_ids))}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_OKOFLknvXKVr7XHjvD9dM65K': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}], 'var_call_uGKDXdtMjSgH85tY4TTcpgzA': ['checkin', 'business'], 'var_call_9DkSLS2Y7nBguytVwKnHhoRZ': 'file_storage/call_9DkSLS2Y7nBguytVwKnHhoRZ.json'}

exec(code, env_args)
