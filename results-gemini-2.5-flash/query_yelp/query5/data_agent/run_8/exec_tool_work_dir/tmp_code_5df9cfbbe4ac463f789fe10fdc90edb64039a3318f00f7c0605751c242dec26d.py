code = """import json
import re
import pandas as pd

business_info_output = locals()['var_function-call-4873346791893292572']['results'][0]

# Extract the JSON array string from the message using a regex that captures everything between the first '[' and the last ']'
json_array_match = re.search(r'\[.*\]', business_info_output, re.DOTALL)

businesses_with_wifi = []
if json_array_match:
    json_array_string = json_array_match.group(0)
    try:
        businesses_with_wifi = json.loads(json_array_string)
    except json.JSONDecodeError as e:
        # Log error for debugging, though in this environment it will be printed if it occurs.
        print(f"JSON decoding error: {e}")

def extract_state(description):
    # Regex to find a two-letter uppercase state code preceded by ', ' and followed by ',' or end of string
    match = re.search(r',\s*([A-Z]{2})(?:,|$)', description)
    if match:
        return match.group(1)
    return None

business_with_states_list = []
for business in businesses_with_wifi:
    if isinstance(business, dict):
        state = extract_state(business.get('description', ''))
        if state:
            business_id = business.get('business_id')
            if business_id:
                # Convert business_id to business_ref by replacing the prefix
                business_ref = business_id.replace('businessid_', 'businessref_')
                business_with_states_list.append({'business_ref': business_ref, 'state': state})

# Convert to DataFrame for easier manipulation
df_businesses_with_wifi = pd.DataFrame(business_with_states_list)

# Aggregate to count businesses per state
state_counts = df_businesses_with_wifi['state'].value_counts().reset_index()
state_counts.columns = ['state', 'business_count']

# Get business_refs to query for reviews
business_refs_for_query = df_businesses_with_wifi['business_ref'].tolist()

# Convert list of business_refs to a format suitable for SQL IN clause
business_refs_str = ", ".join(f"'{ref}'" for ref in business_refs_for_query)

# Store the processed data and the query string for the next step
print('__RESULT__:')
print(json.dumps({
    'df_businesses_with_wifi': df_businesses_with_wifi.to_json(orient='records'),
    'business_refs_str': business_refs_str
}))"""

env_args = {'var_function-call-18163551906860618306': ['business', 'checkin'], 'var_function-call-4873346791893292572': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
