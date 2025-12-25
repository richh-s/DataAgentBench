code = """import json
import re

# Load data
data = locals()['var_function-call-12285495499878674254']
if isinstance(data, str) and data.endswith('.json'):
    with open(data, 'r') as f:
        data = json.load(f)

# Extraction logic
markers = [
    "providing a range of services in ",
    "including ",
    "destination for ",
    "in the fields of ",
    "services in "
]

category_counts = {}
category_businesses = {}

for entry in data:
    desc = entry.get('description', '')
    bid = entry.get('business_id')
    
    # Find the best split point
    split_index = -1
    best_marker_len = 0
    
    for m in markers:
        idx = desc.rfind(m)
        if idx != -1:
            # We want the rightmost marker?
            # Actually, "providing a range of services in" contains "services in".
            # If we take the rightmost "services in", it might correspond to the same location.
            # We should probably take the rightmost occurrence of ANY marker.
            # If multiple markers end at different positions, take the one that ends latest?
            # Or starts latest?
            # Usually the intro phrase is unique.
            if idx > split_index:
                split_index = idx
                best_marker_len = len(m)
            elif idx == split_index:
                if len(m) > best_marker_len:
                    best_marker_len = len(m)
    
    if split_index != -1:
        cats_str = desc[split_index + best_marker_len:]
        # clean up
        if cats_str.endswith('.'):
            cats_str = cats_str[:-1]
        
        # Split by comma
        cats = [c.strip() for c in cats_str.split(',')]
        
        # Handle "and " in the last category
        if len(cats) > 0:
            last = cats[-1]
            if last.startswith('and '):
                cats[-1] = last[4:].strip()
            # sometimes "and" is inside the last chunk but not at start if split by comma failed?
            # E.g. "A, B and C". Split by comma -> "A", " B and C".
            # " B and C".strip() -> "B and C".
            # Wait, usually the oxford comma is used? Or not?
            # "Hair Salons, Beauty & Spas, ... and Makeup Artists."
            # Split by comma: ..., "and Makeup Artists".
            # So checking startswith "and " on the stripped chunk is correct.
            
            # What if "A and B"? (No comma)
            # cats_str = "A and B"
            # Split by comma -> ["A and B"]
            # Check last: starts with "and "? No.
            # We need to split by " and " if it's there.
            if ' and ' in cats[-1]:
                 parts = cats[-1].split(' and ')
                 # replace last element with parts
                 cats.pop()
                 cats.extend([p.strip() for p in parts])

        for c in cats:
            if not c: continue
            if c not in category_counts:
                category_counts[c] = 0
                category_businesses[c] = []
            category_counts[c] += 1
            category_businesses[c].append(bid)

# Find top category
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_category = sorted_cats[0][0]
top_count = sorted_cats[0][1]
top_businesses = category_businesses[top_category]

print("__RESULT__:")
print(json.dumps({
    "top_category": top_category,
    "count": top_count,
    "business_ids": top_businesses
}))"""

env_args = {'var_function-call-8596654735849025447': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-2674299717207068297': [{'_id': '6859a000fe8b31cd7362e2ab', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'attributes': 'None', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-12285495499878674254': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
