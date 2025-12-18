code = """import pandas as pd
import re
import json

query_result_str = locals()['var_function-call-8085027810388199841']['query_db_response']['results'][0]

# Extract the JSON array string using regex
match = re.search(r'\[.*\]', query_result_str, re.DOTALL)
if match:
    business_data_json_str = match.group(0)
else:
    raise ValueError("Could not find JSON array in the query result string.")

business_data = json.loads(business_data_json_str)
df_business = pd.DataFrame(business_data)

def extract_state(description):
    match = re.search(r'in ([A-Z]{2}),', description)
    if match:
        return match.group(1)
    return None

df_business['state'] = df_business['description'].apply(extract_state)
df_business['review_count'] = pd.to_numeric(df_business['review_count'])

df_business_filtered = df_business.dropna(subset=['state'])

state_review_counts = df_business_filtered.groupby('state')['review_count'].sum().reset_index()
highest_review_state_info = state_review_counts.loc[state_review_counts['review_count'].idxmax()]

highest_review_state = highest_review_state_info['state']

business_ids_in_highest_review_state = df_business_filtered[df_business_filtered['state'] == highest_review_state]['business_id'].tolist()

business_refs_in_highest_review_state = [biz_id.replace('businessid_', 'businessref_') for biz_id in business_ids_in_highest_review_state]

print('__RESULT__:')
print(json.dumps({
    "highest_review_state": highest_review_state,
    "business_refs": business_refs_in_highest_review_state
}))"""

env_args = {'var_function-call-8085027810388199841': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
