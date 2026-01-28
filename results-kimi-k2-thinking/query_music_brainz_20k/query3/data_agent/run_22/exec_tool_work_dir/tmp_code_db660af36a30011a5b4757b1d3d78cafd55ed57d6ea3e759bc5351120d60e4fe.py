code = """import json
import pandas as pd

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

# Convert data types safely
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'], errors='coerce')
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'], errors='coerce')
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')

# Remove rows with null values in critical columns
tracks_df = tracks_df.dropna(subset=['track_id']).copy()
sales_df = sales_df.dropna(subset=['track_id', 'revenue_usd']).copy()

# Convert to appropriate types
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# Group sales by track_id and sum revenue
track_revenue = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()

# Get the track with highest revenue
top_revenue = track_revenue['revenue_usd'].max()
top_track_ids = track_revenue[track_revenue['revenue_usd'] == top_revenue]['track_id'].tolist()

print('__RESULT__:')
print(json.dumps({
    'top_revenue': float(top_revenue),
    'top_track_ids': top_track_ids,
    'num_top_tracks': len(top_track_ids)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'tracks_count': 19375, 'sales_count': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_sample': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}], 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}]}, 'var_functions.execute_python:8': {'tracks_shape': [19375, 9], 'sales_shape': [58049, 6], 'revenue_stats': {'min': 0.99, 'max': 641.82, 'mean': 284.72739151406574, 'dtype': 'float64'}}}

exec(code, env_args)
