code = """import json
import ast

reviews_2018 = locals()['var_function-call-3256252732933624935']
businesses = locals()['var_function-call-11923701340149909913']

target_business_ids = set()
for r in reviews_2018:
    ref = r['business_ref']
    if ref.startswith('businessref_'):
        bid = 'businessid_' + ref.split('_')[1]
        target_business_ids.add(bid)

print(f"Target IDs: {target_business_ids}")

count = 0
for b in businesses:
    bid = b.get('business_id')
    if bid in target_business_ids:
        attrs = b.get('attributes')
        if not attrs or attrs == 'None':
            print(f"Business {bid}: No attributes")
            continue
        
        has_p = False
        
        # Check BikeParking
        bp_bike = attrs.get('BikeParking')
        if bp_bike == 'True':
            has_p = True
            print(f"Business {bid}: BikeParking=True")
        
        # Check BusinessParking
        bp_bus = attrs.get('BusinessParking')
        if bp_bus:
            if bp_bus == 'True':
                has_p = True
                print(f"Business {bid}: BusinessParking=True")
            elif bp_bus.startswith('{'):
                try:
                    bp_dict = ast.literal_eval(bp_bus)
                    # Check values
                    found_in_dict = False
                    for k, v in bp_dict.items():
                        if v is True or v == 'True':
                            found_in_dict = True
                            break
                    if found_in_dict:
                        has_p = True
                        print(f"Business {bid}: BusinessParking dict has True ({bp_dict})")
                except Exception as e:
                    print(f"Business {bid}: Failed to parse BusinessParking: {bp_bus} error: {e}")

        if has_p:
            count += 1
        else:
            print(f"Business {bid}: No parking found. Attrs: {attrs}")

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-13623329448438508568': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3256252732933624935': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}], 'var_function-call-11923701340149909913': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_function-call-6523211834709418420': 1}

exec(code, env_args)
