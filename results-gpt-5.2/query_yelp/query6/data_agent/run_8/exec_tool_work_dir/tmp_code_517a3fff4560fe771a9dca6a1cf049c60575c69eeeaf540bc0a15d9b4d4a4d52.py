code = """import json, pandas as pd, re, ast
rec = var_call_VT7sUl6mrVfCEZ8azPHyMLad[0]
desc = rec.get('description') or ''
# Category appears as a comma-separated list after 'featuring'
cat = None
m = re.search(r"featuring\s+(.+?),\s*perfect", desc, flags=re.IGNORECASE)
if m:
    cat = m.group(1).strip()
result = {
    "business_id": rec.get('business_id'),
    "name": rec.get('name'),
    "category": cat,
    "avg_rating": float(var_call_vFXMXbmy3Go9t5TC5c44EgXC[0]['avg_rating']),
    "review_count_in_period": int(var_call_vFXMXbmy3Go9t5TC5c44EgXC[0]['review_ct']),
    "date_range": "2016-01-01 to 2016-06-30"
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vFXMXbmy3Go9t5TC5c44EgXC': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_ct': '5'}], 'var_call_VT7sUl6mrVfCEZ8azPHyMLad': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
