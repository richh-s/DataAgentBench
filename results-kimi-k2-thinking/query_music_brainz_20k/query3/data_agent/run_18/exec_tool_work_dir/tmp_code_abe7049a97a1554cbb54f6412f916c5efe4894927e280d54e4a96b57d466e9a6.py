code = """import json
import pandas as pd
import re
import numpy as np

# Load tracks data
tracks_file = locals()['var_functions.query_db:8']
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

# Load sales data
sales_file = locals()['var_functions.query_db:16']
with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Convert to DataFrames
df_tracks = pd.DataFrame(tracks_data)
df_sales = pd.DataFrame(sales_data)

# Convert data types
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)
df_sales['units_sold'] = df_sales['units_sold'].astype(int)
df_tracks['track_id'] = df_tracks['track_id'].astype(int)

# Clean and normalize track data
def clean_text(text):
    if text is None or pd.isna(text) or str(text).strip().lower() in ['none', '[unknown]', '']:
        return None
    return str(text).strip()

def normalize_year(year):
    if year is None or pd.isna(year) or str(year).strip().lower() in ['none', '']:
        return None
    
    year_str = str(year).strip()
    
    # Handle formats like '11, '89
    if year_str.startswith("'") and len(year_str) >= 3:
        year_str = year_str[1:]
    
    # Extract year from strings like '(2010)', '[2005]'
    year_match = re.search(r'\d{4}', year_str)
    if year_match:
        year_str = year_match.group()
    
    try:
        year_int = int(year_str)
        # Handle 2-digit years
        if year_int < 100:
            if year_int >= 50:
                return 1900 + year_int
            else:
                return 2000 + year_int
        return year_int
    except:
        return None

# Apply cleaning
df_tracks['artist_clean'] = df_tracks['artist'].apply(clean_text)
df_tracks['title_clean'] = df_tracks['title'].apply(clean_text)
df_tracks['album_clean'] = df_tracks['album'].apply(clean_text)
df_tracks['year_clean'] = df_tracks['year'].apply(normalize_year)

# Extract artist from title if artist is missing or [unknown]
def extract_artist_from_title(title):
    if title and ' - ' in str(title):
        parts = str(title).split(' - ', 1)
        if len(parts) == 2:
            artist = clean_text(parts[0])
            if artist:
                return artist
    return None

# Apply artist extraction
mask_missing_artist = (df_tracks['artist_clean'].isna()) | (df_tracks['artist_clean'] == '[unknown]') | (df_tracks['artist_clean'] == 'None')
df_tracks['artist_from_title'] = df_tracks['title'].apply(extract_artist_from_title)

# Use extracted artist if available
mask_extracted = mask_missing_artist & df_tracks['artist_from_title'].notna()
df_tracks.loc[mask_extracted, 'artist_clean'] = df_tracks.loc[mask_extracted, 'artist_from_title']

# Clean title (remove artist prefix if it exists)
def clean_title(title):
    if title is None or pd.isna(title):
        return None
    title_str = str(title).strip()
    if ' - ' in title_str:
        parts = title_str.split(' - ', 1)
        if len(parts) == 2:
            return clean_text(parts[1])
    return clean_text(title)

df_tracks['final_title'] = df_tracks['title'].apply(clean_title)

# Create a grouping key for entity resolution
def create_group_key(row):
    artist = row['artist_clean'] if row['artist_clean'] else 'unknown'
    title = row['final_title'] if row['final_title'] else 'unknown'
    album = row['album_clean'] if row['album_clean'] else 'unknown'
    year = row['year_clean'] if row['year_clean'] else 0
    
    # Clean up for key generation
    artist_key = re.sub(r'[^a-zA-Z0-9]', '', str(artist).lower())[:30]
    title_key = re.sub(r'[^a-zA-Z0-9]', '', str(title).lower())[:40]
    album_key = re.sub(r'[^a-zA-Z0-9]', '', str(album).lower())[:30]
    
    key = f"{artist_key}|{title_key}|{album_key}|{year}"
    return key

df_tracks['group_key'] = df_tracks.apply(create_group_key, axis=1)

# Merge tracks with sales
df_merged = df_sales.merge(df_tracks[['track_id', 'group_key', 'title', 'artist', 'artist_clean', 'final_title']], 
                           on='track_id', how='inner')

# Calculate total revenue per track group
group_revenue = df_merged.groupby('group_key').agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum',
    'title': lambda x: x.iloc[0],  # Keep first title
    'artist': lambda x: x.iloc[0],  # Keep first artist
    'artist_clean': lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0],  # Most common clean artist
    'final_title': lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0]    # Most common clean title
}).reset_index()

# Sort by revenue descending
group_revenue = group_revenue.sort_values('revenue_usd', ascending=False)

# Get the top track
top_track = group_revenue.iloc[0]

# Determine best title and artist to display
title_to_display = top_track['final_title'] if pd.notna(top_track['final_title']) and top_track['final_title'] else top_track['title']
artist_to_display = top_track['artist_clean'] if pd.notna(top_track['artist_clean']) and top_track['artist_clean'] else top_track['artist']

if not artist_to_display or artist_to_display.lower() in ['none', '[unknown]', '']:
    # Try to extract from title
    if ' - ' in str(top_track['title']):
        parts = str(top_track['title']).split(' - ', 1)
        if len(parts) == 2:
            artist_to_display = parts[0].strip()
            title_to_display = parts[1].strip()
    else:
        artist_to_display = top_track['artist']

# Prepare final result
result = {
    'song_title': str(title_to_display) if title_to_display else 'Unknown Title',
    'artist': str(artist_to_display) if artist_to_display else 'Unknown Artist',
    'total_revenue_usd': round(float(top_track['revenue_usd']), 2),
    'total_units_sold': int(top_track['units_sold'])
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': [{'track_count': '19375'}], 'var_functions.query_db:7': [{'sales_count': '58049'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'song_title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'total_revenue_usd': 418.71}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'tracks_count': 19375, 'sales_count': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.execute_python:20': {'status': 'ready', 'tracks_with_keys': 19375}}

exec(code, env_args)
