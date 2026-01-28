code = """import json, pandas as pd
best = var_call_3BzvP5JZaIhjn2xCp7DYucBp[0]
biz = var_call_odM1NlSK4fNGPgNwIPeS6ZGM[0]
# infer category from description (comma-separated list after 'featuring')
desc = biz.get('description','')
cat = None
if 'featuring' in desc:
    after = desc.split('featuring',1)[1]
    # take up to ', perfect' if present
    after = after.split(', perfect',1)[0]
    cat = after.strip().strip('.')
result = {
    'business_name': biz.get('name'),
    'business_id': biz.get('business_id'),
    'category': cat,
    'avg_rating': float(best['avg_rating']),
    'review_count_in_period': int(best['review_cnt']),
    'period': '2016-01-01 to 2016-06-30'
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3BzvP5JZaIhjn2xCp7DYucBp': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_odM1NlSK4fNGPgNwIPeS6ZGM': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
