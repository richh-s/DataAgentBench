code = """import json, ast
# load variables from storage
business_refs = var_call_MiNBxaCtGwjEiGzHLbttK7un
business_file_path = var_call_SgzonBF1tIqvuQwaj1uKVHT1

# build set of business ids corresponding to reviews in 2018
business_ref_ids = set()
for rec in business_refs:
    br = rec.get('business_ref')
    if br and '_' in br:
        suffix = br.split('_', 1)[1]
        business_ref_ids.add('businessid_' + suffix)

# load full business records from file
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

count = 0
matched_ids = set()

for b in businesses:
    bid = b.get('business_id')
    if bid not in business_ref_ids:
        continue
    attrs = b.get('attributes')
    has_bike = False
    has_business = False

    # handle case where attributes is the string 'None'
    if attrs is None or (isinstance(attrs, str) and attrs.strip().lower() == 'none'):
        attrs_dict = None
    elif isinstance(attrs, dict):
        attrs_dict = attrs
    else:
        # unexpected type, try to parse if it's a JSON-like string
        try:
            attrs_dict = ast.literal_eval(attrs)
            if not isinstance(attrs_dict, dict):
                attrs_dict = None
        except Exception:
            attrs_dict = None

    if isinstance(attrs_dict, dict):
        # BikeParking
        bp = attrs_dict.get('BikeParking')
        if isinstance(bp, bool):
            has_bike = bp
        elif isinstance(bp, str):
            v = bp.strip().lower()
            if v == 'true' or "'true'" in v or 'true' in v:
                has_bike = True
            else:
                has_bike = False

        # BusinessParking
        bpar = attrs_dict.get('BusinessParking')
        if isinstance(bpar, dict):
            for val in bpar.values():
                if val is True or (isinstance(val, str) and val.strip().lower() == 'true'):
                    has_business = True
                    break
        elif isinstance(bpar, str):
            s = bpar.strip()
            if s.lower() == 'none':
                has_business = False
            else:
                # try to parse the parking dict representation
                try:
                    parsed = ast.literal_eval(s)
                except Exception:
                    try:
                        parsed = eval(s)
                    except Exception:
                        parsed = None
                if isinstance(parsed, dict):
                    for val in parsed.values():
                        if val is True or (isinstance(val, str) and val.strip().lower() == 'true'):
                            has_business = True
                            break

    if has_bike or has_business:
        count += 1
        matched_ids.add(bid)

# prepare output
import json as _json
result = _json.dumps({"count": count, "matched_business_ids": sorted(list(matched_ids))})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_5w5pUW3qLDCrfKGSvap3avL5': ['business', 'checkin'], 'var_call_8RAbezhC9JPEvQaIUaqnEyOl': ['review', 'tip', 'user'], 'var_call_MiNBxaCtGwjEiGzHLbttK7un': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_SgzonBF1tIqvuQwaj1uKVHT1': 'file_storage/call_SgzonBF1tIqvuQwaj1uKVHT1.json'}

exec(code, env_args)
