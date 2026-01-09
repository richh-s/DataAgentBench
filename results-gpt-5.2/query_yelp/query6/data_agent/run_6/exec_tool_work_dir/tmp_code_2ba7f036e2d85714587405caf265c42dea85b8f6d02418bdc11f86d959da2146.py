code = """import json, pandas as pd, re, ast
rec = var_call_JlPwmEGJezAqNvag6cYAleUV[0]
desc = rec.get('description','') or ''
# categories appear after 'featuring '
cats = None
m = re.search(r"featuring\s+(.+?),\s+perfect", desc)
if m:
    cats = [c.strip() for c in m.group(1).split(',') if c.strip()]
else:
    # fallback: try after 'menu featuring'
    m2 = re.search(r"menu featuring\s+(.+?)\.", desc)
    if m2:
        cats = [c.strip() for c in m2.group(1).split(',') if c.strip()]
category = cats[0] if cats else None
out = {
    "business_id": rec.get('business_id'),
    "name": rec.get('name'),
    "avg_rating": float(var_call_PXZ4IO7Sg7LEMTdX9krKEZn1[0]['avg_rating']),
    "review_cnt": int(var_call_PXZ4IO7Sg7LEMTdX9krKEZn1[0]['review_cnt']),
    "category": category,
    "all_categories": cats
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PXZ4IO7Sg7LEMTdX9krKEZn1': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_JlPwmEGJezAqNvag6cYAleUV': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
