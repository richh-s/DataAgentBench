code = """import json
import re
from collections import defaultdict, Counter

# Get the data from storage - they should be in JSON format already
tracks_key = 'var_functions.query_db:8'
sales_key = 'var_functions.query_db:12'

# Try to get the values directly
tracks_data = locals().get(tracks_key)
sales_data = locals().get(sales_key)

# If not in locals, they might be in a special storage variable
if tracks_data is None:
    try:
        import storage
        tracks_data = storage.get(tracks_key)
        sales_data = storage.get(sales_key)
    except:
        tracks_data = None
        sales_data = None

# If they're file paths, read them
if isinstance(tracks_data, str) and 'query_db' in tracks_data:
    with open(tracks_data, 'r') as f:
        tracks_data = json.load(f)
if isinstance(sales_data, str) and 'query_db' in sales_data:
    with open(sales_data, 'r') as f:
        sales_data = json.load(f)

# First pass: aggregate revenue by track_id
revenue_by_track = defaultdict(float)
for sale in sales_data:
    revenue_by_track[str(sale['track_id'])] += float(sale['revenue_usd'])

# Sort tracks by revenue
tracks_by_revenue = sorted(revenue_by_track.items(), key=lambda x: x[1], reverse=True)

top_10_revenue = tracks_by_revenue[:10]

# Now let's look at track details for these top tracks
top_10_details = []
for track_id, revenue in top_10_revenue:
    track_info = next((t for t in tracks_data if str(t['track_id']) == str(track_id)), None)
    if track_info:
        top_10_details.append({
            'track_id': track_id,
            'revenue': revenue,
            'title': track_info['title'],
            'artist': track_info['artist'],
            'album': track_info['album'],
            'year': track_info['year']
        })
    else:
        top_10_details.append({
            'track_id': track_id,
            'revenue': revenue,
            'title': 'Unknown',
            'artist': 'Unknown',
            'album': 'Unknown',
            'year': 'Unknown'
        })

result = {
    'top_revenue_tracks': top_10_details,
    'total_tracks_analyzed': len(tracks_data),
    'total_sales_analyzed': len(sales_data),
    'track_with_highest_revenue_id': top_10_details[0]['track_id'],
    'highest_revenue_amount': top_10_details[0]['revenue']
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
