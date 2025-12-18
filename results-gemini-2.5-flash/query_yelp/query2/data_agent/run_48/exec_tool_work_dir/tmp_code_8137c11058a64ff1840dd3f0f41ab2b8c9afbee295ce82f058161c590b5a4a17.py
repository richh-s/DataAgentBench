code = """import pandas as pd
business_data = locals()['var_function-call-18032303694745153758']
df_business = pd.DataFrame(business_data)

def extract_state(description):
    if description:
        parts = description.split(' in ')
        if len(parts) > 1:
            location_part = parts[1]
            city_state_zip = location_part.split(', ')
            if len(city_state_zip) > 1:
                state_zip = city_state_zip[1].split(' ')
                if len(state_zip) > 0:
                    return state_zip[0]
    return None

df_business['state'] = df_business['description'].apply(extract_state)
df_business['review_count'] = pd.to_numeric(df_business['review_count'], errors='coerce')

state_review_counts = df_business.groupby('state')['review_count'].sum().reset_index()
highest_review_state = state_review_counts.loc[state_review_counts['review_count'].idxmax()]

result = {'highest_review_state': highest_review_state['state'], 'total_reviews': highest_review_state['review_count']}
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-1861702230981586687': ['business', 'checkin'], 'var_function-call-11945419130728904587': ['review', 'tip', 'user'], 'var_function-call-18032303694745153758': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
