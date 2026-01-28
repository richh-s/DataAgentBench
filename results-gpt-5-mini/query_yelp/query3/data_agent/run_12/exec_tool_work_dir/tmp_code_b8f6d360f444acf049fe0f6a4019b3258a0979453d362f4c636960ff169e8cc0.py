code = """import json

# Access stored tool results
business_refs = var_call_g4UFb2N8a6Zw7UdV3ApJPAFH  # list of dicts
business_file = var_call_36vN43Lt7uJAUHjV9Ui6QzfX  # path to JSON file

# Load full business collection from file
with open(business_file, 'r') as f:
    businesses = json.load(f)

# Build set of business_ids corresponding to the reviewed businesses in 2018
reviewed_business_ids = set()
for r in business_refs:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        reviewed_business_ids.add(br.replace('businessref_', 'businessid_'))

# Helper to determine truthy values in various representations
def truthy(v):
    if v is None:
        return False
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return bool(v)
    if isinstance(v, dict):
        # any True-ish value in dict values
        for val in v.values():
            if truthy(val):
                return True
        return False
    if isinstance(v, str):
        s = v.strip()
        if s.lower() in ('true', "u'true'", '"true"'):
            return True
        # If it's a string representation of a dict, check if 'true' appears
        if 'true' in s.lower():
            return True
        return False
    return False

# Count businesses among reviewed ones that offer either BusinessParking or BikeParking
count = 0
matched_businesses = []
for b in businesses:
    bid = b.get('business_id')
    if bid in reviewed_business_ids:
        attrs = b.get('attributes')
        has_parking = False
        if isinstance(attrs, dict):
            # Check BikeParking
            if 'BikeParking' in attrs and truthy(attrs.get('BikeParking')):
                has_parking = True
            # Check BusinessParking
            if 'BusinessParking' in attrs and truthy(attrs.get('BusinessParking')):
                has_parking = True
        else:
            # attrs might be a string like 'None' or other; handle if contains BikeParking or BusinessParking
            if isinstance(attrs, str):
                s = attrs.lower()
                if 'bikeparking' in s and 'true' in s:
                    has_parking = True
                if 'businessparking' in s and 'true' in s:
                    has_parking = True
        if has_parking:
            count += 1
            matched_businesses.append(bid)

# Prepare result as integer
import json as _json
print("__RESULT__:")
print(_json.dumps(count))"""

env_args = {'var_call_g4UFb2N8a6Zw7UdV3ApJPAFH': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_36vN43Lt7uJAUHjV9Ui6QzfX': 'file_storage/call_36vN43Lt7uJAUHjV9Ui6QzfX.json'}

exec(code, env_args)
