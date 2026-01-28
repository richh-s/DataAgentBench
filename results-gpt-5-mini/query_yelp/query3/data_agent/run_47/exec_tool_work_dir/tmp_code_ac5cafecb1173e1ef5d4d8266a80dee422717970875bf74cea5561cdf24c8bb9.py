code = """import json, ast
# variables from previous tool calls are available: var_call_k7rkxVqBWLNuBzrM3XNftNsv, var_call_sK6XOnmxdsp0wfd443ypJD0r
reviews = var_call_k7rkxVqBWLNuBzrM3XNftNsv
businesses = var_call_sK6XOnmxdsp0wfd443ypJD0r

# Build set of corresponding business_id values
review_business_ids = set()
for r in reviews:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        review_business_ids.add('businessid_' + br.split('_', 1)[1])

count = 0
matching_businesses = []

for b in businesses:
    bid = b.get('business_id')
    if not bid or bid not in review_business_ids:
        continue
    attrs = b.get('attributes')
    if not attrs or attrs == 'None':
        continue
    # attrs might be dict or string
    if isinstance(attrs, str):
        try:
            attrs_parsed = ast.literal_eval(attrs)
        except Exception:
            # try to fix typical issues like u'no'
            attrs_clean = attrs.replace("u'", "'")
            try:
                attrs_parsed = ast.literal_eval(attrs_clean)
            except Exception:
                attrs_parsed = {}
    elif isinstance(attrs, dict):
        attrs_parsed = attrs
    else:
        attrs_parsed = {}

    # normalize keys to check for bike or business parking
    has_bike = False
    has_business_parking = False
    for k, v in attrs_parsed.items():
        key = str(k).lower()
        if key == 'bikeparking':
            # v might be 'True'/'False' or boolean
            if isinstance(v, str):
                val = v.strip().strip("'\"")
                if val.lower() == 'true':
                    has_bike = True
            elif isinstance(v, bool):
                if v:
                    has_bike = True
        if 'businessparking' in key or key == 'businessparking':
            # v might be dict or string repr of dict
            if isinstance(v, str):
                try:
                    bp = ast.literal_eval(v)
                except Exception:
                    bp = {}
            elif isinstance(v, dict):
                bp = v
            else:
                bp = {}
            # check if any parking type is truthy
            for subk, subv in bp.items():
                if isinstance(subv, str):
                    s = str(subv).strip().strip("'\"")
                    if s.lower() == 'true':
                        has_business_parking = True
                        break
                elif isinstance(subv, bool):
                    if subv:
                        has_business_parking = True
                        break
            # also some BusinessParking values might be like "{... 'lot': True ...}"
        if has_bike or has_business_parking:
            break
    if has_bike or has_business_parking:
        count += 1
        matching_businesses.append(bid)

# Prepare result
result = {"count": count, "matching_business_ids": sorted(matching_businesses)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_k7rkxVqBWLNuBzrM3XNftNsv': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_sK6XOnmxdsp0wfd443ypJD0r': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
