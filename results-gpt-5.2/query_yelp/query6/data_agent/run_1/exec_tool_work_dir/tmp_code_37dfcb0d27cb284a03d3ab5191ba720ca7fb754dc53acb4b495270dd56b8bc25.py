code = """import json

# inputs
rec = var_call_2tPeDtdhMyVwfPcQriO9Mnmm[0]
biz = var_call_zZumVZDhGgUMhFYi3GSg2cfo[0]

# category: parse from description after 'featuring'
desc = biz.get('description') or ''
category = None
marker = 'featuring '
if marker in desc:
    tail = desc.split(marker, 1)[1]
    category = tail.split(', perfect', 1)[0].strip().rstrip('.')

out = {
    'business_id': biz.get('business_id'),
    'business_name': biz.get('name'),
    'category': category,
    'avg_rating': float(rec['avg_rating']),
    'review_count_in_period': int(rec['review_cnt'])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_2tPeDtdhMyVwfPcQriO9Mnmm': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_cnt': '7'}], 'var_call_zZumVZDhGgUMhFYi3GSg2cfo': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
