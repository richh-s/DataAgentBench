code = """import json
import pandas as pd

# Load full data
sales_key = 'var_functions.query_db:0'
tracks_key = 'var_functions.query_db:2'

with open(locals()[sales_key], 'r') as f:
    sales_data = json.load(f)

with open(locals()[tracks_key], 'r') as f:
    tracks_data = json.load(f)

# Convert to DataFrames
sales_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

# Clean data types
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['track_id'] = sales_df['track_id'].astype(int)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Aggregate revenue by track_id
revenue_by_track = sales_df.groupby('track_id')['revenue_usd'].sum().sort_values(ascending=False)

# Get top 20 tracks by revenue
top_20_revenue = revenue_by_track.head(20)

# Get track details for top revenue tracks
top_tracks = tracks_df[tracks_df['track_id'].isin(top_20_revenue.index)]

result = {
    'top_20_revenue': top_20_revenue.to_dict(),
    'top_tracks': top_tracks[['track_id', 'title', 'artist', 'album']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'sales_count': 58049, 'tracks_count': 19375, 'first_few_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'first_few_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}]}, 'var_functions.execute_python:8': {'sales_shape': [58049, 6], 'tracks_shape': [19375, 9], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'first_tracks': [{'track_id': 1, 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': 2, 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': 3, 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': 4, 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': 5, 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': 6, 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': 7, 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': 8, 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': 9, 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': 10, 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'sample_sales': [{'sale_id': '1', 'track_id': 1, 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': 408.0}, {'sale_id': '2', 'track_id': 1, 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': 137.59}, {'sale_id': '3', 'track_id': 1, 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': 371.57}, {'sale_id': '4', 'track_id': 1, 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': 269.49}, {'sale_id': '5', 'track_id': 2, 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': 184.74}, {'sale_id': '6', 'track_id': 2, 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': 270.79}, {'sale_id': '7', 'track_id': 2, 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': 186.98}, {'sale_id': '8', 'track_id': 2, 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': 217.41}, {'sale_id': '9', 'track_id': 2, 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': 399.35}, {'sale_id': '10', 'track_id': 3, 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': 418.71}]}}

exec(code, env_args)
