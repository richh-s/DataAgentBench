code = """import json

# Re-using the logic to inspect all counts
data = locals()['var_function-call-7202743272144314356']

category_counts = {}

patterns = [
    "providing a range of services in ",
    "including ",
    "in the fields of ",
    "destination for "
]

def extract_categories(desc):
    found_splits = []
    for p in patterns:
        if p in desc:
            found_splits.append((desc.rfind(p), len(p)))
    
    if not found_splits:
        return []
    
    found_splits.sort(key=lambda x: x[0], reverse=True)
    idx, length = found_splits[0]
    cat_str = desc[idx+length:]
    if cat_str.endswith('.'):
        cat_str = cat_str[:-1]
    
    parts = cat_str.split(', ')
    cats = []
    for part in parts:
        part = part.strip()
        if part.startswith("and "):
            part = part[4:]
        if part:
            cats.append(part)
    return cats

for item in data:
    desc = item.get('description', '')
    cats = extract_categories(desc)
    for cat in cats:
        category_counts[cat] = category_counts.get(cat, 0) + 1

# Sort by count
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps(sorted_cats))"""

env_args = {'var_function-call-12133738051349115655': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-7202743272144314356': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-7197968214844095585': {'top_category': 'Beauty & Spas', 'business_count': 3, 'business_ids': ['businessid_47', 'businessid_33', 'businessid_92']}, 'var_function-call-3877829403852807849': [{'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '1'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '4'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '1'}, {'business_ref': 'businessref_47', 'rating': '4'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '1'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '2'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '3'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '3'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '3'}, {'business_ref': 'businessref_33', 'rating': '1'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '2'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '3'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '1'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '1'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '1'}, {'business_ref': 'businessref_47', 'rating': '3'}, {'business_ref': 'businessref_33', 'rating': '3'}, {'business_ref': 'businessref_92', 'rating': '3'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '4'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '1'}, {'business_ref': 'businessref_33', 'rating': '4'}, {'business_ref': 'businessref_92', 'rating': '1'}, {'business_ref': 'businessref_47', 'rating': '4'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '2'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '1'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '2'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '4'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '1'}, {'business_ref': 'businessref_47', 'rating': '1'}, {'business_ref': 'businessref_33', 'rating': '4'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '1'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '2'}, {'business_ref': 'businessref_92', 'rating': '5'}, {'business_ref': 'businessref_33', 'rating': '4'}, {'business_ref': 'businessref_33', 'rating': '1'}, {'business_ref': 'businessref_92', 'rating': '4'}], 'var_function-call-6169664615296213013': {'business_averages': {'businessref_33': 3.5217391304347827, 'businessref_47': 3.9047619047619047, 'businessref_92': 4.575757575757576}, 'category_avg_rating': 4.000752870318088}}

exec(code, env_args)
