code = """import json, ast
reviews = var_call_OZ9sAC8TFjLE0Ke8KZtHTQrZ
biz_attrs = var_call_gfvqWKYE6J6q7eRMWVSQuAsz

# businesses that received reviews during 2018
biz_2018 = set()
for r in reviews:
    br = r.get('business_ref')
    if br and br.startswith('businessref_'):
        biz_2018.add('businessid_' + br[len('businessref_'):])


def has_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    # BikeParking: accept True / 'True'
    bp = attrs.get('BikeParking')
    if bp is True or (isinstance(bp, str) and bp.strip().lower() == 'true'):
        return True
    # BusinessParking: parse dict-like string and see if any option True
    bpark = attrs.get('BusinessParking')
    if isinstance(bpark, dict):
        return any(bool(v) for v in bpark.values())
    if isinstance(bpark, str):
        s = bpark.strip()
        try:
            d = ast.literal_eval(s)
            if isinstance(d, dict):
                return any(bool(v) for v in d.values())
        except Exception:
            # if unparsable but present, count as offered? assume no.
            return False
    return False

count = 0
for rec in biz_attrs:
    bid = rec.get('business_id')
    if bid in biz_2018 and has_parking(rec.get('attributes')):
        count += 1

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_OZ9sAC8TFjLE0Ke8KZtHTQrZ': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}], 'var_call_gfvqWKYE6J6q7eRMWVSQuAsz': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}}]}

exec(code, env_args)
