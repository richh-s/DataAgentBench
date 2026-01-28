code = """import json
import pandas as pd
import re

# Load complete data
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
df_tracks = pd.DataFrame(tracks_data)
df_sales = pd.DataFrame(sales_data)

# Clean and normalize data
 df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'])
 df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Clean title: extract main song title (remove dates, live info, etc)
def clean_title(title):
    if not title or title == 'None':
        return ''
    # Remove common suffixes like dates, live info, remix info
    title = re.sub(r'\s*-\s*\d{4}.*', '', title)  # Remove - YYYY or - YYYY-MM-DD
    title = re.sub(r'\s*\(.*\d{4}.*\)$', '', title)  # Remove (YYYY) or (live YYYY)
    title = re.sub(r'\s*-\s*live.*', '', title, flags=re.IGNORECASE)  # Remove - live
    title = re.sub(r'\s*\(live.*\)$', '', title, flags=re.IGNORECASE)  # Remove (live)
    title = re.sub(r'\s*remix.*', '', title, flags=re.IGNORECASE)  # Remove remix
    # Extract just the song title (before any hyphens that might separate artist)
    parts = title.split(' - ')
    if len(parts) > 1 and len(parts[0]) < 50:  # If first part looks like artist
        return parts[1].strip() if len(parts[1].strip()) > 2 else title.strip()
    return title.strip()

# Clean artist
def clean_artist(artist):
    if not artist or artist in ['None', '[unknown]', '   ']:
        return 'Unknown'
    return artist.strip()

# Apply cleaning
df_tracks['clean_title'] = df_tracks['title'].apply(clean_title)
df_tracks['clean_artist'] = df_tracks['artist'].apply(clean_artist)

# Remove empty titles
df_tracks = df_tracks[df_tracks['clean_title'].str.len() > 0]

# Create normalized identifiers
df_tracks['title_key'] = df_tracks['clean_title'].str.lower().str.replace(r'[^a-z0-9]', '', regex=True)
df_tracks['artist_key'] = df_tracks['clean_artist'].str.lower().str.replace(r'[^a-z0-9]', '', regex=True)

print('__RESULT__:')
print(json.dumps({
    'tracks_after_cleaning': len(df_tracks),
    'sample_normalized': df_tracks[['track_id', 'title', 'clean_title', 'artist', 'clean_artist', 'title_key', 'artist_key']].head(10).to_dict('records'),
    'unique_title_keys': len(df_tracks['title_key'].unique()),
    'unique_combinations': len(df_tracks.groupby(['title_key', 'artist_key']))
}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:4': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'sales_rows': 58049, 'tracks_rows': 10, 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sample_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375, 'unique_track_ids_in_tracks': 19375, 'sales_revenue_stats': {'mean': 284.72739151406574, 'max': 641.82, 'min': 0.99, 'total': 16528140.350000001}}, 'var_functions.execute_python:18': {'first_20_tracks': [{'id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None'}, {'id': '2', 'title': '007', 'artist': '[unknown]'}, {'id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None'}, {'id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli'}, {'id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet'}, {'id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young'}, {'id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None'}, {'id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None'}, {'id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington'}, {'id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας'}, {'id': '11', 'title': 'None', 'artist': 'Anathema'}, {'id': '12', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal'}, {'id': '13', 'title': '002-Particle/Wave', 'artist': 'Lunchbox'}, {'id': '14', 'title': '001-Deja Vu', 'artist': 'Blanket'}, {'id': '15', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters'}, {'id': '16', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch'}, {'id': '17', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None'}, {'id': '18', 'title': '00-1', 'artist': 'None'}, {'id': '19', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye'}, {'id': '20', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini'}]}}

exec(code, env_args)
