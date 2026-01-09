code = """import json
biz = var_call_levHe9gnyGIzfRaZtPskgC8S[0]
desc = biz.get('description','')
cat = None
if isinstance(desc,str) and 'featuring' in desc:
    cat = desc.split('featuring',1)[1].split('perfect for',1)[0].strip().strip(',').strip()
out = {
  'business_name': biz.get('name'),
  'business_id': biz.get('business_id'),
  'category': cat,
  'avg_rating_2016_01_01_to_2016_06_30': float(var_call_cg7kH02blaqwlcUJkhZ4tpSq[0]['avg_rating']),
  'review_count_in_period': int(var_call_cg7kH02blaqwlcUJkhZ4tpSq[0]['review_cnt'])
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cg7kH02blaqwlcUJkhZ4tpSq': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_levHe9gnyGIzfRaZtPskgC8S': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
