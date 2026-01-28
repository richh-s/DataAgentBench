code = """import json, pandas as pd, re
from collections import defaultdict, Counter

# Access business data
business_file = locals()['var_functions.query_db:38']
with open(business_file, 'r') as f:
    business_data = json.load(f)

print('Total businesses:', len(business_data))

# Function to extract categories from description
def extract_categories(description):
    if not description:
        return ['Miscellaneous']
    
    # Patterns to match categories
    patterns = [
        r"in the (?:fields of|category of) '([^']+)'",
        r"services? in ([^\.\,]+)",
        r"offers? a (?:range of|wide range of|delightful array of|delightful mix of|diverse selection of) ([^\.\,]+)",
        r"offers? enthusiasts a premier destination for ([^\.\,]+)",
        r"specializes in ([^\.\,]+)",
        r"categories? of ([^\.\,]+)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, description.lower(), re.IGNORECASE)
        if match:
            categories_str = match.group(1)
            # Split by comma, 'and', 'to'
            categories = re.split(r',\s*|\sand\s|\sto\s', categories_str)
            # Clean up
            clean_categories = []
            for cat in categories:
                cat = cat.strip().strip('"').strip("'")
                if cat and cat not in ['a', 'an', 'the', 'and', 'to']:
                    clean_categories.append(cat.title())
            return clean_categories if clean_categories else ['Miscellaneous']
    
    return ['Miscellaneous']

# Process businesses
businesses_with_cc = []
business_categories = defaultdict(list)

for business in business_data:
    # Check if accepts credit cards
    attributes = business.get('attributes', {})
    if isinstance(attributes, dict) and attributes.get('BusinessAcceptsCreditCards') == 'True':
        business_id = business['business_id']
        name = business['name']
        description = business.get('description', '')
        
        # Extract categories
        categories = extract_categories(description)
        
        for category in categories:
            business_categories[category].append({
                'business_id': business_id,
                'name': name
            })
        
        businesses_with_cc.append({
            'business_id': business_id,
            'name': name,
            'categories': categories
        })

# Count businesses by category
category_counts = {category: len(businesses) for category, businesses in business_categories.items()}

# Find top category
if category_counts:
    top_category = max(category_counts.items(), key=lambda x: x[1])
    print('Top category:', top_category)
    print('Total credit card businesses:', len(businesses_with_cc))
    print('Sample categories:', dict(list(category_counts.items())[:10]))
else:
    top_category = None

# Save results for next step
result = {
    'total_cc_businesses': len(businesses_with_cc),
    'top_category': top_category[0] if top_category else None,
    'top_category_count': top_category[1] if top_category else 0,
    'business_ids_in_top': [b['business_id'] for b in business_categories[top_category[0]]] if top_category else [],
    'all_category_counts': category_counts
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review', 'tip', 'user'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:24': {'count': 100, 'first_keys': ['business_id', 'name', 'attributes', 'description']}, 'var_functions.query_db:26': [{'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:28': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.execute_python:36': {'type': "<class 'list'>", 'is_list': True, 'length': 5, 'first_item_keys': ['business_id', 'name', 'attributes', 'description']}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
