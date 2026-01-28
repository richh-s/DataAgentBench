code = """import json, pandas as pd

row = var_call_96w2auj6LNRUlMcGKPxQ6e1s[0]
biz = var_call_CEM8D8dM61sIb8pRv1IDDGfg[0]

# category appears embedded in description after 'featuring'
desc = biz.get('description','')
category = None
if 'featuring' in desc:
    category = desc.split('featuring',1)[1].split(', perfect',1)[0].strip()

out = {
    'business_id': biz.get('business_id'),
    'business_name': biz.get('name'),
    'avg_rating': float(row['avg_rating']),
    'review_count_in_period': int(row['review_cnt']),
    'category': category
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_96w2auj6LNRUlMcGKPxQ6e1s': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_CEM8D8dM61sIb8pRv1IDDGfg': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
