code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load data
tracks_file = locals()['var_functions.query_db:8']
sales_file = locals()['var_functions.query_db:10']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

df_tracks = pd.DataFrame(tracks_data)
df_sales = pd.DataFrame(sales_data)

# Convert data types
df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)

# Clean text fields
def clean_field(text):
    if pd.isna(text) or text == 'None':
        return ''
    return str(text).lower().strip()

df_tracks['clean_title'] = df_tracks['title'].apply(clean_field)
df_tracks['clean_artist'] = df_tracks['artist'].apply(clean_field)
df_tracks['clean_album'] = df_tracks['album'].apply(clean_field)

# Filter out very short or numeric titles
df_tracks = df_tracks[
    (df_tracks['clean_title'].str.len() > 2) & 
    (~df_tracks['clean_title'].str.match(r'^[0-9\s\-]+$'))
]

# Create entity resolution key
def normalize_song_key(title, artist, album):
    # Clean title
    title = re.sub(r'\s*[-\(]\s*live[^)]*$', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*[-\(]\s*acoustic[^)]*$', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*[-\(]\s*remix[^)]*$', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\d{4}.*$', '', title)
    title = re.sub(r'\s*\(.*\d{4}.*\)$', '', title)
    title = title.strip()
    
    # Extract primary artist
    artist = artist.split(' & ')[0].split(' and ')[0]
    artist = artist.split(' ft ')[0].split(' feat ')[0]
    artist = artist.split(' with ')[0].split(' pres. ')[0]
    artist = artist.split(',')[0].split(';')[0]
    artist = artist.strip()
    
    return f"{title}###{artist}"

df_tracks['song_key'] = df_tracks.apply(lambda x: normalize_song_key(x['clean_title'], x['clean_artist'], x['clean_album']), axis=1)

# Remove empty keys
df_tracks = df_tracks[df_tracks['song_key'] != '###']

# Build mapping and aggregate revenue
song_revenue = defaultdict(float)
song_track_ids = defaultdict(set)
track_to_song = dict(zip(df_tracks['track_id'].astype(str), df_tracks['song_key']))

for _, sale in df_sales.iterrows():
    track_id = str(sale['track_id'])
    if track_id in track_to_song:
        song_key = track_to_song[track_id]
        song_revenue[song_key] += sale['revenue_usd']
        song_track_ids[song_key].add(track_id)

# Find top song
top_song_key = max(song_revenue, key=song_revenue.get)
top_revenue = song_revenue[top_song_key]
top_title, top_artist = top_song_key.split('###')

# Get all track IDs for this song
top_track_ids = list(song_track_ids[top_song_key])

# Verify by checking some of the actual tracks
sample_tracks = df_tracks[df_tracks['track_id'].isin(top_track_ids[:5])][['track_id', 'title', 'artist', 'album']].to_dict('records')

result = {
    'song_title': top_title,
    'primary_artist': top_artist,
    'total_revenue_usd': top_revenue,
    'distinct_track_ids': len(top_track_ids),
    'sample_track_entries': sample_tracks
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'tracks_rows': 19375, 'sales_rows': 58049, 'track_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'sample_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}]}, 'var_functions.execute_python:20': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375, 'unique_track_ids_in_tracks': 19375, 'sample_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}]}, 'var_functions.execute_python:22': {'song_title': '003-', 'primary_artist': '', 'total_revenue_usd': 7006.609999999999, 'track_ids_count': 28, 'track_ids_sample': ['3833', '3833', '3833', '3833', '5576', '5576', '5576', '5576', '5576', '7540']}, 'var_functions.execute_python:28': {'song_title': 'travel', 'artist': 'guts pie earshot', 'total_revenue_usd': 4783.08, 'duplicate_tracks': 3}, 'var_functions.execute_python:32': {'song_title': 'Systemisch bled', 'artist': 'Stüngö', 'total_revenue_usd': 2522.82}}

exec(code, env_args)
