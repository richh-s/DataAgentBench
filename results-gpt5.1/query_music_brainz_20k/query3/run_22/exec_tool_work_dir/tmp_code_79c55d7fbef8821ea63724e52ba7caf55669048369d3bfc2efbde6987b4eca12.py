code = """import json, pandas as pd
from pathlib import Path

# Load full tracks and sales data
tracks_path = Path(var_call_l7fZoaS9VaCZzjGl8BAiDE5G)
sales_path = Path(var_call_eXyQe6PPLOu6amxzjPZ1usyZ)

with tracks_path.open() as f:
    tracks = json.load(f)
with sales_path.open() as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning: normalize text for title/artist/album to help with duplicates
for col in ['title','artist','album']:
    if col in tracks_df.columns:
        tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

# Also normalize year a bit: keep only last 4 digits if present
tracks_df['year_norm'] = tracks_df['year'].fillna('').astype(str).str.extract('(\\d{4})', expand=False)

# Create a simple canonical key using normalized title + artist + album (and year if available)
# This is a heuristic entity resolution.
key_parts = [tracks_df['title'], tracks_df['artist'], tracks_df['album']]
key = key_parts[0] + '|' + key_parts[1] + '|' + key_parts[2]
# If year_norm exists, append when not null
key = key.where(tracks_df['year_norm'].isna(), key + '|' + tracks_df['year_norm'].fillna(''))
tracks_df['canonical_key'] = key

# Some rows might have extremely poor metadata (e.g. empty title/artist). For those, fall back to unique track_id key
empty_mask = tracks_df['canonical_key'].str.replace('|','', regex=False).str.strip() == ''
tracks_df.loc[empty_mask, 'canonical_key'] = 'id_' + tracks_df.loc[empty_mask, 'track_id'].astype(str)

# Map each track_id to canonical_key
track_to_key = tracks_df.set_index('track_id')['canonical_key']

# Ensure sales track_id matches type
sales_df['track_id'] = sales_df['track_id'].astype(str)
track_to_key = track_to_key.rename_axis('track_id').reset_index()

# Merge sales with canonical keys
sales_with_key = sales_df.merge(track_to_key, on='track_id', how='left')

# Aggregate total revenue per canonical track (all countries and stores)
rev_by_canonical = sales_with_key.groupby('canonical_key', as_index=False)['revenue_usd'].apply(lambda s: pd.to_numeric(s, errors='coerce').sum())
rev_by_canonical = rev_by_canonical.rename(columns={'revenue_usd':'total_revenue_usd'})

# Get the canonical track with max revenue
max_row = rev_by_canonical.sort_values('total_revenue_usd', ascending=False).iloc[0]
max_key = max_row['canonical_key']
max_revenue = float(max_row['total_revenue_usd'])

# For that canonical track, get a representative title/artist from tracks_df
rep = tracks_df[tracks_df['canonical_key'] == max_key].iloc[0]

answer = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'year': rep['year'],
    'total_revenue_usd': round(max_revenue, 2)
}

result = json.dumps(answer)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_l7fZoaS9VaCZzjGl8BAiDE5G': 'file_storage/call_l7fZoaS9VaCZzjGl8BAiDE5G.json', 'var_call_eXyQe6PPLOu6amxzjPZ1usyZ': 'file_storage/call_eXyQe6PPLOu6amxzjPZ1usyZ.json'}

exec(code, env_args)
