code = """import json
import re
from collections import Counter

file_path = locals()['var_function-call-11626173642684947752']
with open(file_path, 'r') as f:
    data = json.load(f)

def extract_categories(desc):
    if not desc:
        return []
    
    # Phrases that precede the category list
    # Ordered roughly by specificity
    split_phrases = [
        "products across various categories, including ",
        "services in the categories of ",
        "in the category of ",
        "in the categories of ",
        "categories such as ",
        "providing a range of services in ",
        "range of services including ",
        "range of services, including ",
        "variety of offerings, including ",
        "variety of services including ",
        "specializes in ",
        "destination for ",
        "fields of ",
        "selection of ", # Risky?
        "array of options ranging from " # Special case?
    ]
    
    # Strategy: Find the rightmost occurrence of any key phrase?
    # Or just try them in order?
    # The descriptions seem to use one main phrase near the end.
    
    best_part = None
    best_index = -1
    
    for phrase in split_phrases:
        idx = desc.rfind(phrase)
        if idx != -1:
            # We found a phrase. 
            # If we have multiple matches (unlikely to overlap in a conflicting way), 
            # usually the one closest to the end is the list start.
            # But wait, "specializes in A, B, C offering D, E"
            # Let's verify.
            # Example: "specializes in Optometrists..., offering a range of..."
            # If I take "specializes in", I get "Optometrists..., offering a range of..."
            # The list might be interrupted.
            if idx > best_index:
                best_index = idx
                # The content is after the phrase
                best_part = desc[idx + len(phrase):]

    if not best_part:
        # Fallback: check for "offers ... including"
        if "including " in desc:
            best_part = desc.split("including ")[-1]
        elif "offers " in desc:
             # Very generic
             pass
    
    if not best_part:
        return []

    # Clean up the string
    # Remove trailing punctuation
    best_part = best_part.strip()
    if best_part.endswith('.'):
        best_part = best_part[:-1]
    
    # Handle "ranging from A, B, to C"
    # Or "from A, B, to C"
    # This is complex. Let's ignore "ranging from" special logic for now and treat "to" as separator if needed?
    # Actually, "ranging from Food, ..., to Event Planning" -> The "to" is part of the flow.
    # If I split by comma, I get " to Event Planning". 
    # Let's just split by comma.
    
    # Replace " and " with ", "
    best_part = best_part.replace(" and ", ", ")
    
    # Split
    raw_cats = best_part.split(',')
    
    clean_cats = []
    for c in raw_cats:
        c = c.strip()
        # Remove "to " prefix if it exists (from "ranging from ... to ...")
        if c.startswith("to ") and len(c) > 3:
            c = c[3:]
        
        # Remove quotes if present (e.g. 'Restaurants, Chinese')
        c = c.replace("'", "")
        
        if c:
            clean_cats.append(c)
            
    return clean_cats

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
    business_ids = category_business_map[top_category]
else:
    top_category = None
    top_count = 0
    business_ids = []

print("__RESULT__:")
print(json.dumps({"top_category": top_category, "count": top_count, "business_ids": business_ids}))"""

env_args = {'var_function-call-7884712707690248077': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-8155170085336384796': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-10104176036617224673': {'top_category': 'Beauty & Spas', 'count': 3, 'business_ids': ['businessid_47', 'businessid_33', 'businessid_92']}, 'var_function-call-7153560885770567269': [{'average_rating': '4.040816326530612'}], 'var_function-call-11626173642684947752': 'file_storage/function-call-11626173642684947752.json'}

exec(code, env_args)
