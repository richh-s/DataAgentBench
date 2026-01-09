code = """import json
import pandas as pd

df_top = pd.DataFrame(var_call_y22unO44jn0j7h7ZTniOmsO8)
df_biz = pd.DataFrame(var_call_RC8JYQ9N24VFVqjGPKB1GeTT)

avg_rating = float(df_top.loc[0,'avg_rating'])
review_count = int(df_top.loc[0,'review_count'])
name = df_biz.loc[0,'name']
description = df_biz.loc[0,'description']

# category appears embedded in description after 'featuring'
category = None
if isinstance(description, str) and 'featuring' in description:
    category = description.split('featuring',1)[1].split(', perfect',1)[0].strip()

out = {
    'business_name': name,
    'business_ref': df_top.loc[0,'business_ref'],
    'avg_rating': avg_rating,
    'review_count': review_count,
    'category': category
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_y22unO44jn0j7h7ZTniOmsO8': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_count': '5'}], 'var_call_RC8JYQ9N24VFVqjGPKB1GeTT': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
