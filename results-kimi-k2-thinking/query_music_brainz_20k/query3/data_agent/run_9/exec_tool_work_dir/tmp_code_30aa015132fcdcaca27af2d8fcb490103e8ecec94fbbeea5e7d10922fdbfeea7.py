code = """import json
import pandas as pd
from collections import defaultdict
import re

# Load data
tracks_result = locals()['var_functions.query_db:12']
sales_result = locals()['var_functions.query_db:13']

if isinstance(tracks_result, str) and '.json' in tracks_result:
    with open(tracks_result, 'r') as f:
        tracks_data = json.load(f)
else:
    tracks_data = tracks_result

if isinstance(sales_result, str) and '.json' in sales_result:
    with open(sales_result, 'r') as f:
        sales_data = json.load(f)
else:
    sales_data = sales_result

# Convert to DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert numeric fields
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Clean and normalize track data
def clean_title(title):
    if not title or title == 'None':
        return ''
    # Remove common prefixes/suffixes, whitespace
    title = title.strip().lower()
    # Remove everything in parentheses and brackets for matching
    title = re.sub(r'\s*\([^)]*\)\s*', ' ', title)
    title = re.sub(r'\s*\[[^\]]*\]\s*', ' ', title)
    # Remove special characters but keep spaces
    title = re.sub(r'[^a-z0-9\s]', ' ', title)
    # Collapse multiple spaces
    title = re.sub(r'\s+', ' ', title)
    return title.strip()

def clean_artist(artist):
    if not artist or artist == 'None' or artist == '[unknown]':
        return ''
    artist = artist.strip().lower()
    # Remove special characters
    artist = re.sub(r'[^a-z0-9\s]', ' ', artist)
    artist = re.sub(r'\s+', ' ', artist)
    return artist.strip()

def clean_album(album):
    if not album or album == 'None':
        return ''
    album = album.strip().lower()
    album = re.sub(r'\s*\([^)]*\)\s*', ' ', album)
    album = re.sub(r'\s*\[[^\]]*\]\s*', ' ', album)
    album = re.sub(r'[^a-z0-9\s]', ' ', album)
    album = re.sub(r'\s+', ' ', album)
    return album.strip()

def normalize_year(year):
    if not year or year == 'None':
        return None
    year = str(year).strip()
    # Extract 4-digit year if present
    match = re.search(r'(19|20)\d{2}', year)
    if match:
        return int(match.group())
    # Handle 2-digit years
    if len(year) == 2:
        if year.startswith('0'):
            return int('20' + year)
        elif int(year) < 30:  # Assuming 00-29 is 2000s
            return int('20' + year)
        else:  # 30-99 is 1900s
            return int('19' + year)
    try:
        return int(year)
    except:
        return None

# Apply cleaning
tracks_df['clean_title'] = tracks_df['title'].apply(clean_title)
tracks_df['clean_artist'] = tracks_df['artist'].apply(clean_artist)
tracks_df['clean_album'] = tracks_df['album'].apply(clean_album)
tracks_df['norm_year'] = tracks_df['year'].apply(normalize_year)

# Remove rows with empty titles or artists
tracks_clean = tracks_df[(tracks_df['clean_title'] != '') & (tracks_df['clean_artist'] != '')].copy()

print('__RESULT__:')
print(json.dumps({
    'original_tracks': len(tracks_df),
    'clean_tracks': len(tracks_clean),
    'removed_tracks': len(tracks_df) - len(tracks_clean)
}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'cid': '0', 'name': 'track_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'source_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'source_track_id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'title', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'artist', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'album', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'year', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'length', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'language', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:9': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:8': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.execute_python:10': {'status': 'data structures understood', 'tracks_fields': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_fields': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.execute_python:18': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375, 'unique_track_ids_in_tracks': 19375}}

exec(code, env_args)
