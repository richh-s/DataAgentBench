code = """import json

# Load tracks data from file
tracks_result = var_functions.query_db:0
if isinstance(tracks_result, str) and '.json' in tracks_result:
    with open(tracks_result, 'r') as f:
        tracks_data = json.load(f)
else:
    tracks_data = tracks_result

# Load sales data from file
sales_result = var_functions.query_db:6
if isinstance(sales_result, str) and '.json' in sales_result:
    with open(sales_result, 'r') as f:
        sales_data = json.load(f)
else:
    sales_data = sales_result

# Calculate total revenue per track
track_revenue = {}
for sale in sales_data:
    track_id = sale['track_id']
    revenue = float(sale['revenue_usd'])
    if track_id in track_revenue:
        track_revenue[track_id] += revenue
    else:
        track_revenue[track_id] = revenue

# Sort by revenue to find top tracks
sorted_tracks = sorted(track_revenue.items(), key=lambda x: x[1], reverse=True)

# Get top 10 tracks with highest revenue
top_tracks = []
for track_id, revenue in sorted_tracks[:10]:
    # Find track details
    track_details = None
    for track in tracks_data:
        if track['track_id'] == track_id:
            track_details = track
            break
    
    if track_details:
        top_tracks.append({
            'track_id': track_id,
            'title': track_details['title'],
            'artist': track_details['artist'],
            'album': track_details['album'],
            'revenue': round(revenue, 2)
        })
    else:
        top_tracks.append({
            'track_id': track_id,
            'title': 'Not found',
            'artist': 'Not found',
            'album': 'Not found',
            'revenue': round(revenue, 2)
        })

print('__RESULT__:')
print(json.dumps(top_tracks[0], ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:4': [{'total_revenue': '2522.82', 'track_id': '14719'}, {'total_revenue': '2503.1899999999996', 'track_id': '5124'}, {'total_revenue': '2500.72', 'track_id': '1344'}, {'total_revenue': '2489.81', 'track_id': '6725'}, {'total_revenue': '2466.71', 'track_id': '10377'}, {'total_revenue': '2466.3100000000004', 'track_id': '5050'}, {'total_revenue': '2452.7000000000003', 'track_id': '6667'}, {'total_revenue': '2436.9700000000003', 'track_id': '7245'}, {'total_revenue': '2428.2200000000003', 'track_id': '11641'}, {'total_revenue': '2425.61', 'track_id': '964'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'track_id': '14719', 'source_id': '5', 'source_track_id': '11323763', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009', 'length': '223000', 'language': 'German'}]}

exec(code, env_args)
