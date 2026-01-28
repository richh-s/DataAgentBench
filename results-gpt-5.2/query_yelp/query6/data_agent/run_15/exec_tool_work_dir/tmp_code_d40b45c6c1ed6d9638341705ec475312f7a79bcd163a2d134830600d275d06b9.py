code = """import json, pandas as pd

r = var_call_5BTrEur6JZjEVoxju0JQIJ52[0]
b = var_call_szXXiXu7mHQS8rSKqpJrPOQv[0]

# category is embedded in description after 'featuring '
desc = b.get('description','')
cat = None
marker = 'featuring '
if marker in desc:
    cat_part = desc.split(marker,1)[1]
    if ', perfect' in cat_part:
        cat_part = cat_part.split(', perfect',1)[0]
    cat = cat_part.strip().rstrip('.')

out = {
    'business_id': b['business_id'],
    'business_name': b['name'],
    'category': cat,
    'avg_rating': float(r['avg_rating']),
    'review_count_in_period': int(r['review_cnt'])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5BTrEur6JZjEVoxju0JQIJ52': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_szXXiXu7mHQS8rSKqpJrPOQv': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
