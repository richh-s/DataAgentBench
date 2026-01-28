code = """import json

# Load tracks data from file
tracks_file = var_functions.query_db:0
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

# Find track 14719
track_14719 = None
for track in tracks_data:
    if track['track_id'] == '14719':
        track_14719 = track
        break

# Load sales data from file
sales_file = var_functions.query_db:6
with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Calculate total revenue per track
track_revenue = {}
for sale in sales_data:
    track_id = sale['track_id']
    revenue = float(sale['revenue_usd'])
    if track_id in track_revenue:
        track_revenue[track_id] += revenue
    else:
        track_revenue[track_id] = revenue

# Find track with max revenue
max_revenue = 0
max_track_id = None
for track_id, revenue in track_revenue.items():
    if revenue > max_revenue:
        max_revenue = revenue
        max_track_id = track_id

# Find the track details
max_track = None
for track in tracks_data:
    if track['track_id'] == max_track_id:
        max_track = track
        break

result = {
    'track_id': max_track_id,
    'title': max_track['title'] if max_track else 'Not found',
    'artist': max_track['artist'] if max_track else 'Not found',
    'album': max_track['album'] if max_track else 'Not found',
    'total_revenue': round(max_revenue, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:4': [{'total_revenue': '2522.82', 'track_id': '14719'}, {'total_revenue': '2503.1899999999996', 'track_id': '5124'}, {'total_revenue': '2500.72', 'track_id': '1344'}, {'total_revenue': '2489.81', 'track_id': '6725'}, {'total_revenue': '2466.71', 'track_id': '10377'}, {'total_revenue': '2466.3100000000004', 'track_id': '5050'}, {'total_revenue': '2452.7000000000003', 'track_id': '6667'}, {'total_revenue': '2436.9700000000003', 'track_id': '7245'}, {'total_revenue': '2428.2200000000003', 'track_id': '11641'}, {'total_revenue': '2425.61', 'track_id': '964'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'track_id': '14719', 'source_id': '5', 'source_track_id': '11323763', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009', 'length': '223000', 'language': 'German'}]}

exec(code, env_args)
