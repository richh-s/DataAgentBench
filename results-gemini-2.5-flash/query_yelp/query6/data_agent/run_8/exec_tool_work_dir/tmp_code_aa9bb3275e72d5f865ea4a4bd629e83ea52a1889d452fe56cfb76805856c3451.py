code = """import json
business_info = json.loads(locals()['var_function-call-8933065007515214609'])['results'][0]
business_name = business_info['name']
description = business_info['description']
# Extract categories from the description string
start_index = description.find('featuring ') + len('featuring ')
end_index = description.find(', perfect for a cozy meal any time of the day.')
categories_str = description[start_index:end_index]
categories = [cat.strip() for cat in categories_str.split(', ')]
print('__RESULT__:')
print(json.dumps({'business_name': business_name, 'categories': categories}))"""

env_args = {'var_function-call-15664062049855015023': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_count': '5'}], 'var_function-call-8933065007515214609': [{'_id': '6859a000fe8b31cd7362e2f3', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
