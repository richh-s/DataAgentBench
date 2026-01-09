code = """import json, re
rec = var_call_StR0fG8xdUaCewiWm1S6aHPr[0]
biz = var_call_T56vhptIqblOiT9F0OAaaB3f[0]
# Extract categories from description after 'featuring'
desc = biz.get('description','')
cat = None
m = re.search(r"featuring\s+(.+?)(?:,\s*perfect|\.|$)", desc, flags=re.I)
if m:
    cat = m.group(1).strip()
result = {
    "business_id": biz.get('business_id'),
    "business_ref": rec.get('business_ref'),
    "name": biz.get('name'),
    "category": cat,
    "avg_rating": float(rec.get('avg_rating')),
    "review_count_in_period": int(rec.get('review_cnt')),
    "period": "2016-01-01 to 2016-06-30"
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_StR0fG8xdUaCewiWm1S6aHPr': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_T56vhptIqblOiT9F0OAaaB3f': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '7:0-15:0', 'Tuesday': '7:0-15:0', 'Wednesday': '7:0-15:0', 'Thursday': '7:0-15:0', 'Friday': '7:0-15:0', 'Saturday': '8:30-15:0', 'Sunday': '8:30-15:0'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
