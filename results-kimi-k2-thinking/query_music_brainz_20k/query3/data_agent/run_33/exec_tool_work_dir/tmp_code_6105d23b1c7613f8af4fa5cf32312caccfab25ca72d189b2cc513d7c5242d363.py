code = """import json
import pandas as pd

# Load tracks data from JSON file
tracks_path = var_functions.query_db:0
with open(tracks_path) as f:
    tracks_data = json.load(f)

# Load sales data from JSON file  
sales_path = var_functions.query_db:5
with open(sales_path) as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert data types
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'])
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])

# Calculate total revenue per track_id
track_revenue = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
top_revenue_track = track_revenue.loc[track_revenue['revenue_usd'].idxmax()]

# Get the highest earning track details
top_track_id = top_revenue_track['track_id']
max_revenue = top_revenue_track['revenue_usd']

top_track = tracks_df[tracks_df['track_id'] == top_track_id].iloc[0]

result = {
    'tracks_loaded': len(tracks_data),
    'sales_loaded': len(sales_data),
    'top_track_id': int(top_track_id),
    'max_revenue': float(max_revenue),
    'top_track_title': top_track.get('title', 'Unknown'),
    'top_track_artist': top_track.get('artist', 'Unknown'),
    'total_tracks_with_sales': len(track_revenue)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
