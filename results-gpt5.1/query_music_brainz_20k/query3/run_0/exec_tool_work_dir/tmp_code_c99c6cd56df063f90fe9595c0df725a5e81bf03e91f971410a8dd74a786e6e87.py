code = """import json, pandas as pd

# Load full results
with open(var_call_TCQHk8Nx8wkcMJ8yPuJyhDTk, 'r') as f:
    sales_agg = json.load(f)
with open(var_call_fxwaLaXHroXqGoD18RT9BYGi, 'r') as f:
    tracks = json.load(f)

sales_df = pd.DataFrame(sales_agg)
tracks_df = pd.DataFrame(tracks)

sales_df['track_id'] = sales_df['track_id'].astype(int)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Simple canonical key for entity resolution: normalized title + artist + album (casefold, stripped)
for col in ['title','artist','album']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.casefold().str.strip()

tracks_df['entity_key'] = tracks_df['title'] + '||' + tracks_df['artist'] + '||' + tracks_df['album']

# Map each track_id to its entity_key
track_entity = tracks_df[['track_id','entity_key']]

# Join sales with entity keys
sales_with_entity = sales_df.merge(track_entity, on='track_id', how='left')

# Aggregate revenue by entity_key
entity_revenue = sales_with_entity.groupby('entity_key', as_index=False)['total_revenue'].sum()

# Find top entity
top_row = entity_revenue.sort_values('total_revenue', ascending=False).iloc[0]

# Get a representative track record for this entity
rep_track = tracks_df[tracks_df['entity_key'] == top_row['entity_key']].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'total_revenue_usd': float(top_row['total_revenue'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TCQHk8Nx8wkcMJ8yPuJyhDTk': 'file_storage/call_TCQHk8Nx8wkcMJ8yPuJyhDTk.json', 'var_call_fxwaLaXHroXqGoD18RT9BYGi': 'file_storage/call_fxwaLaXHroXqGoD18RT9BYGi.json'}

exec(code, env_args)
