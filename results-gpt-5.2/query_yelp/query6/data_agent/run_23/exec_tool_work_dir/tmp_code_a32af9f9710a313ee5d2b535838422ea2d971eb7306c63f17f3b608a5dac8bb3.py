code = """import json, pandas as pd

best = var_call_K9bewGEpW88HWr7JVCy1E2Yg[0]
biz = var_call_4O0WBDImepxt2uQdlqCRoCXZ[0]

desc = biz.get('description','') or ''
# category appears in description after 'featuring '
category = None
marker = 'featuring '
if marker in desc:
    category = desc.split(marker,1)[1].split(', perfect',1)[0].strip()

out = {
    'business_id': biz.get('business_id'),
    'business_ref': best.get('business_ref'),
    'name': biz.get('name'),
    'category': category,
    'avg_rating': float(best.get('avg_rating')),
    'review_count_in_period': int(best.get('review_cnt'))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_K9bewGEpW88HWr7JVCy1E2Yg': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_4O0WBDImepxt2uQdlqCRoCXZ': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
