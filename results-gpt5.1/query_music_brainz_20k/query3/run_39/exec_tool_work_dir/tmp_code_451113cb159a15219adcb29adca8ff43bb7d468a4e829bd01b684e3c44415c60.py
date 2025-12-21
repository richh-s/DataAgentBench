code = """import json, pandas as pd

# Load full data from JSON files
with open(var_call_yz4yx3ZAeWwbNfzWucw2fDZ1, 'r') as f:
    tracks = json.load(f)
with open(var_call_MxMNiQeqVxgDdMgcYJleF8xQ, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert numeric columns
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# Simple entity resolution: consider real-world track identity by exact match on normalized (title, artist, album, year)
# Normalize strings: lower, strip, collapse spaces; treat 'None' and actual None as missing

def norm_str(x):
    if x is None:
        return None
    x = str(x)
    if x.strip().lower() == 'none':
        return None
    return ' '.join(x.strip().lower().split()) or None

for col in ['title', 'artist', 'album', 'year']:
    tracks_df[col + '_norm'] = tracks_df[col].apply(norm_str)

# Define a key; if all are None, fall back to title only; otherwise use available fields
tracks_df['entity_key'] = tracks_df.apply(
    lambda r: (
        r['title_norm'], r['artist_norm'], r['album_norm'], r['year_norm']
    ) if any([r['title_norm'], r['artist_norm'], r['album_norm'], r['year_norm']])
    else (r['title_norm'], None, None, None),
    axis=1
)

# Map each track_id to an entity_id (categorical codes of entity_key)
tracks_df['entity_id'] = tracks_df['entity_key'].astype('category').cat.codes

# Merge sales with tracks to get entity_id
sales_with_entity = sales_df.merge(tracks_df[['track_id', 'entity_id', 'title', 'artist', 'album', 'year']], on='track_id', how='left')

# Aggregate revenue per entity across all stores and countries
agg = sales_with_entity.groupby('entity_id', as_index=False).agg({
    'revenue_usd': 'sum'
})

# Find top entity
top_entity_id = agg.sort_values('revenue_usd', ascending=False).iloc[0]['entity_id']
max_revenue = agg.sort_values('revenue_usd', ascending=False).iloc[0]['revenue_usd']

# Get representative track info for this entity (first occurrence)
rep = tracks_df[tracks_df['entity_id'] == top_entity_id].iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'year': rep['year'],
    'total_revenue_usd': round(float(max_revenue), 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_yz4yx3ZAeWwbNfzWucw2fDZ1': 'file_storage/call_yz4yx3ZAeWwbNfzWucw2fDZ1.json', 'var_call_MxMNiQeqVxgDdMgcYJleF8xQ': 'file_storage/call_MxMNiQeqVxgDdMgcYJleF8xQ.json', 'var_call_9Trb8IHgHw6qQaiAqMTe8D2k': ['tracks'], 'var_call_DVFp3d2YgaZ8iYMSB5xwf6sW': ['sales']}

exec(code, env_args)
