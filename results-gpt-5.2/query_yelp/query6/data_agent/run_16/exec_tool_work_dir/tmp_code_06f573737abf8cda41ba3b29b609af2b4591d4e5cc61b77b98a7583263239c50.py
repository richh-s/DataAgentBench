code = """import json, re

rec = var_call_vHq3DgeNuyGkrlHHnjhYPACd[0]
desc = rec.get('description','')
# categories appear after 'featuring'
cat = None
m = re.search(r"featuring\s+(.+?),\s+perfect", desc)
if m:
    cat = m.group(1).strip()
else:
    # fallback: after 'menu featuring'
    m = re.search(r"menu featuring\s+(.+?)\.", desc)
    if m:
        cat = m.group(1).strip()

out = {
    "business_id": rec.get('business_id'),
    "name": rec.get('name'),
    "category": cat,
    "avg_rating": float(var_call_lJg53GxHZMQjVWg9ivLKhCkB[0]['avg_rating']),
    "review_count_in_period": int(var_call_lJg53GxHZMQjVWg9ivLKhCkB[0]['review_cnt'])
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lJg53GxHZMQjVWg9ivLKhCkB': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_vHq3DgeNuyGkrlHHnjhYPACd': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
