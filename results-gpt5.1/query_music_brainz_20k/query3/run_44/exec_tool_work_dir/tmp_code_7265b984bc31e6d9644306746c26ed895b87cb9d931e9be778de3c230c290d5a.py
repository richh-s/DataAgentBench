code = """import json, pandas as pd

# Load full datasets from files
tracks_path = var_call_5ylbfLA4GBqljTEPyRqDnNQR
sales_path = var_call_A2TKMMmcsDlwvTjESHjGJV31

with open(tracks_path, 'r') as f:
    tracks = json.load(f)
with open(sales_path, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning: normalize string fields for deduping
for col in ['title','artist','album']:
    tracks_df[col] = tracks_df[col].astype(str).str.strip().str.lower()

# Simple heuristic entity resolution: same normalized title & artist considered same song
# If artist is missing/none-like, we rely on title+album
none_like = set(['none','nan','',"[unknown]"])

tracks_df['artist_clean'] = tracks_df['artist'].where(~tracks_df['artist'].isin(none_like), None)
tracks_df['album_clean'] = tracks_df['album'].where(~tracks_df['album'].isin(none_like), None)

# Build song key
tracks_df['song_key'] = None
mask_artist = tracks_df['artist_clean'].notna() & (tracks_df['artist_clean'] != '')
tracks_df.loc[mask_artist, 'song_key'] = tracks_df.loc[mask_artist, 'title'] + '||' + tracks_df.loc[mask_artist, 'artist_clean']

mask_no_artist = tracks_df['song_key'].isna()
tracks_df.loc[mask_no_artist, 'song_key'] = tracks_df.loc[mask_no_artist, 'title'] + '||' + tracks_df.loc[mask_no_artist, 'album_clean'].fillna('')

# Map each track_id to song_key
track_to_song = tracks_df.set_index('track_id')['song_key'].to_dict()

# Attach song_key to sales
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['song_key'] = sales_df['track_id'].map(track_to_song)

# Aggregate revenue by song_key
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
agg = sales_df.groupby('song_key', dropna=False)['revenue_usd'].sum().reset_index()

# Get max revenue song
top = agg.sort_values('revenue_usd', ascending=False).iloc[0]

song_key = top['song_key']
revenue = float(top['revenue_usd'])

# Get representative metadata (first track with this song_key)
rep = tracks_df[tracks_df['song_key'] == song_key].iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist_clean'] if pd.notna(rep['artist_clean']) else None,
    'album': rep['album_clean'] if pd.notna(rep['album_clean']) else None,
    'song_key': song_key,
    'total_revenue_usd': round(revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5ylbfLA4GBqljTEPyRqDnNQR': 'file_storage/call_5ylbfLA4GBqljTEPyRqDnNQR.json', 'var_call_A2TKMMmcsDlwvTjESHjGJV31': 'file_storage/call_A2TKMMmcsDlwvTjESHjGJV31.json'}

exec(code, env_args)
