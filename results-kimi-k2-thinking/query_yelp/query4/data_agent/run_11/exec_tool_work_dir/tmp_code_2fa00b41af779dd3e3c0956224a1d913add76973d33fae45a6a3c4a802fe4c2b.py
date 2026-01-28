code = """import json

# Read the business data
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Filter businesses that accept credit cards
credit_card_businesses = []
for business in businesses:
    if 'attributes' in business and business['attributes'] != 'None' and business['attributes'] is not None:
        attributes = business['attributes']
        if isinstance(attributes, dict) and 'BusinessAcceptsCreditCards' in attributes:
            if attributes['BusinessAcceptsCreditCards'] == 'True':
                credit_card_businesses.append(business)

print('Total credit card businesses:', len(credit_card_businesses))

# Extract categories using a more robust approach
from collections import defaultdict
category_count = defaultdict(int)

for business in credit_card_businesses:
    if 'description' in business and business['description']:
        desc = business['description']
        
        # Look for comma-separated lists of categories at the end of descriptions
        # Common patterns in Yelp data: lists of categories separated by commas
        
        # Method 1: Find the last part of the description which often contains categories
        # Look for patterns like "in Category1, Category2, and Category3"
        
        import re
        
        # Pattern for "in X, Y, Z" or "including X, Y, Z" at the end
        end_patterns = [
            r'(?:in|including|and|for)\s+([A-Z][^\.,]+(?:,\s*[A-Z][^\.,]+)+)',
            r'([A-Z][a-z]+(?:,\s*[A-Z][a-z]+)+)\.?$'  # Simple comma-separated caps ending
        ]
        
        categories_found = []
        for pattern in end_patterns:
            matches = re.findall(pattern, desc)
            for match in matches:
                # Split by comma, handle & and 'and'
                parts = re.split(r',|\s+and\s+|&', match)
                for part in parts:
                    part = part.strip()
                    # Remove trailing punctuation
                    part = re.sub(r'[\.\,;]$', '', part)
                    # Remove leading articles/common words
                    part = re.sub(r'^\s*(the|a|an|and|or)\s+', '', part, flags=re.IGNORECASE)
                    part = part.strip()
                    
                    # Only keep reasonable-looking categories (not too short, not too long, start with caps)
                    if part and len(part) > 3 and len(part) < 50 and part[0].isupper():
                        categories_found.append(part)
        
        # Method 2: Look within the description for quoted or explicit category lists
        quoted = re.findall(r'["\']([^"\']+)["\']', desc)
        for q in quoted:
            if ',' in q:
                parts = q.split(',')
                for part in parts:
                    part = part.strip()
                    if len(part) > 3:
                        categories_found.append(part)
        
        # Count and store
        for cat in categories_found:
            # Simple normalization
            cat_lower = cat.lower()
            # Skip generic terms
            if cat_lower not in ['located at', 'this', 'that', 'these', 'those', 'and', 'or']:
                category_count[cat_lower] += 1
        
        business['extracted_categories'] = categories_found

# Find the top category
if category_count:
    top_category = max(category_count.items(), key=lambda x: x[1])
    top_category_name = top_category[0]
    top_category_count = top_category[1]
    print(f'Top category: {top_category_name} ({top_category_count} businesses)')
else:
    top_category_name = None
    top_category_count = 0
    print('No categories found')

print(f'Total unique categories: {len(category_count)}')
print(f'Top 10 categories: {sorted(category_count.items(), key=lambda x: x[1], reverse=True)[:10]}')

result = {
    'total_credit_card_businesses': len(credit_card_businesses),
    'top_category': top_category_name,
    'top_category_count': top_category_count,
    'unique_categories': len(category_count)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review', 'tip', 'user'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:40': {'total_credit_card_businesses': 75, 'top_category': 'restaurants', 'top_category_count': 2, 'top_category_business_ids': ['businessid_10', 'businessid_36']}}

exec(code, env_args)
