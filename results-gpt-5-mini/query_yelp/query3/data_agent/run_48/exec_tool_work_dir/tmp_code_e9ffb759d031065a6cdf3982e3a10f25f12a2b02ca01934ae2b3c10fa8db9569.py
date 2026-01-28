code = """import json, ast
# Load business collection JSON from file path provided in storage
path = var_call_stgbazZgMOn6xwvqg5cWgZYF
with open(path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
# Load review business_refs from 2018
reviews = var_call_XKW2Q9vsxldUgM0cND8Xj1FX
# Build set of business_id values corresponding to those business_refs
biz_set = set()
for r in reviews:
    ref = r.get('business_ref')
    if ref and ref.startswith('businessref_'):
        biz_set.add(ref.replace('businessref_', 'businessid_'))
import re

def parse_bool(val):
    # Return True if val indicates True for our purposes.
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val)
    if isinstance(val, dict):
        # If dict, consider True if any value is True
        return any(v is True or (isinstance(v, str) and v.lower() == 'true') for v in val.values())
    if isinstance(val, str):
        s = val.strip()
        # direct markers
        if s.lower() == 'true':
            return True
        if s.lower() == 'false':
            return False
        if s == 'None' or s == "None":
            return False
        # try to literal_eval strings that look like dicts
        if (s.startswith('{') and s.endswith('}')) or "'" in s:
            try:
                cleaned = s.replace("u'", "'")
                parsed = ast.literal_eval(cleaned)
                if isinstance(parsed, dict):
                    return any(v is True or (isinstance(v, str) and v.lower() == 'true') for v in parsed.values())
            except Exception:
                pass
        # fallback: check for the substring True
        if 'True' in s or "'True'" in s:
            return True
    return False

counted = set()
for b in businesses:
    bid = b.get('business_id')
    if bid not in biz_set:
        continue
    attrs = b.get('attributes')
    bike = False
    buspark = False
    if isinstance(attrs, dict):
        bike = parse_bool(attrs.get('BikeParking'))
        buspark = parse_bool(attrs.get('BusinessParking'))
        if not buspark:
            for k in attrs:
                if k and k.lower() == 'businessparking':
                    buspark = parse_bool(attrs.get(k))
                    if buspark:
                        break
    else:
        # attrs might be a string like 'None'
        if isinstance(attrs, str):
            if 'BikeParking' in attrs and 'True' in attrs:
                bike = True
            if 'BusinessParking' in attrs and 'True' in attrs:
                buspark = True
    if bike or buspark:
        counted.add(bid)

result_count = len(counted)
print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_call_2zsT4OnJlNaXrC7pOOPYSfkh': ['checkin', 'business'], 'var_call_XKW2Q9vsxldUgM0cND8Xj1FX': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}], 'var_call_stgbazZgMOn6xwvqg5cWgZYF': 'file_storage/call_stgbazZgMOn6xwvqg5cWgZYF.json'}

exec(code, env_args)
