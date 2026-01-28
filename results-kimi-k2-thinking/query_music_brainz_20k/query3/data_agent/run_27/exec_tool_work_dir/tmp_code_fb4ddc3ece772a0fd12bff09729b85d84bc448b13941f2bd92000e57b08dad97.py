code = """import json
import pandas as pd
import numpy as np
import re

# Load data
tracks_file = locals()['var_functions.query_db:6']
sales_file = locals()['var_functions.query_db:8']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)
    
with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Convert to DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert numeric columns
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'])
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['units_sold'] = pd.to_numeric(sales_df['units_sold'])

# Clean/normalize function for entity resolution
def normalize_text(text):
    """Normalize text for comparison"""
    if pd.isna(text) or text is None or text == 'None':
        return ''
    # Convert to string and lowercase
    text = str(text).lower()
    # Remove special characters and extra whitespace
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    # Collapse multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Normalize year - extract 4-digit year if possible
def normalize_year(year):
    """Extract year as 4-digit number"""
    if pd.isna(year) or year is None or year == 'None':
        return None
    year_str = str(year)
    # Look for 4-digit year
    match = re.search(r'(19|20)\d{2}', year_str)
    if match:
        return int(match.group())
    # Look for 2-digit year and try to convert to 4-digit
    match = re.search(r'\d{2}', year_str)
    if match:
        year_val = int(match.group())
        if year_val >= 50:
            return 1900 + year_val
        else:
            return 2000 + year_val
    return None

# Normalize track data
tracks_df['norm_title'] = tracks_df['title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)
tracks_df['norm_album'] = tracks_df['album'].apply(normalize_text)
tracks_df['norm_year'] = tracks_df['year'].apply(normalize_year)

# For entity resolution, create a composite key using title and artist primarily
# Group similar tracks
group_keys = []

for _, track in tracks_df.iterrows():
    # Create a signature for grouping
    # Use title first 30 chars, artist first 20 chars, and first 4 chars of album
    title_sig = track['norm_title'][:30]
    artist_sig = track['norm_artist'][:20]
    album_sig = track['norm_album'][:15]
    year_sig = str(track['norm_year']) if track['norm_year'] else 'none'
    
    # Create group key
    group_key = f"{title_sig}|{artist_sig}|{album_sig}|{year_sig}"
    group_keys.append(group_key)

tracks_df['group_key'] = group_keys

print('__RESULT__:')
print(json.dumps({
    'status': 'Data normalized',
    'unique_groups': len(tracks_df['group_key'].unique()),
    'total_tracks': len(tracks_df)
}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:20': {'message': 'test'}, 'var_functions.execute_python:28': {'first_chars': '[\n  {\n    "track_id": "1",\n    "source_id": "2",\n    "source_track_id": "MBox7368722-HH",\n    "title": "Daniel Balavoine - L\'enfant aux yeux d\'Italie",\n    "artist": "None",\n    "album": "De vous \\u00e0 elle en passant par moi",\n    "year": "75",\n    "length": "219",\n    "language": "French"\n  },\n  {\n    "track_id": "2",\n    "source_id": "4",\n    "source_track_id": "139137-A047",\n    "title": "007",\n    "artist": "[unknown]",\n    "album": "Cantigas de roda (unknown)",\n    "year": "None",\n    "le'}, 'var_functions.execute_python:30': {'tracks_count': 19375, 'sales_count': 58049, 'sample_track': {'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, 'sample_sale': {'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}}}

exec(code, env_args)
