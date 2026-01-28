code = """import json
import pandas as pd
import re

# Load data from the stored JSON files (file paths provided in variables)
with open(var_call_jZEL08NkDEmjwOrm2hls2Id8, 'r') as f:
    businesses = json.load(f)
with open(var_call_VHSQ4WPpBD7ghRgUueDxfic2, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Ensure columns exist
if 'business_id' not in df_b.columns:
    df_b['business_id'] = None
if 'description' not in df_b.columns:
    df_b['description'] = None

# Normalize types
df_b['business_id'] = df_b['business_id'].astype(str)
df_b['description'] = df_b['description'].astype(str)

# Define US state codes (50 states + DC)
states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

# Function to extract state code from description
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not desc or desc.lower() in ('none', 'nan'):
        return None
    # find all matches and return the first that is a valid US state code
    matches = state_pattern.findall(desc)
    for m in matches:
        if m in states:
            return m
    return None

df_b['state'] = df_b['description'].apply(extract_state)

# Prepare business_ref to join with reviews (replace prefix)
def to_business_ref(bid):
    return bid.replace('businessid_', 'businessref_')

df_b['business_ref'] = df_b['business_id'].apply(to_business_ref)

# Clean review ratings
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.NA

# Merge reviews with business info to get state for each review
df_merged = pd.merge(df_r, df_b[['business_ref','state','business_id','name']], on='business_ref', how='left')

# Drop reviews without state
df_merged = df_merged.dropna(subset=['state'])

# Compute total number of reviews per state (count of review rows)
reviews_by_state = df_merged.groupby('state').size()
if reviews_by_state.empty:
    result = {"state": None, "total_reviews": 0, "avg_review_rating": None, "avg_business_rating": None}
else:
    state_max = reviews_by_state.idxmax()
    total_reviews = int(reviews_by_state.max())
    # Average rating across all reviews in that state
    avg_review_rating = float(df_merged.loc[df_merged['state']==state_max, 'rating'].mean())
    # Average rating per business (first compute per-business average, then average those)
    biz_avg = df_merged[df_merged['state']==state_max].groupby('business_ref')['rating'].mean()
    avg_business_rating = float(biz_avg.mean()) if not biz_avg.empty else None
    result = {
        "state": state_max,
        "total_reviews": total_reviews,
        "avg_review_rating": round(avg_review_rating, 4) if avg_review_rating is not None else None,
        "avg_business_average_rating": round(avg_business_rating, 4) if avg_business_rating is not None else None
    }

import sys
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jZEL08NkDEmjwOrm2hls2Id8': 'file_storage/call_jZEL08NkDEmjwOrm2hls2Id8.json', 'var_call_VHSQ4WPpBD7ghRgUueDxfic2': 'file_storage/call_VHSQ4WPpBD7ghRgUueDxfic2.json'}

exec(code, env_args)
