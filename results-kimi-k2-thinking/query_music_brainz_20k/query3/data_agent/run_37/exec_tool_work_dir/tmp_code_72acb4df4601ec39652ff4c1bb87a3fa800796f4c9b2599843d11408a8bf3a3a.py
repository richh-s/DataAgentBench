code = """import json
import pandas as pd

# Read tracks data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    tracks_data = json.load(f)

# Read sales data
with open(locals()['var_functions.query_db:6'], 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert total_revenue to float
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)

# Find track with highest revenue
max_revenue = sales_df['total_revenue'].max()
max_track_id = sales_df.loc[sales_df['total_revenue'].idxmax(), 'track_id']

# Get track info
track_info = tracks_df[tracks_df['track_id'] == str(max_track_id)]
track_title = track_info['title'].iloc[0] if not track_info.empty else None
track_artist = track_info['artist'].iloc[0] if not track_info.empty else None

print('__RESULT__:')
print(json.dumps({
    'track_id': str(max_track_id),
    'title': str(track_title) if track_title is not None else 'Unknown',
    'artist': str(track_artist) if track_artist is not None else 'Unknown',
    'total_revenue': float(max_revenue)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'max_track_id': '17096', 'total_revenue': 999.8799999999999, 'track_info': {'title': 'Vinger Alleen (feat. Adriaan Brand) - Die Heuwels Fantasties', 'artist': 'Heuwels Fantasties', 'album': 'None', 'year': "'09"}}}

exec(code, env_args)
