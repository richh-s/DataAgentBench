code = """import json
import ast

# variables from previous tool calls
reviewed_business_ids = var_call_N4WS1m2ZTTK6cDSpTQUTsejy
business_docs = var_call_j4g5GkEHANMTvDfLjWlvI9sW

# Create a set for quick lookup
reviewed_set = set(reviewed_business_ids)

matching_ids = []

for doc in business_docs:
    bid = doc.get('business_id')
    if bid not in reviewed_set:
        continue
    attrs = doc.get('attributes')
    bike_ok = False
    business_ok = False
    if isinstance(attrs, dict):
        # Check BikeParking
        if 'BikeParking' in attrs:
            v = attrs['BikeParking']
            if isinstance(v, bool):
                bike_ok = v
            elif isinstance(v, str):
                if v.lower() == "true":
                    bike_ok = True
                else:
                    bike_ok = False
        # Check any Business Parking-like field
        for k, v in attrs.items():
            if 'businessparking' in k.lower() or ('business' in k.lower() and 'parking' in k.lower()):
                # v might be a string representation of a dict
                if isinstance(v, dict):
                    # check any True values
                    if any((val is True) or (isinstance(val, str) and val.lower()=='true') for val in v.values()):
                        business_ok = True
                elif isinstance(v, str):
                    # try to parse as literal dict
                    try:
                        parsed = ast.literal_eval(v)
                        if isinstance(parsed, dict) and any((val is True) or (isinstance(val, str) and val.lower()=='true') for val in parsed.values()):
                            business_ok = True
                    except Exception:
                        # fallback: check if the string contains 'True'
                        if 'True' in v:
                            business_ok = True
                elif isinstance(v, bool):
                    if v:
                        business_ok = True
    # If attributes is string like 'None' or None, skip
    if bike_ok or business_ok:
        matching_ids.append(bid)

result = {"count": len(matching_ids), "matching_business_ids": matching_ids}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4ead7utHX2uGv2VfE1aMmxIt': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_N4WS1m2ZTTK6cDSpTQUTsejy': ['businessid_13', 'businessid_79', 'businessid_91', 'businessid_46', 'businessid_47', 'businessid_73', 'businessid_66', 'businessid_25', 'businessid_59', 'businessid_67', 'businessid_15', 'businessid_24', 'businessid_36', 'businessid_17', 'businessid_43', 'businessid_99', 'businessid_80', 'businessid_86', 'businessid_62', 'businessid_8', 'businessid_57', 'businessid_37', 'businessid_40', 'businessid_83', 'businessid_26', 'businessid_4', 'businessid_68', 'businessid_82', 'businessid_35', 'businessid_45', 'businessid_77', 'businessid_27', 'businessid_20', 'businessid_22', 'businessid_14', 'businessid_28'], 'var_call_j4g5GkEHANMTvDfLjWlvI9sW': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
