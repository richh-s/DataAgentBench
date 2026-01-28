code = """import json
import pandas as pd
from collections import defaultdict

# Read all businesses that accept credit cards
file_path = locals()['var_functions.query_db:16']
with open(file_path, 'r') as file:
    cc_businesses = json.load(file)

# Read all reviews
review_file_path = locals()['var_functions.query_db:14']
with open(review_file_path, 'r') as file:
    reviews = json.load(file)

# Create review lookup by business_ref
reviews_by_business = defaultdict(list)
for review in reviews:
    business_ref = review.get('business_ref')
    if business_ref:
        reviews_by_business[business_ref].append(int(review.get('rating', 0)))

# Parse categories and collect business IDs for Beauty & Spas
beauty_spas_businesses = []

for biz in cc_businesses:
    description = biz.get('description', '')
    business_id = biz.get('business_id')
    if not description or not business_id:
        continue
    
    # Extract categories from description
    if 'services in' in description:
        parts = description.split('services in')
    elif 'services including' in description:
        parts = description.split('services including')
    elif 'category of' in description:
        parts = description.split('category of')
    else:
        continue
        
    if len(parts) > 1:
        cat_part = parts[1].strip().rstrip('.'
        
        # Standardize category names
        if 'Beauty & Spas' in cat_part or 'Nail Salons' in cat_part or 'Hair Salons' in cat_part or 'Cosmetics' in cat_part:
            beauty_spas_businesses.append(biz['business_id'])

# Look up ratings for these businesses
ratings = []
business_refs = [bid.replace('businessid_', 'businessref_') for bid in beauty_spas_businesses]

for bus_ref in business_refs:
    if bus_ref in reviews_by_business:
        ratings.extend(reviews_by_business[bus_ref])

# Calculate average rating
average_rating = sum(ratings) / len(ratings) if ratings else 0

print('__RESULT__:')
print(json.dumps({
    'category': 'Beauty & Spas',
    'business_count': len(beauty_spas_businesses),
    'average_rating': round(average_rating, 2),
    'total_reviews': len(ratings),
    'business_ids': beauty_spas_businesses
}))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'total_businesses_with_cc': 75}, 'var_functions.query_db:12': [{'review_id': 'reviewid_135', 'business_ref': 'businessref_34', 'rating': '2'}, {'review_id': 'reviewid_1067', 'business_ref': 'businessref_89', 'rating': '5'}, {'review_id': 'reviewid_871', 'business_ref': 'businessref_82', 'rating': '4'}, {'review_id': 'reviewid_314', 'business_ref': 'businessref_66', 'rating': '2'}, {'review_id': 'reviewid_487', 'business_ref': 'businessref_95', 'rating': '1'}, {'review_id': 'reviewid_1031', 'business_ref': 'businessref_24', 'rating': '4'}, {'review_id': 'reviewid_441', 'business_ref': 'businessref_40', 'rating': '4'}, {'review_id': 'reviewid_40', 'business_ref': 'businessref_47', 'rating': '5'}, {'review_id': 'reviewid_1807', 'business_ref': 'businessref_16', 'rating': '3'}, {'review_id': 'reviewid_1741', 'business_ref': 'businessref_96', 'rating': '5'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'category_counts': [['Beauty & Spas', 7], ['Local Services', 4], ['Shopping', 3], ['Health & Medical', 3], ['Hotels & Travel', 3], ['Home Services', 3], ['Hair Removal', 2], ['Restaurants', 2], ['Chinese', 2], ['Gas Stations', 2], ['Automotive', 2], ['Food', 2], ['Hair Salons', 2], ['Education', 1], ['Elementary Schools', 1]], 'total_businesses_accepting_cc': 75, 'total_categories': 58}}

exec(code, env_args)
