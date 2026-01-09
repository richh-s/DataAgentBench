code = """import json, re

biz = var_call_gxeBKfUIqyD6KAxyJbLLSg5K[0]
desc = biz.get('description') or ''
# Try to parse categories from description after 'featuring'
cats = None
m = re.search(r'featuring\s+([^,].*?)\s*,\s*perfect for', desc, flags=re.IGNORECASE)
if m:
    cats = [c.strip() for c in m.group(1).split(',') if c.strip()]
category = cats[0] if cats else None

out = {
  'business_id': biz.get('business_id'),
  'name': biz.get('name'),
  'category': category,
  'review_cnt': int(var_call_8sydvpxO5DfEJVVKRdFdEUNR[0]['review_cnt']),
  'avg_rating': float(var_call_8sydvpxO5DfEJVVKRdFdEUNR[0]['avg_rating'])
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8sydvpxO5DfEJVVKRdFdEUNR': [{'business_ref': 'businessref_9', 'review_cnt': '7', 'avg_rating': '4.285714285714286'}], 'var_call_gxeBKfUIqyD6KAxyJbLLSg5K': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
