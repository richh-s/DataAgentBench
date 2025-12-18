code = """import pandas as pd
import json
import re

business_data = locals()['var_function-call-3588827974056047557']
df_business = pd.DataFrame(business_data)

# Filter for businesses that offer WiFi (excluding 'no' and 'paid')
df_wifi_businesses = df_business[df_business['attributes'].apply(lambda x: x.get('WiFi') == "u'free'")]

# Function to extract state using regex
def extract_state_refined(description):
    if isinstance(description, str):
        match = re.search(r',\s*([A-Z]{2})(?:\s|\.)', description)
        if match:
            return match.group(1)
    return None

df_wifi_businesses['state'] = df_wifi_businesses['description'].apply(extract_state_refined)

# Drop rows where state could not be extracted
df_wifi_businesses = df_wifi_businesses.dropna(subset=['state'])

# Clean up business_id for joining (prefix for review table is businessref_)
df_wifi_businesses['business_ref'] = df_wifi_businesses['business_id'].apply(lambda x: x.replace('businessid_', 'businessref_'))

# Select relevant columns
wifi_businesses_output = df_wifi_businesses[['business_ref', 'state']].to_json(orient='records')

print('__RESULT__:')
print(wifi_businesses_output)"""

env_args = {'var_function-call-3588827974056047557': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_function-call-13025557474635624925': [{'business_id_clean': '64', 'state': 'Beauty'}, {'business_id_clean': '54', 'state': 'and'}, {'business_id_clean': '91', 'state': 'making'}]}

exec(code, env_args)
