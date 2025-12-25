code = """import pandas as pd
import json

business_data_full_string = locals()['var_function-call-524677173873361957']['results'][0]

# Find the start and end of the actual JSON array
start_index = business_data_full_string.find('[')
end_index = business_data_full_string.rfind(']')

if start_index != -1 and end_index != -1 and end_index > start_index:
    json_string_only = business_data_full_string[start_index : end_index + 1]
    businesses_with_wifi_data = json.loads(json_string_only)
else:
    print('__RESULT__:')
    print(json.dumps({'top_state': None, 'top_state_business_refs': []}))
    exit()

businesses_with_wifi_df = pd.DataFrame(businesses_with_wifi_data)

# Filter for businesses that offer WiFi (excluding 'no' or False)
wifi_businesses = businesses_with_wifi_df[
    businesses_with_wifi_df['attributes'].apply(
        lambda x: x and str(x.get('WiFi')) in ["u'free'", "u'yes'", "True"]
    )
].copy()

# Extract state from description
wifi_businesses['state'] = wifi_businesses['description'].str.extract(r', ([A-Z]{2}),')

# Drop rows where state extraction failed (NaN)
wifi_businesses = wifi_businesses.dropna(subset=['state'])

# Count businesses per state
state_counts = wifi_businesses['state'].value_counts().reset_index()
state_counts.columns = ['state', 'business_count']

# Get the state with the highest number of businesses offering WiFi
if not state_counts.empty:
    top_state = state_counts.loc[state_counts['business_count'].idxmax()]
    top_state_name = top_state['state']
    top_state_business_ids = wifi_businesses[wifi_businesses['state'] == top_state_name]['business_id'].tolist()

    # Convert business_id format for joining with review table
    top_state_business_refs = [biz_id.replace('businessid_', 'businessref_') for biz_id in top_state_business_ids]
else:
    top_state_name = None
    top_state_business_refs = []

print('__RESULT__:')
print(json.dumps({'top_state': top_state_name, 'top_state_business_refs': top_state_business_refs}))"""

env_args = {'var_function-call-524677173873361957': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
