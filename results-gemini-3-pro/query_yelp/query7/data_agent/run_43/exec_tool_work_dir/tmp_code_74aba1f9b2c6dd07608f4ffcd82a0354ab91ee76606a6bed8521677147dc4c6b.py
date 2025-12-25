code = """import json

# Load data
reviews_data = locals().get('var_function-call-9999548885396168596', [])
# Check if reviews_data is a string (file path) or list
if isinstance(reviews_data, str):
    if reviews_data.endswith('.json'):
        with open(reviews_data, 'r') as f:
            reviews_data = json.load(f)
    else:
        # Maybe it's a JSON string?
        try:
            reviews_data = json.loads(reviews_data)
        except:
            pass # Maybe it's a raw string message?

businesses_data = locals().get('var_function-call-7681288178934198536', [])
if isinstance(businesses_data, str):
    if businesses_data.endswith('.json'):
        with open(businesses_data, 'r') as f:
            businesses_data = json.load(f)
    else:
        try:
            businesses_data = json.loads(businesses_data)
        except:
            pass

def get_id_suffix(s):
    return s.split('_')[-1]

# Map business_id (suffix) -> count
review_counts = {}
for r in reviews_data:
    bid = get_id_suffix(r['business_ref'])
    cnt = int(r['cnt'])
    review_counts[bid] = cnt

# Parse categories
business_cats = {}
markers = ["services in ", "including ", "destination for "]

for b in businesses_data:
    if 'business_id' not in b: continue
    bid = get_id_suffix(b['business_id'])
    desc = b.get('description', '')
    
    cats_str = ""
    for m in markers:
        if m in desc:
            parts = desc.split(m)
            if len(parts) > 1:
                cats_str = parts[-1]
                break
    
    if not cats_str:
        continue
        
    cats_str = cats_str.strip().rstrip('.')
    
    # Split by comma
    raw_cats = [c.strip() for c in cats_str.split(',')]
    clean_cats = []
    for i, c in enumerate(raw_cats):
        # Remove "and " from the last element if it exists
        if i == len(raw_cats) - 1 and c.startswith('and '):
            c = c[4:]
        if c:
            clean_cats.append(c)
    
    business_cats[bid] = clean_cats

# Aggregate
cat_totals = {}
for bid, count in review_counts.items():
    if bid in business_cats:
        for cat in business_cats[bid]:
            cat_totals[cat] = cat_totals.get(cat, 0) + count

# Top 5
sorted_cats = sorted(cat_totals.items(), key=lambda x: x[1], reverse=True)
top5 = [c[0] for c in sorted_cats[:5]]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_function-call-9999548885396168596': [{'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_9', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_51', 'cnt': '2'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '2'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_33', 'cnt': '3'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_8', 'cnt': '1'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_97', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_72', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}], 'var_function-call-9999548885396167451': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-7681288178934198536': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
