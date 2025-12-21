code = """import json, pandas as pd

# Load full results from files
with open(var_call_iPGM8zN91nQLYJo7J2m2py8W, 'r') as f:
    tracks = json.load(f)
with open(var_call_bWCWovnw37PwQahoiLrGaFvQ, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert numeric fields
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# Very simple entity resolution: normalize title & artist (lowercase, strip) and group
for col in ['title','artist','album']:
    tracks_df[col] = tracks_df[col].fillna('None').astype(str).str.strip().str.lower()

tracks_df['entity_key'] = tracks_df['title'] + '||' + tracks_df['artist'] + '||' + tracks_df['album']

# Map each track_id to entity_key
track_to_entity = tracks_df.set_index('track_id')['entity_key']
sales_df = sales_df.merge(track_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

# Aggregate revenue by entity
entity_revenue = sales_df.groupby('entity_key', as_index=False)['revenue_usd'].sum()

# Get top entity
top_entity = entity_revenue.sort_values('revenue_usd', ascending=False).iloc[0]

# For reporting, pick the most common (title, artist, album) for this entity
entity_tracks = tracks_df[tracks_df['entity_key'] == top_entity['entity_key']]
mode_title = entity_tracks['title'].mode().iloc[0]
mode_artist = entity_tracks['artist'].mode().iloc[0]
mode_album = entity_tracks['album'].mode().iloc[0]

result = {
    'title': mode_title,
    'artist': mode_artist,
    'album': mode_album,
    'total_revenue_usd': round(float(top_entity['revenue_usd']), 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_iPGM8zN91nQLYJo7J2m2py8W': 'file_storage/call_iPGM8zN91nQLYJo7J2m2py8W.json', 'var_call_bWCWovnw37PwQahoiLrGaFvQ': 'file_storage/call_bWCWovnw37PwQahoiLrGaFvQ.json', 'var_call_kWSFHQXdAvS6IA00m0OCcXhI': ['tracks'], 'var_call_6Wl5ntmnoxyIeT57DckNRSAH': ['sales']}

exec(code, env_args)
