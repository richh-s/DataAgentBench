code = """import json
import re

# Load data
reviews_data = locals()['var_function-call-12568532036613232003']
business_data = locals()['var_function-call-10962640141121964900']

# If data is in file (string path), load it. 
if isinstance(reviews_data, str):
    with open(reviews_data, 'r') as f:
        reviews_data = json.load(f)

if isinstance(business_data, str):
    with open(business_data, 'r') as f:
        business_data = json.load(f)

# Create mapping business_id -> count
# Convert businessref_X to businessid_X
biz_counts = {}
for r in reviews_data:
    ref = r['business_ref']
    count = int(r['cnt'])
    # Convert ref
    if ref.startswith('businessref_'):
        bid = 'businessid_' + ref.split('_')[1]
        biz_counts[bid] = count

# Category counts
category_counts = {}

# Splitters to identify start of categories
splitters = [
    "providing a range of services in ",
    "offers a range of services in ",
    "including ",
    "destination for "
]

def extract_categories(description):
    # Find the splitter that appears last in the string
    best_splitter = None
    max_index = -1
    
    for s in splitters:
        idx = description.rfind(s)
        if idx != -1:
            if idx > max_index:
                max_index = idx
                best_splitter = s
    
    if best_splitter:
        # Extract content after the splitter
        content = description[max_index + len(best_splitter):]
        # Remove trailing period
        if content.endswith('.'):
            content = content[:-1]
        
        # Split by comma
        parts = content.split(', ')
        cats = []
        for i, p in enumerate(parts):
            p = p.strip()
            # Handle "and " in the last part
            if i == len(parts) - 1 and p.startswith('and '):
                p = p[4:]
            if p:
                cats.append(p)
        return cats
    return []

for biz in business_data:
    bid = biz['business_id']
    if bid in biz_counts:
        desc = biz.get('description', '')
        cats = extract_categories(desc)
        count = biz_counts[bid]
        for c in cats:
            category_counts[c] = category_counts.get(c, 0) + count

# Sort top 5
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:5]
result = [c[0] for c in sorted_cats]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9794413967874923631': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-12568532036613232003': [{'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '2'}, {'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_9', 'cnt': '1'}, {'business_ref': 'businessref_33', 'cnt': '3'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_51', 'cnt': '2'}, {'business_ref': 'businessref_8', 'cnt': '1'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_97', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_72', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}], 'var_function-call-10962640141121964900': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
