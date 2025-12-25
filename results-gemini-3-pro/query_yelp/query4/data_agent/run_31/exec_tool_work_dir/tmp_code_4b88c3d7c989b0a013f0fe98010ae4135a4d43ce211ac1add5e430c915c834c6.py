code = """import json
from collections import Counter

# Load the previous results to avoid re-parsing if possible, 
# but I need the map again. I'll just re-run the parsing logic on the stored businesses list.
data = locals()['var_function-call-2560747226847755645']
if isinstance(data, str):
    with open(data, 'r') as f:
        businesses = json.load(f)
else:
    businesses = data

keywords = ["services in ", "including ", "destination for ", "fields of "]
category_business_map = [] 

for b in businesses:
    desc = b.get('description', '')
    bid = b.get('business_id')
    cat_string = None
    last_idx = -1
    for kw in keywords:
        idx = desc.rfind(kw)
        if idx > last_idx:
            last_idx = idx
            cat_string = desc[idx + len(kw):]
    if cat_string:
        if cat_string.endswith('.'):
            cat_string = cat_string[:-1]
        cats = [c.strip() for c in cat_string.split(',')]
        for c in cats:
            if c.lower().startswith('and '):
                c = c[4:]
            if c:
                category_business_map.append((c, bid))

cat_counts = Counter([c for c, bid in category_business_map])
print("__RESULT__:")
print(json.dumps(cat_counts.most_common(5)))"""

env_args = {'var_function-call-6480467345779119152': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-2560747226847755645': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-15050334787531627484': {'top_category': 'Beauty & Spas', 'business_count': 3, 'target_bids': ['businessid_47', 'businessid_33', 'businessid_92']}, 'var_function-call-15776718248112251344': [{'avg_rating': '4.040816326530612'}]}

exec(code, env_args)
