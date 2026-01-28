code = """import json
import pandas as pd

# Read the full businesses data from the file
file_path = "file_storage/functions.query_db:2.json"
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Extract business categories and credit card acceptance
business_data = []
for biz in businesses:
    business_id = biz['business_id']
    attributes = biz.get('attributes', {})
    
    # Check if accepts credit cards
    accepts_credit = False
    if attributes and isinstance(attributes, dict):
        credit_card_attr = attributes.get('BusinessAcceptsCreditCards')
        if credit_card_attr == 'True' or credit_card_attr == True:
            accepts_credit = True
    
    # Extract categories from description
    description = biz.get('description', '')
    categories = []
    if 'providing a range of services in ' in description:
        category_text = description.split('providing a range of services in ')[1]
        categories_str = category_text.split('.')[0]
        categories = [cat.strip() for cat in categories_str.split(',')]
    elif 'offers a wide range of services, including ' in description:
        category_text = description.split('offers a wide range of services, including ')[1]
        categories_str = category_text.split('.')[0]
        categories = [cat.strip() for cat in categories_str.split(',')]
    elif 'offers a range of services' in description:
        if 'offers a range of services in ' in description:
            category_text = description.split('offers a range of services in ')[1]
            categories_str = category_text.split('.')[0]
            categories = [cat.strip() for cat in categories_str.split(',')]
        elif 'offers a range of services including ' in description:
            category_text = description.split('offers a range of services including ')[1]
            categories_str = category_text.split('.')[0]
            categories = [cat.strip() for cat in categories_str.split(',')]
    elif 'offers' in description and 'services' in description:
        # More generic parsing
        parts = description.split('services')
        if len(parts) > 1:
            category_part = parts[1]
            if 'in ' in category_part:
                category_text = category_part.split('in ')[1]
                categories_str = category_text.split('.')[0]
                categories = [cat.strip() for cat in categories_str.split(',')]
    
    if not categories:
        # Fallback: parse category from the end of description
        if 'category of ' in description:
            category_text = description.split('category of ')[1]
            categories_str = category_text.split("'")[0] if "'" in category_text else category_text
            categories = [cat.strip() for cat in categories_str.split(',')]
        # Other patterns
        elif 'fields of ' in description:
            category_text = description.split('fields of ')[1]
            categories_str = category_text.split('.')[0]
            categories = [cat.strip() for cat in categories_str.split(',')]
    
    business_data.append({
        'business_id': business_id,
        'accepts_credit_cards': accepts_credit,
        'categories': categories
    })

# Count businesses by category for those accepting credit cards
category_count = {}
for biz in business_data:
    if biz['accepts_credit_cards']:
        for category in biz['categories']:
            if category:
                category_count[category] = category_count.get(category, 0) + 1

# Sort by count descending
sorted_categories = sorted(category_count.items(), key=lambda x: x[1], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'top_categories': sorted_categories[:10],
    'total_businesses_analyzed': len(business_data)
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'file_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
