code = """import json, re
rec = var_call_gwdliZDTfRcRJZb9dmk1ks5N[0]
desc = rec.get('description') or ''
# Extract categories from "featuring ... , perfect" pattern
m = re.search(r"featuring\s+(.*?),\s*perfect", desc, flags=re.IGNORECASE)
cat = m.group(1).strip() if m else None
out = {
  'business_id': rec.get('business_id'),
  'name': rec.get('name'),
  'category': cat,
  'avg_rating': float(var_call_pLbWN2lGhcJaoQ9dyUqcTpi0[0]['avg_rating']),
  'review_count': int(var_call_pLbWN2lGhcJaoQ9dyUqcTpi0[0]['review_count'])
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_pLbWN2lGhcJaoQ9dyUqcTpi0': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_count': '7'}], 'var_call_gwdliZDTfRcRJZb9dmk1ks5N': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
