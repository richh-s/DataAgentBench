code = """import json
import pandas as pd

# Reload data
tracks_file = locals()['var_functions.query_db:8']
sales_file = locals()['var_functions.query_db:16']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)
with open(sales_file, 'r') as f:
    sales_data = json.load(f)

df_tracks = pd.DataFrame(tracks_data)
df_sales = pd.DataFrame(sales_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(int)

# Get the top group key from previous analysis
top_group_key = 'песняры|издалекихизкраев|альбомсолнца|2003'

# Find all track_ids that belong to this group
tracks_in_group = df_tracks[df_tracks['group_key'] == top_group_key]

# Get sales for these tracks
track_ids_in_group = tracks_in_group['track_id'].tolist()
group_sales = df_sales[df_sales['track_id'].isin(track_ids_in_group)]

# Calculate revenue breakdown
total_revenue = group_sales['revenue_usd'].sum()
revenue_by_track = group_sales.groupby('track_id')['revenue_usd'].sum().sort_values(ascending=False)

# Get track details
result = {
    'group_key': top_group_key,
    'tracks_in_group': len(tracks_in_group),
    'total_revenue': float(total_revenue),
    'sales_records': len(group_sales),
    'top_tracks_in_group': []
}

for track_id, revenue in revenue_by_track.head().items():
    track_info = df_tracks[df_tracks['track_id'] == track_id].iloc[0]
    result['top_tracks_in_group'].append({
        'track_id': int(track_id),
        'revenue': float(revenue),
        'title': str(track_info.get('title', 'Unknown')),
        'artist': str(track_info.get('artist', 'Unknown')),
        'album': str(track_info.get('album', 'Unknown')),
        'year': str(track_info.get('year', 'Unknown'))
    })

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': [{'track_count': '19375'}], 'var_functions.query_db:7': [{'sales_count': '58049'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'song_title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'total_revenue_usd': 418.71}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'tracks_count': 19375, 'sales_count': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.execute_python:20': {'status': 'ready', 'tracks_with_keys': 19375}, 'var_functions.execute_python:22': {'song_title': 'Из далеких из краев', 'artist': 'Песняры', 'total_revenue_usd': 11630.39, 'total_units_sold': 10210}, 'var_functions.execute_python:24': {'top_tracks_by_id': [{'track_id': 14719, 'revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö'}, {'track_id': 5124, 'revenue': 2503.19, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels'}, {'track_id': 1344, 'revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen'}, {'track_id': 6725, 'revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers'}, {'track_id': 10377, 'revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas'}], 'total_top_revenue': 2522.82}}

exec(code, env_args)
