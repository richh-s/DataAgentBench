code = """import json

review_data = json.loads(locals()['var_function-call-10007741989300991743']['results'][0])
business_data = json.loads(locals()['var_function-call-4507570865237694837']['results'][0])

if review_data and business_data:
    highest_rated_business_ref = review_data[0]['business_ref']
    highest_average_rating = float(review_data[0]['average_rating'])

    business_name = business_data[0]['name']
    business_description = business_data[0]['description']

    # Extract category from the description. Assuming it's the part after "featuring" and before "perfect for a cozy meal"
    category_start = business_description.find("featuring ") + len("featuring ")
    category_end = business_description.find(", perfect for a cozy meal")
    category = business_description[category_start:category_end]

    result = {
        "business_name": business_name,
        "average_rating": highest_average_rating,
        "category": category
    }
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('__RESULT__:')
    print(json.dumps({"error": "No data found"}))"""

env_args = {'var_function-call-10007741989300991743': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-4507570865237694837': [{'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'review_count': '53', 'is_open': '0', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'hours': {'Monday': '7:0-15:0', 'Tuesday': '7:0-15:0', 'Wednesday': '7:0-15:0', 'Thursday': '7:0-15:0', 'Friday': '7:0-15:0', 'Saturday': '8:30-15:0', 'Sunday': '8:30-15:0'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
