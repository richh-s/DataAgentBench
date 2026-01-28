code = """import json

# Access the business data with attributes
business_data = var_functions.query_db:14

# Count businesses that offer either business parking or bike parking
count = 0
eligible_businesses = []

for business in business_data:
    has_business_parking = False
    has_bike_parking = False
    
    attributes = business.get('attributes', {})
    
    # Check for business parking
    if 'BusinessParking' in attributes:
        bp = attributes['BusinessParking']
        # If it's a dictionary/string representation and not "None"
        if bp != 'None' and bp != None and bp != '':
            has_business_parking = True
    
    # Check for bike parking
    if 'BikeParking' in attributes:
        bike_parking = attributes['BikeParking']
        if bike_parking == 'True':
            has_bike_parking = True
    
    # If either is true, count it
    if has_business_parking or has_bike_parking:
        count += 1
        eligible_businesses.append({
            'business_id': business['business_id'],
            'has_business_parking': has_business_parking,
            'has_bike_parking': has_bike_parking,
            'attributes': attributes
        })

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'businesses': eligible_businesses
}, indent=2))"""

env_args = {'var_functions.query_db:0': [{'date': '2018-02-19 14:12:00'}, {'date': '2018-08-12 15:51:00'}, {'date': '2018-06-02 14:52:00'}, {'date': '2018-07-09 02:34:16'}, {'date': '2018-12-08 19:50:00'}], 'var_functions.query_db:2': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}], 'var_functions.execute_python:12': ['businessid_13', 'businessid_79', 'businessid_80', 'businessid_82', 'businessid_35', 'businessid_45', 'businessid_59', 'businessid_77', 'businessid_27', 'businessid_86'], 'var_functions.query_db:14': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'attributes': {'BusinessAcceptsCreditCards': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b9', 'business_id': 'businessid_59', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsTakeOut': 'None', 'RestaurantsDelivery': 'None', 'HasTV': 'True', 'Ambience': "{'touristy': False, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': None, 'trendy': None, 'upscale': False, 'classy': None, 'casual': True}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}"}}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'attributes': {'RestaurantsPriceRange2': '2', 'AcceptsInsurance': 'True', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': 'None', 'ByAppointmentOnly': 'False'}}]}

exec(code, env_args)
