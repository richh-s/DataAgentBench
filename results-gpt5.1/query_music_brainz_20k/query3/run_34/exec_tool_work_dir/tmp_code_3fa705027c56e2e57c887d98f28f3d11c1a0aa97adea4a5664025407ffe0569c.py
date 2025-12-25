code = """import json, pandas as pd

# Load full data from files
with open(var_call_w3ibfwDdmGwsvjctDkVp1e90, 'r') as f:
    tracks = json.load(f)
with open(var_call_3YkHP555LNW5q43PMLPhJJ6Y, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic normalization: lowercase and strip title/artist/album for dedup
for col in ['title','artist','album']:
    tracks_df[col + '_norm'] = tracks_df[col].fillna('').str.lower().str.strip()

# Define a key using title + artist (and album if available)
tracks_df['entity_key'] = tracks_df['title_norm'] + '|' + tracks_df['artist_norm'] + '|' + tracks_df['album_norm']

# Map track_id to entity_key
id_to_entity = tracks_df.set_index('track_id')['entity_key'].to_dict()

# Attach entity_key to sales
sales_df['entity_key'] = sales_df['track_id'].map(id_to_entity)

# Aggregate revenue by entity_key
agg = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()

# Find max revenue entity
max_row = agg.loc[agg['revenue_usd'].astype(float).idxmax()]
entity_key = max_row['entity_key']
max_revenue = float(max_row['revenue_usd'])

# Get representative track info for this entity
rep_track = tracks_df[tracks_df['entity_key'] == entity_key].iloc[0]
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

env_args = {'var_call_w3ibfwDdmGwsvjctDkVp1e90': 'file_storage/call_w3ibfwDdmGwsvjctDkVp1e90.json', 'var_call_3YkHP555LNW5q43PMLPhJJ6Y': 'file_storage/call_3YkHP555LNW5q43PMLPhJJ6Y.json', 'var_call_BqomMSlvxI7CtyM9zmFfK6bc': ['tracks'], 'var_call_QBEdsye4RjaITJlOl0RLDarY': ['sales']}

exec(code, env_args)
