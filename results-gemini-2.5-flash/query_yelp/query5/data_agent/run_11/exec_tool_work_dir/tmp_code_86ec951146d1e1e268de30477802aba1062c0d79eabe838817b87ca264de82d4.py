code = """import json
import pandas as pd

businesses_with_wifi = locals()['var_function-call-12877081103103650348']['query_db_response']['results']
df_businesses = pd.DataFrame(businesses_with_wifi)

# Filter for businesses where WiFi is offered (not 'no')
df_businesses_filtered = df_businesses[df_businesses['attributes'].apply(lambda x: x.get('WiFi') not in ["u'no'", "no"])]

# Extract state from description
def extract_state(description):
    if description:
        parts = description.split(',')
        if len(parts) >= 2:
            city_state_zip = parts[-2].strip().split(' ')
            if len(city_state_zip) >= 2:
                return city_state_zip[-2] # Assuming state is the second to last element
    return None

df_businesses_filtered['state'] = df_businesses_filtered['description'].apply(extract_state)

# Count businesses per state
state_counts = df_businesses_filtered['state'].value_counts().reset_index()
state_counts.columns = ['state', 'business_count']

# Get the state with the highest number of businesses with WiFi
top_state = state_counts.loc[state_counts['business_count'].idxmax()]
top_state_name = top_state['state']
top_state_business_ids = df_businesses_filtered[df_businesses_filtered['state'] == top_state_name]['business_id'].tolist()

# Convert business_id to business_ref format
top_state_business_refs = [bid.replace('businessid_', 'businessref_') for bid in top_state_business_ids]

print('__RESULT__:')
print(json.dumps({'top_state_name': top_state_name, 'top_state_business_refs': top_state_business_refs}))"""

env_args = {'var_function-call-12877081103103650348': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
