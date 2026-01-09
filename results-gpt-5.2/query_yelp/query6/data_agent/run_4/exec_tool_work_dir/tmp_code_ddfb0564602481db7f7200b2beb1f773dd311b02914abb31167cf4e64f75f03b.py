code = """import json, pandas as pd, re
row = var_call_Y7HZBSibHcSqGVU99JI6HUVm[0]
desc = row.get('description','') or ''
# Category list appears in description like: "featuring Restaurants, Breakfast & Brunch, American (New), Cafes,"
cat = None
m = re.search(r"featuring\s+(.+?),\s*perfect", desc)
if m:
    cats = [c.strip() for c in m.group(1).split(',') if c.strip()]
    cat = cats[0] if cats else None
# fallback: first capitalized word sequence after 'featuring'
if not cat:
    m2 = re.search(r"featuring\s+([^,]+)", desc)
    if m2:
        cat = m2.group(1).strip()
result = {
    "business": row.get('name'),
    "category": cat,
    "business_id": row.get('business_id')
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bI9S8dP7vj8zBlsnwzZsv0eC': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_cnt': '7'}], 'var_call_Y7HZBSibHcSqGVU99JI6HUVm': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
