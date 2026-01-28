code = """import json
import re

# Get reviews from var_functions.query_db:2
reviews_data = [
    {"business_ref": "businessref_16", "rating": "1"}, {"business_ref": "businessref_23", "rating": "5"}, {"business_ref": "businessref_8", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_96", "rating": "5"}, {"business_ref": "businessref_8", "rating": "5"}, {"business_ref": "businessref_47", "rating": "3"}, {"business_ref": "businessref_37", "rating": "5"}, {"business_ref": "businessref_8", "rating": "4"}, {"business_ref": "businessref_43", "rating": "4"}, {"business_ref": "businessref_14", "rating": "3"}, {"business_ref": "businessref_21", "rating": "1"}, {"business_ref": "businessref_16", "rating": "3"}, {"business_ref": "businessref_31", "rating": "1"}, {"business_ref": "businessref_30", "rating": "2"}, {"business_ref": "businessref_81", "rating": "1"}, {"business_ref": "businessref_71", "rating": "5"}, {"business_ref": "businessref_31", "rating": "1"}, {"business_ref": "businessref_46", "rating": "5"}, {"business_ref": "businessref_99", "rating": "5"}, {"business_ref": "businessref_40", "rating": "5"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_11", "rating": "5"}, {"business_ref": "businessref_21", "rating": "1"}, {"business_ref": "businessref_9", "rating": "5"}, {"business_ref": "businessref_8", "rating": "3"}, {"business_ref": "businessref_46", "rating": "5"}, {"business_ref": "businessref_68", "rating": "1"}, {"business_ref": "businessref_88", "rating": "5"}, {"business_ref": "businessref_9", "rating": "2"}, {"business_ref": "businessref_71", "rating": "1"}, {"business_ref": "businessref_28", "rating": "5"}, {"business_ref": "businessref_71", "rating": "5"}, {"business_ref": "businessref_37", "rating": "5"}, {"business_ref": "businessref_9", "rating": "3"}, {"business_ref": "businessref_17", "rating": "5"}, {"business_ref": "businessref_82", "rating": "4"}
]

# Get businesses from var_functions.query_db:3
businesses_data = [
    {"_id": "6859a000fe8b31cd7362e2ab", "business_id": "businessid_49", "name": "Steps to Learning Montessori Preschool", "attributes": {"BusinessAcceptsCreditCards": "True", "WiFi": "u'no'", "BusinessAcceptsBitcoin": "False"}}, {"_id": "6859a000fe8b31cd7362e2ac", "business_id": "businessid_47", "name": "Breeze Blow Dry Bar", "attributes": {"ByAppointmentOnly": "False", "BusinessAcceptsCreditCards": "True", "GoodForKids": "True", "RestaurantsPriceRange2": "2", "BikeParking": "False", "BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {"_id": "6859a000fe8b31cd7362e2ad", "business_id": "businessid_88", "name": "Impact Guns", "attributes": {"BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", "GoodForKids": "True", "BusinessAcceptsCreditCards": "True", "ByAppointmentOnly": "False", "BikeParking": "True"}}, {"_id": "6859a000fe8b31cd7362e2ae", "business_id": "businessid_41", "name": "Palms Primary Care", "attributes": "None"}, {"_id": "6859a000fe8b31cd7362e2af", "business_id": "businessid_33", "name": "J&Q Nails", "attributes": {"BusinessParking": "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", "BusinessAcceptsCreditCards": "True", "AcceptsInsurance": "False", "ByAppointmentOnly": "False", "RestaurantsPriceRange2": "2", "WheelchairAccessible": "True", "BikeParking": "False"}}
]

# Convert ratings to integers and extract business_id numbers
for review in reviews_data:
    review['rating'] = int(review['rating'])
    # Extract the number from business_ref (e.g., businessref_16 -> 16)
    match = re.search(r'businessref_(\d+)', review['business_ref'])
    if match:
        review['business_num'] = match.group(1)

# Create dictionary mapping business_id to name and attributes
business_dict = {}
for business in businesses_data:
    # Extract the number from business_id
    match = re.search(r'businessid_(\d+)', business['business_id'])
    if match:
        business_num = match.group(1)
        # Determine category from attributes if possible
        category = None
        if business['attributes'] != "None" and isinstance(business['attributes'], dict):
            attrs = business['attributes']
            if 'RestaurantsPriceRange2' in attrs:
                category = 'Restaurant'
            elif 'BusinessParking' in attrs or 'BikeParking' in attrs or 'valet' in str(attrs):
                category = 'Service/Business'
            elif 'WiFi' in attrs or 'BusinessAcceptsCreditCards' in attrs:
                if 'Montessori' in business['name'] or 'Preschool' in business['name']:
                    category = 'Education'
                else:
                    category = 'Business'
        
        business_dict[business_num] = {
            'name': business['name'],
            'category': category or 'Unknown'
        }

# Group reviews by business and calculate average rating
business_ratings = {}
for review in reviews_data:
    business_num = review.get('business_num')
    if business_num:
        if business_num not in business_ratings:
            business_ratings[business_num] = []
        business_ratings[business_num].append(review['rating'])

# Calculate average ratings and filter businesses with at least 5 reviews
business_avg_ratings = {}
for business_num, ratings in business_ratings.items():
    if len(ratings) >= 5:
        avg_rating = sum(ratings) / len(ratings)
        business_avg_ratings[business_num] = {
            'avg_rating': avg_rating,
            'review_count': len(ratings),
            'business_info': business_dict.get(business_num, {'name': f'Unknown (ID: {business_num})', 'category': 'Unknown'})
        }

# Find business with highest average rating
if business_avg_ratings:
    highest_rated = max(business_avg_ratings.items(), key=lambda x: x[1]['avg_rating'])
    business_num, data = highest_rated
    
    result = {
        'business_id': f'businessid_{business_num}',
        'business_ref': f'businessref_{business_num}',
        'name': data['business_info']['name'],
        'category': data['business_info']['category'],
        'avg_rating': data['avg_rating'],
        'review_count': data['review_count']
    }
    
    print('__RESULT__:')
    print(json.dumps(result, indent=2))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No businesses found with at least 5 reviews'}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}], 'var_functions.query_db:3': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}]}

exec(code, env_args)
