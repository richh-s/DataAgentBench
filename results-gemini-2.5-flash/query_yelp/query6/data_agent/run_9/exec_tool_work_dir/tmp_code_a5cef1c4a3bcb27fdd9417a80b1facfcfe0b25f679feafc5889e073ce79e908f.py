code = """import json

business_info_list_str = locals()['var_function-call-8330808566102405408']['results'][0]
business_info = json.loads(business_info_list_str)[0]
description = business_info['description']

start_index = description.find('featuring')
end_index = description.find(', perfect for a cozy meal')

if start_index != -1 and end_index != -1:
    categories_str = description[start_index + len('featuring') : end_index].strip()
    categories = categories_str
else:
    categories = "Category information not found"

review_details_list_str = locals()['var_function-call-2411167914170131885']['results'][0]
review_details = json.loads(review_details_list_str)[0]

final_result = {
    "business_ref": review_details['business_ref'],
    "average_rating": float(review_details['average_rating']),
    "review_count": int(review_details['review_count']),
    "category": categories
}

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-2411167914170131885': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-8330808566102405408': [{'_id': '6859a000fe8b31cd7362e2f3', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
