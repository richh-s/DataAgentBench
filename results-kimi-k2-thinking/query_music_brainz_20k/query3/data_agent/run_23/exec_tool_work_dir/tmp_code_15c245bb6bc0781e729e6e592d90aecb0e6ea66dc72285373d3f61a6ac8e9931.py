code = """import json
import os

# Load data from results
tracks_result = var_functions.query_db:20
sales_result = var_functions.query_db:18

print('Tracks data is a JSON list:', type(tracks_result))
print('Sales data is a JSON list:', type(sales_result))
print('Number of track records:', len(tracks_result))
print('Number of sales records:', len(sales_result))

# Simple analysis
tracks_data = tracks_result
sales_data = sales_result

# Aggregate revenue by title and artist
tracks_dict = {str(t['track_id']): t for t in tracks_data}
sales_by_track = {}

for sale in sales_data:
    track_id = str(sale['track_id'])
    revenue = float(sale['total_revenue'])
    sales_by_track[track_id] = revenue

# Create song groups by title+artist
song_groups = {}
for track_id, revenue in sales_by_track.items():
    if track_id in tracks_dict:
        track = tracks_dict[track_id]
        title = track.get('title', '')
        artist = track.get('artist', '')
        if title and artist:
            # Normalize for comparison
            key = f"{title.lower().strip()}::{artist.lower().strip()}"
            if key not in song_groups:
                song_groups[key] = {'revenue': 0, 'title': title, 'artist': artist}
            song_groups[key]['revenue'] += revenue

# Sort by revenue
sorted_songs = sorted(song_groups.items(), key=lambda x: x[1]['revenue'], reverse=True)

print('Top 5 songs by revenue:')
for i in range(min(5, len(sorted_songs))):
    key, song = sorted_songs[i]
    print(f"{i+1}. {song['title']} by {song['artist']} - ${song['revenue']:.2f}")

# Get the top song
top_song = sorted_songs[0][1] if sorted_songs else None

result = {
    'title': top_song['title'],
    'artist': top_song['artist'],
    'revenue': round(top_song['revenue'], 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}], 'var_functions.query_db:7': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}], 'var_functions.query_db:8': [{'total_tracks': '19375'}], 'var_functions.query_db:10': [{'total_sales': '58049'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003'}, {'track_id': '964', 'total_revenue': '2425.61'}], 'var_functions.query_db:20': [{'track_id': '964', 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'album': 'None', 'year': 'None'}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}, {'track_id': '5050', 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'album': 'Munich City Nights, Volume 11', 'year': '90'}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}, {'track_id': '6667', 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'album': 'None', 'year': "'04"}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}, {'track_id': '7245', 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'album': 'Indul a boksz', 'year': '1996'}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}, {'track_id': '11641', 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'album': 'Share Your Love', 'year': '1981'}, {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
