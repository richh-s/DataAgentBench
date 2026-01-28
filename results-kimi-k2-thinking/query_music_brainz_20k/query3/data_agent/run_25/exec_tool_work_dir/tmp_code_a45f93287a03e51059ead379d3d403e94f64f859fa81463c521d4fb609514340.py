code = """import json
import pandas as pd
import numpy as np
from collections import defaultdict
import re

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

# Data cleaning function for entity resolution
def clean_text(text):
    if pd.isna(text) or text is None or text == 'None' or text == '':
        return ''
    return str(text).strip().lower()

# Clean track data for entity matching
tracks_df['clean_title'] = tracks_df['title'].apply(clean_text)
tracks_df['clean_artist'] = tracks_df['artist'].apply(clean_text)
tracks_df['clean_album'] = tracks_df['album'].apply(clean_text)
tracks_df['clean_year'] = tracks_df['year'].apply(clean_text)

# Remove common prefixes/suffixes and normalize
def normalize_title(title):
    # Remove patterns like "- live", "(live)", "- acoustic", etc.
    title = re.sub(r'\s*[-:,]\s*(live|acoustic|remix|version).*', '', title)
    title = re.sub(r'\s*\(.*?(live|acoustic|remix|version).*?\).*', '', title)
    # Remove extra whitespace
    title = re.sub(r'\s+', ' ', title).strip()
    return title

tracks_df['normalized_title'] = tracks_df['clean_title'].apply(normalize_title)

# Group by normalized attributes to find potential duplicates
def get_match_key(row):
    # Use title + artist as primary key, with some flexibility
    title = row['normalized_title']
    artist = row['clean_artist']
    album = row['clean_album']
    year = row['clean_year']
    
    # If we have a good title and artist, use that
    if title and artist and title != '' and artist != '' and artist != '[unknown]' and artist != 'none':
        return f"{title}|{artist}"
    # Otherwise use title + album
    elif title and album and title != '' and album != '' and album != 'none':
        return f"{title}|{album}"
    # Otherwise just use the original title if it's specific enough
    elif title and len(title) > 10:
        return f"{title}|{year or 'unknown'}"
    else:
        return None

tracks_df['match_key'] = tracks_df.apply(get_match_key, axis=1)

# Find tracks with sales
sales_track_ids = set(sales_df['track_id'].astype(str))
tracks_with_sales = tracks_df[tracks_df['track_id'].astype(str).isin(sales_track_ids)]

print(f"Total tracks: {len(tracks_df)}")
print(f"Tracks with sales: {len(tracks_with_sales)}")
print(f"Unique match keys: {tracks_with_sales['match_key'].nunique()}")

# Show some examples of potential duplicates
sample_matches = tracks_with_sales.groupby('match_key').size().reset_index(name='count')
sample_matches = sample_matches[sample_matches['count'] > 1].head(10)

print('\nSample duplicate groups:')
for _, row in sample_matches.iterrows():
    match_key = row['match_key']
    count = row['count']
    if match_key:
        print(f"Key: {match_key[:50]}... - Count: {count}")

result = {
    'total_tracks': len(tracks_df),
    'tracks_with_sales': len(tracks_with_sales),
    'unique_match_keys': tracks_with_sales['match_key'].nunique(),
    'potential_duplicates': len(sample_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'tracks_rows': 19375, 'sales_rows': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_sample': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}], 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}]}}

exec(code, env_args)
