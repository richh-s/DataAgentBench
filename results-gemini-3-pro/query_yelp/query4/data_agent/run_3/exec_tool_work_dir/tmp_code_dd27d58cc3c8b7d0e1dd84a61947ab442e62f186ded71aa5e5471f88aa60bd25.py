code = """import json
import re

# Load the data
data = locals()['var_function-call-15368553860358527870']
if isinstance(data, str):
    # If it's a file path
    with open(data, 'r') as f:
        data = json.load(f)

category_counts = {}
category_businesses = {}

markers = [
    "providing a range of services in ",
    "including ",
    "fields of ",
    "destination for "
]

for item in data:
    desc = item.get('description', '')
    bid = item.get('business_id')
    
    # Find the start of the category list
    cat_string = None
    best_idx = -1
    best_marker_len = 0
    
    for m in markers:
        idx = desc.rfind(m)
        if idx != -1:
            # We want the last occurrence of the marker? 
            # Usually these phrases appear once.
            # But if multiple appear, the categories usually follow the last introduction clause.
            if idx > best_idx:
                best_idx = idx
                best_marker_len = len(m)
    
    if best_idx != -1:
        cat_section = desc[best_idx + best_marker_len:]
        # Remove trailing period if exists
        if cat_section.endswith('.'):
            cat_section = cat_section[:-1]
        
        # Split by comma and ' and '
        # "Cat1, Cat2, and Cat3" -> ["Cat1", " Cat2", " Cat3"]
        # Replace ' and ' with ',' first to handle the last item
        cat_section = cat_section.replace(' and ', ', ')
        cats = [c.strip() for c in cat_section.split(',')]
        
        for c in cats:
            if not c: continue
            if c not in category_counts:
                category_counts[c] = 0
                category_businesses[c] = []
            category_counts[c] += 1
            category_businesses[c].append(bid)

# Find top category
if category_counts:
    top_category = max(category_counts, key=category_counts.get)
    top_count = category_counts[top_category]
    top_businesses = category_businesses[top_category]
else:
    top_category = None
    top_count = 0
    top_businesses = []

result = {
    "top_category": top_category,
    "count": top_count,
    "business_ids": top_businesses
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-364485386677142330': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-15368553860358527870': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
