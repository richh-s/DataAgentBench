code = """import pandas as pd
import json
import re

business_data_message = locals()['var_function-call-5955670962806364541']['results'][0]

# Extract the JSON array string using regex
match = re.search(r'\[.*\]', business_data_message, re.DOTALL)
if match:
    json_string = match.group(0)
    business_data_list = json.loads(json_string)
    df_business = pd.DataFrame(business_data_list)

    def extract_state(description):
        if description and ' in ' in description:
            location_part = description.split(' in ')[-1]
            city_state_zip_parts = location_part.split(', ')
            if len(city_state_zip_parts) >= 2:
                state_zip = city_state_zip_parts[1].strip()
                state_code = state_zip.split(' ')[0]
                return state_code.strip()
        return None

    df_business['state'] = df_business['description'].apply(extract_state)
    df_business['review_count'] = pd.to_numeric(df_business['review_count'])

    df_us_businesses = df_business.dropna(subset=['state'])

    state_review_counts = df_us_businesses.groupby('state')['review_count'].sum().reset_index()
    highest_review_state_row = state_review_counts.loc[state_review_counts['review_count'].idxmax()]

    highest_review_state_name = highest_review_state_row['state']

    business_ids_in_highest_state = df_us_businesses[df_us_businesses['state'] == highest_review_state_name]['business_id'].tolist()

    # Transform business_id to business_ref format
    business_refs_in_highest_state = [bid.replace("businessid_", "businessref_") for bid in business_ids_in_highest_state]

    result = {
        'highest_review_state': highest_review_state_name,
        'business_refs': business_refs_in_highest_state
    }
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'Could not extract JSON from the business data message.'}))"""

env_args = {'var_function-call-5955670962806364541': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
