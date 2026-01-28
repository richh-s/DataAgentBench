code = """import json
import pandas as pd

# Load tracks data from JSON file
tracks_file_path = locals()['var_functions.query_db:0']
with open(tracks_file_path, 'r') as file:
    tracks_data = json.load(file)

# Load sales data from JSON file
sales_file_path = locals()['var_functions.query_db:5']
with open(sales_file_path, 'r') as file:
    sales_data = json.load(file)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert numeric fields
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'])
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])

# Calculate total revenue by track_id
track_revenue = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
track_revenue = track_revenue.sort_values('revenue_usd', ascending=False)

# Get the track with maximum revenue
max_revenue_row = track_revenue.iloc[0]
max_track_id = int(max_revenue_row['track_id'])
max_revenue = float(max_revenue_row['revenue_usd'])

# Get track details
track_info = tracks_df[tracks_df['track_id'] == max_track_id].iloc[0]
track_title = str(track_info.get('title', 'Unknown'))
track_artist = str(track_info.get('artist', 'Unknown'))

result = {
    'track_id': max_track_id,
    'revenue_usd': max_revenue,
    'title': track_title,
    'artist': track_artist
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
