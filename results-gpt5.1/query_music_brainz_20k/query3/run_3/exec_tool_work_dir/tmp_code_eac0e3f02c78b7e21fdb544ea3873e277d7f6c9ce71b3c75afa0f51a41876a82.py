code = """import json, pandas as pd

# Load full results from the JSON files
with open(var_call_SKC2PzRFO8BfAVH9wjt22xz8, 'r') as f:
    tracks = json.load(f)
with open(var_call_piGz1LHoyyDvxxcObVO5VFXS, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert numeric fields
for col in ['track_id']:
    tracks_df[col] = pd.to_numeric(tracks_df[col], errors='coerce')
for col in ['sale_id', 'track_id', 'units_sold', 'revenue_usd']:
    sales_df[col] = pd.to_numeric(sales_df[col], errors='coerce')

# Basic normalization of title & artist for entity resolution
import re

def norm_text(x):
    if not isinstance(x, str):
        return None
    x = x.lower()
    x = re.sub(r"[^a-z0-9]+", " ", x)
    x = re.sub(r"\s+", " ", x).strip()
    return x or None

tracks_df['norm_title'] = tracks_df['title'].apply(norm_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(norm_text)

# Define a simple blocking key: title + artist when available, else just title
tracks_df['block_key'] = tracks_df['norm_title'].fillna('') + '|' + tracks_df['norm_artist'].fillna('')

# For missing artist, just rely on title
mask_no_artist = tracks_df['norm_artist'].isna()
tracks_df.loc[mask_no_artist, 'block_key'] = tracks_df.loc[mask_no_artist, 'norm_title'].fillna('')

# Aggregate track attributes within each block to define a canonical real-world track
# We'll define the real-world track id as the minimum track_id in the block
tracks_df['entity_id'] = tracks_df.groupby('block_key')['track_id'].transform('min')

# Map each sale to the entity_id
sales_with_entity = sales_df.merge(tracks_df[['track_id', 'entity_id']], on='track_id', how='left')

# Aggregate revenue per entity across all stores and countries
entity_revenue = sales_with_entity.groupby('entity_id', as_index=False)['revenue_usd'].sum()

# Find the entity with the highest revenue
top_entity = entity_revenue.sort_values('revenue_usd', ascending=False).iloc[0]

# Get all tracks that belong to this entity to infer canonical title/artist
entity_tracks = tracks_df[tracks_df['entity_id'] == top_entity['entity_id']]

# Choose the most common (title, artist) pair as the representative
rep = (entity_tracks.groupby(['title','artist'])
       .size()
       .reset_index(name='cnt')
       .sort_values('cnt', ascending=False)
       .iloc[0])

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'total_revenue_usd': float(round(top_entity['revenue_usd'], 2))
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_SKC2PzRFO8BfAVH9wjt22xz8': 'file_storage/call_SKC2PzRFO8BfAVH9wjt22xz8.json', 'var_call_piGz1LHoyyDvxxcObVO5VFXS': 'file_storage/call_piGz1LHoyyDvxxcObVO5VFXS.json'}

exec(code, env_args)
