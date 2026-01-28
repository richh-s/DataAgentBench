code = """import json, pandas as pd
from ast import literal_eval

best = pd.DataFrame(var_call_NLo5uuNFI5syCxUzAzv043j4).iloc[0].to_dict()
biz = var_call_td3dj84Cy9fpOevAEnEfMnvH[0]

desc = biz.get('description','')
# categories appear after 'featuring'
cat = None
if 'featuring' in desc:
    cat = desc.split('featuring',1)[1].split(', perfect',1)[0].strip()

out = {
    'business_name': biz.get('name'),
    'business_id': biz.get('business_id'),
    'avg_rating': float(best['avg_rating']),
    'review_count_in_period': int(best['review_cnt']),
    'category': cat
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NLo5uuNFI5syCxUzAzv043j4': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_fhlxRuyFFp84zltktEfioNE7': ['checkin', 'business'], 'var_call_td3dj84Cy9fpOevAEnEfMnvH': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
