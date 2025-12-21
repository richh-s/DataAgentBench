code = """import json, pandas as pd

# Load full data from files
tracks_path = var_call_oIbyCX0K1zCATtGj0CcmpNH9
sales_path = var_call_akFQdpBdtlpAq3SNiMRnznD3

with open(tracks_path, 'r') as f:
    tracks = json.load(f)
with open(sales_path, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)

# Normalize basic fields for similarity grouping
for col in ['title', 'artist', 'album', 'year']:
    tracks_df[col] = tracks_df[col].astype(str).str.strip().str.lower()

# Heuristic: treat records as same song if title and artist match exactly after normalization.
# If artist is missing/none-like, require title and album match.

# Build a canonical song key
def canonical_key(row):
    title = row['title']
    artist = row['artist']
    album = row['album']
    # identify missing artist
    if artist in ('none', 'unknown', '[unknown]', 'nan', ''):
        return ('title_album', title, album)
    return ('title_artist', title, artist)

tracks_df['song_key'] = tracks_df.apply(canonical_key, axis=1)

# Map track_id -> song_key
track_to_key = tracks_df.set_index('track_id')['song_key'].to_dict()

sales_df = pd.DataFrame(sales)

# ensure numeric
types = {'revenue_usd': float}
for col, t in types.items():
    sales_df[col] = sales_df[col].astype(t)

# attach song_key via track_id
sales_df['track_id'] = sales_df['track_id'].astype(str)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
track_to_key = tracks_df.set_index('track_id')['song_key'].to_dict()

sales_df['song_key'] = sales_df['track_id'].map(track_to_key)

# aggregate revenue per song_key
agg = sales_df.groupby('song_key', dropna=False)['revenue_usd'].sum().reset_index()

# find max revenue song
max_row = agg.loc[agg['revenue_usd'].idxmax()]
max_key = max_row['song_key']
max_revenue = float(max_row['revenue_usd'])

# get a representative track for this song_key
rep_track = tracks_df[tracks_df['song_key'] == max_key].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'year': rep_track['year'],
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oIbyCX0K1zCATtGj0CcmpNH9': 'file_storage/call_oIbyCX0K1zCATtGj0CcmpNH9.json', 'var_call_akFQdpBdtlpAq3SNiMRnznD3': 'file_storage/call_akFQdpBdtlpAq3SNiMRnznD3.json'}

exec(code, env_args)
