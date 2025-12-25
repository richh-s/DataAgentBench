code = """import json
import re

review_counts_data = locals()['var_function-call-1831943725105221082']
businesses = locals()['var_function-call-2511881889809102580']

review_counts = {}
for r in review_counts_data:
    bid = r['business_ref'].replace('businessref_', 'businessid_')
    review_counts[bid] = int(r['review_count'])

categories_count = {}

patterns = [
    r"services in (.*)",
    r"services including (.*)",
    r"seeking (.*)",
    r"fields of (.*)",
    r"category of (.*)"
]

unparsed = []

for b in businesses:
    desc = b.get('description', '')
    bid = b.get('business_id')
    count = review_counts.get(bid, 0)
    
    if desc.endswith('.'):
        desc = desc[:-1]
    
    cats_str = None
    for p in patterns:
        m = re.search(p, desc)
        if m:
            cats_str = m.group(1)
            break
            
    if not cats_str:
        unparsed.append(desc)
        continue
        
    cats_str = cats_str.strip("'\"")
    items = cats_str.split(',')
    for item in items:
        item = item.strip()
        if item.lower().startswith('and '):
            item = item[4:].strip()
        
        if item:
            categories_count[item] = categories_count.get(item, 0) + count

sorted_cats = sorted(categories_count.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps({"top_categories": sorted_cats[:10], "unparsed": unparsed}))"""

env_args = {'var_function-call-8147118810549250836': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-1831943725105221082': [{'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}], 'var_function-call-13000719492267290873': 26, 'var_function-call-5366253599007629493': ['businessid_6', 'businessid_13', 'businessid_79', 'businessid_15', 'businessid_33', 'businessid_36', 'businessid_60', 'businessid_12', 'businessid_31', 'businessid_57', 'businessid_86', 'businessid_62', 'businessid_37', 'businessid_92', 'businessid_26', 'businessid_68', 'businessid_41', 'businessid_10', 'businessid_53', 'businessid_45', 'businessid_96', 'businessid_98', 'businessid_14', 'businessid_20', 'businessid_74', 'businessid_66'], 'var_function-call-2511881889809102580': [{'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'."}]}

exec(code, env_args)
