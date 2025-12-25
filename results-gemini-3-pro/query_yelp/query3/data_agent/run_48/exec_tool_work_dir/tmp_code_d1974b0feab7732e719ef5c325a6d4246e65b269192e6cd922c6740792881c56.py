code = """import json
import ast

# Load reviewed businesses
reviewed_refs = locals()['var_function-call-16430310729693730399']
# Convert to businessid format
reviewed_ids = set()
for r in reviewed_refs:
    ref = r['business_ref']
    # map businessref_X to businessid_X
    if ref.startswith('businessref_'):
        bid = 'businessid_' + ref.split('_')[1]
        reviewed_ids.add(bid)

# Load business attributes
# The previous result might be a list (if small) or a path (if large).
# Based on the output, it showed a list preview, but usually if it's large it's a path.
# However, the preview showed [ ... ] and the message said "The result is stored under key...".
# Let's check the type.
business_data = locals()['var_function-call-4907661616707184504']

if isinstance(business_data, str) and not business_data.startswith('['):
    # It's a file path
    with open(business_data, 'r') as f:
        business_list = json.load(f)
else:
    business_list = business_data

count = 0
matched_businesses = []

for b in business_list:
    bid = b.get('business_id')
    if bid not in reviewed_ids:
        continue
    
    attrs = b.get('attributes')
    if not attrs or attrs == 'None':
        continue
    
    # Check Bike Parking
    bike_parking = False
    if 'BikeParking' in attrs and attrs['BikeParking'] == 'True':
        bike_parking = True
        
    # Check Business Parking
    business_parking = False
    if 'BusinessParking' in attrs:
        bp_val = attrs['BusinessParking']
        # It's a string representation of a dict, e.g. "{'garage': False, ...}"
        if isinstance(bp_val, str) and bp_val.startswith('{'):
            try:
                # ast.literal_eval is safer than eval
                bp_dict = ast.literal_eval(bp_val)
                if any(v is True for v in bp_dict.values()):
                    business_parking = True
            except:
                pass
        elif bp_val == 'True': # Rare case if schema varies
            business_parking = True

    if bike_parking or business_parking:
        count += 1
        matched_businesses.append(bid)

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-16430310729693730399': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}], 'var_function-call-8780420354495396198': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_function-call-4907661616707184504': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
