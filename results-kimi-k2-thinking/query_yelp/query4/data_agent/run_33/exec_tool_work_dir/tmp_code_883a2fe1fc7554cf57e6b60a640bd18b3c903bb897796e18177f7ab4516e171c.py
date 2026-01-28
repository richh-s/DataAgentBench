code = """import json
import pandas as pd
import re
from collections import defaultdict

# Read all businesses that accept credit cards
file_path = locals()['var_functions.query_db:16']
with open(file_path, 'r') as file:
    cc_businesses = json.load(file)

# Read all reviews
review_file_path = locals()['var_functions.query_db:14']
with open(review_file_path, 'r') as file:
    reviews = json.load(file)

# Parse categories from descriptions
category_businesses = defaultdict(list)
for biz in cc_businesses:
    description = biz.get('description', '')
    if description:
        # Extract categories from description
        # Categories are after "services in" or "services including" or similar patterns
        if 'services in' in description:
            parts = description.split('services in')
        elif 'services including' in description:
            parts = description.split('services including')
        elif 'category of' in description:
            parts = description.split('category of')
        else:
            continue
            
        if len(parts) > 1:
            cat_part = parts[1].strip().rstrip('.')
            
            # Clean up
            cat_part = cat_part.replace("\\"", "'")
            cat_part = cat_part.replace("'", "")
            
            # Split by comma or "and"
            if ',' in cat_part:
                categories = [c.strip() for c in cat_part.split(',')]
            elif ' and ' in cat_part:
                categories = [c.strip() for c in cat_part.split('and')]
            else:
                categories = [cat_part]
            
            # Filter out empty categories and standardize
            for cat in categories:
                if cat and cat not in ['', 'making']:
                    # Standardize category names
                    if 'Restaurants' in cat:
                        category_businesses['Restaurants'].append(biz['business_id'])
                    elif 'Nail Salons' in cat or 'Beauty & Spas' in cat:
                        category_businesses['Beauty & Spas'].append(biz['business_id'])
                    elif 'Shopping' in cat:
                        category_businesses['Shopping'].append(biz['business_id'])
                    elif 'Health & Medical' in cat:
                        category_businesses['Health & Medical'].append(biz['business_id'])
                    elif 'Food' in cat:
                        category_businesses['Food'].append(biz['business_id'])
                    elif 'Automotive' in cat:
                        category_businesses['Automotive'].append(biz['business_id'])
                    elif 'Local Services' in cat:
                        category_businesses['Local Services'].append(biz['business_id'])
                    elif 'Home Services' in cat:
                        category_businesses['Home Services'].append(biz['business_id'])
                    elif 'Education' in cat:
                        category_businesses['Education'].append(biz['business_id'])
                    elif 'Hotels & Travel' in cat or 'Transportation' in cat:
                        category_businesses['Hotels & Travel'].append(biz['business_id'])
                    else:
                        category_businesses[cat].append(biz['business_id'])

# Count businesses per category
category_counts = {cat: len(business_ids) for cat, business_ids in category_businesses.items()}

# Sort by count
sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'category_counts': sorted_categories[:15] if sorted_categories else [],
    'total_businesses_accepting_cc': len(cc_businesses),
    'total_categories': len(category_counts)
}))"""

env_args = {'var_functions.list_db:0': ['business', 'checkin'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'name': 'Candy Barrel', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop", 'attributes': {'BikeParking': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsDelivery': 'None'}}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok', 'attributes': {'RestaurantsGoodForGroups': 'True', 'RestaurantsDelivery': 'False', 'RestaurantsTakeOut': 'True', 'HasTV': 'True', 'BusinessAcceptsCreditCards': 'True', 'Ambience': "{'touristy': False, 'hipster': False, 'romantic': False, 'divey': False, 'intimate': False, 'trendy': False, 'upscale': False, 'classy': False, 'casual': False}", 'GoodForMeal': "{'dessert': False, 'latenight': False, 'lunch': False, 'dinner': False, 'brunch': False, 'breakfast': False}", 'BusinessParking': "{u'valet': False, u'garage': False, u'street': False, u'lot': True, u'validated': False}"}}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'total_businesses_with_cc': 75}, 'var_functions.query_db:12': [{'review_id': 'reviewid_135', 'business_ref': 'businessref_34', 'rating': '2'}, {'review_id': 'reviewid_1067', 'business_ref': 'businessref_89', 'rating': '5'}, {'review_id': 'reviewid_871', 'business_ref': 'businessref_82', 'rating': '4'}, {'review_id': 'reviewid_314', 'business_ref': 'businessref_66', 'rating': '2'}, {'review_id': 'reviewid_487', 'business_ref': 'businessref_95', 'rating': '1'}, {'review_id': 'reviewid_1031', 'business_ref': 'businessref_24', 'rating': '4'}, {'review_id': 'reviewid_441', 'business_ref': 'businessref_40', 'rating': '4'}, {'review_id': 'reviewid_40', 'business_ref': 'businessref_47', 'rating': '5'}, {'review_id': 'reviewid_1807', 'business_ref': 'businessref_16', 'rating': '3'}, {'review_id': 'reviewid_1741', 'business_ref': 'businessref_96', 'rating': '5'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
