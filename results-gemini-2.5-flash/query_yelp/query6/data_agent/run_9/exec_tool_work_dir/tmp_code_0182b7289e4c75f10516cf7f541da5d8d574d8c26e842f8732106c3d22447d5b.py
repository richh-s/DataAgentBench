code = """import json

def extract_json_from_tool_output(tool_output_string):
    start_index = tool_output_string.find('[')
    end_index = tool_output_string.rfind(']')
    if start_index != -1 and end_index != -1:
        json_string = tool_output_string[start_index : end_index + 1]
        return json.loads(json_string)
    return None

# Process the review details from the first query
review_details_raw_string = locals()['var_function-call-2411167914170131885']['results'][0]
review_details_list = extract_json_from_tool_output(review_details_raw_string)
review_details = review_details_list[0] if review_details_list else {}

# Process the business info from the second query
business_info_raw_string = locals()['var_function-call-8330808566102405408']['results'][0]
business_info_list = extract_json_from_tool_output(business_info_raw_string)
business_info = business_info_list[0] if business_info_list else {}

description = business_info.get('description', '')

start_index = description.find('featuring')
end_index = description.find(', perfect for a cozy meal')

if start_index != -1 and end_index != -1:
    categories_str = description[start_index + len('featuring') : end_index].strip()
    categories = categories_str
else:
    categories = "Category information not found"

final_result = {
    "business_ref": review_details.get('business_ref'),
    "average_rating": float(review_details.get('average_rating', 0.0)),
    "review_count": int(review_details.get('review_count', 0)),
    "category": categories
}

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-2411167914170131885': [{'business_ref': 'businessref_9', 'average_rating': '4.0', 'review_count': '5'}], 'var_function-call-8330808566102405408': [{'_id': '6859a000fe8b31cd7362e2f3', 'attributes': {'HasTV': 'False', 'GoodForKids': 'True', 'Ambience': "{'romantic': False, 'intimate': False, 'classy': False, 'hipster': False, 'divey': False, 'touristy': False, 'trendy': False, 'upscale': False, 'casual': True}", 'NoiseLevel': "u'average'", 'RestaurantsTakeOut': 'True', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': True, 'dinner': False, 'brunch': True, 'breakfast': True}", 'WheelchairAccessible': 'True', 'OutdoorSeating': 'False', 'WiFi': "u'no'", 'RestaurantsReservations': 'True', 'BusinessAcceptsBitcoin': 'False', 'RestaurantsAttire': "u'casual'", 'RestaurantsDelivery': 'True', 'Alcohol': "u'none'", 'RestaurantsTableService': 'True', 'Caters': 'True', 'BikeParking': 'False', 'RestaurantsPriceRange2': '2', 'DogsAllowed': 'True', 'RestaurantsGoodForGroups': 'True', 'BusinessAcceptsCreditCards': 'True'}, 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
