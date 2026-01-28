code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load the data
tracks_file = locals()['var_functions.query_db:0']
sales_file = locals()['var_functions.query_db:2']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert track_id to int for proper joining
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# Normalize functions
def normalize_string(s):
    if pd.isna(s) or s is None or s == 'None' or s == '[unknown]':
        return ''
    s = str(s).lower().strip()
    # Remove common prefixes/suffixes that don't affect matching
    s = re.sub(r'^[^\w]*', '', s)  # Remove leading non-word chars
    s = re.sub(r'[^\w]*$', '', s)  # Remove trailing non-word chars
    # Remove extra whitespace and special chars
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def normalize_year(y):
    if pd.isna(y) or y is None or y == 'None':
        return None
    y = str(y).strip()
    # Extract 4-digit year
    match = re.search(r'(\d{4})', y)
    if match:
        year = int(match.group(1))
        # Handle 2-digit years like '75' -> 1975, '05' -> 2005
        return year
    # Handle 2-digit years
    match = re.search(r'(\d{2})', y)
    if match:
        year = int(match.group(1))
        if year < 20:
            return 2000 + year
        elif year < 100:
            return 1900 + year
    return None

# Apply normalization
tracks_df['title_norm'] = tracks_df['title'].apply(normalize_string)
tracks_df['artist_norm'] = tracks_df['artist'].apply(normalize_string)
tracks_df['album_norm'] = tracks_df['album'].apply(normalize_string)
tracks_df['year_norm'] = tracks_df['year'].apply(normalize_year)

# Remove rows where title is empty or None after normalization
tracks_df = tracks_df[tracks_df['title_norm'] != ''].copy()

# Create a key for grouping similar tracks
# Using title + artist as primary key, with some flexibility
tracks_df['match_key'] = tracks_df['title_norm'] + '|' + tracks_df['artist_norm']

# Aggregate sales by track_id first to get total revenue per track_id
sales_agg = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
sales_agg.columns = ['track_id', 'total_revenue']

# Join with tracks
tracks_with_revenue = tracks_df.merge(sales_agg, on='track_id', how='inner')

# Group by match_key to aggregate duplicates
grouped = tracks_with_revenue.groupby('match_key').agg({
    'track_id': list,
    'total_revenue': 'sum',
    'title': lambda x: x.iloc[0],  # Take first title
    'artist': lambda x: x.iloc[0],  # Take first artist
    'title_norm': 'first',
    'artist_norm': 'first'
}).reset_index()

# Find the track with highest revenue
top_track = grouped.loc[grouped['total_revenue'].idxmax()]

print('__RESULT__:')
print(json.dumps({
    'top_track_title': top_track['title'],
    'top_track_artist': top_track['artist'],
    'total_revenue': float(top_track['total_revenue']),
    'matching_track_ids': top_track['track_id'],
    'total_matching_tracks': len(top_track['track_id'])
}, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'tracks_count': 19375, 'sales_count': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_sample': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}], 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}]}}

exec(code, env_args)
