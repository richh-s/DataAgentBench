code = """import json, pandas as pd

biz_with_wifi = var_call_IKdmUAzzyxmy5F19bvraWWbs
review_path = var_call_A90UHucgGAXT4z8sxdlrSLZi

with open(review_path, 'r') as f:
    reviews = json.load(f)

biz_df = pd.DataFrame(biz_with_wifi)
# extract state from description, assuming pattern 'City, ST'
import re

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r",\s*([A-Z]{2})\b", desc)
    return m.group(1) if m else None

biz_df['state'] = biz_df['description'].apply(extract_state)

# map business_id to business_ref
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

rev_df = pd.DataFrame(reviews)
rev_df['rating'] = rev_df['rating'].astype(float)

# join reviews to wifi businesses
merged = pd.merge(rev_df, biz_df[['business_ref','state']], on='business_ref', how='inner')

# count wifi businesses per state (unique businesses)
biz_state_counts = biz_df.groupby('state')['business_id'].nunique().reset_index(name='wifi_business_count')

# average rating per state for wifi businesses
state_ratings = merged.groupby('state')['rating'].mean().reset_index(name='avg_rating')

summary = pd.merge(biz_state_counts, state_ratings, on='state', how='left')
summary = summary.sort_values('wifi_business_count', ascending=False)

# get top state (if tie, first in sort)
if not summary.empty:
    top = summary.iloc[0].to_dict()
    result = {
        'state_with_most_wifi_businesses': top['state'],
        'wifi_business_count': int(top['wifi_business_count']),
        'average_rating_for_wifi_businesses_in_state': round(float(top['avg_rating']), 3) if pd.notna(top['avg_rating']) else None
    }
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_IKdmUAzzyxmy5F19bvraWWbs': [{'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_call_A90UHucgGAXT4z8sxdlrSLZi': 'file_storage/call_A90UHucgGAXT4z8sxdlrSLZi.json'}

exec(code, env_args)
