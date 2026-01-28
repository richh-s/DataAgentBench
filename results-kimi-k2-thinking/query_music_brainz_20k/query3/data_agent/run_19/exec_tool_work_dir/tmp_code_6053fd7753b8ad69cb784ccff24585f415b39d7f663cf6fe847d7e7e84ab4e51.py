code = """import json
import pandas as pd
from collections import defaultdict

# Get the processed data from previous execution
result_data = locals()['var_functions.execute_python:28']

# Load the DataFrames again from storage
tracks_file_path = locals()['var_functions.query_db:14']
sales_file_path = locals()['var_functions.query_db:20']

import os
if isinstance(tracks_file_path, str) and os.path.exists(tracks_file_path):
    with open(tracks_file_path, 'r') as f:
        tracks_data = json.load(f)
    with open(sales_file_path, 'r') as f:
        sales_data = json.load(f)
else:
    tracks_data = tracks_file_path
    sales_data = sales_file_path

# Recreate cleaned DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Use the same cleaning logic as before
def clean_text(text):
    if pd.isna(text) or text is None:
        return ''
    return str(text).lower().strip()

def extract_year(year):
    if pd.isna(year) or year is None:
        return None
    try:
        s = str(year)
        import re
        match = re.search(r'(\d{4})', s)
        if match:
            return int(match.group(1))
        if len(s.strip()) == 2 and s.strip().isdigit():
            y = int(s.strip())
            return 2000 + y if y <= 25 else 1900 + y
        return None
    except:
        return None

tracks_df['title_clean'] = tracks_df['title'].apply(clean_text)
tracks_df['artist_clean'] = tracks_df['artist'].apply(clean_text)
tracks_df['album_clean'] = tracks_df['album'].apply(clean_text)
tracks_df['year_clean'] = tracks_df['year'].apply(extract_year)

# Extract artist from title when missing
mask_no_artist = (tracks_df['artist_clean'] == '') | (tracks_df['artist_clean'] == 'none') | (tracks_df['artist_clean'] == '[unknown]')
def extract_artist_from_title(title):
    if pd.notna(title) and ' - ' in str(title):
        parts = str(title).split(' - ', 1)
        if len(parts) == 2:
            return clean_text(parts[0])
    return ''
tracks_df.loc[mask_no_artist, 'artist_clean'] = tracks_df.loc[mask_no_artist, 'title'].apply(extract_artist_from_title)

# Clean sales
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['units_sold'] = pd.to_numeric(sales_df['units_sold'])

# Create a key for entity resolution - use title, artist, album, and year
# For grouping, we'll use title_clean and artist_clean as primary keys
# Group by these fields to identify unique tracks across different track_ids
track_groups = tracks_df.groupby(['title_clean', 'artist_clean', 'album_clean', 'year_clean'])

# For each group, collect all track_ids and find the best representative
entity_to_tracks = {}
for (title, artist, album, year), group in track_groups:
    track_ids = group['track_id'].tolist()
    # Choose a representative (e.g., the one with most complete info)
    best_idx = group['track_id'].iloc[0]  # Just use first one
    entity_to_tracks[(title, artist, album, year)] = track_ids

# Map each track_id to its entity key
track_to_entity = {}
for entity, track_ids in entity_to_tracks.items():
    for tid in track_ids:
        track_to_entity[tid] = entity

# Calculate total revenue per entity
entity_revenue = defaultdict(float)
if 'entity_key' not in sales_df.columns:
    sales_df['entity_key'] = sales_df['track_id'].map(track_to_entity)

# Remove rows where entity_key is NaN (track_id not found)
valid_sales = sales_df.dropna(subset=['entity_key'])

# Sum revenue by entity
entity_revenue = valid_sales.groupby('entity_key')['revenue_usd'].sum()

# Get top entity
top_entity = entity_revenue.idxmax()
top_revenue = entity_revenue.max()

title, artist, album, year = top_entity

result = {
    'top_track_title': title,
    'top_track_artist': artist,
    'top_track_album': album,
    'top_track_year': year,
    'total_revenue_usd': round(top_revenue, 2),
    'num_track_ids': len(entity_to_tracks[top_entity])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'var_functions.query_db:8': [{'track_count': '19375'}], 'var_functions.query_db:10': [{'title': 'All Is Forgiven', 'album': 'All Is Forgiven', 'artist': 'Siren', 'year': 'None', 'count': '2'}, {'title': 'Asa Di War - Part 1', 'album': 'Asa Di War', 'artist': 'Bhai Ravinder Singh Ji', 'year': '1997', 'count': '2'}, {'title': 'Avenida', 'album': 'Avenida', 'artist': 'Jukkis Uotila', 'year': '1987', 'count': '2'}, {'title': 'Beautiful (instrumental)', 'album': 'Beautiful', 'artist': 'Damian Marley', 'year': '2006', 'count': '2'}, {'title': 'Bende Can', 'album': 'Bende Can', 'artist': 'Yurdal Tokcan', 'year': 'None', 'count': '2'}], 'var_functions.query_db:12': [{'sale_count': '58049'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'tracks_loaded': 19375, 'sales_loaded': 58049, 'sample_tracks': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'title_clean': "daniel balavoine - l'enfant aux yeux d'italie", 'artist_clean': 'daniel balavoine'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'title_clean': '007', 'artist_clean': ''}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'title_clean': 'action painting! - mustard gas', 'artist_clean': 'action painting!'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': 349, 'revenue_usd': 408.0}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': 122, 'revenue_usd': 137.59}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': 373, 'revenue_usd': 371.57}]}}

exec(code, env_args)
