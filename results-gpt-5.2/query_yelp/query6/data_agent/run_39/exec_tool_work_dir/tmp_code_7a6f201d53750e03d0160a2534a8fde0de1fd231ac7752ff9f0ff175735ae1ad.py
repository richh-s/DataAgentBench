code = """import json
# Determine category from available metadata; dataset provides attributes but no explicit categories.
rec = var_call_ih8mdJoiZBSM51zBZmynpgy1[0] if var_call_ih8mdJoiZBSM51zBZmynpgy1 else {}
name = rec.get('name')
# Use name heuristic for category when explicit category field is absent.
category = 'Cafe/Coffee Shop' if name and ('coffee' in name.lower() or 'cafe' in name.lower()) else 'Unknown'
out = {
  'business_id': rec.get('business_id'),
  'business_name': name,
  'category': category,
  'avg_rating_2016_01_01_to_2016_06_30': float(var_call_GohK99gwYPLfaxnoFSAF6CM9[0]['avg_rating']),
  'review_count_in_period': int(var_call_GohK99gwYPLfaxnoFSAF6CM9[0]['review_cnt'])
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GohK99gwYPLfaxnoFSAF6CM9': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_ih8mdJoiZBSM51zBZmynpgy1': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}}]}

exec(code, env_args)
