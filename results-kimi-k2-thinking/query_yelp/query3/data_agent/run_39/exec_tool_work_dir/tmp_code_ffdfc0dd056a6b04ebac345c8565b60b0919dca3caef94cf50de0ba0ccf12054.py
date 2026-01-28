code = """import json

# Access the stored results
business_data = locals()['var_functions.query_db:18']
review_data = locals()['var_functions.query_db:2']

# Get all unique business references from 2018 reviews
business_refs_2018 = set()
for record in review_data:
    business_refs_2018.add(record['business_ref'])

# Convert to business_id format for comparison
business_ids_2018 = set()
for ref in business_refs_2018:
    if ref.startswith('businessref_'):
        num = ref.split('_')[1]
        business_ids_2018.add(f'businessid_{num}')

# Check which businesses have parking info and if they offer parking
count_with_parking = 0
parking_details = []

for business in business_data:
    business_id = business['business_id']
    if business_id not in business_ids_2018:
        continue
    
    attributes = business.get('attributes', {})
    if not attributes:
        continue
    
    # Check BusinessParking
    has_business_parking = False
    business_parking = attributes.get('BusinessParking')
    if business_parking and str(business_parking) not in ['None', 'False', 'null']:
        # Check if it's a dict with any True values
        if isinstance(business_parking, str) and business_parking.startswith('{'):
            try:
                parking_dict = eval(business_parking)
                if isinstance(parking_dict, dict) and any(parking_dict.values()):
                    has_business_parking = True
            except:
                # If parsing fails, count it
                has_business_parking = True
        else:
            has_business_parking = True
    
    # Check BikeParking
    has_bike_parking = False
    bike_parking = attributes.get('BikeParking')
    if bike_parking and str(bike_parking).lower() == 'true':
        has_bike_parking = True
    
    if has_business_parking or has_bike_parking:
        count_with_parking += 1
        parking_details.append({
            'business_id': business_id,
            'business_parking': has_business_parking,
            'bike_parking': has_bike_parking,
            'raw_business_parking': str(business_parking) if business_parking else None,
            'raw_bike_parking': str(bike_parking) if bike_parking else None
        })

print('__RESULT__:')
print(json.dumps({
    'total_businesses_with_2018_reviews': len(business_ids_2018),
    'businesses_with_parking_data': len(business_data),
    'businesses_offering_parking': count_with_parking,
    'details': parking_details
}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'business_ref': 'businessref_77'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_43'}], 'var_functions.execute_python:6': {'unique_business_refs_count': 36, 'sample_business_refs': ['businessref_86', 'businessref_15', 'businessref_80', 'businessref_22', 'businessref_14', 'businessref_17', 'businessref_47', 'businessref_46', 'businessref_68', 'businessref_20']}, 'var_functions.execute_python:8': {'business_numbers_count': 36, 'business_numbers_list': ['27', '15', '22', '47', '8', '66', '57', '4', '77', '37', '80', '59', '82', '24', '13', '25', '91', '83', '28', '40']}, 'var_functions.query_db:10': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}], 'var_functions.query_db:12': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}], 'var_functions.execute_python:14': {'count': 3, 'businesses': [{'business_id': 'businessid_47', 'business_parking': True, 'bike_parking': False}, {'business_id': 'businessid_59', 'business_parking': True, 'bike_parking': False}, {'business_id': 'businessid_91', 'business_parking': True, 'bike_parking': True}]}, 'var_functions.query_db:16': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8'}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83'}], 'var_functions.query_db:18': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'attributes': {'BusinessParking': 'None'}}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'attributes': {'BikeParking': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}"}}]}

exec(code, env_args)
