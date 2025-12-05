code = """import json, re, pandas as pd
from pathlib import Path

# Load full results from files
with open(var_call_f6pgaggJwLAVXpKn3bPgWAX2, 'r') as f:
    business_records = json.load(f)
with open(var_call_yX3BkSjmthOiNfLHxSUnkqVg, 'r') as f:
    review_records = json.load(f)

bdf = pd.DataFrame(business_records)
rdf = pd.DataFrame(review_records)

# Extract state abbreviation from description (pattern like ", XX" before ZIP or end, or " in City, XX,")
state_pattern = re.compile(r',\s*([A-Z]{2})(?:\s*\d{5})?[, ]')

def extract_state(desc: str):
    if not isinstance(desc, str):
        return None
    # common phrasing: "in City, ST," or "in City, ST "
    m = re.search(r'in [^,]+,\s*([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    m = state_pattern.search(desc + ' ')
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Map business_id -> state
state_map = bdf.set_index('business_id')['state'].to_dict()

# Convert business_ref (businessref_X) to business_id (businessid_X)
def ref_to_id(ref: str):
    if not isinstance(ref, str):
        return None
    if ref.startswith('businessref_'):
        return 'businessid_' + ref.split('_',1)[1]
    return None

rdf['business_id'] = rdf['business_ref'].apply(ref_to_id)

# Attach state
rdf['state'] = rdf['business_id'].map(state_map)

# Filter to rows with a state
rdf = rdf[~rdf['state'].isna()].copy()

# Ensure rating numeric
rdf['rating'] = pd.to_numeric(rdf['rating'])

# Compute per-state review count and avg rating
agg = rdf.groupby('state').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()

# Find state with max review_count
idx = agg['review_count'].idxmax()
row = agg.loc[idx]

result = {
    'state_with_most_reviews': row['state'],
    'number_of_reviews': int(row['review_count']),
    'average_rating_in_that_state': round(float(row['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_f6pgaggJwLAVXpKn3bPgWAX2': 'file_storage/call_f6pgaggJwLAVXpKn3bPgWAX2.json', 'var_call_yX3BkSjmthOiNfLHxSUnkqVg': 'file_storage/call_yX3BkSjmthOiNfLHxSUnkqVg.json'}

exec(code, env_args)
