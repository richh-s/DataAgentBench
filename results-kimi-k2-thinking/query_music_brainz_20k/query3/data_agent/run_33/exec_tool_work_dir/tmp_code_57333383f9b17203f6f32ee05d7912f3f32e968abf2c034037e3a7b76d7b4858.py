code = """import json
import pandas as pd

# Load the data
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
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])

# Get the track with max revenue
total_revenue_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
max_revenue_track_id = total_revenue_by_track.loc[total_revenue_by_track['revenue_usd'].idxmax(), 'track_id']
max_revenue = total_revenue_by_track.loc[total_revenue_by_track['revenue_usd'].idxmax(), 'revenue_usd']

# Find the track title
max_revenue_track = tracks_df[tracks_df['track_id'] == max_revenue_track_id].iloc[0]
title = max_revenue_track['title']
artist = max_revenue_track['artist']

# Get all sales for this track
track_sales = sales_df[sales_df['track_id'] == max_revenue_track_id]

# Check if there are other tracks with the same title/artist (entity resolution)
potential_duplicates = tracks_df[
    (tracks_df['title'] == title) | 
    (tracks_df['artist'] == artist)
]

# If there are duplicates, sum their revenue as well
if len(potential_duplicates) > 1:
    duplicate_track_ids = potential_duplicates['track_id'].tolist()
    all_revenue = sales_df[sales_df['track_id'].isin(duplicate_track_ids)]['revenue_usd'].sum()
    
    result = {
        'title': str(title),
        'artist': str(artist),
        'primary_track_id': int(max_revenue_track_id),
        'primary_track_revenue': float(max_revenue),
        'found_duplicates': len(potential_duplicates) - 1,
        'total_revenue_with_duplicates': float(all_revenue),
        'duplicate_track_ids': [int(x) for x in duplicate_track_ids if x != max_revenue_track_id],
        'sales_countries': track_sales['country'].nunique(),
        'sales_stores': track_sales['store'].nunique(),
        'total_units_sold': int(track_sales['units_sold'].sum())
    }
else:
    result = {
        'title': str(title),
        'artist': str(artist),
        'track_id': int(max_revenue_track_id),
        'total_revenue': float(max_revenue),
        'found_duplicates': 0,
        'sales_countries': track_sales['country'].nunique(),
        'sales_stores': track_sales['store'].nunique(),
        'total_units_sold': int(track_sales['units_sold'].sum())
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'track_id': 14719, 'revenue_usd': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö'}}

exec(code, env_args)
