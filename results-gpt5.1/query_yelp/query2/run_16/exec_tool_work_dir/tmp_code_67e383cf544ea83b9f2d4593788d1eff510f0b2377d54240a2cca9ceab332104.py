code = """import re, json, pandas as pd

# Load full review data from file path
import pathlib, json as js
reviews_path = var_call_2RZmtozw2aybz9XvWvytJXP7
with open(reviews_path, 'r') as f:
    reviews = js.load(f)

# Business data is directly available
business = var_call_MizXPnEaNq3DH3N7680vCBH0

# Create DataFrames
rev_df = pd.DataFrame(reviews)
# ratings are strings, convert to int
rev_df['rating'] = rev_df['rating'].astype(int)

biz_df = pd.DataFrame(business)

# Extract state abbreviation from description using regex: ", XX" where XX is 2 capital letters
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1)
    return None

biz_df['state'] = biz_df['description'].apply(extract_state)

# Filter to U.S. state codes (50 states + DC)
valid_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])
biz_df = biz_df[biz_df['state'].isin(valid_states)]

# Map business_id to business_ref prefix change
# businessid_123 -> businessref_123
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Merge reviews with business states
merged = rev_df.merge(biz_df[['business_ref','state']], on='business_ref', how='inner')

# Compute per-state review counts and average ratings
state_stats = merged.groupby('state').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()

# Find state with max reviews
if state_stats.empty:
    result = {"state": None, "review_count": 0, "avg_rating": None}
else:
    top = state_stats.sort_values(['review_count','state'], ascending=[False, True]).iloc[0]
    result = {
        'state': top['state'],
        'review_count': int(top['review_count']),
        'avg_rating': round(float(top['avg_rating']), 3)
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nE02a9VBJOQGluhU2qRjFT5v': [{'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}], 'var_call_2RZmtozw2aybz9XvWvytJXP7': 'file_storage/call_2RZmtozw2aybz9XvWvytJXP7.json', 'var_call_MizXPnEaNq3DH3N7680vCBH0': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
