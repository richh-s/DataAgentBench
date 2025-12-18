code = """import pandas as pd
business_data = locals()['var_function-call-9640767253786095022']
df_business = pd.DataFrame(business_data)

def extract_state(description):
    if description and ' in ' in description:
        parts = description.split(' in ')
        if len(parts) > 1:
            location_part = parts[1]
            if ',' in location_part:
                state_zip = location_part.split(',')[1].strip()
                if len(state_zip.split()) > 1:
                    return state_zip.split()[0]
    return None

df_business['state'] = df_business['description'].apply(extract_state)

print('__RESULT__:')
print(df_business['state'].value_counts().to_json())"""

env_args = {'var_function-call-9640767253786095022': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
