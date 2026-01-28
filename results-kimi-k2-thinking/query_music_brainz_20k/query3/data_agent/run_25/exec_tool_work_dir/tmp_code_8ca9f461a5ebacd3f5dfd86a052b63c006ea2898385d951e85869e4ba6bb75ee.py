code = """import json
import pandas as pd

# Load data
tracks_file = locals()['var_functions.query_db:2']
sales_file = locals()['var_functions.query_db:6']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Clean text function
import re

def clean_text(text):
    if not text or text == 'None' or text == '':
        return ''
    return str(text).strip().lower()

# Clean tracks data
tracks_df['clean_title'] = tracks_df['title'].apply(clean_text)
tracks_df['clean_artist'] = tracks_df['artist'].apply(clean_text)
tracks_df['clean_album'] = tracks_df['album'].apply(clean_text)

# Simple title normalization: remove common suffixes
remove_patterns = [r'\(live\)', r'\(acoustic\)', r'\(remix\)', r'- live', r'- acoustic', r'- remix']
tracks_df['simple_title'] = tracks_df['clean_title']
for pattern in remove_patterns:
    tracks_df['simple_title'] = tracks_df['simple_title'].str.replace(pattern, '', regex=True)
tracks_df['simple_title'] = tracks_df['simple_title'].str.strip()

# Calculate total revenue per track_id
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
track_revenue = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
track_revenue['track_id'] = track_revenue['track_id'].astype(str)

# Join with tracks
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
tracks_with_revenue = tracks_df.merge(track_revenue, on='track_id', how='inner')

# Create match key: simple title + artist (if available)
def create_match_key(row):
    title = row['simple_title']
    artist = row['clean_artist']
    if title and artist and artist not in ['', '[unknown]', 'none']:
        return title + '|' + artist
    return title

tracks_with_revenue['match_key'] = tracks_with_revenue.apply(create_match_key, axis=1)

# Aggregate revenue by match key
grouped_revenue = tracks_with_revenue.groupby('match_key').agg({
    'revenue_usd': 'sum',
    'title': 'first',
    'artist': 'first'
}).reset_index()

# Find highest revenue track
top_track = grouped_revenue.loc[grouped_revenue['revenue_usd'].idxmax()]

result = {
    'top_track_title': top_track['title'],
    'top_track_artist': top_track['artist'],
    'total_revenue': round(top_track['revenue_usd'], 2),
    'match_key': top_track['match_key']
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'tracks_rows': 19375, 'sales_rows': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_sample': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}], 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}]}}

exec(code, env_args)
