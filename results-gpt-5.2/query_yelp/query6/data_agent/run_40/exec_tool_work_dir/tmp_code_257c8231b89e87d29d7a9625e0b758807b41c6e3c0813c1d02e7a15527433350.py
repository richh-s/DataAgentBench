code = """import json, pandas as pd
rows = var_call_s3zFZyxRybylvGzPzKWAYaPR
biz = var_call_X1OKclCp3I7oXbJZLrudpI5N[0]
# Extract category list from description after 'featuring'
desc = biz.get('description','')
cat = None
if 'featuring' in desc:
    cat_part = desc.split('featuring',1)[1]
    # take until comma 'perfect' if exists
    if 'perfect' in cat_part:
        cat_part = cat_part.split('perfect',1)[0]
    cat_part = cat_part.strip().strip('.')
    cat = cat_part
out = {
    'business_id': biz['business_id'],
    'business_name': biz['name'],
    'avg_rating': float(rows[0]['avg_rating']),
    'review_count_in_period': int(rows[0]['review_cnt']),
    'category': cat
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_s3zFZyxRybylvGzPzKWAYaPR': [{'business_ref': 'businessref_9', 'review_cnt': '7', 'avg_rating': '4.285714285714286'}], 'var_call_X1OKclCp3I7oXbJZLrudpI5N': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
