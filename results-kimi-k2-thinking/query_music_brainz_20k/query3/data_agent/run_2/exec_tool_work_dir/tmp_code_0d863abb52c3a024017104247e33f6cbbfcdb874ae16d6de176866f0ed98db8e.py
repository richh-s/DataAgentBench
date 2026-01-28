code = """import json
import pandas as pd

# Load tracks data from file
tracks_file = var_functions.query_db:5
tracks_df = pd.read_json(tracks_file)
print(f'Tracks data shape: {tracks_df.shape}')
print(f'Columns: {tracks_df.columns.tolist()}')

# Load sales data from file
sales_file = var_functions.query_db:6
sales_df = pd.read_json(sales_file)
print(f'Sales data shape: {sales_df.shape}')
print(f'Columns: {sales_df.columns.tolist()}')

# Convert revenue to numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
print(f'Total revenue sum: ${sales_df["revenue_usd"].sum():,.2f}')

# Calculate total revenue per track_id
revenue_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()

# Get the track with highest revenue
top_track_row = revenue_by_track.loc[revenue_by_track['revenue_usd'].idxmax()]
top_track_id = str(top_track_row['track_id'])
top_revenue = top_track_row['revenue_usd']
print(f'\nTrack ID {top_track_id} has the highest revenue: ${top_revenue:.2f}')

# Show corresponding track info for top revenue track
top_track_info = tracks_df[tracks_df['track_id'].astype(str) == top_track_id]
print('\nCorresponding track info:')
print(top_track_info.to_string())

# For entity resolution, lets clean title and artist fields
tracks_df['title_clean'] = tracks_df['title'].astype(str).str.lower().str.strip()
tracks_df['artist_clean'] = tracks_df['artist'].astype(str).str.lower().str.strip()

# Merge tracks with their revenues
merged = pd.merge(tracks_df, revenue_by_track, on='track_id', how='left')
merged['revenue_usd'] = merged['revenue_usd'].fillna(0)

# Group by cleaned title and artist to aggregate revenue across duplicates
revenue_by_entity = merged.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().reset_index()
top_entity = revenue_by_entity.loc[revenue_by_entity['revenue_usd'].idxmax()]

print(f"\nTop earning entity (grouped by title+artist):")
print(f"Title: {top_entity['title_clean']}")
print(f"Artist: {top_entity['artist_clean']}")
print(f"Total revenue: ${top_entity['revenue_usd']:.2f}")

# Find all track IDs for this entity
top_entity_tracks = merged[
    (merged['title_clean'] == top_entity['title_clean']) & 
    (merged['artist_clean'] == top_entity['artist_clean'])
]
print(f"Number of track records: {len(top_entity_tracks)}")
print('\nTrack records for top entity:')
for idx, row in top_entity_tracks.iterrows():
    print(f"Track ID: {row['track_id']}, Revenue: ${row['revenue_usd']:.2f}")

# Get top 10 entities
top_10_entities = revenue_by_entity.sort_values('revenue_usd', ascending=False).head(10)
print('\nTop 10 entities by revenue:')
for idx, row in top_10_entities.iterrows():
    print(f"{row['title_clean']} by {row['artist_clean']}: ${row['revenue_usd']:.2f}")

print('__RESULT__:')
print(json.dumps({
    'top_track_id': top_track_id,
    'top_track_revenue': float(top_revenue),
    'top_entity_title': top_entity['title_clean'],
    'top_entity_artist': top_entity['artist_clean'],
    'top_entity_revenue': float(top_entity['revenue_usd']),
    'entity_track_count': len(top_entity_tracks)
}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
