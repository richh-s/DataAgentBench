code = """import json
import pandas as pd
from collections import defaultdict

# Load full data
sales_key = 'var_functions.query_db:0'
tracks_key = 'var_functions.query_db:2'

with open(locals()[sales_key], 'r') as f:
    sales_data = json.load(f)

with open(locals()[tracks_key], 'r') as f:
    tracks_data = json.load(f)

# Convert to DataFrames for easier manipulation
sales_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

# Clean up data types
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['track_id'] = sales_df['track_id'].astype(int)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

print('__RESULT__:')
print(json.dumps({
    'sales_shape': sales_df.shape,
    'tracks_shape': tracks_df.shape,
    'sales_columns': list(sales_df.columns),
    'tracks_columns': list(tracks_df.columns),
    'first_tracks': tracks_df.head(10).to_dict('records'),
    'sample_sales': sales_df.head(10).to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'sales_count': 58049, 'tracks_count': 19375, 'first_few_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'first_few_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}]}}

exec(code, env_args)
