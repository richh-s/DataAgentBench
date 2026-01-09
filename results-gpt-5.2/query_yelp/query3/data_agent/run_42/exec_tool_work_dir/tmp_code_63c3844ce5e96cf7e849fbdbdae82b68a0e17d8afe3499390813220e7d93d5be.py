code = """import json, pandas as pd

reviews = pd.DataFrame(var_call_UDMbNbNeBq1MIvGDinLTf3rY)
biz = pd.DataFrame(var_call_cZDCjuoEDIBiIGFkWnz8hYCC)

# convert businessref_X -> businessid_X
reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# determine which businesses offer business parking or bike parking

def has_any_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    # BikeParking
    bp = attrs.get('BikeParking', None)
    bike = str(bp).lower() in ['true','1','yes']

    # BusinessParking: may be dict or stringified dict
    bpar = attrs.get('BusinessParking', None)
    if isinstance(bpar, dict):
        bpar_dict = bpar
    elif isinstance(bpar, str):
        s = bpar.strip()
        try:
            bpar_dict = eval(s, {"__builtins__": {}}) if s.startswith('{') and s.endswith('}') else None
        except Exception:
            bpar_dict = None
    else:
        bpar_dict = None

    business_parking = False
    if isinstance(bpar_dict, dict):
        business_parking = any(bool(v) for v in bpar_dict.values())

    return bike or business_parking

biz['has_parking'] = biz['attributes'].apply(has_any_parking)

eligible_biz_ids = set(biz.loc[biz['has_parking'], 'business_id'])
reviewed_biz_ids_2018 = set(reviews['business_id'])

count = len(eligible_biz_ids & reviewed_biz_ids_2018)

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_UDMbNbNeBq1MIvGDinLTf3rY': [{'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}], 'var_call_cZDCjuoEDIBiIGFkWnz8hYCC': [{'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}}, {'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}]}

exec(code, env_args)
