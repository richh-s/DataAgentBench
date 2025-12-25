code = """import pandas as pd
import re
import json

data = locals()['var_function-call-14619191610086424557']
if isinstance(data, str) and data.endswith('.json'):
    with open(data, 'r') as f:
        businesses = json.load(f)
else:
    businesses = data

category_counts = {}
category_businesses = {}

# Regex to capture the list of categories
# We look for the phrase introducing the list, and capture everything until the end.
pattern = re.compile(r"(?:services in|including|destination for|fields of)\s+(.*)$")

for b in businesses:
    desc = b.get('description', '')
    if not desc:
        continue
    
    match = pattern.search(desc)
    if match:
        cat_str = match.group(1)
        # Remove trailing period if exists
        if cat_str.endswith('.'):
            cat_str = cat_str[:-1]
        
        # Replace 'and ' used as a conjunction for the last item
        # E.g. "A, B, and C" -> "A, B, C"
        # Check for ", and "
        cat_str = cat_str.replace(", and ", ", ")
        # Also just " and " if no oxford comma? "A and B". 
        # But be careful about "Bed and Breakfast". "Health and Medical".
        # Usually categories are capitalized. "Bed and Breakfast" is a category.
        # "and" as a separator is usually surrounded by commas or is the last separator.
        # If I split by ", ", I might get "and Waxing". Then I remove "and " from the start of that part.
        
        cats = [c.strip() for c in cat_str.split(', ')]
        
        # Clean up the last item if it starts with "and " (in case of "A, B and C")
        if len(cats) > 1 and cats[-1].startswith("and "):
             cats[-1] = cats[-1][4:]
        
        for cat in cats:
            if not cat: continue
            category_counts[cat] = category_counts.get(cat, 0) + 1
            if cat not in category_businesses:
                category_businesses[cat] = []
            category_businesses[cat].append(b['business_id'])

# Find the category with the largest number of businesses
if not category_counts:
    print("__RESULT__:")
    print(json.dumps({"error": "No categories found"}))
else:
    most_common_cat = max(category_counts, key=category_counts.get)
    count = category_counts[most_common_cat]
    business_ids = category_businesses[most_common_cat]
    
    result = {
        "most_common_category": most_common_cat,
        "count": count,
        "business_ids": business_ids
    }
    
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-979204996136720875': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-14619191610086424557': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
