code = """import json

business = var_call_z3Z1KG247njEduTyRnoRCpTy[0]
desc = business.get('description','')
# categories appear in description as "featuring <cats>, perfect"
cat = None
if 'featuring' in desc and 'perfect' in desc:
    cat = desc.split('featuring',1)[1].split('perfect',1)[0].strip().strip(',')
result = {
    'business_name': business.get('name'),
    'business_id': business.get('business_id'),
    'category': cat,
    'avg_rating': float(var_call_2DJgbzuyuG2i7S364HnI3ImK[0]['avg_rating']),
    'review_count_in_period': int(var_call_2DJgbzuyuG2i7S364HnI3ImK[0]['review_cnt'])
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2DJgbzuyuG2i7S364HnI3ImK': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_z3Z1KG247njEduTyRnoRCpTy': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
