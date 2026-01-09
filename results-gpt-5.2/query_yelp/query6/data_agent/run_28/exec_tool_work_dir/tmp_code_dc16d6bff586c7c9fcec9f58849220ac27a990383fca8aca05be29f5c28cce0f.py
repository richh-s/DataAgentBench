code = """import json, re
rec = var_call_ViBQnMIbGAw20mOThQEkOnzk[0]
desc = rec.get('description','') or ''
# try to extract category list after 'featuring'
cat = None
m = re.search(r"featuring\s+(.+?),\s+perfect", desc, flags=re.IGNORECASE)
if m:
    cat = m.group(1).strip()
else:
    # fallback: take after 'menu featuring'
    m2 = re.search(r"menu featuring\s+(.+?)\.", desc, flags=re.IGNORECASE)
    if m2:
        cat = m2.group(1).strip()
result = {
  "business_id": rec.get('business_id'),
  "name": rec.get('name'),
  "category": cat
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TOv2lHL0KdizIz3xcRrdnDPg': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_ViBQnMIbGAw20mOThQEkOnzk': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
