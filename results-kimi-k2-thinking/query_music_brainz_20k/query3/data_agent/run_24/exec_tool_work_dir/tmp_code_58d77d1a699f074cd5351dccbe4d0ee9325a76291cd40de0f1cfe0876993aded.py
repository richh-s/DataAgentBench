code = """import json

# Read the data from files
with open('file_storage/functions.query_db:16.json', 'r') as f:
    sales_data = json.load(f)

with open('file_storage/functions.query_db:18.json', 'r') as f:
    tracks_data = json.load(f)

# Create a mapping from track_id to track attributes
track_attributes = {}
for track in tracks_data:
    track_id = int(track['track_id'])
    # Clean up the attributes for comparison
    title = track['title'].strip() if track['title'] and track['title'] != 'None' else ''
    artist = track['artist'].strip() if track['artist'] and track['artist'] != 'None' else ''
    album = track['album'].strip() if track['album'] and track['album'] != 'None' else ''
    year = track['year'].strip() if track['year'] and track['year'] != 'None' else ''
    
    track_attributes[track_id] = {
        'title': title,
        'artist': artist,
        'album': album,
        'year': year,
        'original_track': track
    }

# Group tracks by title, artist, and album to find duplicates
from collections import defaultdict

track_groups = defaultdict(list)
for track_id, attrs in track_attributes.items():
    # Use title, artist, album as the grouping key
    # Normalize to lowercase for better matching
    key = (attrs['title'].lower(), attrs['artist'].lower(), attrs['album'].lower())
    track_groups[key].append(track_id)

# Aggregate revenue for each track group
group_revenue = defaultdict(float)
group_sales_count = defaultdict(int)
group_countries = defaultdict(set)
group_stores = defaultdict(set)
group_track_ids = defaultdict(list)

for sale in sales_data:
    track_id = int(sale['track_id'])
    revenue = float(sale['revenue_usd'])
    country = sale['country']
    store = sale['store']
    
    if track_id in track_attributes:
        attrs = track_attributes[track_id]
        key = (attrs['title'].lower(), attrs['artist'].lower(), attrs['album'].lower())
        
        group_revenue[key] += revenue
        group_sales_count[key] += 1
        group_countries[key].add(country)
        group_stores[key].add(store)
        group_track_ids[key].append(track_id)

# Find the group with highest revenue
top_group = sorted(group_revenue.items(), key=lambda x: x[1], reverse=True)[0]
top_key = top_group[0]
top_revenue = top_group[1]

# Get the representative track for this group (first one)
representative_track_id = group_track_ids[top_key][0]
representative_track = track_attributes[representative_track_id]['original_track']

result = {
    'song_title': representative_track['title'],
    'artist': representative_track['artist'],
    'album': representative_track['album'],
    'total_revenue_usd': round(top_revenue, 2),
    'duplicate_count': len(group_track_ids[top_key]),
    'total_sales_transactions': group_sales_count[top_key],
    'countries': list(group_countries[top_key]),
    'stores': list(group_stores[top_key]),
    'track_ids': group_track_ids[top_key]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.list_db:4': ['sales'], 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'tracks_count': 38, 'sales_count': 10, 'tracks_sample': 'fi', 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:24': {'sales_type': "<class 'str'>", 'sales_preview': 'file_storage/functions.query_db:16.json', 'tracks_type': "<class 'str'>", 'tracks_preview': 'file_storage/functions.query_db:18.json'}, 'var_functions.execute_python:26': {'top_track_id': 14719, 'top_revenue': 2522.82, 'track_details': {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, 'sales_for_track': 5, 'top_10_tracks': [[14719, 2522.82], [5124, 2503.1899999999996], [1344, 2500.72], [6725, 2489.81], [10377, 2466.71], [5050, 2466.3100000000004], [6667, 2452.7000000000003], [7245, 2436.9700000000003], [11641, 2428.2200000000003], [964, 2425.61]], 'total_tracks': 19375, 'total_sales_records': 58049}, 'var_functions.execute_python:28': {'original_track_id': 14719, 'track_title': 'Systemisch bled', 'track_artist': 'Stüngö', 'track_album': "Um wos gehts'n?", 'duplicate_count': 1, 'total_revenue_all_duplicates': 2522.82, 'revenue_by_country': {'Germany': 1024.31, 'UK': 538.92, 'Canada': 959.59}, 'revenue_by_store': {'Spotify': 977.91, 'Apple Music': 1030.47, 'iTunes': 514.44}}}

exec(code, env_args)
