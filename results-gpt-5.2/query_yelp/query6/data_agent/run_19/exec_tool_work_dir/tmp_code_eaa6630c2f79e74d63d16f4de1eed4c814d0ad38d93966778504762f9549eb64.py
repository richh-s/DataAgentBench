code = """import json, re
best = var_call_16FbnSkPtSYIxLcANLSKXcmd[0]
biz = var_call_p9OPqTtHLDFvNf3RuqUDuI5i[0]
# extract categories from description: 'featuring ... , perfect'
desc = biz.get('description','')
cat = None
m = re.search(r'featuring (.*?),\s*perfect', desc)
if m:
    cat = m.group(1).strip()
result = {
  'business_id': biz.get('business_id'),
  'name': biz.get('name'),
  'avg_rating': float(best['avg_rating']),
  'review_count_in_period': int(best['review_cnt']),
  'category': cat
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_16FbnSkPtSYIxLcANLSKXcmd': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_cnt': '7'}], 'var_call_p9OPqTtHLDFvNf3RuqUDuI5i': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
