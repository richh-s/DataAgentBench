code = """import json

businesses_accept_cc = locals()['var_function-call-7682599052518415997']['results']
category_counts = {}

for business in businesses_accept_cc:
    description = business['description']
    # Categories are at the end, separated by ', and '.
    if ' and ' in description:
        categories_str = description.split(', and ')[-1]
        categories = categories_str.split(', ')
        for category in categories:
            category_counts[category] = category_counts.get(category, 0) + 1

max_category = None
max_count = 0

for category, count in category_counts.items():
    if count > max_count:
        max_count = count
        max_category = category

print("__RESULT__:")
print(json.dumps({'max_category': max_category, 'max_count': max_count}))"""

env_args = {'var_function-call-8206199070460095541': ['checkin', 'business'], 'var_function-call-12483048272205992477': [], 'var_function-call-15936352313412126287': [{'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}], 'var_function-call-7682599052518415997': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
