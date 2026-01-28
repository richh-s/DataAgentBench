code = """import json
import pandas as pd
import re

# Read the full data again for a fresh analysis
tracks_file_path = locals()['var_functions.query_db:6']
sales_file_path = locals()['var_functions.query_db:8']

with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert revenue and units to numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')
sales_df['units_sold'] = pd.to_numeric(sales_df['units_sold'], errors='coerce')

# Extract clean artist and title
def parse_track_info(row):
    title = str(row['title']) if row['title'] and str(row['title']) != 'None' else ''
    artist = str(row['artist']) if row['artist'] and str(row['artist']) != 'None' else ''
    
    # Try to parse "Artist - Title" format
    if not artist and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2 and len(parts[0]) < 100:  # Reasonable artist name length
            artist = parts[0]
            title = parts[1]
    
    return pd.Series({'parsed_title': title.strip(), 'parsed_artist': artist.strip()})

tracks_df[['parsed_title', 'parsed_artist']] = tracks_df.apply(parse_track_info, axis=1)

# Get top revenue tracks by individual track_id first (simple aggregation)
simple_revenue = sales_df.groupby('track_id').agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum'
}).reset_index()

# Merge with track info
tracks_simple = simple_revenue.merge(
    tracks_df[['track_id', 'parsed_title', 'parsed_artist']], 
    on='track_id', 
    how='left'
)

# Fill missing values
tracks_simple['parsed_title'] = tracks_simple['parsed_title'].fillna('Unknown')
tracks_simple['parsed_artist'] = tracks_simple['parsed_artist'].fillna('Unknown')

# Filter out generic/placeholder tracks
valid_tracks = tracks_simple[
    ~tracks_simple['parsed_title'].isin(['', 'None', 'Unknown', '-']) &
    ~tracks_simple['parsed_artist'].isin(['', 'None', 'Unknown', '[unknown]', ' '])
]

# Remove tracks with suspiciously short titles that might be test data
valid_tracks = valid_tracks[
    (valid_tracks['parsed_title'].str.len() > 2) | 
    (valid_tracks['parsed_artist'].str.len() > 2)
]

# Find the top revenue track
top_track = valid_tracks.loc[valid_tracks['revenue_usd'].idxmax()]

# Also aggregate by artist-title combination for entity resolution
def normalize_text(text):
    if pd.isna(text) or text == 'None':
        return ''
    return re.sub(r'[^\w\s]', '', str(text).lower().strip())

valid_tracks['norm_title'] = valid_tracks['parsed_title'].apply(normalize_text)
valid_tracks['norm_artist'] = valid_tracks['parsed_artist'].apply(normalize_text)

# Group by normalized title and artist (basic entity resolution)
entity_groups = valid_tracks.groupby(['norm_title', 'norm_artist']).agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum',
    'parsed_title': 'first',
    'parsed_artist': 'first'
}).reset_index()

# Sort by revenue
top_entities = entity_groups.nlargest(10, 'revenue_usd')

# Get actual top song
top_entity = top_entities.iloc[0]

result = {
    'top_song_by_single_track_id': {
        'title': top_track['parsed_title'],
        'artist': top_track['parsed_artist'],
        'revenue': float(top_track['revenue_usd']),
        'units_sold': int(top_track['units_sold']),
        'track_id': int(top_track['track_id'])
    },
    'top_song_by_entity_resolution': {
        'title': top_entity['parsed_title'],
        'artist': top_entity['parsed_artist'],
        'revenue': float(top_entity['revenue_usd']),
        'units_sold': int(top_entity['units_sold'])
    },
    'top_10_entities': top_entities[['parsed_title', 'parsed_artist', 'revenue_usd']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'song_title': 'None', 'artist': 'None', 'total_revenue_usd': 14647.52, 'top_10_preview': [{'entity_key': 'none|none', 'revenue_usd': 14647.52, 'title': 'None', 'artist': 'None'}, {'entity_key': '010-|none', 'revenue_usd': 4163.48, 'title': '010-', 'artist': 'None'}, {'entity_key': 'groovey|rich matteson', 'revenue_usd': 4128.59, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'entity_key': 'the fire still burns|russ ballard', 'revenue_usd': 3807.4, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'entity_key': 'vostok|craig padilla', 'revenue_usd': 3767.95, 'title': 'Vostok', 'artist': 'Craig Padilla'}, {'entity_key': '001-|none', 'revenue_usd': 3742.44, 'title': '001-', 'artist': 'None'}, {'entity_key': '003-|none', 'revenue_usd': 3446.78, 'title': '003-', 'artist': 'None'}, {'entity_key': '003-|', 'revenue_usd': 3394.3999999999996, 'title': '003-', 'artist': ' '}, {'entity_key': '005-|none', 'revenue_usd': 3347.8900000000003, 'title': '005-', 'artist': 'None'}, {'entity_key': '002-|none', 'revenue_usd': 3343.61, 'title': '002-', 'artist': 'None'}]}, 'var_functions.execute_python:12': {'song_title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue_usd': 5417.34, 'total_units_sold': 4823, 'top_10_preview': [{'clean_title': 'Groovey', 'clean_artist': 'Rich Matteson', 'revenue_usd': 5417.34}, {'clean_title': 'All My Friends Say (album version)', 'clean_artist': 'Luke Bryan', 'revenue_usd': 4110.55}, {'clean_title': 'Kapitel 01', 'clean_artist': 'Kerstin Gier', 'revenue_usd': 4091.12}, {'clean_title': 'Beautiful (instrumental)', 'clean_artist': 'Damian Marley', 'revenue_usd': 4004.4199999999996}, {'clean_title': 'The Story of Your Life', 'clean_artist': 'Matthew Barber', 'revenue_usd': 3962.9700000000003}, {'clean_title': 'A Wand\'ring Minstrel I, From "The Mikado"', 'clean_artist': 'Sir William Gilbert & Sir Arthur Sullivan', 'revenue_usd': 3877.4300000000003}, {'clean_title': 'The Fire Still Burns', 'clean_artist': 'Russ Ballard', 'revenue_usd': 3807.4}, {'clean_title': 'Vostok', 'clean_artist': 'Craig Padilla', 'revenue_usd': 3767.95}, {'clean_title': 'Oblivion Beckons', 'clean_artist': 'Byzantine', 'revenue_usd': 3759.01}, {'clean_title': 'So in Love With You', 'clean_artist': 'Kenny Rogers', 'revenue_usd': 3642.04}]}}

exec(code, env_args)
