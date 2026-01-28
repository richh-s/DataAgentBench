code = """import json
import pandas as pd

r = pd.DataFrame(var_call_n1ja5Wsiiy2NZGoyIa1Ft3f1).iloc[0].to_dict()
b = var_call_y9GRfX9jr5OmVxit6gnZtd1S[0]

# Category appears embedded in description after 'featuring'
desc = b.get('description','')
cat = None
if 'featuring' in desc:
    cat = desc.split('featuring',1)[1].strip().rstrip('.')

out = {
    'business_id': b.get('business_id'),
    'name': b.get('name'),
    'avg_rating': float(r['avg_rating']),
    'review_count_in_period': int(r['review_cnt']),
    'category': cat
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_n1ja5Wsiiy2NZGoyIa1Ft3f1': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_y9GRfX9jr5OmVxit6gnZtd1S': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
