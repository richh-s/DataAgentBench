code = """import json
import pandas as pd
import re

# Load the full tracks data from file
with open('var_functions.query_db:12.json', 'r') as f:
    tracks_data = json.load(f)

# Load the full sales data
with open('var_functions.query_db:5.json', 'r') as f:
    sales_data = json.load(f)

# Convert to DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

print('Loaded', len(tracks_df), 'tracks and', len(sales_df), 'sales records')

# Function to normalize text for comparison
def normalize_text(text):
    if pd.isna(text) or text is None or text == 'None':
        return ''
    return str(text).strip().lower()

# Add normalized columns
tracks_df['title_norm'] = tracks_df['title'].apply(normalize_text)
tracks_df['artist_norm'] = tracks_df['artist'].apply(normalize_text)
tracks_df['album_norm'] = tracks_df['album'].apply(normalize_text)

# Create a key for grouping similar tracks
# Use title and artist primarily, but also consider album for additional context
tracks_df['group_key'] = tracks_df['title_norm'] + '::' + tracks_df['artist_norm']

# Merge tracks with sales data
print('Merging tracks with sales...')
sales_with_tracks = sales_df.merge(tracks_df, on='track_id', how='left')

# Calculate revenue by actual track_id
revenue_by_track_id = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
print('Top 10 track_ids by revenue:')
print(revenue_by_track_id.sort_values('revenue_usd', ascending=False).head(10))

# Calculate revenue after grouping by title and artist (entity resolution)
print('\nAggregating revenue by song (title+artist)...')
songs_with_revenue = sales_with_tracks.groupby(['title_norm', 'artist_norm']).agg({
    'revenue_usd': 'sum',
    'track_id': list
}).reset_index()

# Get top songs after entity resolution
top_songs = songs_with_revenue.sort_values('revenue_usd', ascending=False).head(20)
print('\nTop 20 songs by aggregate revenue:')
for idx, row in top_songs.iterrows():
    title = row['title_norm']
    artist = row['artist_norm']
    revenue = row['revenue_usd']
    track_ids = row['track_id']
    
    # Get actual track info for debugging
    actual_tracks = tracks_df[tracks_df['track_id'].isin(track_ids)][['track_id', 'title', 'artist', 'album']].to_dict('records')
    
    print(f'\nRevenue: ${revenue:.2f}')
    print(f'Title: {title}')
    print(f'Artist: {artist}')
    print(f'Track IDs: {track_ids}')
    print('Actual tracks:')
    for t in actual_tracks:
        print(f"  - ID {t['track_id']}: {t['title']} by {t['artist']} ({t['album']})")

# Get the absolute top song
top_song = top_songs.iloc[0]
final_track_ids = top_song['track_id']
final_title = top_song['title_norm']
final_artist = top_song['artist_norm']
final_revenue = top_song['revenue_usd']

# Get the best representation of this song (most common actual title)
actual_tracks = tracks_df[tracks_df['track_id'].isin(final_track_ids)]
most_common_title = actual_tracks['title'].mode().iloc[0]
most_common_artist = actual_tracks['artist'].mode().iloc[0]

result = {
    'song_title': most_common_title,
    'song_artist': most_common_artist,
    'total_revenue_usd': round(final_revenue, 2),
    'track_ids_count': len(final_track_ids),
    'normalized_title': final_title,
    'normalized_artist': final_artist
}

----BEGIN PRINT FORMAT----
print('__RESULT__:')
print(json.dumps(result))
----END PRINT FORMAT----"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}], 'var_functions.query_db:7': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}], 'var_functions.query_db:8': [{'total_tracks': '19375'}], 'var_functions.query_db:10': [{'total_sales': '58049'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003'}, {'track_id': '964', 'total_revenue': '2425.61'}], 'var_functions.query_db:20': [{'track_id': '964', 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'album': 'None', 'year': 'None'}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}, {'track_id': '5050', 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'album': 'Munich City Nights, Volume 11', 'year': '90'}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}, {'track_id': '6667', 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'album': 'None', 'year': "'04"}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}, {'track_id': '7245', 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'album': 'Indul a boksz', 'year': '1996'}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}, {'track_id': '11641', 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'album': 'Share Your Love', 'year': '1981'}, {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}]}

exec(code, env_args)
