code = """import pandas as pd
import re
import json

business_data_raw = locals()['var_function-call-14800440221700262084']['results']
business_data = [json.loads(item) for item in business_data_raw]

df = pd.DataFrame(business_data)

# Filter for businesses with WiFi (not 'no')
df_wifi = df[df['attributes'].apply(lambda x: x.get('WiFi') not in ["u'no'", "'no'", 'no'])]

# Extract state from description
def extract_state(description):
    match = re.search(r',\s*([A-Z]{2})\b', description)
    return match.group(1) if match else None

df_wifi['state'] = df_wifi['description'].apply(extract_state)

# Filter out rows where state could not be extracted
df_wifi = df_wifi.dropna(subset=['state'])

# Get business_ids for filtering reviews later
business_ids_with_wifi = df_wifi['business_id'].tolist()

# Count businesses per state
state_counts = df_wifi['state'].value_counts().reset_index()
state_counts.columns = ['state', 'business_count']

# Find the state with the highest number of businesses
highest_state = state_counts.loc[state_counts['business_count'].idxmax()]

# Store results for later use
result = {
    'highest_state': highest_state.to_dict(),
    'business_ids_with_wifi': business_ids_with_wifi
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14800440221700262084': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
