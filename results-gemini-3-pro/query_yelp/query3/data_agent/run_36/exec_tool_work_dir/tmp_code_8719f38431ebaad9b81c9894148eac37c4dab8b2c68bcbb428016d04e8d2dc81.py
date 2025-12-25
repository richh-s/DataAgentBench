code = """import json
import ast

# Load previous results
reviewed_list = locals()['var_function-call-17452870736414877789']
# business_data might be a file path if large, or list if small. 
# The system description says: "If a tool result is large, the next message will include a preview ... and the storage entry will be the .json file path".
# Since the output was a preview, 'var_function-call-10961423656352222677' is likely a file path.
business_data_var = locals()['var_function-call-10961423656352222677']

if isinstance(business_data_var, str) and business_data_var.endswith('.json'):
    with open(business_data_var, 'r') as f:
        business_data = json.load(f)
else:
    business_data = business_data_var

# Create set of reviewed business refs
reviewed_refs = set(item['business_ref'] for item in reviewed_list)

count = 0
matched_businesses = []

for bus in business_data:
    b_id = bus.get('business_id')
    if not b_id:
        continue
    
    # Convert to business_ref format
    # businessid_X -> businessref_X
    b_ref = b_id.replace('businessid_', 'businessref_')
    
    if b_ref not in reviewed_refs:
        continue
        
    attrs = bus.get('attributes')
    if not attrs or attrs == "None":
        continue
        
    # Check for BikeParking or BusinessParking
    has_bike = False
    has_parking = False
    
    # BikeParking
    # According to preview: "BikeParking": "True" or "False"
    if 'BikeParking' in attrs:
        val = attrs['BikeParking']
        if val == 'True':
            has_bike = True
            
    # BusinessParking
    # According to preview: "{'garage': False, ...}"
    if 'BusinessParking' in attrs:
        val = attrs['BusinessParking']
        if val == 'True':
            has_parking = True
        elif val and val.startswith('{'):
            try:
                # Use ast.literal_eval to parse python-like dict string
                parking_dict = ast.literal_eval(val)
                if isinstance(parking_dict, dict):
                    # Check if any value is True
                    if any(v is True for v in parking_dict.values()):
                        has_parking = True
            except:
                pass
                
    if has_bike or has_parking:
        count += 1
        matched_businesses.append(b_ref)

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-17452870736414877789': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}], 'var_function-call-17452870736414875816': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-10961423656352222677': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
