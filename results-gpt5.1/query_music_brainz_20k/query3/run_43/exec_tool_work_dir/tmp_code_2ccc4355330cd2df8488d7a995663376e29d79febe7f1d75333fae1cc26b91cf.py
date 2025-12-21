code = """import json, pandas as pd
from pathlib import Path

# Load full data from JSON files
tracks_path = Path(var_call_cldQ6e8e7SafteT3fUTs0X7m)
sales_path = Path(var_call_L9xfAgOFV7C22ZANplIA0QIU)

tracks = pd.read_json(tracks_path)
sales = pd.read_json(sales_path)

# Basic cleaning: ensure correct dtypes
sales['revenue_usd'] = sales['revenue_usd'].astype(float)

# Entity resolution heuristic:
# We'll consider tracks to be the same song if title and artist (case-insensitive, stripped) match
# after simple normalization, and album/year differences are ignored.

def norm(x):
    if pd.isna(x):
        return None
    return ' '.join(str(x).strip().lower().split())

tracks['norm_title'] = tracks['title'].apply(norm)
tracks['norm_artist'] = tracks['artist'].apply(norm)

# Create a song key as (norm_title, norm_artist). If artist is missing but title present,
# still group by title alone with artist None.
tracks['song_key'] = list(zip(tracks['norm_title'], tracks['norm_artist']))

# Map track_id -> song_key
track_to_song = tracks.set_index('track_id')['song_key']

# Join sales with song_key
sales = sales.merge(track_to_song.rename('song_key'), left_on='track_id', right_index=True, how='left')

# Aggregate revenue by song_key
song_rev = sales.groupby('song_key', dropna=False)['revenue_usd'].sum().reset_index()

# Find song_key with max revenue
best_row = song_rev.loc[song_rev['revenue_usd'].idxmax()]
best_key = best_row['song_key']
best_revenue = float(best_row['revenue_usd'])

best_title, best_artist = best_key

result = {
    'title': best_title,
    'artist': best_artist,
    'total_revenue_usd': round(best_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cldQ6e8e7SafteT3fUTs0X7m': 'file_storage/call_cldQ6e8e7SafteT3fUTs0X7m.json', 'var_call_L9xfAgOFV7C22ZANplIA0QIU': 'file_storage/call_L9xfAgOFV7C22ZANplIA0QIU.json'}

exec(code, env_args)
