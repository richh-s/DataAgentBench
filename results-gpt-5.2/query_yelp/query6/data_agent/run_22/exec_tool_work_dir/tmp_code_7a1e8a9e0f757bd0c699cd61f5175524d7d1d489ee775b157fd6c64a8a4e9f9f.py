code = """import json

rec = var_call_L6pWHvCvdc8yqRMNtQsf9l7c[0]
desc = rec.get('description') or ''
category = None
# Try to parse categories from description after 'featuring'
if 'featuring' in desc:
    tail = desc.split('featuring',1)[1]
    if 'perfect for' in tail:
        tail = tail.split('perfect for',1)[0]
    category = tail.strip().strip(' ,.')

result = {
    'business_id': rec.get('business_id'),
    'name': rec.get('name'),
    'category': category
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_mpNUhcrF3ULgHTc4eeXekxOT': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'n_reviews': '7'}], 'var_call_L6pWHvCvdc8yqRMNtQsf9l7c': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
