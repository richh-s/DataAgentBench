code = """import json, pandas as pd
r = var_call_Kj6Y9zirwWlYQLO23wUgt7qi[0]
b = var_call_Ns9hgxLzuUJTTi6FoebfHXs5[0]
# Category appears embedded in description after 'featuring'
desc = b.get('description','')
category = None
if 'featuring' in desc:
    category = desc.split('featuring',1)[1].split(', perfect',1)[0].strip()
answer = {
  'business_name': b.get('name'),
  'business_id': b.get('business_id'),
  'category': category,
  'avg_rating': float(r['avg_rating']),
  'review_count_in_period': int(r['review_ct']),
  'period': '2016-01-01 to 2016-06-30'
}
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_Kj6Y9zirwWlYQLO23wUgt7qi': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_ct': '5'}], 'var_call_Ns9hgxLzuUJTTi6FoebfHXs5': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
