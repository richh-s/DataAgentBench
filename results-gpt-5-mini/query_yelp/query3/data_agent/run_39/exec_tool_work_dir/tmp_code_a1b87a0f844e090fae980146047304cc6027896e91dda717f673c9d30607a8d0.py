code = """import json
# load the full result from the storage var
path = var_call_7G5eO5QFcXpqMZaaLCAraJUu
with open(path, 'r') as f:
    data = json.load(f)

# We'll process the attributes to determine if a business has bike parking or business parking
results = []
for rec in data:
    bid = rec.get('business_id')
    attrs = rec.get('attributes')
    has_bike = False
    has_parking = False
    if isinstance(attrs, dict):
        # BikeParking could be present and be a string 'True'/'False' or actual boolean
        bp = attrs.get('BikeParking')
        if bp is not None:
            # normalize string representations
            if isinstance(bp, bool):
                has_bike = bp
            else:
                s = str(bp).lower()
                if 'true' in s:
                    has_bike = True
                elif 'yes' in s:
                    has_bike = True
                elif 'none' in s or 'false' in s or 'null' in s:
                    has_bike = False
                else:
                    # if ambiguous, leave False
                    has_bike = False
        # BusinessParking could be a dict-string or 'None'
        park = attrs.get('BusinessParking')
        if park is not None and park != 'None':
            # park may be a string representation of a dict like:"{'garage': False, 'street': True, ...}"
            if isinstance(park, dict):
                # check if any value is True
                has_parking = any(v is True or (isinstance(v, str) and 'true' in v.lower()) for v in park.values())
            else:
                s = str(park).lower()
                if 'true' in s:
                    has_parking = True
                elif 'lot' in s or 'street' in s or 'garage' in s or 'valet' in s:
                    # check if any of these appear with True; crude check: look for patterns "'lot': True" etc
                    if "'lot': true" in s or "'street': true" in s or "'garage': true" in s or "'valet': true" in s:
                        has_parking = True
                    else:
                        # sometimes values are False; check for any True tokens
                        if ': true' in s:
                            has_parking = True
                        else:
                            # if it contains the word false everywhere, treat as False
                            has_parking = False
                else:
                    has_parking = False
    results.append({'business_id': bid, 'has_bike': has_bike, 'has_parking': has_parking})

# Count businesses where has_bike or has_parking is True
count = sum(1 for r in results if r['has_bike'] or r['has_parking'])

out = {'count': count, 'details': results}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_4bVDKwobGvMuQI1YEeWAS2Jh': ['checkin', 'business'], 'var_call_Kw6LGA1yugAU5jIrA3ExioJW': ['review', 'tip', 'user'], 'var_call_jROIbAtHgN3G3szif63SoS4V': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}], 'var_call_7G5eO5QFcXpqMZaaLCAraJUu': 'file_storage/call_7G5eO5QFcXpqMZaaLCAraJUu.json'}

exec(code, env_args)
