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
top_tracks = revenue_by_track.sort_values('revenue_usd', ascending=False).head(10)
print('\nTop 10 tracks by revenue:')
print(top_tracks.to_string())

# Get the top earning track_id
top_track_id = top_tracks.iloc[0]['track_id']
top_revenue = top_tracks.iloc[0]['revenue_usd']
print(f'\nTrack ID {top_track_id} has the highest revenue: ${top_revenue:.2f}')

# Show corresponding track info for top revenue track
top_track_info = tracks_df[tracks_df['track_id'] == top_track_id]
print('\nCorresponding track info:')
print(top_track_info.to_string())

# Save key variables for further analysis
result_dict = {
    'tracks_df': tracks_df,
    'sales_df': sales_df,
    'revenue_by_track': revenue_by_track,
    'top_tracks': top_tracks
}

# Check for potential duplicates by examining titles and artists
print('\nAnalyzing potential duplicates...')

# Clean title and artist fields for better matching
tracks_df['title_clean'] = tracks_df['title'].astype(str).str.lower().str.strip()
tracks_df['artist_clean'] = tracks_df['artist'].astype(str).str.lower().str.strip()

# Merge revenue with track info
merged = pd.merge(tracks_df, revenue_by_track, on='track_id', how='left')
merged['revenue_usd'] = merged['revenue_usd'].fillna(0)

# Group by cleaned title and artist to aggregate revenue (entity resolution approach)
revenue_by_entity = merged.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().reset_index()
top_entities = revenue_by_entity.sort_values('revenue_usd', ascending=False).head(20)
print('\nTop 20 entities by revenue (grouped by title+artist):')
print(top_entities.to_string())

# Get the top earning entity
top_entity = top_entities.iloc[0]
print(f"\nTop earning entity: '{top_entity['title_clean']}' by '{top_entity['artist_clean']}'")
print(f"Total revenue: ${top_entity['revenue_usd']:.2f}")

# Find all track_ids that belong to this entity
top_entity_tracks = merged[
    (merged['title_clean'] == top_entity['title_clean']) & 
    (merged['artist_clean'] == top_entity['artist_clean'])
]
print(f"Number of track records for top entity: {len(top_entity_tracks)}")
print('\nAll track records for top entity:')
print(top_entity_tracks[['track_id', 'title', 'artist', 'album', 'revenue_usd']].to_string())

print('__RESULT__:')
print('Analysis completed. Top earning entity identified.')"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
