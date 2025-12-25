code = """import json

businesses_accept_cc = locals()['var_function-call-7682599052518415997']
category_counts = {}
business_ids_by_category = {}

for business in businesses_accept_cc:
    description = business['description']
    business_id = business['business_id']

    # Split the description to get the categories part
    if "services in " in description:
        categories_part = description.split("services in ", 1)[1]
        # Split by ', and ' first to handle the last 'and' case
        temp_categories = categories_part.split(', and ')
        # Then split the remaining parts by ', '
        all_categories = []
        for tc in temp_categories:
            all_categories.extend(tc.split(', '))
        
        # Clean up categories (remove trailing periods and strip whitespace)
        cleaned_categories = [cat.replace('.', '').strip() for cat in all_categories if cat.strip()]
        
        for category in cleaned_categories:
            category_counts[category] = category_counts.get(category, 0) + 1
            if category not in business_ids_by_category:
                business_ids_by_category[category] = []
            business_ids_by_category[category].append(business_id)

max_category = None
max_count = 0

for category, count in category_counts.items():
    if count > max_count:
        max_count = count
        max_category = category

# Get business_ids for the max_category
business_ids_for_max_category = business_ids_by_category.get(max_category, [])

print("__RESULT__:")
print(json.dumps({
    'max_category': max_category,
    'max_count': max_count,
    'business_ids_for_max_category': business_ids_for_max_category
}))"""

env_args = {'var_function-call-8206199070460095541': ['checkin', 'business'], 'var_function-call-12483048272205992477': [], 'var_function-call-15936352313412126287': [{'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}], 'var_function-call-7682599052518415997': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-15031399990858659041': {'max_category': 'Montessori Schools.', 'max_count': 1}}

exec(code, env_args)
