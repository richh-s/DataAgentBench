code = """import pandas as pd
import json

df_business = pd.DataFrame(locals()['var_function-call-216222473230292108'])

with open(locals()['var_function-call-4508870068286011511'], 'r') as f:
    reviews_data = json.load(f)
df_reviews = pd.DataFrame(reviews_data)

def extract_state(description):
    if isinstance(description, str):
        parts = description.split(' in ')
        if len(parts) > 1:
            location_part = parts[1]
            state_zip_city = location_part.split(',')
            if len(state_zip_city) > 1:
                state = state_zip_city[1].strip().split(' ')[0]
                return state
    return None

df_business['state'] = df_business['description'].apply(extract_state)
df_business['review_count'] = pd.to_numeric(df_business['review_count'])

# Normalize business_id and business_ref for merging
df_business['normalized_business_id'] = df_business['business_id'].apply(lambda x: x.replace('businessid_', ''))
df_reviews['normalized_business_id'] = df_reviews['business_ref'].apply(lambda x: x.replace('businessref_', ''))

merged_df = pd.merge(df_business, df_reviews, on='normalized_business_id', how='inner')

state_review_counts = merged_df.groupby('state')['review_count'].sum().reset_index()
highest_review_state = state_review_counts.loc[state_review_counts['review_count'].idxmax()]

state_with_highest_reviews = highest_review_state['state']

average_rating_in_highest_state = merged_df[merged_df['state'] == state_with_highest_reviews]['rating'].astype(float).mean()

result = {
    'state_with_highest_reviews': state_with_highest_reviews,
    'average_rating': average_rating_in_highest_state
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-216222473230292108': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-17670146689017691690': {'state': 'MO', 'review_count': 81}, 'var_function-call-4508870068286011511': 'file_storage/function-call-4508870068286011511.json'}

exec(code, env_args)
