code = """import json

# variables from previous tool calls are available:
# var_call_d4PdTsliNaabocq2vBvZqhK2 -> list of dicts with 'business_ref'
# var_call_PXQqvXxSNiXm5YVuh23ZEyS9 -> list of dicts with 'business_id' and 'attributes'

review_refs = [r['business_ref'] for r in var_call_d4PdTsliNaabocq2vBvZqhK2]
# Map to business_id format
review_business_ids = set(r.replace('businessref_', 'businessid_') for r in review_refs)

# Build mapping of business_id to attributes
biz_attrs = {b['business_id']: b.get('attributes') for b in var_call_PXQqvXxSNiXm5YVuh23ZEyS9}

def has_bike_parking(val):
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        s = val.lower()
        return 'true' in s or 'yes' in s
    return False

def business_parking_has_true(val):
    if val is None:
        return False
    if isinstance(val, dict):
        # check any value truthy
        return any(str(v).lower() == 'true' for v in val.values())
    if isinstance(val, str):
        s = val.lower()
        return 'true' in s
    return False

matched = []
for bid in review_business_ids:
    attrs = biz_attrs.get(bid)
    if attrs is None:
        continue
    # attrs might be string 'None'
    if isinstance(attrs, str) and attrs.strip().lower() == 'none':
        continue
    # attrs might be a dict
    # Normalize if keys present as strings
    bike = False
    bpark = False
    if isinstance(attrs, dict):
        # BikeParking key check
        if 'BikeParking' in attrs:
            bike = has_bike_parking(attrs['BikeParking'])
        # BusinessParking key check
        if 'BusinessParking' in attrs:
            bpark = business_parking_has_true(attrs['BusinessParking'])
        # sometimes key spelled 'Businessparking' etc -> check case-insensitive
        else:
            for k,v in attrs.items():
                if k.lower() == 'bikeparking':
                    bike = has_bike_parking(v)
                if k.lower() == 'businessparking':
                    bpark = business_parking_has_true(v)
    else:
        # attrs is likely a string representing a dict, try simple checks
        s = str(attrs)
        bike = 'bikeparking' in s.lower() and 'true' in s.lower()
        bpark = 'businessparking' in s.lower() and 'true' in s.lower()
        # Also detect if BusinessParking dict contains True anywhere
        if 'businessparking' in s.lower() and 'true' in s.lower():
            bpark = True

    if bike or bpark:
        matched.append(bid)

result = {
    'count': len(matched),
    'business_ids': sorted(matched)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_d4PdTsliNaabocq2vBvZqhK2': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_PXQqvXxSNiXm5YVuh23ZEyS9': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
