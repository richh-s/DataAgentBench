code = """import json, pandas as pd
import os

# Load aggregated revenue per track
path_rev = var_call_5nXItPjOzUHvztso9aPVwWVd
with open(path_rev, 'r') as f:
    rev_data = json.load(f)

# Find track_id with max total_revenue
rev_df = pd.DataFrame(rev_data)
rev_df['total_revenue'] = rev_df['total_revenue'].astype(float)
max_row = rev_df.loc[rev_df['total_revenue'].idxmax()]
max_track_id = int(max_row['track_id'])
max_revenue = float(max_row['total_revenue'])

# Load tracks metadata
path_tracks = var_call_e0Ypmxle59NzCUtUCUsqUTOE
with open(path_tracks, 'r') as f:
    tracks_data = json.load(f)
tracks_df = pd.DataFrame(tracks_data)

track_row = tracks_df[tracks_df['track_id'].astype(int) == max_track_id].iloc[0]

result = {
    'track_id': max_track_id,
    'title': track_row['title'],
    'artist': track_row['artist'],
    'album': track_row['album'],
    'year': track_row['year'],
    'total_revenue_usd': max_revenue
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5nXItPjOzUHvztso9aPVwWVd': 'file_storage/call_5nXItPjOzUHvztso9aPVwWVd.json', 'var_call_e0Ypmxle59NzCUtUCUsqUTOE': 'file_storage/call_e0Ypmxle59NzCUtUCUsqUTOE.json', 'var_call_IUxPzhGfYCcLlzEmuIIGT6P4': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}]}

exec(code, env_args)
