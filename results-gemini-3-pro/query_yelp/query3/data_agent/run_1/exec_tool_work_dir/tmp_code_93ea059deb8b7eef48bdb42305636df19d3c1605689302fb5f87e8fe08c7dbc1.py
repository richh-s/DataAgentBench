code = """import pandas as pd
import json
import ast

# Load results
# The keys are from previous tool outputs
reviewed_list = locals()['var_function-call-4585531244859699601']
# The MongoDB result might be a list or a file path if large. 
# Based on the prompt "If a tool result is large, the next message will include a preview... and the storage entry will be the .json file path"
# The previous message showed a list, but it also said "The result is stored under key...". 
# Usually if it's a list in the variable, I use it directly. If it's a string ending in .json, I load it.
biz_data = locals()['var_function-call-7117607587256428319']

if isinstance(biz_data, str) and biz_data.endswith('.json'):
    with open(biz_data, 'r') as f:
        biz_data = json.load(f)

# Process reviewed businesses
reviewed_ids = set()
for item in reviewed_list:
    ref = item['business_ref']
    # Extract ID part. "businessref_13" -> "13"
    if ref and '_' in ref:
        reviewed_ids.add(ref.split('_')[1])

# Process business attributes
count = 0
for biz in biz_data:
    b_id_str = biz.get('business_id')
    if not b_id_str:
        continue
    # Extract ID. "businessid_49" -> "49"
    b_id = b_id_str.split('_')[1]
    
    # Only check if this business was reviewed in 2018
    if b_id not in reviewed_ids:
        continue
        
    attrs = biz.get('attributes')
    
    # Check Bike Parking
    has_bike = False
    if attrs and isinstance(attrs, dict):
        if attrs.get('BikeParking') == 'True':
            has_bike = True
            
    # Check Business Parking
    has_biz_park = False
    if attrs and isinstance(attrs, dict):
        park_str = attrs.get('BusinessParking')
        if park_str and park_str != 'None':
            try:
                # The string is like "{'garage': False, ...}" which is valid python dict syntax
                # We can use ast.literal_eval
                park_dict = ast.literal_eval(park_str)
                if isinstance(park_dict, dict):
                    # If any value is True, they have parking
                    if any(park_dict.values()):
                        has_biz_park = True
            except:
                pass
    
    if has_bike or has_biz_park:
        count += 1

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-984983090001950165': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_function-call-4585531244859699601': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_function-call-7117607587256428319': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
