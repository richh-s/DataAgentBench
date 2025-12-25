code = """import json
import ast

# Load reviews result
reviews = locals()['var_function-call-10456593153731356547']
reviewed_ids = set()
for r in reviews:
    # business_ref looks like "businessref_91"
    # we strip the prefix to get "91"
    ref = r['business_ref']
    if '_' in ref:
        reviewed_ids.add(ref.split('_')[1])
    else:
        reviewed_ids.add(ref)

# Load businesses result
# The previous result is in a file
file_path = locals()['var_function-call-309311967501424082']
with open(file_path, 'r') as f:
    businesses = json.load(f)

count = 0
matched_businesses = []

for b in businesses:
    # business_id looks like "businessid_49"
    bid_full = b['business_id']
    if '_' in bid_full:
        bid = bid_full.split('_')[1]
    else:
        bid = bid_full
    
    if bid in reviewed_ids:
        attrs = b.get('attributes')
        
        # Check if attributes is valid
        if not attrs or attrs == 'None':
            continue
            
        # Check BikeParking
        # It seems to be a string "True" or "False" in the dict
        bike_parking = False
        if 'BikeParking' in attrs:
            val = attrs['BikeParking']
            if val == 'True':
                bike_parking = True
        
        # Check BusinessParking
        bus_parking = False
        if 'BusinessParking' in attrs:
            val = attrs['BusinessParking']
            if val and val != 'None':
                # It's a string representation of a dict
                try:
                    # Use ast.literal_eval to parse python-like dict string
                    parking_dict = ast.literal_eval(val)
                    if isinstance(parking_dict, dict):
                        # Check if any value is True
                        if any(parking_dict.values()):
                            bus_parking = True
                except Exception as e:
                    # Fallback or ignore if parse fails
                    pass
        
        if bike_parking or bus_parking:
            count += 1
            matched_businesses.append(bid)

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-10456593153731356547': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}], 'var_function-call-10456593153731354882': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_function-call-1902380160992146062': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_function-call-309311967501424082': 'file_storage/function-call-309311967501424082.json'}

exec(code, env_args)
