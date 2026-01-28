code = """import json
import pandas as pd
import re

# Load data
tracks_var = locals()['var_functions.query_db:12']
if isinstance(tracks_var, str) and tracks_var.endswith('.json'):
    with open(tracks_var, 'r') as f:
        tracks_data = json.load(f)
else:
    tracks_data = tracks_var

sales_var = locals()['var_functions.query_db:6']
if isinstance(sales_var, str) and sales_var.endswith('.json'):
    with open(sales_var, 'r') as f:
        sales_data = json.load(f)
else:
    sales_data = sales_var

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Clean data types
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

# Calculate revenue per track
track_revenues = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()

# Merge with tracks
tracks_with_revenue = pd.merge(tracks_df, track_revenues, on='track_id', how='inner')

# Filter out placeholder titles
placeholder_patterns = [
    r'^none$', r'^\s*$', r'^\s*[-_]+\s*$', r'^\d+$', r'^\d+[-_].*',
    r'^\s*\[untitled\]\s*$', r'^\s*n\.a\.\s*$', r'^0+-*\s*$'
]

mask = pd.Series(True, index=tracks_with_revenue.index)
for pattern in placeholder_patterns:
    mask = mask & ~tracks_with_revenue['title'].str.fullmatch(pattern, case=False, na=True)

tracks_clean = tracks_with_revenue[mask].copy()

# Clean title function
def clean_title(title):
    if pd.isna(title):
        return ''
    title = str(title)
    # Remove leading numbers
    title = re.sub(r'^\s*\d+[-\s\.\)]*\s*', '', title)
    # Extract title from "Artist - Title"
    if ' - ' in title:
        parts = title.split(' - ')
        if len(parts) >= 2 and len(parts[0]) < 100:
            title = parts[-1]
    # Remove dates and markers
    title = re.sub(r'\(.*?(?:live|acoustic|remix|edit|version|\d{4}).*\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s+', ' ', title).strip()
    return title

tracks_clean['clean_title'] = tracks_clean['title'].apply(clean_title)
tracks_clean = tracks_clean[tracks_clean['clean_title'].str.len() > 2]

# Normalize for grouping
tracks_clean['title_norm'] = tracks_clean['clean_title'].str.lower().str.replace(r'[^a-z0-9\s]', '', regex=True)
tracks_clean['artist_norm'] = tracks_clean['artist'].fillna('unknown').str.lower().str.strip()

# Group by normalized title and artist, sum revenues
song_groups = tracks_clean.groupby(['title_norm', 'artist_norm']).agg({
    'revenue_usd': 'sum',
    'track_id': 'count'
}).reset_index()

song_groups = song_groups.sort_values('revenue_usd', ascending=False)

top_song = song_groups.iloc[0]

# Get examples of this song
example_tracks = tracks_clean[
    (tracks_clean['title_norm'] == top_song['title_norm']) &
    (tracks_clean['artist_norm'] == top_song['artist_norm'])
][['track_id', 'title', 'artist', 'revenue_usd']].head()

result = {
    'song_title': top_song['title_norm'],
    'artist': top_song['artist_norm'],
    'total_revenue': float(top_song['revenue_usd']),
    'track_variations': int(top_song['track_id']),
    'example_tracks': example_tracks.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:4': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'sales_rows': 58049, 'tracks_rows': 10, 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sample_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375, 'unique_track_ids_in_tracks': 19375, 'sales_revenue_stats': {'mean': 284.72739151406574, 'max': 641.82, 'min': 0.99, 'total': 16528140.350000001}}, 'var_functions.execute_python:18': {'first_20_tracks': [{'id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None'}, {'id': '2', 'title': '007', 'artist': '[unknown]'}, {'id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None'}, {'id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli'}, {'id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet'}, {'id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young'}, {'id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None'}, {'id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None'}, {'id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington'}, {'id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας'}, {'id': '11', 'title': 'None', 'artist': 'Anathema'}, {'id': '12', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal'}, {'id': '13', 'title': '002-Particle/Wave', 'artist': 'Lunchbox'}, {'id': '14', 'title': '001-Deja Vu', 'artist': 'Blanket'}, {'id': '15', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters'}, {'id': '16', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch'}, {'id': '17', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None'}, {'id': '18', 'title': '00-1', 'artist': 'None'}, {'id': '19', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye'}, {'id': '20', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini'}]}, 'var_functions.execute_python:22': {'tracks_after_cleaning': 19308, 'sample_normalized': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'clean_title': "L'enfant aux yeux d'Italie", 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'lenfantauxyeuxditalie', 'artist_key': 'unknown'}, {'track_id': '2', 'title': '007', 'clean_title': '007', 'artist': '[unknown]', 'clean_artist': 'Unknown', 'title_key': '007', 'artist_key': 'unknown'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'clean_title': 'Mustard Gas', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'mustardgas', 'artist_key': 'unknown'}, {'track_id': '4', 'title': 'Your Grace', 'clean_title': 'Your Grace', 'artist': 'Kathy Troccoli', 'clean_artist': 'Kathy Troccoli', 'title_key': 'yourgrace', 'artist_key': 'kathytroccoli'}, {'track_id': '5', 'title': "Well You Needn't", 'clean_title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'clean_artist': 'Ernie Stadler Jazz Quintet', 'title_key': 'wellyouneednt', 'artist_key': 'erniestadlerjazzquintet'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'clean_title': 'Try (acoustic)', 'artist': 'Neil Young', 'clean_artist': 'Neil Young', 'title_key': 'tryacoustic', 'artist_key': 'neilyoung'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'clean_title': 'Sttreet Hype', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'sttreethype', 'artist_key': 'unknown'}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'clean_title': 'Ballade à donner', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'balladedonner', 'artist_key': 'unknown'}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'clean_title': "Just Like Tom Thumb's Blues", 'artist': 'Wendy Saddington', 'clean_artist': 'Wendy Saddington', 'title_key': 'justliketomthumbsblues', 'artist_key': 'wendysaddington'}, {'track_id': '10', 'title': 'Στα καμένα', 'clean_title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'clean_artist': 'Λαυρέντης Μαχαιρίίτσας', 'title_key': '', 'artist_key': ''}], 'unique_title_keys': 16881, 'unique_combinations': 18500}, 'var_functions.execute_python:24': {'top_song_title': 'None', 'top_song_artist': 'None', 'total_revenue': 14647.519999999997, 'track_count': 17, 'track_ids_sample': ['2126', '2153', '3422', '4421', '5048'], 'revenue_by_track': [{'track_id': '2126', 'revenue': 1102.6899999999998}, {'track_id': '2153', 'revenue': 1246.92}, {'track_id': '3422', 'revenue': 492.4}, {'track_id': '4421', 'revenue': 3.14}, {'track_id': '5048', 'revenue': 1630.66}, {'track_id': '7036', 'revenue': 745.94}, {'track_id': '7146', 'revenue': 45.93}, {'track_id': '7481', 'revenue': 786.56}, {'track_id': '9478', 'revenue': 455.7}, {'track_id': '9788', 'revenue': 1791.84}]}, 'var_functions.execute_python:26': {'top_song_normalized_title': '[untitled]', 'total_revenue': 23134.27, 'track_variations': 25, 'example_variations': [{'original_title': 'David Weber - [untitled]', 'artist': 'None', 'revenue': 1236.1000000000001}, {'original_title': '[untitled]', 'artist': 'WB Loops', 'revenue': 849.13}, {'original_title': 'Amino People - [untitled]', 'artist': 'None', 'revenue': 915.63}, {'original_title': 'Howard Blake - [untitled]', 'artist': 'None', 'revenue': 708.72}, {'original_title': '[untitled]', 'artist': '神聖かまってちゃん', 'revenue': 710.3100000000001}]}, 'var_functions.execute_python:28': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': [{'track_id': '14719', 'revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö'}, {'track_id': '5124', 'revenue': 2503.19, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels'}, {'track_id': '1344', 'revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen'}, {'track_id': '6725', 'revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers'}, {'track_id': '10377', 'revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas'}, {'track_id': '5050', 'revenue': 2466.31, 'title': "Chilliwack - Who's Winning", 'artist': 'None'}, {'track_id': '6667', 'revenue': 2452.7, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven'}, {'track_id': '7245', 'revenue': 2436.97, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick'}, {'track_id': '11641', 'revenue': 2428.22, 'title': 'So in Love With You', 'artist': 'Kenny Rogers'}, {'track_id': '964', 'revenue': 2425.61, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge'}]}

exec(code, env_args)
