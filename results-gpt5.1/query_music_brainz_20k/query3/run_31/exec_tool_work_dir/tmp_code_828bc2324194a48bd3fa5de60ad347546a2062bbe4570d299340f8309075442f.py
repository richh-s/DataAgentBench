code = """import json, pandas as pd

# Load full results from files
with open(var_call_otNRRnZZlmOUmE6wg58jVIAc, 'r') as f:
    tracks = json.load(f)
with open(var_call_tYHRJR5RKqvvex6TKD234a92, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning: normalize strings for matching
for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

# Build a simple canonical key using title + artist + (album if non-empty)
tracks_df['canon_key'] = tracks_df['title'] + '|' + tracks_df['artist'] + '|' + tracks_df['album']

# There may be very noisy/empty keys; still, group by this as an approximation
# Map each track_id to its canon_key
track_id_to_key = tracks_df.set_index('track_id')['canon_key']

# Attach canon_key to sales
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df = sales_df.merge(track_id_to_key.rename('canon_key'), left_on='track_id', right_index=True, how='left')

# Aggregate revenue by canonical key (real-world track) across all stores and countries
agg = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].astype(float).sum().reset_index()

# Find the canonical key with highest revenue
top_row = agg.sort_values('revenue_usd', ascending=False).iloc[0]

best_key = top_row['canon_key']
best_revenue = float(top_row['revenue_usd'])

# Get a representative metadata row for this canonical key
rep = tracks_df[tracks_df['canon_key'] == best_key].iloc[0]

answer = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'total_revenue_usd': round(best_revenue, 2)
}

result = json.dumps(answer)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_otNRRnZZlmOUmE6wg58jVIAc': 'file_storage/call_otNRRnZZlmOUmE6wg58jVIAc.json', 'var_call_tYHRJR5RKqvvex6TKD234a92': 'file_storage/call_tYHRJR5RKqvvex6TKD234a92.json'}

exec(code, env_args)
