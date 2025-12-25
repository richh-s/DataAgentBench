code = """import json, pandas as pd
from pathlib import Path

# Load full results
with open(var_call_rMsPW5EhduvM9th2ysXFjLn5, 'r') as f:
    sales_agg = json.load(f)
with open(var_call_blPQWASHqFJ0vJi4ojS4ltqG, 'r') as f:
    tracks = json.load(f)

sales_df = pd.DataFrame(sales_agg)
tracks_df = pd.DataFrame(tracks)

# Ensure numeric
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Basic normalization for entity resolution
for col in ['title','artist','album']:
    tracks_df[col] = tracks_df[col].fillna('').str.strip().str.lower()

# Create a simple canonical key using title + artist (and album if available)
tracks_df['canon_key'] = tracks_df['title'] + '|' + tracks_df['artist']

# Some titles may be very generic or empty; in that case fall back to album+title
empty_mask = tracks_df['title'].eq('')
tracks_df.loc[empty_mask, 'canon_key'] = tracks_df.loc[empty_mask, 'album'] + '|' + tracks_df.loc[empty_mask, 'artist']

# Aggregate total revenue at canonical track level
merged = sales_df.merge(tracks_df[['track_id','canon_key','title','artist','album']], on='track_id', how='left')
canon_revenue = merged.groupby('canon_key', as_index=False)['total_revenue'].sum()

# Find the canonical key with max revenue
best = canon_revenue.sort_values('total_revenue', ascending=False).iloc[0]
best_key = best['canon_key']
best_rev = float(best['total_revenue'])

# Get a representative track row for this canonical key
rep = tracks_df[tracks_df['canon_key'] == best_key].iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'total_revenue_usd': round(best_rev, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rMsPW5EhduvM9th2ysXFjLn5': 'file_storage/call_rMsPW5EhduvM9th2ysXFjLn5.json', 'var_call_blPQWASHqFJ0vJi4ojS4ltqG': 'file_storage/call_blPQWASHqFJ0vJi4ojS4ltqG.json'}

exec(code, env_args)
