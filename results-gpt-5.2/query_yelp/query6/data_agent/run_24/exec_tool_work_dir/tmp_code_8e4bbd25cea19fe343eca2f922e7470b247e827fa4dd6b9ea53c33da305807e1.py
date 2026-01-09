code = """import json
best = var_call_fHsuGC0JROOkXPiWL0W50Ixb[0]
biz = var_call_mVHGAmRCq8DpZoOYsTzBO2Ac[0]
# categories not a field; parse from description after 'featuring'
desc = biz.get('description','')
cat = None
if 'featuring' in desc:
    part = desc.split('featuring',1)[1]
    # take until comma 'perfect' phrase
    part = part.split('perfect',1)[0]
    cat = part.strip().strip(',').strip('.')
res = {
    'business_name': biz.get('name'),
    'business_id': biz.get('business_id'),
    'avg_rating': float(best['avg_rating']),
    'review_count_in_period': int(best['review_cnt']),
    'category': cat
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_HI723P6mwmBkujmrjOXicVne': [], 'var_call_fHsuGC0JROOkXPiWL0W50Ixb': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_cnt': '7'}], 'var_call_mVHGAmRCq8DpZoOYsTzBO2Ac': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
