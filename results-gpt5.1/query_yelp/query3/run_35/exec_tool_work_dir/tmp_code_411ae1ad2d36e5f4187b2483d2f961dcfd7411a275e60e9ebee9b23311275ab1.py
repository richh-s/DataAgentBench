code = """import json, pandas as pd, os

# load review business_refs
review_refs = var_call_ciKmsMy7IOQbXF9I3ldhWewP
refs = [r['business_ref'] for r in review_refs]

# convert to corresponding business_ids
# businessref_13 -> businessid_13
bus_ids = set([ref.replace('businessref_', 'businessid_') for ref in refs])

# load full business attributes from file
path = var_call_PD0ZbdFw4LnMlis9FeLByo1C
with open(path, 'r') as f:
    biz_attr = json.load(f)

# filter businesses that both have reviews in 2018 and offer parking or bike parking
count = 0
for b in biz_attr:
    bid = b.get('business_id')
    if bid not in bus_ids:
        continue
    attrs = b.get('attributes') or {}
    has_bike = attrs.get('BikeParking') == 'True'
    has_parking = 'BusinessParking' in attrs and attrs.get('BusinessParking') not in [None, 'None']
    if has_bike or has_parking:
        count += 1

import json as js
res = js.dumps(count)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_brDmZMPfy1VDyWuVisXamfWf': ['checkin', 'business'], 'var_call_uOxbO92k8znGs9uSG4Q60fwa': [], 'var_call_ciKmsMy7IOQbXF9I3ldhWewP': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}], 'var_call_PD0ZbdFw4LnMlis9FeLByo1C': 'file_storage/call_PD0ZbdFw4LnMlis9FeLByo1C.json'}

exec(code, env_args)
