code = """import json
import pandas as pd
import re

# Load reviews from the provided JSON file path (large result stored in a file)
with open(var_call_7GyE5BK438ZGhzrrRc5a3UDm, 'r') as f:
    reviews = json.load(f)

businesses = var_call_pQX5EYcHbXM3dsmb1fLPdaIB

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
# Ensure rating is numeric
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

df_business = pd.DataFrame(businesses)

# Extract state from description using regex (two-letter state abbreviation)
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Search for patterns like ", XX" where XX are uppercase letters
    m = re.search(r',\s*([A-Z]{2})(?:\b|,)', desc)
    if m:
        return m.group(1)
    # fallback: look for 'in City, ST' pattern
    m2 = re.search(r'in\s+[^,]+,\s*([A-Z]{2})', desc)
    if m2:
        return m2.group(1)
    return None

if 'description' in df_business.columns:
    df_business['state'] = df_business['description'].apply(extract_state)
else:
    df_business['state'] = None

# Map review business_ref to business_id by replacing prefix
if 'business_ref' in df_reviews.columns:
    df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
else:
    df_reviews['business_id'] = None

# Merge reviews with businesses to attach state
merged = pd.merge(df_reviews, df_business[['business_id', 'state']], on='business_id', how='left')

# Drop reviews without state
merged = merged[merged['state'].notna()]

# Group by state to compute counts and average rating
grouped = merged.groupby('state').agg(review_count=('rating', 'count'), average_rating=('rating', 'mean')).reset_index()

# If no data available, prepare empty result
if grouped.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    # Find state with highest number of reviews (if tie, pick first)
    top = grouped.sort_values(['review_count', 'average_rating'], ascending=[False, False]).iloc[0]
    result = {
        "state": str(top['state']),
        "review_count": int(top['review_count']),
        "average_rating": float(round(top['average_rating'], 3))
    }

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_bzO0DOGTem3DUAtYpd5ON8u9': ['checkin', 'business'], 'var_call_GscQQaO70wvN09o0WGq033xs': ['review', 'tip', 'user'], 'var_call_pQX5EYcHbXM3dsmb1fLPdaIB': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_7GyE5BK438ZGhzrrRc5a3UDm': 'file_storage/call_7GyE5BK438ZGhzrrRc5a3UDm.json'}

exec(code, env_args)
