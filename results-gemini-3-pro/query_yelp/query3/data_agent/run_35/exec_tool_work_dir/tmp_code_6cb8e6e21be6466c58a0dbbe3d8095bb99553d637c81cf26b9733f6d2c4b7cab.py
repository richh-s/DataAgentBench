code = """import json
import ast

# Load reviews
reviews_2018 = locals()['var_function-call-3256252732933624935']

# Load businesses from file
filepath = locals()['var_function-call-4540959241420737671']
with open(filepath, 'r') as f:
    businesses = json.load(f)

# Get target business IDs
target_business_ids = set()
for r in reviews_2018:
    ref = r['business_ref']
    if ref.startswith('businessref_'):
        bid = 'businessid_' + ref.split('_')[1]
        target_business_ids.add(bid)

print(f"DEBUG: Found {len(target_business_ids)} unique businesses in 2018 reviews.")

# Map businesses
bus_map = {b['business_id']: b for b in businesses}
print(f"DEBUG: Loaded {len(bus_map)} businesses from DB.")

count = 0
found_list = []

for bid in target_business_ids:
    if bid in bus_map:
        b = bus_map[bid]
        attrs = b.get('attributes')
        
        has_p = False
        if not attrs or attrs == 'None':
            pass
        else:
            # Check BikeParking
            if attrs.get('BikeParking') == 'True':
                has_p = True
            
            # Check BusinessParking
            if not has_p:
                bp = attrs.get('BusinessParking')
                if bp:
                    if bp == 'True':
                        has_p = True
                    elif bp.startswith('{'):
                        try:
                            bp_dict = ast.literal_eval(bp)
                            # Check values
                            for k, v in bp_dict.items():
                                if v is True or v == 'True':
                                    has_p = True
                                    break
                        except:
                            pass
        if has_p:
            count += 1
            found_list.append(bid)

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-13623329448438508568': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3256252732933624935': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}], 'var_function-call-11923701340149909913': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_function-call-6523211834709418420': 1, 'var_function-call-10418178213882397321': 1, 'var_function-call-260510515748504392': {'count': 1, 'debug': ['businessid_80: Not found in business collection', 'businessid_66: Not found in business collection', "businessid_47: YES. BusinessParking dict has True ({'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False})", 'businessid_20: Not found in business collection', 'businessid_17: Not found in business collection', 'businessid_73: Not found in business collection', 'businessid_68: Not found in business collection', 'businessid_22: Not found in business collection', 'businessid_57: Not found in business collection', 'businessid_77: Not found in business collection', 'businessid_14: Not found in business collection', 'businessid_25: Not found in business collection', 'businessid_27: Not found in business collection', 'businessid_82: Not found in business collection', 'businessid_83: Not found in business collection', 'businessid_99: Not found in business collection', 'businessid_46: Not found in business collection', 'businessid_79: Not found in business collection', 'businessid_35: Not found in business collection', 'businessid_28: Not found in business collection', 'businessid_59: Not found in business collection', 'businessid_8: Not found in business collection', 'businessid_26: Not found in business collection', 'businessid_36: Not found in business collection', 'businessid_91: Not found in business collection', 'businessid_62: Not found in business collection', 'businessid_45: Not found in business collection', 'businessid_67: Not found in business collection', 'businessid_86: Not found in business collection', 'businessid_40: Not found in business collection', 'businessid_24: Not found in business collection', 'businessid_15: Not found in business collection', 'businessid_37: Not found in business collection', 'businessid_4: Not found in business collection', 'businessid_13: Not found in business collection']}, 'var_function-call-11146877226261132838': 5, 'var_function-call-4540959241420737671': 'file_storage/function-call-4540959241420737671.json'}

exec(code, env_args)
