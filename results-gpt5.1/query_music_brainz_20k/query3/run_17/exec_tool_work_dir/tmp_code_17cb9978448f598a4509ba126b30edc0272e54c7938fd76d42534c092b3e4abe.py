code = """import pandas as pd, json

# Load full results from files
tracks_path = var_call_wCAYIq3Kjy81kVZiaf3x3ARH
sales_path = var_call_m0j1tHIjIFqHOKoXtEnd0ZRH

tracks = pd.read_json(tracks_path)
sales = pd.read_json(sales_path)

# Basic normalization of key fields for entity resolution
for col in ['title','artist','album']:
    tracks[col] = tracks[col].fillna('').astype(str).str.strip().str.lower()

# Create a simple blocking key on normalized title and artist
tracks['block_key'] = tracks['title'] + '|' + tracks['artist']

# Aggregate revenue by raw track_id
track_rev = sales.groupby('track_id', as_index=False)['revenue_usd'].sum()

# Merge with tracks to get metadata and block key
tracks['track_id'] = tracks['track_id'].astype(str)
track_rev['track_id'] = track_rev['track_id'].astype(str)
track_rev_meta = track_rev.merge(tracks[['track_id','block_key','title','artist','album']], on='track_id', how='left')

# Aggregate revenue by block_key as an approximation of real-world track
entity_rev = track_rev_meta.groupby(['block_key','title','artist','album'], as_index=False)['revenue_usd'].sum()

# Find the entity with max revenue
best = entity_rev.sort_values('revenue_usd', ascending=False).iloc[0]

result = {
    'title': best['title'],
    'artist': best['artist'],
    'album': best['album'],
    'total_revenue_usd': float(best['revenue_usd'])
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_wCAYIq3Kjy81kVZiaf3x3ARH': 'file_storage/call_wCAYIq3Kjy81kVZiaf3x3ARH.json', 'var_call_m0j1tHIjIFqHOKoXtEnd0ZRH': 'file_storage/call_m0j1tHIjIFqHOKoXtEnd0ZRH.json', 'var_call_aPyTI3XPQtRmj8kMs4hE4jsD': ['tracks'], 'var_call_QcGXKkB9TYUdlg5SpGj2oBst': ['sales']}

exec(code, env_args)
