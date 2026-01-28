code = """import json, ast
# Variables from storage:
# var_call_CFe9y0rdJH8XyegjhU51xaHz : list of dicts with business_ref
# var_call_DdxzqxhgKCo4LXNMIUFkspsL : file path to large JSON result (business collection)
reviews_2018 = var_call_CFe9y0rdJH8XyegjhU51xaHz
business_file_path = var_call_DdxzqxhgKCo4LXNMIUFkspsL

# Build set of business IDs corresponding to reviews (replace prefix)
business_ids = set()
for r in reviews_2018:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        business_ids.add('businessid_' + br.split('_',1)[1])

# Load business collection data from file
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

# Map business_id to attributes
biz_attrs = {b.get('business_id'): b.get('attributes') for b in businesses}

import math

def has_parking(attributes):
    if attributes is None:
        return False
    # sometimes attributes is the string "None"
    if isinstance(attributes, str):
        if attributes.strip().lower() == 'none':
            return False
        # sometimes attributes is a stringified dict? Try to parse
        try:
            attributes = ast.literal_eval(attributes)
        except Exception:
            # cannot parse, treat as no attributes
            return False
    # Now attributes should be a dict
    if not isinstance(attributes, dict):
        return False
    # Check BikeParking
    bike = attributes.get('BikeParking')
    if bike is not None:
        # bike could be True/False or string like 'True'/'False' or u'no'
        try:
            if isinstance(bike, bool) and bike:
                return True
            s = str(bike).lower()
            if 'true' in s or 'yes' in s or 'free' in s:
                return True
            # sometimes values like 'u"free"' or 'true' included
        except Exception:
            pass
    # Check BusinessParking
    bpark = attributes.get('BusinessParking')
    if bpark is None:
        return False
    # If bpark is string 'None'
    if isinstance(bpark, str) and bpark.strip().lower() == 'none':
        return False
    # If bpark is dict already
    if isinstance(bpark, dict):
        for v in bpark.values():
            if isinstance(v, bool) and v:
                return True
            if str(v).lower() == 'true':
                return True
        return False
    # If bpark is string representation of dict, try to parse
    if isinstance(bpark, str):
        try:
            parsed = ast.literal_eval(bpark)
            if isinstance(parsed, dict):
                for v in parsed.values():
                    if isinstance(v, bool) and v:
                        return True
                    if str(v).lower() == 'true':
                        return True
        except Exception:
            # fallback: check if substring 'true' exists
            if 'true' in bpark.lower() or 'lot' in bpark.lower() and 'true' in bpark.lower():
                return True
    return False

# Count businesses
count = 0
details = []
for bid in sorted(business_ids):
    attrs = biz_attrs.get(bid)
    if has_parking(attrs):
        count += 1
        details.append(bid)

# Prepare result JSON-serializable string
result = json.dumps({"count": count, "businesses": details})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_NNrmFnFvCegXx1G08dh4KHEi': ['checkin', 'business'], 'var_call_LPiVm9FUiahtciin1nYye2mW': ['review', 'tip', 'user'], 'var_call_CFe9y0rdJH8XyegjhU51xaHz': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_DdxzqxhgKCo4LXNMIUFkspsL': 'file_storage/call_DdxzqxhgKCo4LXNMIUFkspsL.json'}

exec(code, env_args)
