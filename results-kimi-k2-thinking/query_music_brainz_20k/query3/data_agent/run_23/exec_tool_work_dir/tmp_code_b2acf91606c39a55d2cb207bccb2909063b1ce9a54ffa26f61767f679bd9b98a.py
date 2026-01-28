code = """import json
import pandas as pd

# Load the full tracks data from the file
with open('var_functions.query_db:12.json', 'r') as f:
    tracks_data = json.load(f)

# Convert to DataFrame
tracks_df = pd.DataFrame(tracks_data)
print('Tracks dataset:', len(tracks_df), 'records')
print('First record keys:', list(tracks_df.columns))

# Get full sales data
with open('var_functions.query_db:5.json', 'r') as f:
    sales_data = json.load(f)

sales_df = pd.DataFrame(sales_data)
print('Sales dataset:', len(sales_df), 'records')

# Aggregate sales by track_id
sales_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
top_tracks = sales_by_track.sort_values('revenue_usd', ascending=False).head(10)
print('Top tracks by revenue:', top_tracks.to_dict())

# Now let's find the actual track info for the top tracks
tracks_dict = {str(t['track_id']): t for t in tracks_data}
for idx, row in top_tracks.head(3).iterrows():
    track_id = str(row['track_id'])
    if track_id in tracks_dict:
        track = tracks_dict[track_id]
        print('Track ID', track_id, 'revenue:', row['revenue_usd'])
        print('Title:', track.get('title'))
        print('Artist:', track.get('artist'))
        print('---')

# Aggregate by combining duplicates - need to do entity resolution
# Let's create a simple key: title + artist (normalized)
tracks_df['title_norm'] = tracks_df['title'].astype(str).str.strip().str.lower()
tracks_df['artist_norm'] = tracks_df['artist'].astype(str).str.strip().str.lower()

# Merge tracks with sales
tracks_with_sales = tracks_df.merge(sales_by_track, on='track_id', how='inner')
print('Tracks with sales:', len(tracks_with_sales))

# Group by title and artist to find duplicates
revenue_by_song = tracks_with_sales.groupby(['title_norm', 'artist_norm'])['revenue_usd'].sum().reset_index()
top_songs = revenue_by_song.sort_values('revenue_usd', ascending=False).head(10)
print('Top songs by aggregated revenue:')
for idx, row in top_songs.head(3).iterrows():
    print('Song:', row['title_norm'], '-', row['artist_norm'])
    print('Total revenue:', row['revenue_usd'])

result = {
    'top_songs': top_songs.head(1).to_dict('records'),
    'total_unique_tracks': len(tracks_df),
    'total_sales_records': len(sales_df)
}

----BEGIN PRINT FORMAT----
print('__RESULT__:')
print(json.dumps(result))
----END PRINT FORMAT----"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}], 'var_functions.query_db:7': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}], 'var_functions.query_db:8': [{'total_tracks': '19375'}], 'var_functions.query_db:10': [{'total_sales': '58049'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
