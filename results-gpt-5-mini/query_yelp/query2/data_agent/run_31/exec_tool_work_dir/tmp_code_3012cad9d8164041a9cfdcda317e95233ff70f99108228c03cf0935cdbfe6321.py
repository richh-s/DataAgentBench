code = """import json
import pandas as pd
import re

# Load business data
with open(var_call_vMGXuI53wq0eW4Vemftx7DtR, 'r') as f:
    businesses = json.load(f)

# Load reviews data
with open(var_call_4HQRgdsBpQAu39sp5yy9i8TJ, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Ensure review_count numeric
if 'review_count' in bdf.columns:
    bdf['review_count'] = pd.to_numeric(bdf['review_count'], errors='coerce').fillna(0).astype(int)
else:
    bdf['review_count'] = 0

# Extract state abbreviation from description using regex
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Look for pattern ', XX' where XX are two uppercase letters
    m = re.search(r',\s*([A-Z]{2})(?:[,\.]|\s|$)', desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf.get('description', '').apply(extract_state)

# Drop rows without state
bdf_states = bdf.dropna(subset=['state']).copy()

# Sum review_count by state
state_reviews = bdf_states.groupby('state')['review_count'].sum().reset_index()
if state_reviews.empty:
    result = {'state': None, 'total_reviews': 0, 'average_rating': None}
else:
    # Find state with highest number of reviews
    top = state_reviews.sort_values('review_count', ascending=False).iloc[0]
    top_state = top['state']
    total_reviews = int(top['review_count'])

    # Find business_ids in that state and map to business_ref
    biz_ids = bdf_states.loc[bdf_states['state'] == top_state, 'business_id'].astype(str).tolist()
    # Convert businessid_# -> businessref_#
    biz_refs = [bid.replace('businessid_', 'businessref_') for bid in biz_ids]

    # Filter reviews for these business_refs
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
    rdf_filtered = rdf[rdf['business_ref'].isin(biz_refs)]

    if rdf_filtered.empty:
        avg_rating = None
    else:
        avg_rating = float(rdf_filtered['rating'].mean())

    result = {'state': top_state, 'total_reviews': total_reviews, 'average_rating': avg_rating}

import json
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_W0QWXsiSpVgJm2BCZSW1e27L': ['checkin', 'business'], 'var_call_hjslD6OF7jzHMRitQ48vuV5W': ['review', 'tip', 'user'], 'var_call_CKGBWQXersjt2ti94Aw4L5Id': 'file_storage/call_CKGBWQXersjt2ti94Aw4L5Id.json', 'var_call_vMGXuI53wq0eW4Vemftx7DtR': 'file_storage/call_vMGXuI53wq0eW4Vemftx7DtR.json', 'var_call_4HQRgdsBpQAu39sp5yy9i8TJ': 'file_storage/call_4HQRgdsBpQAu39sp5yy9i8TJ.json'}

exec(code, env_args)
