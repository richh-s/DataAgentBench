code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_HQD7mGfFikwZuhlclfUmw94T, 'r') as f:
    business_data = json.load(f)
with open(var_call_G1Yf9x7TGGrbuxMEChgTqj71, 'r') as f:
    review_data = json.load(f)

# Extract state code from description, assuming pattern like ", XX," where XX is state abbreviation
state_pattern = re.compile(r',\s*([A-Z]{2})\s*,')

business_rows = []
for b in business_data:
    desc = b.get('description') or ''
    m = state_pattern.search(desc)
    if not m:
        continue
    state = m.group(1)
    bid = b.get('business_id')
    if not bid:
        continue
    # Convert businessid_# to businessref_#
    if bid.startswith('businessid_'):
        bref = 'businessref_' + bid.split('_',1)[1]
    else:
        bref = bid
    business_rows.append({'business_id': bid, 'business_ref': bref, 'state': state})

biz_df = pd.DataFrame(business_rows)

rev_df = pd.DataFrame(review_data)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
rev_df = rev_df.dropna(subset=['rating'])

merged = rev_df.merge(biz_df, on='business_ref', how='inner')

state_stats = merged.groupby('state').agg(
    review_count=('rating', 'size'),
    avg_rating=('rating', 'mean')
).reset_index()

# Find state with max review_count
idxmax = state_stats['review_count'].idxmax()
row = state_stats.loc[idxmax]

result = {
    'state_with_most_reviews': row['state'],
    'review_count': int(row['review_count']),
    'average_rating': round(float(row['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_HQD7mGfFikwZuhlclfUmw94T': 'file_storage/call_HQD7mGfFikwZuhlclfUmw94T.json', 'var_call_G1Yf9x7TGGrbuxMEChgTqj71': 'file_storage/call_G1Yf9x7TGGrbuxMEChgTqj71.json'}

exec(code, env_args)
