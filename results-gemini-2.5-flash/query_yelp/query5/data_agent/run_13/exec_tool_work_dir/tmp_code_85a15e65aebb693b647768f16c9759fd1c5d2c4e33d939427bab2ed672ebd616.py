code = """import pandas as pd
import json
import re

# The result from query_db is a list where the first element contains the JSON string.
business_data_raw = locals()['var_function-call-6159886771663471372']['results'][0]

# Extract the JSON array string using regex
json_match = re.search(r'\[.*?\]', business_data_raw, re.DOTALL)
if json_match:
    business_data_str = json_match.group(0)
    business_data = json.loads(business_data_str)
else:
    business_data = [] # Handle case where JSON is not found

df_business = pd.DataFrame(business_data)

def extract_state(description):
    # The state is usually a 2-letter uppercase code following a comma and space.
    match = re.search(r',\s([A-Z]{2})(?:\s|$|,)', description)
    if match:
        return match.group(1)
    return None

df_business['state'] = df_business['description'].apply(extract_state)
df_business['business_ref'] = df_business['business_id'].str.replace('businessid_', 'businessref_')

# Filter for businesses with extracted states and WiFi
wifi_businesses = df_business[df_business['state'].notna()][['business_ref', 'state']]

print('__RESULT__:')
print(wifi_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-6159886771663471372': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
