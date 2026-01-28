code = """import json
rows = var_call_EFCG5BahPwDg9ljk26qkzKIG
rev = var_call_60wKzhzf3HOqPHUQM4suAzcT[0]
rec = rows[0]
# category appears embedded in description after 'featuring'
desc = rec.get('description','')
cat = None
if 'featuring' in desc:
    cat = desc.split('featuring',1)[1].split('perfect for',1)[0].strip().strip(',')
out = {
    'business_id': rec['business_id'],
    'name': rec['name'],
    'avg_rating': float(rev['avg_rating']),
    'review_cnt': int(rev['review_cnt']),
    'category': cat
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Uyznxzip3T2nUsMipR2DqaZ5': ['business', 'checkin'], 'var_call_vzskPRhC8A2w2Ev8MWkgK7Ll': [], 'var_call_60wKzhzf3HOqPHUQM4suAzcT': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_cnt': '7'}], 'var_call_EFCG5BahPwDg9ljk26qkzKIG': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
