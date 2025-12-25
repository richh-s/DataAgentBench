code = """import json
import re
from collections import Counter

data = locals()['var_function-call-8155170085336384796']
if isinstance(data, str) and data.endswith('.json'):
    with open(data, 'r') as f:
        data = json.load(f)

# Function to extract categories
def extract_categories(desc):
    if not desc:
        return []
    
    # Common split points based on observation
    split_phrases = [
        "providing a range of services in ",
        "services, including ",
        "services including ",
        "destination for ",
        "fields of "
    ]
    
    categories_str = None
    for phrase in split_phrases:
        if phrase in desc:
            parts = desc.split(phrase)
            if len(parts) > 1:
                categories_str = parts[-1]
                break
    
    if not categories_str:
        # Fallback or specific handling if needed
        # Check for "offers ... " structure
        if "offers " in desc:
             parts = desc.split("offers ")
             # This is risky as "offers" is followed by description
             pass
        return []

    # Clean up the string (remove trailing punctuation)
    if categories_str.endswith('.'):
        categories_str = categories_str[:-1]
    
    # Split by comma and 'and'
    # "A, B, C, and D" -> ["A", " B", " C", " D"]
    # Replace " and " with "," to simplify
    categories_str = categories_str.replace(" and ", ", ")
    cats = [c.strip() for c in categories_str.split(',')]
    return [c for c in cats if c]

category_counts = Counter()
category_business_map = {}

for item in data:
    bid = item.get('business_id')
    desc = item.get('description')
    cats = extract_categories(desc)
    
    for cat in cats:
        category_counts[cat] += 1
        if cat not in category_business_map:
            category_business_map[cat] = []
        category_business_map[cat].append(bid)

if category_counts:
    top_category = category_counts.most_common(1)[0][0]
    top_count = category_counts[top_category]
    target_business_ids = category_business_map[top_category]
else:
    top_category = None
    top_count = 0
    target_business_ids = []

print("__RESULT__:")
print(json.dumps({"top_category": top_category, "count": top_count, "business_ids": target_business_ids}))"""

env_args = {'var_function-call-7884712707690248077': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-8155170085336384796': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
