code = """import json
import pandas as pd

# Load file paths from storage
tracks_file_path = locals()['var_functions.query_db:5']
sales_file_path = locals()['var_functions.query_db:6']

print(f'Loading tracks from: {tracks_file_path}')
tracks_df = pd.read_json(tracks_file_path)
print(f'Tracks shape: {tracks_df.shape}')

print(f'Loading sales from: {sales_file_path}')
sales_df = pd.read_json(sales_file_path)
print(f'Sales shape: {sales_df.shape}')

# Convert revenue to numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
print(f'Total revenue across all sales: ${sales_df["revenue_usd"].sum():,.2f}')

# Calculate total revenue per track_id
revenue_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()

# Get top track by revenue
top_track_idx = revenue_by_track['revenue_usd'].idxmax()
top_track_id = revenue_by_track.loc[top_track_idx, 'track_id']
top_track_revenue = revenue_by_track.loc[top_track_idx, 'revenue_usd']

print(f'\nTop individual track: ID={top_track_id}, Revenue=${top_track_revenue:.2f}')

# Get track info for the top track
top_track_info = tracks_df[tracks_df['track_id'] == top_track_id]
print('\nTop track details:')
print(top_track_info.to_string())

# Now perform entity resolution to combine duplicates
# Clean title and artist for better matching
tracks_df['title_clean'] = tracks_df['title'].astype(str).str.lower().str.strip()
tracks_df['artist_clean'] = tracks_df['artist'].astype(str).str.lower().str.strip()

# Merge tracks with revenues
merged = pd.merge(tracks_df, revenue_by_track, on='track_id', how='left')
merged['revenue_usd'] = merged['revenue_usd'].fillna(0)

# Group by cleaned title and artist to aggregate revenue across duplicates
revenue_by_entity = merged.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().reset_index()

# Get top entity
top_entity_idx = revenue_by_entity['revenue_usd'].idxmax()
top_entity = revenue_by_entity.loc[top_entity_idx]

top_entity_title = top_entity['title_clean']
top_entity_artist = top_entity['artist_clean']
top_entity_revenue = top_entity['revenue_usd']

print(f'\nTop entity after grouping duplicates:')
print(f'Title: {top_entity_title}')
print(f'Artist: {top_entity_artist}')
print(f'Total Revenue: ${top_entity_revenue:.2f}')

# Find all track records for this entity
entity_tracks = merged[
    (merged['title_clean'] == top_entity_title) & 
    (merged['artist_clean'] == top_entity_artist)
]

print(f'Number of track records for this entity: {len(entity_tracks)}')
print('\nTrack records for top entity:')
for _, row in entity_tracks.iterrows():
    print(f"  Track ID: {row['track_id']}, Album: {row['album']}, Revenue: ${row['revenue_usd']:.2f}")

# Show top 10 entities
print('\nTop 10 entities by revenue:')
top_10 = revenue_by_entity.sort_values('revenue_usd', ascending=False).head(10)
for i, (_, row) in enumerate(top_10.iterrows(), 1):
    print(f"{i}. {row['title_clean']} by {row['artist_clean']}: ${row['revenue_usd']:.2f}")

result = {
    'entity_title': top_entity_title,
    'entity_artist': top_entity_artist,
    'total_revenue': float(top_entity_revenue),
    'track_record_count': len(entity_tracks),
    'track_ids': entity_tracks['track_id'].tolist()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:18': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:20': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}]}

exec(code, env_args)
