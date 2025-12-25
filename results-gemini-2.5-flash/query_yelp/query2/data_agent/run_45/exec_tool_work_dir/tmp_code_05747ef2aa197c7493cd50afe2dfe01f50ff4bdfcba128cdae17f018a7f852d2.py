code = """import json
import re
import pandas as pd

business_data = locals()['var_function-call-9968362349435832335']

# Extract business_id, review_count, and state from description
extracted_business_data = []
for business in business_data:
    business_id = business.get('business_id')
    review_count = int(business.get('review_count', 0))
    description = business.get('description', '')

    # Extract state from description using regex
    state_match = re.search(r',\s*([A-Z]{2})\b', description)
    state = state_match.group(1) if state_match else 'Unknown'

    extracted_business_data.append({
        'business_id': business_id,
        'review_count': review_count,
        'state': state
    })

df_business = pd.DataFrame(extracted_business_data)

# Remove the 'businessid_' prefix from 'business_id' for merging
df_business['business_id_cleaned'] = df_business['business_id'].str.replace('businessid_', '')

review_data = locals()['var_function-call-7138576747902570682']

df_review = pd.DataFrame(review_data)

# Remove the 'businessref_' prefix from 'business_ref' for merging
df_review['business_ref_cleaned'] = df_review['business_ref'].str.replace('businessref_', '')

# Merge the two dataframes
merged_df = pd.merge(df_business, df_review, left_on='business_id_cleaned', right_on='business_ref_cleaned', how='inner')

# Calculate total review count per state
state_review_counts = merged_df.groupby('state')['review_count'].sum().reset_index()

# Find the state with the highest review count
state_with_highest_reviews = state_review_counts.loc[state_review_counts['review_count'].idxmax()]
highest_review_state = state_with_highest_reviews['state']

# Calculate the average rating for businesses in the state with the highest reviews
avg_rating_highest_review_state = merged_df[merged_df['state'] == highest_review_state]['rating'].astype(int).mean()

print('__RESULT__:')
print(json.dumps({
    'state_with_highest_reviews': highest_review_state,
    'average_rating': avg_rating_highest_review_state
}))"""

env_args = {'var_function-call-2935976998528478912': 'file_storage/function-call-2935976998528478912.json', 'var_function-call-9968362349435832335': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-7138576747902570682': 'file_storage/function-call-7138576747902570682.json'}

exec(code, env_args)
