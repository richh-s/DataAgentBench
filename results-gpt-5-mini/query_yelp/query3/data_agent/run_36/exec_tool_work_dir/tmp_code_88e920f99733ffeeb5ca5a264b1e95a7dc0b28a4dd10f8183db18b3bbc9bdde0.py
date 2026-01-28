code = """import json
from collections import defaultdict
# load the query result from var_call_B6wgfWuBuZPA6EkJPvanbW1J
path = var_call_B6wgfWuBuZPA6EkJPvanbW1J
with open(path, 'r') as f:
    data = json.load(f)

# We have list of business documents with business_id and attributes.
# Determine which businesses have BikeParking == True or BusinessParking indicating any True for keys.

def has_parking(attrs):
    if not attrs or attrs == 'None':
        return False
    # attributes may be dict with string boolean values like 'True'/'False' or nested strings for BusinessParking
    # check BikeParking
    bp = attrs.get('BikeParking') if isinstance(attrs, dict) else None
    if bp in (True, 'True', "True", "u'True'", "u'free'"):
        return True
    if isinstance(bp, str) and bp.lower()=='true':
        return True
    # check BusinessParking
    busp = attrs.get('BusinessParking') if isinstance(attrs, dict) else None
    if busp and isinstance(busp, str):
        # busp looks like "{'garage': False, 'street': True, ...}"
        # parse by checking for True values (True, 'True', True-like)
        lowered = busp.lower()
        # naive check: if 'true' or "true" present -> indicate parking available
        if 'true' in lowered:
            return True
        # also check for 'lot': True etc in non-lowercase
        if "true" in busp:
            return True
    return False

# build set of business_ids that have parking
parking_businesses = set()
all_business_ids = []
for doc in data:
    bid = doc.get('business_id')
    all_business_ids.append(bid)
    attrs = doc.get('attributes')
    if has_parking(attrs):
        parking_businesses.add(bid)

# Now load the 2018 review business_refs from var_call_Nx5RCPSwJlNkHzPRjnfwoeK8
review_records = var_call_Nx5RCPSwJlNkHzPRjnfwoeK8
review_business_refs = [r['business_ref'] for r in review_records]
# convert to businessid_ prefix
review_business_ids = ['businessid_' + ref.split('_',1)[1] for ref in review_business_refs]

# Count how many reviewed businesses in 2018 offered either business parking or bike parking
count = 0
matched = []
for bid in review_business_ids:
    if bid in parking_businesses:
        count += 1
        matched.append(bid)

# prepare result
result = {
    'count': count,
    'matching_business_ids': sorted(list(matched)),
    'total_reviewed_businesses_2018': len(review_business_ids)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Nx5RCPSwJlNkHzPRjnfwoeK8': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_B6wgfWuBuZPA6EkJPvanbW1J': 'file_storage/call_B6wgfWuBuZPA6EkJPvanbW1J.json'}

exec(code, env_args)
