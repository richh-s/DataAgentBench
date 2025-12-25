code = """import pandas as pd
import re
import json

business_data_raw_string = locals()['var_function-call-9847933403698828291']['query_db_response']['results'][0]

# Extract the JSON array string using regex
match = re.search(r'(\[.*?\])', business_data_raw_string, re.DOTALL)

business_data_list = []
if match:
    json_string = match.group(1)
    business_data_list = json.loads(json_string)

df_business = pd.DataFrame(business_data_list)

def extract_state(description):
    match = re.search(r', ([A-Z]{2}),', description)
    if match:
        return match.group(1)
    return None

df_business['state'] = df_business['description'].apply(extract_state)
df_business['review_count'] = pd.to_numeric(df_business['review_count'])

# Drop rows where state is None before finding the state with the highest review count
df_business_filtered = df_business.dropna(subset=['state'])

state_review_counts = df_business_filtered.groupby('state')['review_count'].sum().reset_index()

highest_review_state = None
formatted_business_ids = []

if not state_review_counts.empty:
    highest_review_state_row = state_review_counts.loc[state_review_counts['review_count'].idxmax()]
    highest_review_state = highest_review_state_row['state']

    business_ids_in_highest_state = df_business_filtered[df_business_filtered['state'] == highest_review_state]['business_id'].tolist()
    # Format business_ids for SQL query by replacing 'businessid_' with 'businessref_'
    formatted_business_ids = [bid.replace("businessid_", "businessref_") for bid in business_ids_in_highest_state]

print('__RESULT__:')
print(json.dumps({'highest_review_state': highest_review_state, 'formatted_business_ids': formatted_business_ids}))"""

env_args = {'var_function-call-17440068663410546858': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-9847933403698828291': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
