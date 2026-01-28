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

# Find the track with highest revenue
max_revenue_row = sales_df.loc[sales_df['total_revenue'].idxmax()]
max_track_id = max_revenue_row['track_id']
max_revenue = max_revenue_row['total_revenue']

# Get track info
track_info = tracks_df[tracks_df['track_id'] == str(max_track_id)]

print('__RESULT__:')
print(json.dumps({
    'max_track_id': str(max_track_id),
    'total_revenue': float(max_revenue),
    'track_info': track_info[['title', 'artist', 'album', 'year']].fillna('None').to_dict('records')[0] if not track_info.empty else None
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
