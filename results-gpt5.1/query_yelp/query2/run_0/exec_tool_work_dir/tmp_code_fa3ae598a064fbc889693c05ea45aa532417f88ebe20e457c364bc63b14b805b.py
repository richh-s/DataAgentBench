code = """import json, re, pandas as pd

# Load full business data
with open(var_call_GuN5g3h1OHWwjJif6ozpeTSS, 'r') as f:
    business = json.load(f)

# Load full review data
with open(var_call_6xZSeJdCd8FzrnCsoAPDqma5, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(business)
rdf = pd.DataFrame(reviews)

# Extract state from description, assuming pattern 'City, ST'
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    return m.group(1) if m else None

bdf['state'] = bdf['description'].apply(extract_state)

# Map business_id -> state and review_count (convert to int)
bdf['review_count'] = pd.to_numeric(bdf['review_count'], errors='coerce').fillna(0).astype(int)

# Compute total number of reviews per state using review_count per business
state_reviews = bdf.groupby('state', dropna=True)['review_count'].sum().reset_index(name='total_reviews')

# Identify state with highest number of reviews
top_state_row = state_reviews.sort_values('total_reviews', ascending=False).iloc[0]
TopState = top_state_row['state']

# Prepare business_ref->business_id join key
rdf['business_id'] = rdf['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

# Merge reviews with business state
merged = rdf.merge(bdf[['business_id','state']], on='business_id', how='left')

# Filter to top state and compute average rating
state_reviews_subset = merged[merged['state'] == TopState]
avg_rating = state_reviews_subset['rating'].mean()

result = {
  'state_with_most_reviews': TopState,
  'total_reviews_in_state': int(top_state_row['total_reviews']),
  'average_rating_in_state': round(float(avg_rating), 3) if pd.notnull(avg_rating) else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_GuN5g3h1OHWwjJif6ozpeTSS': 'file_storage/call_GuN5g3h1OHWwjJif6ozpeTSS.json', 'var_call_6xZSeJdCd8FzrnCsoAPDqma5': 'file_storage/call_6xZSeJdCd8FzrnCsoAPDqma5.json'}

exec(code, env_args)
