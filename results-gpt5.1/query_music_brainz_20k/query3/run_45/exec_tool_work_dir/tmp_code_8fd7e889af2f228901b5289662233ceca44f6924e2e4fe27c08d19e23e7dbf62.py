code = """import json, pandas as pd

# Load full datasets from files
with open(var_call_ny8QwwLZyBQvmoNPpdwr7vWO, 'r') as f:
    tracks = json.load(f)
with open(var_call_YEJwgLvJAvcPW8sTdtqf5pfl, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize key text fields for entity matching
for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].fillna('')
    tracks_df[col + '_norm'] = tracks_df[col].str.lower().str.replace('[^a-z0-9]+', ' ', regex=True).str.strip()

# Build a canonical key combining normalized title and artist, fallback to album when artist missing
tracks_df['canon_key'] = tracks_df['title_norm'] + '|' + tracks_df['artist_norm']
missing_artist = tracks_df['artist_norm'].eq('') & tracks_df['album_norm'].ne('')
tracks_df.loc[missing_artist, 'canon_key'] = tracks_df.loc[missing_artist, 'title_norm'] + '|' + tracks_df.loc[missing_artist, 'album_norm']

# Some records may have extremely messy titles; keep as-is for now

# Map each track_id to canon_key
track_to_key = tracks_df.set_index('track_id')['canon_key'].to_dict()

sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['canon_key'] = sales_df['track_id'].map(track_to_key)

# Aggregate revenue per real-world song (canon_key)
revenue_by_song = sales_df.groupby('canon_key', dropna=False)['revenue_usd'].astype(float).sum().reset_index()

# Find max revenue canon_key
max_row = revenue_by_song.loc[revenue_by_song['revenue_usd'].idxmax()]
max_key = max_row['canon_key']
max_revenue = float(max_row['revenue_usd'])

# Get a representative title/artist for that canon_key
rep = tracks_df[tracks_df['canon_key'] == max_key].iloc[0]
result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ny8QwwLZyBQvmoNPpdwr7vWO': 'file_storage/call_ny8QwwLZyBQvmoNPpdwr7vWO.json', 'var_call_YEJwgLvJAvcPW8sTdtqf5pfl': 'file_storage/call_YEJwgLvJAvcPW8sTdtqf5pfl.json', 'var_call_vR9qLtLK9OGQwSdi2MzoKD9z': ['tracks'], 'var_call_zIrIWzRLO8aSrItD9UhresHK': ['sales']}

exec(code, env_args)
