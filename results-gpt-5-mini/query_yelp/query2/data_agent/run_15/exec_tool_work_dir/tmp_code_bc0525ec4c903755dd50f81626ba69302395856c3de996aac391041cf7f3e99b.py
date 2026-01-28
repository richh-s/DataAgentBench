code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_TSqCUkEY0vhOlnZRPg8wu2mC, 'r') as f:
    businesses = json.load(f)
with open(var_call_1kX3P5DuItxNRk2ftwUG1nKs, 'r') as f:
    reviews = json.load(f)

# Build business_id -> state mapping by extracting two-letter state code from description
biz_state = {}
state_pattern = re.compile(r",\s*([A-Z]{2})(?:\b|,)")
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    m = state_pattern.search(desc)
    state = m.group(1) if m else None
    biz_state[bid] = state

# Process reviews: map businessref_x to businessid_x
rows = []
for r in reviews:
    bref = r.get('business_ref')
    rating = r.get('rating')
    if bref is None or rating is None:
        continue
    # convert prefix
    bid = bref.replace('businessref_', 'businessid_')
    state = biz_state.get(bid)
    try:
        rating_val = float(rating)
    except:
        continue
    rows.append({'business_id': bid, 'state': state, 'rating': rating_val})

df = pd.DataFrame(rows)
# Filter out records without state
df = df[df['state'].notnull()]

# Aggregate by state: count of reviews and average rating across reviews
agg = df.groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()
# Find state with max reviews
if agg.empty:
    result = {'state': None, 'review_count': 0, 'average_rating': None}
else:
    top = agg.sort_values('review_count', ascending=False).iloc[0]
    result = {
        'state': str(top['state']),
        'review_count': int(top['review_count']),
        'average_rating': round(float(top['average_rating']), 3)
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IGLYLgQijBtG2PgQDUhD50JK': ['checkin', 'business'], 'var_call_AnDnU1bs45X4r3lfdOzxAbAI': ['review', 'tip', 'user'], 'var_call_TSqCUkEY0vhOlnZRPg8wu2mC': 'file_storage/call_TSqCUkEY0vhOlnZRPg8wu2mC.json', 'var_call_1kX3P5DuItxNRk2ftwUG1nKs': 'file_storage/call_1kX3P5DuItxNRk2ftwUG1nKs.json'}

exec(code, env_args)
