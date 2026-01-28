code = """import json
import pandas as pd
import re

# Load data
tracks_file_path = locals()['var_functions.query_db:0']
sales_file_path = locals()['var_functions.query_db:5']

with open(tracks_file_path, 'r') as file:
    tracks_data = json.load(file)
    
with open(sales_file_path, 'r') as file:
    sales_data = json.load(file)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert data types
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'])
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['units_sold'] = pd.to_numeric(sales_df['units_sold'])
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])

# Clean/normalize title and artist for entity resolution
def normalize_text(text):
    if pd.isna(text) or text is None or text == 'None':
        return ''
    return str(text).lower().strip()

tracks_df['norm_title'] = tracks_df['title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)

# Remove empty values and standardize
tracks_df['norm_title'] = tracks_df['norm_title'].replace('', 'unknown')
tracks_df['norm_artist'] = tracks_df['norm_artist'].replace('', 'unknown')

# Merge tracks and sales
tracks_with_sales = tracks_df.merge(sales_df, on='track_id', how='inner')

# Group by normalized title and artist (entity resolution)
entity_revenue = tracks_with_sales.groupby(['norm_title', 'norm_artist']).agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum',
    'track_id': 'nunique',
    'country': 'nunique',
    'store': 'nunique'
}).reset_index()

entity_revenue = entity_revenue.sort_values('revenue_usd', ascending=False)

# Get top entity
top_entity = entity_revenue.iloc[0]

# Get original title and artist (first occurrence)
original_tracks = tracks_df[
    (tracks_df['norm_title'] == top_entity['norm_title']) & 
    (tracks_df['norm_artist'] == top_entity['norm_artist'])
]

original_title = original_tracks.iloc[0]['title']
original_artist = original_tracks.iloc[0]['artist']

# Get all track_ids for this entity
track_ids = original_tracks['track_id'].tolist()

# Verify no entity resolution issues with top track
# Check if there are multiple track_ids for the same song
is_duplicated_entity = top_entity['track_id'] > 1

result = {
    'title': str(original_title),
    'artist': str(original_artist),
    'total_revenue_usd': float(top_entity['revenue_usd']),
    'track_ids': [int(x) for x in track_ids],
    'is_entity_with_duplicates': bool(is_duplicated_entity),
    'num_duplicates': int(top_entity['track_id'] - 1) if is_duplicated_entity else 0,
    'total_units_sold': int(top_entity['units_sold']),
    'countries': int(top_entity['country']),
    'stores': int(top_entity['store'])
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'track_id': 14719, 'revenue_usd': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö'}, 'var_functions.execute_python:12': {'title': 'Systemisch bled', 'artist': 'Stüngö', 'track_id': 14719, 'total_revenue': 2522.82, 'found_duplicates': 0, 'sales_countries': 3, 'sales_stores': 3, 'total_units_sold': 361428441458421}}

exec(code, env_args)
