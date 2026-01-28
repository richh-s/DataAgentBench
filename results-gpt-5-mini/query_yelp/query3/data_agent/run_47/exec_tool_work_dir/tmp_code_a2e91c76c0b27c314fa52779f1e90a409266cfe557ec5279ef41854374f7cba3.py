code = """import json, ast
reviews = var_call_k7rkxVqBWLNuBzrM3XNftNsv
businesses = var_call_sK6XOnmxdsp0wfd443ypJD0r

review_business_ids = set()
for r in reviews:
    br = r.get('business_ref')
    if br and isinstance(br, str) and br.startswith('businessref_'):
        parts = br.split('_', 1)
        if len(parts) > 1:
            review_business_ids.add('businessid_' + parts[1])

count = 0
matching_businesses = []

def parse_attrs(attrs):
    if attrs is None:
        return {}
    if isinstance(attrs, dict):
        return attrs
    if isinstance(attrs, str):
        s = attrs.strip()
        if s == 'None':
            return {}
        try:
            return ast.literal_eval(s)
        except Exception:
            try:
                s2 = s.replace("u'", "'")
                return ast.literal_eval(s2)
            except Exception:
                return {}
    return {}

for b in businesses:
    bid = b.get('business_id')
    if not bid or bid not in review_business_ids:
        continue
    attrs_raw = b.get('attributes')
    attrs = parse_attrs(attrs_raw)
    if not attrs:
        continue
    has_bike = False
    has_business_parking = False
    for k, v in attrs.items():
        if k is None:
            continue
        key = str(k).lower()
        if key == 'bikeparking' or ('bike' in key and 'parking' in key):
            if isinstance(v, bool):
                if v:
                    has_bike = True
            else:
                if str(v).strip().lower() == 'true':
                    has_bike = True
        if 'businessparking' in key or 'business_parking' in key or 'business parking' in key:
            bp = {}
            if isinstance(v, dict):
                bp = v
            else:
                try:
                    bp = ast.literal_eval(str(v))
                except Exception:
                    try:
                        bp = ast.literal_eval(str(v).replace("u'", "'"))
                    except Exception:
                        bp = {}
            if isinstance(bp, dict):
                for subk, subv in bp.items():
                    if isinstance(subv, bool):
                        if subv:
                            has_business_parking = True
                            break
                    else:
                        if str(subv).strip().lower() == 'true':
                            has_business_parking = True
                            break
        if has_bike or has_business_parking:
            break
    if has_bike or has_business_parking:
        count += 1
        matching_businesses.append(bid)

result = {'count': count, 'matching_business_ids': sorted(matching_businesses)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_k7rkxVqBWLNuBzrM3XNftNsv': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_sK6XOnmxdsp0wfd443ypJD0r': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
