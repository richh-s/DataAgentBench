code = """import json
# Load business attribute records from the provided JSON file path variable
with open(var_call_tymbm6pVVPvGriQz1xCivrLA, 'r') as f:
    businesses = json.load(f)
# Load review business refs from variable
reviews = var_call_7kgpWnrl7F5pKIRqiRviwiX6

# Convert review business_ref to business_id format
review_business_ids = set()
for r in reviews:
    br = r.get('business_ref')
    if br is None:
        continue
    if br.startswith('businessref_'):
        bid = 'businessid_' + br.split('_', 1)[1]
    else:
        bid = br
    review_business_ids.add(bid)

# Business IDs that have either BusinessParking or BikeParking (from the queried results)
parking_business_ids = set()
for b in businesses:
    bid = b.get('business_id')
    if bid:
        parking_business_ids.add(bid)

# Intersection
matching = sorted(list(review_business_ids & parking_business_ids))
count = len(matching)

import json as _json
output = _json.dumps({"count": count, "business_ids": matching})
print("__RESULT__:")
print(output)"""

env_args = {'var_call_NiQix5Gqa7PNOyyDkvRmxNEC': ['checkin', 'business'], 'var_call_c0tHAl5skB7IXm6wxnE09ZUv': ['review', 'tip', 'user'], 'var_call_tymbm6pVVPvGriQz1xCivrLA': 'file_storage/call_tymbm6pVVPvGriQz1xCivrLA.json', 'var_call_7kgpWnrl7F5pKIRqiRviwiX6': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_17'}]}

exec(code, env_args)
