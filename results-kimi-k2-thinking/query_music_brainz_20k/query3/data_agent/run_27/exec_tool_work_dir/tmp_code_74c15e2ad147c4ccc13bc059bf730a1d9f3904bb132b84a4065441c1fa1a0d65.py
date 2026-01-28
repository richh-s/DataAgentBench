code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load all track data
tracks_file = var_functions.query_db:6
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

# Load all sales data
sales_file = var_functions.query_db:8
with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert data types
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'])
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['units_sold'] = pd.to_numeric(sales_df['units_sold'])

# Normalize function for entity resolution
def normalize_text(text):
    if pd.isna(text) or text == 'None':
        return ''
    return str(text).lower().strip()

def normalize_year(year):
    if pd.isna(year) or year == 'None':
        return None
    match = re.search(r'(19|20)\d{2}', str(year))
    return int(match.group()) if match else None

# Normalize tracks
tracks_df['norm_title'] = tracks_df['title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)
tracks_df['norm_album'] = tracks_df['album'].apply(normalize_text)
tracks_df['norm_year'] = tracks_df['year'].apply(normalize_year)

# Create group keys for entity resolution based on title and artist similarity
# Use a simple approach: group by normalized title first 40 chars + normalized artist first 30 chars
tracks_df['group_key'] = tracks_df.apply(
    lambda r: f"{r['norm_title'][:40]}|{r['norm_artist'][:30]}", axis=1
)

# Find potential duplicate groups
group_sizes = tracks_df['group_key'].value_counts()
print('__RESULT__:')
print(json.dumps({
    'total_tracks': len(tracks_df),
    'total_sales': len(sales_df),
    'unique_groups': len(tracks_df['group_key'].unique()),
    'groups_size_1': (group_sizes == 1).sum(),
    'groups_size_2+': (group_sizes >= 2).sum(),
    'largest_group_size': int(group_sizes.max()),
    'sample_duplicate_groups': group_sizes[group_sizes >= 2].head(5).to_dict()
}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:20': {'message': 'test'}, 'var_functions.execute_python:28': {'first_chars': '[\n  {\n    "track_id": "1",\n    "source_id": "2",\n    "source_track_id": "MBox7368722-HH",\n    "title": "Daniel Balavoine - L\'enfant aux yeux d\'Italie",\n    "artist": "None",\n    "album": "De vous \\u00e0 elle en passant par moi",\n    "year": "75",\n    "length": "219",\n    "language": "French"\n  },\n  {\n    "track_id": "2",\n    "source_id": "4",\n    "source_track_id": "139137-A047",\n    "title": "007",\n    "artist": "[unknown]",\n    "album": "Cantigas de roda (unknown)",\n    "year": "None",\n    "le'}, 'var_functions.execute_python:30': {'tracks_count': 19375, 'sales_count': 58049, 'sample_track': {'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, 'sample_sale': {'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}}, 'var_functions.query_db:36': [{'track_id': '14719', 'total_revenue': '2522.82', 'total_units': '2109.0'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996', 'total_units': '2216.0'}, {'track_id': '1344', 'total_revenue': '2500.72', 'total_units': '2186.0'}, {'track_id': '6725', 'total_revenue': '2489.81', 'total_units': '2050.0'}, {'track_id': '10377', 'total_revenue': '2466.71', 'total_units': '2263.0'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004', 'total_units': '2063.0'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003', 'total_units': '2182.0'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003', 'total_units': '2086.0'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003', 'total_units': '2136.0'}, {'track_id': '964', 'total_revenue': '2425.61', 'total_units': '2194.0'}], 'var_functions.query_db:38': [{'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}, {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:40': [{'track_id': '14719', 'source_id': '5', 'source_track_id': '11323763', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009', 'length': '223000', 'language': 'German'}], 'var_functions.query_db:44': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:46': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:48': [{'track_id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010'}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}, {'track_id': '5184', 'title': "I'll Tell You - Autumn o f Their Years", 'artist': 'Beau Brummels', 'album': 'None', 'year': 'None'}, {'track_id': '15506', 'title': "The Beau Brummels - I'll Tell You", 'artist': 'None', 'album': 'Autumn of Their Years', 'year': 'None'}], 'var_functions.query_db:50': [{'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}, {'track_id': '2751', 'title': '004-Life Cycles', 'artist': 'Chosen', 'album': 'Space Jams (2011)', 'year': 'None'}, {'track_id': '16384', 'title': 'Life Cycles - Space Jams', 'artist': 'Chosen', 'album': 'None', 'year': "'11"}], 'var_functions.query_db:52': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:54': [{'track_id': '1344', 'revenue_usd': '504.59'}, {'track_id': '1344', 'revenue_usd': '548.79'}, {'track_id': '1344', 'revenue_usd': '534.69'}, {'track_id': '1344', 'revenue_usd': '411.47'}, {'track_id': '1344', 'revenue_usd': '501.18'}, {'track_id': '2751', 'revenue_usd': '361.08'}, {'track_id': '2751', 'revenue_usd': '454.11'}, {'track_id': '2751', 'revenue_usd': '444.0'}, {'track_id': '2751', 'revenue_usd': '18.5'}, {'track_id': '2751', 'revenue_usd': '179.44'}, {'track_id': '16384', 'revenue_usd': '360.77'}, {'track_id': '16384', 'revenue_usd': '228.2'}]}

exec(code, env_args)
