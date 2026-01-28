code = """import json
import pandas as pd

# Load data
tracks_df = pd.read_json(var_functions.query_db:5)
sales_df = pd.read_json(var_functions.query_db:6)

# Convert revenue to numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Calculate total revenue per track
revenue_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()

# Clean track data for entity resolution
tracks_df['title_clean'] = tracks_df['title'].astype(str).str.lower().str.strip()
tracks_df['artist_clean'] = tracks_df['artist'].astype(str).str.lower().str.strip()

# Merge tracks with revenues
merged = pd.merge(tracks_df, revenue_by_track, on='track_id', how='left')
merged['revenue_usd'] = merged['revenue_usd'].fillna(0)

# Aggregate revenue by entity (title + artist)
revenue_by_entity = merged.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().reset_index()

# Get top entity
top_entity_idx = revenue_by_entity['revenue_usd'].idxmax()
top_entity = revenue_by_entity.loc[top_entity_idx]

# Get all track records for this entity
entity_tracks = merged[
    (merged['title_clean'] == top_entity['title_clean']) & 
    (merged['artist_clean'] == top_entity['artist_clean'])
]

result = {
    'title': top_entity['title_clean'],
    'artist': top_entity['artist_clean'],
    'revenue': float(top_entity['revenue_usd']),
    'track_count': len(entity_tracks),
    'track_ids': entity_tracks['track_id'].tolist()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
