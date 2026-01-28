code = """import json
import pandas as pd

# Load data from the query results (these are file paths)
tracks_file_path = var_functions.query_db:5
sales_file_path = var_functions.query_db:6

print('Loading tracks data...')
tracks_df = pd.read_json(tracks_file_path)
print(f'Tracks shape: {tracks_df.shape}')

print('Loading sales data...')  
sales_df = pd.read_json(sales_file_path)
print(f'Sales shape: {sales_df.shape}')

# Convert revenue to numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
print(f'Total revenue: ${sales_df["revenue_usd"].sum():,.2f}')

# Revenue per track
revenue_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()

# Top individual track
top_track_idx = revenue_by_track['revenue_usd'].idxmax()
top_track_row = revenue_by_track.loc[top_track_idx]
print(f'Top track ID: {top_track_row["track_id"]}, Revenue: ${top_track_row["revenue_usd"]:.2f}')

# Entity resolution - clean fields for matching
tracks_df['title_clean'] = tracks_df['title'].astype(str).str.lower().str.strip()
tracks_df['artist_clean'] = tracks_df['artist'].astype(str).str.lower().str.strip()

# Merge and aggregate by entity
merged = pd.merge(tracks_df, revenue_by_track, on='track_id', how='left')
merged['revenue_usd'] = merged['revenue_usd'].fillna(0)

# Group by title + artist to combine duplicates
revenue_by_entity = merged.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().reset_index()

# Top entity
top_entity_idx = revenue_by_entity['revenue_usd'].idxmax()
top_entity = revenue_by_entity.loc[top_entity_idx]

print(f'Entity: {top_entity["title_clean"]} by {top_entity["artist_clean"]}')
print(f'Total Revenue: ${top_entity["revenue_usd"]:.2f}')

# Get all track IDs for this entity
entity_tracks = merged[
    (merged['title_clean'] == top_entity['title_clean']) & 
    (merged['artist_clean'] == top_entity['artist_clean'])
]
print(f'Track records: {len(entity_tracks)}')

# Show top 5 entities
print('\nTop 5 entities:')
top_5 = revenue_by_entity.sort_values('revenue_usd', ascending=False).head(5)
for _, row in top_5.iterrows():
    print(f"{row['title_clean']} by {row['artist_clean']}: ${row['revenue_usd']:.2f}")

result = {
    'title': top_entity['title_clean'],
    'artist': top_entity['artist_clean'],
    'revenue': float(top_entity['revenue_usd']),
    'track_count': len(entity_tracks)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
