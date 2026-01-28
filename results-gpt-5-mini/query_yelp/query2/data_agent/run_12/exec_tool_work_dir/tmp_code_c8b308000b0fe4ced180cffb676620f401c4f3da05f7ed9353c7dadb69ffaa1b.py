code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_29NbFVBLxVQw9DZ4jU0BHgZN, 'r') as f:
    business_data = json.load(f)
with open(var_call_zJ3tUM6dqGmRVBAGwQKmuy8R, 'r') as f:
    review_data = json.load(f)

dfb = pd.DataFrame(business_data)
dfr = pd.DataFrame(review_data)

# Extract state from description
pattern = re.compile(r",\s*([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    if m:
        return m.group(1)
    # fallback: look for 'City, ST' without comma? try any two-letter uppercase
    m2 = re.search(r"\b([A-Z]{2})\b", desc)
    return m2.group(1) if m2 else None

dfb['state'] = dfb['description'].apply(extract_state)

# Convert review_count to numeric
dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce').fillna(0).astype(int)

# Sum reviews by state
state_reviews = dfb.groupby('state', dropna=True)['review_count'].sum()
if state_reviews.empty:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    top_state = state_reviews.idxmax()
    total_reviews = int(state_reviews.loc[top_state])

    # Get business_refs for that state (convert prefixes)
    biz_ids = dfb.loc[dfb['state'] == top_state, 'business_id'].dropna().unique().tolist()
    biz_refs = [b.replace('businessid_', 'businessref_') for b in biz_ids]
    biz_ref_set = set(biz_refs)

    # Filter reviews for these business_refs
    if 'business_ref' in dfr.columns:
        dfr_filtered = dfr[dfr['business_ref'].isin(biz_ref_set)].copy()
        if not dfr_filtered.empty:
            dfr_filtered['rating'] = pd.to_numeric(dfr_filtered['rating'], errors='coerce')
            avg_rating = float(dfr_filtered['rating'].mean())
        else:
            avg_rating = None
    else:
        avg_rating = None

    result = {"state": top_state, "total_reviews": total_reviews, "average_rating": (None if avg_rating is None else round(avg_rating, 3))}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QVob1VqNPAgiofwEAKHrIiTr': ['checkin', 'business'], 'var_call_Pnw1vvitcoZD7CwhfWOMCoaw': ['review', 'tip', 'user'], 'var_call_29NbFVBLxVQw9DZ4jU0BHgZN': 'file_storage/call_29NbFVBLxVQw9DZ4jU0BHgZN.json', 'var_call_zJ3tUM6dqGmRVBAGwQKmuy8R': 'file_storage/call_zJ3tUM6dqGmRVBAGwQKmuy8R.json'}

exec(code, env_args)
