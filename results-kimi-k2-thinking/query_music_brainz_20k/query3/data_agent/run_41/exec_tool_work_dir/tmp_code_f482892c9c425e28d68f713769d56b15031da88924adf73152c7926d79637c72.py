code = """import json
import pandas as pd
import re

# Load the full sales data by track_id
sales_file_path = locals()['var_functions.query_db:11']
with open(sales_file_path, 'r') as f:
    sales_by_track = json.load(f)

# Load the full tracks data
tracks_file_path = locals()['var_functions.query_db:8']
with open(tracks_file_path, 'r') as f:
    tracks = json.load(f)

# Convert to DataFrames
df_sales = pd.DataFrame(sales_by_track)
df_tracks = pd.DataFrame(tracks)

# Ensure revenue is numeric
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge sales with tracks
df_merged = df_sales.merge(df_tracks[['track_id', 'title', 'artist', 'album']], on='track_id', how='left')

# Clean the data for entity resolution
def clean_text(text):
    if pd.isna(text) or text is None or text == 'None':
        return ''
    return str(text).strip().lower()

# Clean track metadata for grouping
df_merged['clean_title'] = df_merged['title'].apply(clean_text)
df_merged['clean_artist'] = df_merged['artist'].apply(clean_text)
df_merged['clean_album'] = df_merged['album'].apply(clean_text)

# Remove common noise from titles like "(live)", "- acoustic", etc.
def normalize_title(title):
    if not title:
        return title
    # Remove common suffixes/prefixes that indicate versions
    title = re.sub(r'\s*[-:]\s*(live|acoustic|remix|version|edit|demo|radio|studio|alternate).*', '', title)
    title = re.sub(r'\s*\(.*?(live|acoustic|remix|version|edit|demo|radio|studio|alternate).*?\)', '', title)
    title = re.sub(r'^[^-]*-\s*', '', title)  # Remove "Artist - " prefix if in title
    return title.strip()

df_merged['normalized_title'] = df_merged['clean_title'].apply(normalize_title)

# Group by normalized metadata to consolidate duplicates
revenue_by_song = df_merged.groupby([
    'normalized_title', 
    'clean_artist'
]).agg({
    'total_revenue': 'sum',
    'clean_album': lambda x: x.mode().iloc[0] if not x.empty and not x.mode().empty else ''
}).reset_index()

# Find the song with highest revenue
top_song = revenue_by_song.loc[revenue_by_song['total_revenue'].idxmax()]

result = {
    'title': top_song['normalized_title'].title() if top_song['normalized_title'] else 'Unknown Title',
    'artist': top_song['clean_artist'].title() if top_song['clean_artist'] else 'Unknown Artist', 
    'album': top_song['clean_album'].title() if top_song['clean_album'] else 'Unknown Album',
    'total_revenue': round(float(top_song['total_revenue']), 2)
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:4': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}, {'track_id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005'}, {'track_id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05'}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96'}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007'}, {'track_id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997'}], 'var_functions.query_db:7': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
