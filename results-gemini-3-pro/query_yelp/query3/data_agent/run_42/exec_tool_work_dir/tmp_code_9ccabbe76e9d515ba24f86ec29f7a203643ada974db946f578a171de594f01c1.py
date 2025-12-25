code = """import pandas as pd
import ast
import json

# Load data
reviewed_data = locals()['var_function-call-6932898484997511621']
business_data = locals()['var_function-call-13920892638362114968']

# Check if business_data is a file path (str) or list
if isinstance(business_data, str) and business_data.endswith('.json'):
    with open(business_data, 'r') as f:
        business_data = json.load(f)
        
# Check reviewed_data similarly
if isinstance(reviewed_data, str) and reviewed_data.endswith('.json'):
    with open(reviewed_data, 'r') as f:
        reviewed_data = json.load(f)

# Get set of reviewed business IDs (normalized)
reviewed_ids = set()
for item in reviewed_data:
    ref = item['business_ref']
    # Convert businessref_X to businessid_X
    # Assuming the format is strictly replacing the prefix
    bid = ref.replace('businessref_', 'businessid_')
    reviewed_ids.add(bid)

count = 0

for biz in business_data:
    bid = biz.get('business_id')
    if bid not in reviewed_ids:
        continue
        
    attrs = biz.get('attributes')
    if not attrs or attrs == 'None':
        continue
    
    # If attributes is a string that looks like a dict, try to parse it (though the preview shows it as a dict object in the list, except where it is "None")
    # Wait, the preview showed: "attributes": {"BusinessAcceptsCreditCards": "True", ...}
    # But one entry was "attributes": "None".
    # So if it's a dict, we use it. If it's a string != "None", we might need to parse, but likely it's handled by the db_query tool as json.
    
    if isinstance(attrs, str):
        # This case handles "attributes": "None" or potential parsing issues if it came as string
        if attrs == 'None':
            continue
        try:
            attrs = ast.literal_eval(attrs)
        except:
            continue
            
    if not isinstance(attrs, dict):
        continue

    # Check Bike Parking
    has_bike = False
    bike_val = attrs.get('BikeParking')
    # Values seen: "True", "False", maybe u'True'
    if bike_val == 'True' or bike_val is True:
        has_bike = True
        
    # Check Business Parking
    has_parking = False
    park_val = attrs.get('BusinessParking')
    
    if park_val:
        if park_val == 'True' or park_val is True:
            has_parking = True
        elif isinstance(park_val, str) and park_val.startswith('{'):
            try:
                park_dict = ast.literal_eval(park_val)
                if isinstance(park_dict, dict):
                    # Check if any value is True
                    # The dictionary values in the string are usually Booleans (True/False)
                    if any(v is True for v in park_dict.values()):
                        has_parking = True
            except:
                pass
        elif isinstance(park_val, dict):
             if any(v is True for v in park_val.values()):
                 has_parking = True

    if has_bike or has_parking:
        count += 1

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-6932898484997511621': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_function-call-13920892638362114968': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
