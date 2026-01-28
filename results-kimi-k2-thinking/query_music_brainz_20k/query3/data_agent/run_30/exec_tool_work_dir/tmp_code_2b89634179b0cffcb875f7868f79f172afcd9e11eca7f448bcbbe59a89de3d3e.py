code = """import json
import pandas as pd
import numpy as np

# Load full data
tracks_file = locals()['var_functions.query_db:7']
sales_file = locals()['var_functions.query_db:8']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Convert to DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Ensure proper numeric types
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')
sales_df['units_sold'] = pd.to_numeric(sales_df['units_sold'], errors='coerce')

# Aggregate sales by track_id
sales_agg = sales_df.groupby('track_id').agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum'
}).reset_index()

# Get top 10 tracks by revenue
top_10_tracks = sales_agg.nlargest(10, 'revenue_usd')

# Merge with track info
top_10_with_info = top_10_tracks.merge(tracks_df[['track_id', 'title', 'artist']], on='track_id', how='left')

# Safely convert to JSON-serializable format
result = []
for _, row in top_10_with_info.iterrows():
    result.append({
        'rank': len(result) + 1,
        'track_id': str(row['track_id']),
        'title': str(row['title']) if pd.notna(row['title']) else 'Unknown',
        'artist': str(row['artist']) if pd.notna(row['artist']) else 'Unknown',
        'total_revenue_usd': float(row['revenue_usd']),
        'total_units_sold': float(row['units_sold'])
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:3': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'tracks_shape': [19375, 9], 'sales_shape': [58049, 6], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.execute_python:18': {'top_track_title': '', 'top_track_artist': '', 'total_revenue_usd': 6862.5599999999995, 'total_units_sold': 4408889047653400.0, 'track_ids': ['2', '30', '182', '228', '462']}, 'var_functions.execute_python:20': {'top_revenue_track_id': '14378', 'top_revenue_title': 'Van Halen - Eagles Fly', 'top_revenue_artist': 'None', 'top_revenue_original': 634.55, 'relevant_tracks': [{'track_id': '2', 'title': '007', 'artist': '[unknown]', 'revenue_usd': nan}, {'track_id': '30', 'title': '011- ', 'artist': '   ', 'revenue_usd': 283.95}, {'track_id': '182', 'title': '011- ', 'artist': 'None', 'revenue_usd': nan}, {'track_id': '228', 'title': '031-', 'artist': 'None', 'revenue_usd': 39.13}, {'track_id': '462', 'title': '013--', 'artist': '  ', 'revenue_usd': 225.19}]}, 'var_functions.query_db:22': [{'track_id': '14719', 'total_revenue': '2522.82', 'total_units': '2109.0'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996', 'total_units': '2216.0'}, {'track_id': '1344', 'total_revenue': '2500.72', 'total_units': '2186.0'}, {'track_id': '6725', 'total_revenue': '2489.81', 'total_units': '2050.0'}, {'track_id': '10377', 'total_revenue': '2466.71', 'total_units': '2263.0'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004', 'total_units': '2063.0'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003', 'total_units': '2182.0'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003', 'total_units': '2086.0'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003', 'total_units': '2136.0'}, {'track_id': '964', 'total_revenue': '2425.61', 'total_units': '2194.0'}, {'track_id': '12984', 'total_revenue': '2401.71', 'total_units': '2018.0'}, {'track_id': '6208', 'total_revenue': '2385.0299999999997', 'total_units': '2035.0'}, {'track_id': '666', 'total_revenue': '2382.74', 'total_units': '2077.0'}, {'track_id': '12620', 'total_revenue': '2377.59', 'total_units': '2119.0'}, {'track_id': '19232', 'total_revenue': '2368.7499999999995', 'total_units': '2059.0'}, {'track_id': '17757', 'total_revenue': '2365.59', 'total_units': '2144.0'}, {'track_id': '3462', 'total_revenue': '2359.23', 'total_units': '2104.0'}, {'track_id': '9639', 'total_revenue': '2351.68', 'total_units': '1919.0'}, {'track_id': '18760', 'total_revenue': '2349.33', 'total_units': '1939.0'}, {'track_id': '2516', 'total_revenue': '2346.18', 'total_units': '1899.0'}], 'var_functions.query_db:24': [{'track_id': '1344', 'source_id': '5', 'source_track_id': '11415767', 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011', 'length': '187000', 'language': 'English'}, {'track_id': '5124', 'source_id': '4', 'source_track_id': '26725-A060', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None', 'length': '2m 45sec', 'language': 'Eng.'}, {'track_id': '14719', 'source_id': '5', 'source_track_id': '11323763', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009', 'length': '223000', 'language': 'German'}]}

exec(code, env_args)
