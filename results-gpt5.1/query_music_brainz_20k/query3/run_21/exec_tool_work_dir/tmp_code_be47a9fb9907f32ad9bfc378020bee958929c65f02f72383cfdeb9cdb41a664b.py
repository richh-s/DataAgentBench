code = """import json, pandas as pd, os

# Load full sales aggregation
with open(var_call_OYLRavnu0iDZqI4Udmb37sJH, 'r') as f:
    sales_agg = json.load(f)

# Load full tracks data
with open(var_call_PyzXV5CwyQ2gPDeAuh6Lpex1, 'r') as f:
    tracks = json.load(f)

sales_df = pd.DataFrame(sales_agg)
tracks_df = pd.DataFrame(tracks)

# Convert numeric columns
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue'] = sales_df['total_revenue'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Basic normalization helpers
def norm_text(s):
    if pd.isna(s):
        return None
    s = str(s).strip().lower()
    for ch in ["-", "_", "/", "(", ")", "[", "]", ":", ";", ",", "'", '"']:
        s = s.replace(ch, " ")
    s = " ".join(s.split())
    return s or None

for col in ['title','artist','album']:
    tracks_df[f'norm_{col}'] = tracks_df[col].apply(norm_text)

# Create a heuristic key: normalized title + artist, fallback to title+album
tracks_df['entity_key'] = tracks_df['norm_title'].fillna('') + '||' + tracks_df['norm_artist'].fillna('')
mask_empty = tracks_df['entity_key'].isin(['||','| |'])
tracks_df.loc[mask_empty, 'entity_key'] = tracks_df.loc[mask_empty, 'norm_title'].fillna('') + '||' + tracks_df.loc[mask_empty, 'norm_album'].fillna('')

# Join sales with tracks to get entity_key
merged = sales_df.merge(tracks_df[['track_id','entity_key','title','artist']], on='track_id', how='left')

# Aggregate revenue by entity_key
entity_rev = merged.groupby('entity_key', dropna=False)['total_revenue'].sum().reset_index()

# Find max
max_row = entity_rev.loc[entity_rev['total_revenue'].idxmax()]
key = max_row['entity_key']
max_revenue = float(max_row['total_revenue'])

# Get representative title/artist: pick the track with highest revenue within this entity
entity_tracks = merged[merged['entity_key'] == key].copy()
track_rev = entity_tracks.groupby(['track_id','title','artist'])['total_revenue'].sum().reset_index()
rep_row = track_rev.loc[track_rev['total_revenue'].idxmax()]

result = {
    'title': rep_row['title'],
    'artist': rep_row['artist'],
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OYLRavnu0iDZqI4Udmb37sJH': 'file_storage/call_OYLRavnu0iDZqI4Udmb37sJH.json', 'var_call_PyzXV5CwyQ2gPDeAuh6Lpex1': 'file_storage/call_PyzXV5CwyQ2gPDeAuh6Lpex1.json'}

exec(code, env_args)
