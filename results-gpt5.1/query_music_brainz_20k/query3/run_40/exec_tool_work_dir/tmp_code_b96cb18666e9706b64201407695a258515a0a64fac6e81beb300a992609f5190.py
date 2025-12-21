code = """import json, pandas as pd
from pathlib import Path

# Load full data from files
tracks_path = Path(var_call_gFjDL2FhRtw5ViYz36WbnSNz)
sales_path = Path(var_call_774kYdhUWXj2P1VM9jK6Dx70)

with open(tracks_path, 'r') as f:
    tracks = json.load(f)
with open(sales_path, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning: normalize key text fields for fuzzy grouping
for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].astype(str).str.strip().str.lower()

# Heuristic: consider tracks the same song if title and artist match exactly after normalization
# (album and year differences are allowed). This is a reasonable entity-resolution heuristic.
tracks_df['song_key'] = tracks_df['title'] + '||' + tracks_df['artist']

# Map each track_id to its song_key
track_to_song = tracks_df[['track_id', 'song_key']].drop_duplicates()

# Merge song_key into sales
sales_df = sales_df.merge(track_to_song, on='track_id', how='left')

# Ensure revenue_usd is numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Aggregate revenue by song_key
song_revenue = sales_df.groupby('song_key', dropna=False)['revenue_usd'].sum().reset_index()

# Find song_key with max revenue
max_row = song_revenue.loc[song_revenue['revenue_usd'].idxmax()]
max_key = max_row['song_key']
max_revenue = float(max_row['revenue_usd'])

# Decode song_key to a representative title/artist from tracks_df
rep = tracks_df[tracks_df['song_key'] == max_key].iloc[0]
result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_gFjDL2FhRtw5ViYz36WbnSNz': 'file_storage/call_gFjDL2FhRtw5ViYz36WbnSNz.json', 'var_call_774kYdhUWXj2P1VM9jK6Dx70': 'file_storage/call_774kYdhUWXj2P1VM9jK6Dx70.json'}

exec(code, env_args)
