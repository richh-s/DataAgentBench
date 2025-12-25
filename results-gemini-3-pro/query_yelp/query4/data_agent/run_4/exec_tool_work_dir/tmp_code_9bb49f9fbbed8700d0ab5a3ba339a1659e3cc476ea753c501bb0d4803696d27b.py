code = """import json
import pandas as pd
import re

# Load data
data = locals()['var_function-call-1827484918260546124']
if isinstance(data, str):
    with open(data, 'r') as f:
        data = json.load(f)

# Filter for credit card acceptance
filtered_businesses = []
for b in data:
    attrs = b.get('attributes')
    if isinstance(attrs, dict):
        # Check for True/False string
        acc = attrs.get('BusinessAcceptsCreditCards')
        if acc == 'True':
            filtered_businesses.append(b)

# Extract categories and count
category_counts = {}
category_businesses = {} # cat -> list of business_ids

regex_pattern = re.compile(r"(?:services(?:,| in| including)+|destination for) (.*)")

for b in filtered_businesses:
    desc = b.get('description', '')
    match = regex_pattern.search(desc)
    if match:
        cats_str = match.group(1).strip()
        if cats_str.endswith('.'):
            cats_str = cats_str[:-1]
        
        # Split by comma
        cats = [c.strip() for c in cats_str.split(',')]
        
        for c in cats:
            if c not in category_counts:
                category_counts[c] = 0
                category_businesses[c] = []
            category_counts[c] += 1
            category_businesses[c].append(b['business_id'])

# Find top category
if category_counts:
    top_category = max(category_counts, key=category_counts.get)
    top_count = category_counts[top_category]
    top_businesses = category_businesses[top_category]
else:
    top_category = None
    top_count = 0
    top_businesses = []

print("__RESULT__:")
print(json.dumps({
    "top_category": top_category,
    "count": top_count,
    "business_ids": top_businesses
}))"""

env_args = {'var_function-call-18439703079313721671': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-1827484918260546124': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
