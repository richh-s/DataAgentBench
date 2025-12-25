code = """import ast

reviews_2018 = locals()['var_function-call-17353121157768695018']
businesses = locals()['var_function-call-12881833137496584056']

reviewed_ids = set()
for r in reviews_2018:
    if r['business_ref']:
        reviewed_ids.add(r['business_ref'].replace('businessref', 'businessid'))

print("Number of reviewed businesses:", len(reviewed_ids))
print("Sample reviewed IDs:", list(reviewed_ids)[:5])

found_count = 0
details = []

for b in businesses:
    bid = b.get('business_id')
    if bid in reviewed_ids:
        attrs = b.get('attributes')
        # Check details
        bike = None
        bus_park = None
        has_park = False
        
        if isinstance(attrs, dict):
            bike = attrs.get('BikeParking')
            bus_park = attrs.get('BusinessParking')
            
            # Check Bike
            if bike and str(bike).lower() == 'true':
                has_park = True
            
            # Check Bus
            if not has_park and bus_park:
                if str(bus_park).lower() == 'true':
                    has_park = True
                elif isinstance(bus_park, str) and bus_park.startswith('{'):
                    try:
                        park_dict = ast.literal_eval(bus_park)
                        if any(v is True for v in park_dict.values()):
                            has_park = True
                    except:
                        pass

        if has_park:
            found_count += 1
        
        details.append({
            "id": bid,
            "attrs": attrs,
            "has_park": has_park
        })

print("Found matching businesses:", found_count)
print("__RESULT__:")
import json
print(json.dumps(details[:10])) # Print first 10 for inspection"""

env_args = {'var_function-call-17353121157768695018': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}], 'var_function-call-17353121157768694959': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-12881833137496584056': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}], 'var_function-call-13449753231358829280': 1}

exec(code, env_args)
