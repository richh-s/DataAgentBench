code = """import json, ast
# var_call_nQRuRqVrTQCcRroUxKV71tWS and var_call_A0lfLLn6DWSqvGLUnJfva8Qk are provided by storage
reviews = var_call_nQRuRqVrTQCcRroUxKV71tWS
businesses = var_call_A0lfLLn6DWSqvGLUnJfva8Qk

# Build set of business_ids corresponding to reviews in 2018
review_business_ids = set()
for r in reviews:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        review_business_ids.add('businessid_' + br.split('_', 1)[1])

def parse_attr(attr):
    # handle None, string "None", dict, or other types
    if attr is None:
        return {}
    if isinstance(attr, str):
        s = attr.strip()
        if s == 'None':
            return {}
        # try to literal_eval if looks like a dict
        if s.startswith('{'):
            try:
                return ast.literal_eval(s)
            except Exception:
                return {}
        # otherwise cannot parse
        return {}
    if isinstance(attr, dict):
        return attr
    return {}

def truthy(val):
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val)
    if isinstance(val, str):
        low = val.lower()
        return 'true' in low
    return False

count = 0
matched = []
for b in businesses:
    bid = b.get('business_id')
    if not bid or bid not in review_business_ids:
        continue
    attrs = parse_attr(b.get('attributes'))
    has_bike = False
    has_parking = False
    # BikeParking may be present
    if 'BikeParking' in attrs:
        has_bike = truthy(attrs.get('BikeParking'))
    # BusinessParking may be present (note sometimes key is BusinessParking or BusinessParking with different casing)
    # check common keys
    bp = None
    if 'BusinessParking' in attrs:
        bp = attrs.get('BusinessParking')
    elif 'BusinessParking' in attrs:
        bp = attrs.get('BusinessParking')
    if bp is not None:
        if isinstance(bp, dict):
            # any value True
            for v in bp.values():
                if truthy(v):
                    has_parking = True
                    break
        elif isinstance(bp, str):
            # try to parse dict-like string
            try:
                parsed = ast.literal_eval(bp)
                if isinstance(parsed, dict):
                    for v in parsed.values():
                        if truthy(v):
                            has_parking = True
                            break
            except Exception:
                # if string not dict, check if contains 'true'
                if truthy(bp):
                    has_parking = True
    if has_bike or has_parking:
        count += 1
        matched.append(bid)

# Print result as JSON-serializable simple type
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_nwtvFfQQXYWEL4wFelbIAG53': ['business', 'checkin'], 'var_call_MWvsFdEBpAz7rntr9FPkpC4r': ['review', 'tip', 'user'], 'var_call_nQRuRqVrTQCcRroUxKV71tWS': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}], 'var_call_A0lfLLn6DWSqvGLUnJfva8Qk': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
