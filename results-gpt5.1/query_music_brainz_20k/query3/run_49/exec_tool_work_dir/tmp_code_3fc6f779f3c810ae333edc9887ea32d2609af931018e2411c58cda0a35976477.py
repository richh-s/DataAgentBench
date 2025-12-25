code = """import json, pandas as pd, os

# Load full aggregates and tracks
with open(var_call_UpHyUJCRSRIiLZD6BvFiPx9Z, 'r') as f:
    sales_agg = json.load(f)
with open(var_call_7FAftJ7OjDRt14EHCduY3wMS, 'r') as f:
    tracks = json.load(f)

sales_df = pd.DataFrame(sales_agg)
tracks_df = pd.DataFrame(tracks)

# Convert dtypes
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Basic normalization helpers
def norm_text(s):
    if s is None:
        return None
    s = str(s).strip().lower()
    return ' '.join(s.split()) if s else None

for col in ['title','artist','album']:
    tracks_df[col + '_norm'] = tracks_df[col].apply(norm_text)

# We will treat tracks with same normalized title and artist as same song (album ignored first).
# Build a key
tracks_df['song_key'] = tracks_df['title_norm'].fillna('') + '||' + tracks_df['artist_norm'].fillna('')

# Some rows may have missing or unknown artist; keep album in that case
mask_unknown_artist = tracks_df['artist_norm'].isna() | tracks_df['artist_norm'].isin(['none','[unknown]','unknown',''])
tracks_df.loc[mask_unknown_artist, 'song_key'] = (
    tracks_df.loc[mask_unknown_artist, 'title_norm'].fillna('') + '||' +
    tracks_df.loc[mask_unknown_artist, 'album_norm'].fillna(''))

# Merge sales with tracks to get song_key
merged = sales_df.merge(tracks_df[['track_id','song_key','title','artist','album']], on='track_id', how='left')

# Aggregate revenue per logical song
song_rev = merged.groupby('song_key', dropna=False)['total_revenue'].sum().reset_index()

# Get max revenue song_key
max_row = song_rev.loc[song_rev['total_revenue'].idxmax()]
max_key = max_row['song_key']
max_revenue = float(max_row['total_revenue'])

# For reporting, pick one representative track (e.g., lowest track_id) for that song_key
rep_track = tracks_df[tracks_df['song_key'] == max_key].sort_values('track_id').iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UpHyUJCRSRIiLZD6BvFiPx9Z': 'file_storage/call_UpHyUJCRSRIiLZD6BvFiPx9Z.json', 'var_call_7FAftJ7OjDRt14EHCduY3wMS': 'file_storage/call_7FAftJ7OjDRt14EHCduY3wMS.json', 'var_call_B4AHAm5ZHmpi7szL6Vwk8W2W': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}]}

exec(code, env_args)
