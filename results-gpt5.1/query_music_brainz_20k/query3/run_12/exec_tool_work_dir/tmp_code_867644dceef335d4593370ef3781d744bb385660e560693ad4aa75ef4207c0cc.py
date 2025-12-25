code = """import json, pandas as pd

# Load full results from JSON files
with open(var_call_HRAWn0wxcLZik9JvzyxLkSWm, 'r') as f:
    tracks = json.load(f)
with open(var_call_6tOxe5ap1usLD4YqjKQQahu0, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic normalization: lowercase and strip title and artist for deduping, fill Nones
for col in ['title','artist','album','year']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

# Create a simple canonical key using title + artist + (album if available)
tracks_df['canon_key'] = tracks_df['title'] + '|' + tracks_df['artist'] + '|' + tracks_df['album']

# Some records might have missing artist or album; fall back to title only when others are empty
empty_mask = (tracks_df['artist'] == '') & (tracks_df['album'] == '')
tracks_df.loc[empty_mask, 'canon_key'] = 'title_only|' + tracks_df.loc[empty_mask, 'title']

# Map each track_id to its canon_key
track_to_key = tracks_df.set_index('track_id')['canon_key'].to_dict()

# Add canon_key to sales via track_id
sales_df['track_id'] = sales_df['track_id'].astype(str)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

sales_df['canon_key'] = sales_df['track_id'].map(track_to_key)

# Aggregate revenue by canonical track
agg = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].sum().reset_index()

# revenue_usd might be strings; convert to float
agg['revenue_usd'] = agg['revenue_usd'].astype(float)

# Find top canonical track by revenue
top = agg.sort_values('revenue_usd', ascending=False).iloc[0]

# Get a representative metadata row for this canon_key
rep = tracks_df[tracks_df['canon_key'] == top['canon_key']].iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'year': rep['year'],
    'total_revenue_usd': float(top['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_HRAWn0wxcLZik9JvzyxLkSWm': 'file_storage/call_HRAWn0wxcLZik9JvzyxLkSWm.json', 'var_call_6tOxe5ap1usLD4YqjKQQahu0': 'file_storage/call_6tOxe5ap1usLD4YqjKQQahu0.json', 'var_call_0Dmz6pnubJhIHHZWa90aIEQU': ['tracks'], 'var_call_DsGEzT4kPiiYmjglAZkHg0Dl': ['sales']}

exec(code, env_args)
