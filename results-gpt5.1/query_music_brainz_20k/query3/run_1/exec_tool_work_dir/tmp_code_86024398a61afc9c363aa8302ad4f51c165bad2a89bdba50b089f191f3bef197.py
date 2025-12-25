code = """import json, pandas as pd

# Load full datasets
tracks_path = var_call_l3Kuutr8UteuG8BdsXkiTqdk
sales_path = var_call_Tkpdo1oUcoKRyEX4vwCEpmGr

with open(tracks_path, 'r') as f:
    tracks = json.load(f)
with open(sales_path, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure correct dtypes
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# For this question, assume each track_id represents a distinct song entity.
# Aggregate total revenue by track_id
rev_by_track = sales_df.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Get track_id with max revenue
top_row = rev_by_track.sort_values('revenue_usd', ascending=False).iloc[0]

top_track_id = int(top_row['track_id'])
max_revenue = float(top_row['revenue_usd'])

track_row = tracks_df[tracks_df['track_id'] == top_track_id].iloc[0]

result = {
    'track_id': top_track_id,
    'title': track_row['title'],
    'artist': track_row['artist'],
    'album': track_row['album'],
    'year': track_row['year'],
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_l3Kuutr8UteuG8BdsXkiTqdk': 'file_storage/call_l3Kuutr8UteuG8BdsXkiTqdk.json', 'var_call_Tkpdo1oUcoKRyEX4vwCEpmGr': 'file_storage/call_Tkpdo1oUcoKRyEX4vwCEpmGr.json'}

exec(code, env_args)
