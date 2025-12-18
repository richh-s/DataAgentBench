code = """import pandas as pd
import re
import json

businesses_credit_card = pd.DataFrame(locals()['var_function-call-16338033825438695023'])

def extract_categories(description):
    match = re.search(r'providing a range of services in (.*)\.', description)
    if match:
        categories_str = match.group(1)
        return [cat.strip() for cat in categories_str.split(', ')]
    match = re.search(r'this establishment offers a wide range of services, including (.*)\.', description)
    if match:
        categories_str = match.group(1)
        return [cat.strip() for cat in categories_str.split(', ')]
    match = re.search(r'this facility offers enthusiasts a premier destination for (.*)\.', description)
    if match:
        categories_str = match.group(1)
        return [cat.strip() for cat in categories_str.split(', ')]
    match = re.search(r'this establishment offers a range of services including (.*)\.', description)
    if match:
        categories_str = match.group(1)
        return [cat.strip() for cat in categories_str.split(', ')]
    match = re.search(r'this business offers a diverse range of services and products in the fields of (.*)\.', description)
    if match:
        categories_str = match.group(1)
        return [cat.strip() for cat in categories_str.split(', ')]
    return []

businesses_credit_card['categories'] = businesses_credit_card['description'].apply(extract_categories)

exploded_businesses = businesses_credit_card.explode('categories')

beauty_spas_businesses = exploded_businesses[exploded_businesses['categories'] == 'Beauty & Spas']

business_ids_beauty_spas = beauty_spas_businesses['business_id'].str.replace("businessid_", "businessref_").tolist()

print("__RESULT__:")
print(json.dumps(business_ids_beauty_spas))"""

env_args = {'var_function-call-1116522841368556705': ['business', 'checkin'], 'var_function-call-9107770549610480261': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-13950439019693685678': ['review', 'tip', 'user'], 'var_function-call-16338033825438695023': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-11636320669866461942': {'category': 'Beauty & Spas', 'count': 3}}

exec(code, env_args)
