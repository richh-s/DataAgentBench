code = """import json
import re

# Load the businesses
data = locals()['var_function-call-2560747226847755645']
if isinstance(data, str):
    with open(data, 'r') as f:
        businesses = json.load(f)
else:
    businesses = data

# Keywords indicating start of categories
keywords = ["services in ", "including ", "destination for ", "fields of "]

category_business_map = [] # (category, business_id)

for b in businesses:
    desc = b.get('description', '')
    bid = b.get('business_id')
    
    # Simple extraction logic: find the last occurrence of any keyword
    cat_string = None
    last_idx = -1
    
    for kw in keywords:
        idx = desc.rfind(kw)
        if idx > last_idx:
            last_idx = idx
            cat_string = desc[idx + len(kw):]
            
    if cat_string:
        # Remove trailing period
        if cat_string.endswith('.'):
            cat_string = cat_string[:-1]
        
        cats = [c.strip() for c in cat_string.split(',')]
        for c in cats:
            # clean up "and " if it appears in the last item
            if c.lower().startswith('and '):
                c = c[4:]
            if c:
                category_business_map.append((c, bid))

# Count categories
from collections import Counter
cat_counts = Counter([c for c, bid in category_business_map])

if cat_counts:
    top_category = cat_counts.most_common(1)[0]
    print(f"Top category: {top_category}")
    
    # Get business IDs for top category
    target_category = top_category[0]
    target_bids = [bid for c, bid in category_business_map if c == target_category]
    
    result = {
        "top_category": target_category,
        "business_count": top_category[1],
        "target_bids": target_bids
    }
else:
    result = {"error": "No categories found"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6480467345779119152': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-2560747226847755645': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
