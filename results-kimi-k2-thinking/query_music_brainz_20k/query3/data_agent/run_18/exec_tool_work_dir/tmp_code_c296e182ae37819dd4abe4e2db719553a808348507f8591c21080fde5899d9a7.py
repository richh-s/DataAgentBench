code = """import json
import pandas as pd
import re
from datetime import datetime

# Load tracks data from file
tracks_file = var_functions.query_db:8
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

# Load sales data
sales_data = var_functions.query_db:2

# Convert to DataFrames
df_tracks = pd.DataFrame(tracks_data)
df_sales = pd.DataFrame(sales_data)

# Clean and normalize track data
def clean_text(text):
    """Clean and normalize text fields"""
    if text is None or pd.isna(text) or text == 'None' or text == '[unknown]':
        return None
    return str(text).strip().lower()

def extract_artist_from_title(title):
    """Extract artist from title if it's in 'Artist - Title' format"""
    if title and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            return clean_text(parts[0])
    return None

def normalize_year(year):
    """Normalize year to 4-digit format"""
    if year is None or pd.isna(year) or year == 'None':
        return None
    
    year_str = str(year).strip()
    
    # Handle various formats
    if year_str.startswith("'"):  # '11, '89
        year_str = year_str[1:]
    
    try:
        year_int = int(year_str)
        if year_int < 100:
            # Convert 2-digit year to 4-digit (assuming 1900s for >= 50, 2000s for < 50)
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

# Extract artist from title if artist is missing
mask_missing_artist = df_tracks['artist_clean'].isna() | (df_tracks['artist_clean'] == 'none') | (df_tracks['artist_clean'] == '[unknown]')
df_tracks.loc[mask_missing_artist, 'artist_from_title'] = df_tracks.loc[mask_missing_artist, 'title'].apply(extract_artist_from_title)

# Use extracted artist if available
df_tracks['final_artist'] = df_tracks['artist_clean']
mask_extracted = df_tracks['artist_from_title'].notna()
df_tracks.loc[mask_extracted, 'final_artist'] = df_tracks.loc[mask_extracted, 'artist_from_title']

# Clean title (remove artist prefix if it exists)
def clean_title(title, artist):
    """Remove artist prefix from title if present"""
    if title is None or pd.isna(title) or title == 'None':
        return None
    title_clean = str(title).strip().lower()
    if artist and ' - ' in str(title):
        parts = str(title).split(' - ', 1)
        if len(parts) == 2:
            return clean_text(parts[1])
    return clean_text(title)

df_tracks['final_title'] = df_tracks.apply(lambda row: clean_title(row['title'], row['final_artist']), axis=1)

# Create a grouping key for entity resolution
def create_group_key(row):
    """Create a key for grouping similar tracks"""
    artist = row['final_artist'] if row['final_artist'] else 'unknown'
    title = row['final_title'] if row['final_title'] else 'unknown'
    album = row['album_clean'] if row['album_clean'] else 'unknown'
    year = row['year_clean'] if row['year_clean'] else 0
    
    # Use first 20 chars of each field to allow for minor variations
    key = f"{artist[:30]}|{title[:40]}|{album[:30]}|{year}"
    return key

df_tracks['group_key'] = df_tracks.apply(create_group_key, axis=1)

# Merge with sales data
df_merged = df_sales.merge(df_tracks[['track_id', 'group_key', 'title', 'artist']], on='track_id', how='left')

# Calculate total revenue per track group
group_revenue = df_merged.groupby('group_key').agg({
    'revenue_usd': 'sum',
    'title': lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0],  # Most common title
    'artist': lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0]   # Most common artist
}).reset_index()

# Sort by revenue descending
group_revenue = group_revenue.sort_values('revenue_usd', ascending=False)

# Get the top track
top_track = group_revenue.iloc[0]

# Print the result in the required format
result = {
    'song_title': str(top_track['title']),
    'artist': str(top_track['artist']),
    'total_revenue_usd': float(top_track['revenue_usd'])
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': [{'track_count': '19375'}], 'var_functions.query_db:7': [{'sales_count': '58049'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
