code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_LjupHZT0VtqECU8KE4SeSAnp, 'r') as f:
    business_data = json.load(f)
with open(var_call_19ROHgyy9PuFR8E5UuhwBnNE, 'r') as f:
    review_data = json.load(f)

bdf = pd.DataFrame(business_data)
rdf = pd.DataFrame(review_data)

# Extract state from description, e.g., 'City, ST'
state_pattern = re.compile(r',\s*([A-Z]{2})[,. ]')

states = []
for desc in bdf['description'].fillna(''):
    m = state_pattern.search(desc)
    states.append(m.group(1) if m else None)

bdf['state'] = states

# Map business_id to business_ref
bdf['business_ref'] = bdf['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Merge reviews with business states
merged = rdf.merge(bdf[['business_ref','state']], on='business_ref', how='left')

# Drop rows without state
merged = merged.dropna(subset=['state'])

# Convert rating to numeric
merged['rating'] = pd.to_numeric(merged['rating'])

# Compute total reviews per state and average rating
agg = merged.groupby('state').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()

# Find state with max reviews
top = agg.sort_values('review_count', ascending=False).iloc[0]

result = {"state_with_most_reviews": top['state'], "number_of_reviews": int(top['review_count']), "average_rating": round(float(top['avg_rating']), 3)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_LjupHZT0VtqECU8KE4SeSAnp': 'file_storage/call_LjupHZT0VtqECU8KE4SeSAnp.json', 'var_call_19ROHgyy9PuFR8E5UuhwBnNE': 'file_storage/call_19ROHgyy9PuFR8E5UuhwBnNE.json'}

exec(code, env_args)
