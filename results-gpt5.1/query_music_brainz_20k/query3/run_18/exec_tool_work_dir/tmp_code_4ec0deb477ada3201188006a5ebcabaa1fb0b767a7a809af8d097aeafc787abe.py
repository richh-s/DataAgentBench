code = """import json, pandas as pd
from pathlib import Path

tracks_path = Path(var_call_ZRkFc88xVV4xDYDazLu8Bkl5)
sales_path = Path(var_call_B74wYRv6NKTGyXKca7pasf9v)

tracks = pd.read_json(tracks_path)
sales = pd.read_json(sales_path)

sales['revenue_usd'] = sales['revenue_usd'].astype(float)

# Aggregate revenue per track_id
rev_per_track = sales.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Join with tracks to get metadata
merged = rev_per_track.merge(tracks, on='track_id', how='left')

# For simple entity resolution, treat (normalized title, normalized artist) as real-world track key
for col in ['title','artist']:
    merged[col] = merged[col].fillna('').astype(str).str.strip().str.lower()

merged['entity_key'] = merged['title'] + '||' + merged['artist']

rev_per_entity = merged.groupby('entity_key', as_index=False)['revenue_usd'].sum()

# Find top entity
top_entity = rev_per_entity.sort_values('revenue_usd', ascending=False).iloc[0]

# Recover a representative title/artist for that entity from original tracks (non-normalized)
entity_key = top_entity['entity_key']
rep_row = merged[merged['entity_key'] == entity_key].iloc[0]

result = {
    'title': rep_row['title'],
    'artist': rep_row['artist'],
    'total_revenue_usd': float(top_entity['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ZRkFc88xVV4xDYDazLu8Bkl5': 'file_storage/call_ZRkFc88xVV4xDYDazLu8Bkl5.json', 'var_call_B74wYRv6NKTGyXKca7pasf9v': 'file_storage/call_B74wYRv6NKTGyXKca7pasf9v.json'}

exec(code, env_args)
