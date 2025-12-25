code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_7Hmhgnqgfl0lBUCAbtZPV19p, 'r') as f:
    business_data = json.load(f)
with open(var_call_2rlTosskMA8DdtDhqj9tA9o8, 'r') as f:
    review_data = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(business_data)
rdf = pd.DataFrame(review_data)

# Extract state from description, assuming patterns like ", XX" or " in City, XX" where XX is 2-letter state
state_pattern = re.compile(r",\s*([A-Z]{2})[\s,]")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Normalize business ids: businessid_# -> businessref_#
bdf['business_ref'] = bdf['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Merge reviews with business to get state per review
merged = rdf.merge(bdf[['business_ref','state']], on='business_ref', how='left')

# Drop reviews with no state
merged = merged.dropna(subset=['state'])

# Convert rating to numeric
merged['rating'] = pd.to_numeric(merged['rating'])

# Aggregate: count reviews and average rating per state
agg = merged.groupby('state').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()

# Find state with max reviews
agg_sorted = agg.sort_values('review_count', ascending=False)

if not agg_sorted.empty:
    top = agg_sorted.iloc[0]
    result = {
        'state_with_most_reviews': top['state'],
        'review_count': int(top['review_count']),
        'average_rating': round(float(top['avg_rating']), 3)
    }
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7Hmhgnqgfl0lBUCAbtZPV19p': 'file_storage/call_7Hmhgnqgfl0lBUCAbtZPV19p.json', 'var_call_2rlTosskMA8DdtDhqj9tA9o8': 'file_storage/call_2rlTosskMA8DdtDhqj9tA9o8.json'}

exec(code, env_args)
