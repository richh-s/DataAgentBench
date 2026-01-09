code = """import json, pandas as pd
best = var_call_4RNg6qqRjoEiOH7v3vcgI8uG[0]
biz = var_call_uqeeuWLtjf1B6vPS44MsJSoY[0]
# category: parse from description after 'featuring'
desc = biz.get('description','')
cat = None
if 'featuring' in desc:
    cat_part = desc.split('featuring',1)[1]
    if 'perfect for' in cat_part:
        cat_part = cat_part.split('perfect for',1)[0]
    cat = cat_part.strip().strip(',').strip()
result = {
    'business_id': biz.get('business_id'),
    'name': biz.get('name'),
    'category': cat,
    'avg_rating': float(best['avg_rating']),
    'review_count_in_period': int(best['review_ct'])
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2gUDVXUEYB09kPQci20jdLBX': [], 'var_call_T6oKEbcLWonFvIZJKsJtcwPY': [{'business_ref': 'businessref_34', 'date': 'August 01, 2016 at 03:44 AM', 'rating': '2'}, {'business_ref': 'businessref_89', 'date': 'June 14, 2021 at 11:39 AM', 'rating': '5'}, {'business_ref': 'businessref_82', 'date': '29 May 2013, 23:01', 'rating': '4'}, {'business_ref': 'businessref_66', 'date': '21 May 2016, 18:48', 'rating': '2'}, {'business_ref': 'businessref_95', 'date': 'November 01, 2021 at 05:11 PM', 'rating': '1'}], 'var_call_4RNg6qqRjoEiOH7v3vcgI8uG': [{'business_ref': 'businessref_9', 'avg_rating': '4.545454545454546', 'review_ct': '11'}], 'var_call_uqeeuWLtjf1B6vPS44MsJSoY': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
