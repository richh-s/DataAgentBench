code = """import json, re, pandas as pd

biz = pd.DataFrame(var_call_4divnvUyB42cdyn4UUPUohHd)

# Extract US state as two-letter code from description (pattern like ", XX " or "XX, USA")
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

states = []
for desc in biz['description'].fillna(''):
    m = state_pattern.search(desc)
    states.append(m.group(1) if m else None)

biz['state'] = states
biz = biz.dropna(subset=['state'])

# Map business_id -> state
biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Load large review file
import os
path = var_call_jLQjt4b2cDI9i2pfa38LMZvz
with open(path, 'r') as f:
    reviews = json.load(f)

rv = pd.DataFrame(reviews)
rv['rating'] = rv['rating'].astype(float)

# Join
merged = rv.merge(biz[['business_ref','state']], on='business_ref', how='inner')

# Aggregate by state
agg = merged.groupby('state').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()

# Get state with max review_count
idx = agg['review_count'].idxmax()
row = agg.loc[idx]

result = {'state_with_most_reviews': row['state'], 'number_of_reviews': int(row['review_count']), 'average_rating': round(float(row['avg_rating']),3)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4divnvUyB42cdyn4UUPUohHd': [{'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'}], 'var_call_jLQjt4b2cDI9i2pfa38LMZvz': 'file_storage/call_jLQjt4b2cDI9i2pfa38LMZvz.json'}

exec(code, env_args)
