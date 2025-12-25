code = """import json
import re
import pandas as pd

# Load data
review_counts = locals()['var_function-call-13353977543139218697']
business_data = locals()['var_function-call-5669739630655256387']

# If data is in file (string path), load it.
if isinstance(review_counts, str) and review_counts.endswith('.json'):
    with open(review_counts, 'r') as f:
        review_counts = json.load(f)
        
if isinstance(business_data, str) and business_data.endswith('.json'):
    with open(business_data, 'r') as f:
        business_data = json.load(f)

# Create lookup for business categories
# Map ID suffix to categories list
business_cats = {}

def extract_categories(desc):
    # known patterns
    patterns = [
        r"providing a range of services in (.*)",
        r"offers a wide range of services, including (.*)",
        r"offers a range of services including (.*)",
        r"offers a range of services in (.*)",
        r"offers enthusiasts a premier destination for (.*)"
    ]
    
    cat_str = None
    for p in patterns:
        m = re.search(p, desc)
        if m:
            cat_str = m.group(1)
            break
            
    if not cat_str:
        return []
    
    # Clean trailing period
    if cat_str.endswith('.'):
        cat_str = cat_str[:-1]
        
    # Split
    # Split by comma
    parts = cat_str.split(',')
    cats = []
    for part in parts:
        part = part.strip()
        if part.lower().startswith('and '):
            part = part[4:]
        if part:
            cats.append(part)
    return cats

for b in business_data:
    bid = b.get('business_id') # e.g. businessid_49
    desc = b.get('description', '')
    cats = extract_categories(desc)
    
    # Normalize ID: extract number or simple replacement
    # businessid_49 -> 49
    if bid:
        # Assuming format businessid_X
        if 'businessid_' in bid:
            core_id = bid.replace('businessid_', '')
            business_cats[core_id] = cats

# Aggregate
category_counts = {}

for rc in review_counts:
    bref = rc['business_ref'] # businessref_13
    count = int(rc['review_cnt'])
    
    if 'businessref_' in bref:
        core_id = bref.replace('businessref_', '')
        
        if core_id in business_cats:
            cats = business_cats[core_id]
            for c in cats:
                category_counts[c] = category_counts.get(c, 0) + count

# Sort top 5
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-9124020475973035076': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-13353977543139218697': [{'business_ref': 'businessref_13', 'review_cnt': '1'}, {'business_ref': 'businessref_79', 'review_cnt': '1'}, {'business_ref': 'businessref_15', 'review_cnt': '1'}, {'business_ref': 'businessref_33', 'review_cnt': '2'}, {'business_ref': 'businessref_36', 'review_cnt': '2'}, {'business_ref': 'businessref_60', 'review_cnt': '2'}, {'business_ref': 'businessref_12', 'review_cnt': '1'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_57', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '1'}, {'business_ref': 'businessref_37', 'review_cnt': '1'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_26', 'review_cnt': '1'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_6', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '3'}, {'business_ref': 'businessref_96', 'review_cnt': '2'}, {'business_ref': 'businessref_98', 'review_cnt': '1'}, {'business_ref': 'businessref_14', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}], 'var_function-call-5669739630655256387': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
