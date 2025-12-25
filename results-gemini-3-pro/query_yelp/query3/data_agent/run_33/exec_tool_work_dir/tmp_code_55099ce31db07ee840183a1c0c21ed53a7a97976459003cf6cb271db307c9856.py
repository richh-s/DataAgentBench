code = """import json
import ast

reviewed_list = locals()['var_function-call-7123310931460408034']
business_list = locals()['var_function-call-16229247920698268974']

# Convert reviewed refs to business ids
reviewed_ids = set()
for item in reviewed_list:
    ref = item['business_ref']
    if ref:
        bid = ref.replace('businessref_', 'businessid_')
        reviewed_ids.add(bid)

count = 0
for biz in business_list:
    bid = biz.get('business_id')
    
    # Only consider businesses reviewed in 2018
    if bid not in reviewed_ids:
        continue
    
    attrs = biz.get('attributes')
    if not attrs or attrs == 'None':
        continue
    
    has_bike = False
    has_car = False
    
    # Check BikeParking
    if 'BikeParking' in attrs:
        val = attrs['BikeParking']
        # Handle string "True", "False", "u'True'", etc.
        s_val = str(val).lower()
        if s_val == 'true':
            has_bike = True
            
    # Check BusinessParking
    if 'BusinessParking' in attrs:
        val = attrs['BusinessParking']
        # It's usually a string representation of a dict or "True"/"False"
        if isinstance(val, str):
            if val.lower() == 'true':
                has_car = True
            elif val.startswith('{'):
                try:
                    # Parse dict string
                    p_dict = ast.literal_eval(val)
                    if isinstance(p_dict, dict):
                        # If any key is True (garage, street, lot, valet)
                        if any(v is True for v in p_dict.values()):
                            has_car = True
                except:
                    pass
    
    if has_bike or has_car:
        count += 1

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-7123310931460408034': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_function-call-16229247920698268974': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
