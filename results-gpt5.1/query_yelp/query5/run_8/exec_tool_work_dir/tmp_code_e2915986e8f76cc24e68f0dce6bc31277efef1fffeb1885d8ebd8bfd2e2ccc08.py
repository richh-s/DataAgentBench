code = """import json, pandas as pd, re

biz_wifi = pd.DataFrame(var_call_TX9VfiRhK2xK7KAt7q5EMr0X)

# Extract state abbreviation from description (e.g., ", CA,")
state_pattern = re.compile(r',\s*([A-Z]{2})\s*,')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    return m.group(1) if m else None

biz_wifi['state'] = biz_wifi['description'].apply(extract_state)

# Count businesses with WiFi per state
state_counts = biz_wifi.groupby('state', dropna=True)['business_id'].nunique().reset_index(name='wifi_business_count')

# Determine state with max count
if state_counts.empty:
    result = {"state": None, "wifi_business_count": 0, "avg_rating": None}
else:
    top_state_row = state_counts.sort_values(['wifi_business_count','state'], ascending=[False,True]).iloc[0]
    top_state = top_state_row['state']

    # Load reviews file
    import os
    with open(var_call_KfZZpwZhuIrvAk4avAbGNDF4, 'r') as f:
        reviews = json.load(f)
    rev_df = pd.DataFrame(reviews)

    # Normalize types
    rev_df['rating'] = rev_df['rating'].astype(float)

    # Map business_id -> business_ref
    biz_wifi['business_ref'] = biz_wifi['business_id'].str.replace('businessid_', 'businessref_', regex=False)

    # Filter to businesses in top_state
    top_biz_refs = biz_wifi.loc[biz_wifi['state'] == top_state, 'business_ref'].unique()

    # Filter reviews to those businesses
    top_rev = rev_df[rev_df['business_ref'].isin(top_biz_refs)]

    avg_rating = float(top_rev['rating'].mean()) if not top_rev.empty else None

    result = {"state": top_state, "wifi_business_count": int(top_state_row['wifi_business_count']), "avg_rating": avg_rating}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TX9VfiRhK2xK7KAt7q5EMr0X': [{'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_call_KfZZpwZhuIrvAk4avAbGNDF4': 'file_storage/call_KfZZpwZhuIrvAk4avAbGNDF4.json'}

exec(code, env_args)
