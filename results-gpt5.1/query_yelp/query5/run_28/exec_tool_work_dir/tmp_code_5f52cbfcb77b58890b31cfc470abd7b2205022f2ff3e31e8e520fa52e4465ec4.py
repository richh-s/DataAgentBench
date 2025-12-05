code = """import json, re, pandas as pd

# Load full business WiFi data
path = var_call_shU5BDW4Ratpc5aVjGTpxOyk
with open(path, 'r') as f:
    biz_wifi = json.load(f)

# Filter to businesses that actually offer WiFi (value contains 'free' or 'paid', case-insensitive)
rows = []
for b in biz_wifi:
    wifi_val = None
    attrs = b.get('attributes') or {}
    if isinstance(attrs, dict):
        wifi_val = attrs.get('WiFi')
    if not isinstance(wifi_val, str):
        continue
    val = wifi_val.lower()
    if 'free' not in val and 'paid' not in val:
        continue

    desc = b.get('description') or ''
    # Extract state as the two-letter token before the last comma and ZIP, e.g., "Saint Louis, MO, ..."
    state = None
    m = re.search(r',\s*([A-Z]{2})\s*,', desc)
    if m:
        state = m.group(1)
    if not state:
        continue

    rows.append({'business_id': b.get('business_id'), 'state': state})

biz_df = pd.DataFrame(rows)

# Load reviews
path_r = var_call_p240oOWqpQt86RCdi9xwwAmS
with open(path_r, 'r') as f:
    reviews = json.load(f)
rev_df = pd.DataFrame(reviews)

# Normalize business ids: businessid_X <-> businessref_X
rev_df['business_id'] = rev_df['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
rev_df['rating'] = pd.to_numeric(rev_df['rating'])

# Join WiFi businesses with reviews
merged = pd.merge(biz_df, rev_df[['business_id','rating']], on='business_id', how='left')

# Compute counts and average ratings per state
agg = merged.groupby('state').agg(num_businesses=('business_id','nunique'), avg_rating=('rating','mean')).reset_index()

# Find state with max num_businesses
agg = agg.dropna(subset=['num_businesses'])
agg_sorted = agg.sort_values(['num_businesses','state'], ascending=[False, True])
result_row = agg_sorted.iloc[0].to_dict()

result = json.dumps({'state': result_row['state'], 'num_businesses': int(result_row['num_businesses']), 'avg_rating': result_row['avg_rating']})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_shU5BDW4Ratpc5aVjGTpxOyk': 'file_storage/call_shU5BDW4Ratpc5aVjGTpxOyk.json', 'var_call_Vyy2nJmcciQ8rZX6KuSmEBg7': ['review', 'tip', 'user'], 'var_call_p240oOWqpQt86RCdi9xwwAmS': 'file_storage/call_p240oOWqpQt86RCdi9xwwAmS.json'}

exec(code, env_args)
