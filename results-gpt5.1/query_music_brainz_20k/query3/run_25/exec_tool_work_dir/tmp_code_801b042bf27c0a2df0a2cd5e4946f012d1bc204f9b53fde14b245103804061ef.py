code = """import json, pandas as pd, os

# Load full tracks and sales data
with open(var_call_5d8IHUwtUgQDYq7TtQgShUN5, 'r') as f:
    tracks = json.load(f)
with open(var_call_wMbn0jh2PucVRaaFjSU6R423, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning: normalize title and artist for grouping
for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

# Consider same real-world track if title, artist, album match after normalization
tracks_df['entity_key'] = tracks_df['title'] + '||' + tracks_df['artist'] + '||' + tracks_df['album']

# Map track_id to entity_key
track_to_entity = tracks_df.set_index('track_id')['entity_key']

# Ensure track_id types align
sales_df['track_id'] = sales_df['track_id'].astype(str)
track_to_entity.index = track_to_entity.index.astype(str)

sales_df = sales_df.merge(track_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

# Aggregate revenue by entity_key
revenue_by_entity = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].astype(float).sum().reset_index()

# Find max revenue entity
max_row = revenue_by_entity.loc[revenue_by_entity['revenue_usd'].idxmax()]
max_key = max_row['entity_key']
max_revenue = float(max_row['revenue_usd'])

# Extract a representative track for this entity_key to get readable title/artist/album
rep_track = tracks_df[tracks_df['entity_key'] == max_key].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_5d8IHUwtUgQDYq7TtQgShUN5': 'file_storage/call_5d8IHUwtUgQDYq7TtQgShUN5.json', 'var_call_wMbn0jh2PucVRaaFjSU6R423': 'file_storage/call_wMbn0jh2PucVRaaFjSU6R423.json', 'var_call_tb6PcrrJIHhC6ifp10e31yub': ['tracks'], 'var_call_IxgfvTz1ehEqSoD22xa5MT7o': ['sales']}

exec(code, env_args)
