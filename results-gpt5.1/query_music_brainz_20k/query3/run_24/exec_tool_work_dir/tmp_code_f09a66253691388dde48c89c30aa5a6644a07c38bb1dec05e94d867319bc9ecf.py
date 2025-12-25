code = """import json, pandas as pd

# Load full results from JSON files
with open(var_call_BST1vpImtUhsW4YJRaIkY3uA, 'r') as f:
    tracks = json.load(f)
with open(var_call_lja2mOhr73bxmZazPMlBqetM, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize track attributes for entity resolution
for col in ['title', 'artist', 'album']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()
tracks_df['year_norm'] = tracks_df['year'].fillna('').astype(str).str.extract(r'(\d{2,4})', expand=False)

# Create a simple blocking key based on title and artist (and album when available)
tracks_df['block_key'] = tracks_df['title'] + '|' + tracks_df['artist'] + '|' + tracks_df['album']

# For tracks that have very generic or missing info, fall back to title only
mask_generic = (tracks_df['artist'].isin(['', 'none', '[unknown]']) | tracks_df['artist'].str.contains('unknown'))
tracks_df.loc[mask_generic, 'block_key'] = tracks_df.loc[mask_generic, 'title']

# Group by block_key to treat each group as a real-world track entity
entity_groups = tracks_df.groupby('block_key')['track_id'].apply(list).reset_index(name='track_ids')

# Build a mapping from track_id to canonical entity id (index in entity_groups)
track_to_entity = {}
for idx, row in entity_groups.iterrows():
    for tid in row['track_ids']:
        track_to_entity[int(tid)] = int(idx)

sales_df['track_id'] = sales_df['track_id'].astype(int)

# Map each sale to an entity_id
sales_df['entity_id'] = sales_df['track_id'].map(track_to_entity)

# There might be track_ids in sales that don't exist in tracks (edge case); drop them
sales_df = sales_df.dropna(subset=['entity_id'])

# Aggregate revenue by entity_id
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
entity_revenue = sales_df.groupby('entity_id')['revenue_usd'].sum().reset_index()

# Find entity with max revenue
max_row = entity_revenue.loc[entity_revenue['revenue_usd'].idxmax()]
max_entity_id = int(max_row['entity_id'])
max_revenue = float(max_row['revenue_usd'])

# Get representative track (first track_id in that entity group)
entity_track_ids = entity_groups.loc[max_entity_id, 'track_ids']
rep_track_id = int(entity_track_ids[0])
rep_track = tracks_df[tracks_df['track_id'].astype(int) == rep_track_id].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'year': rep_track['year'],
    'total_revenue_usd': round(max_revenue, 2)
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_BST1vpImtUhsW4YJRaIkY3uA': 'file_storage/call_BST1vpImtUhsW4YJRaIkY3uA.json', 'var_call_lja2mOhr73bxmZazPMlBqetM': 'file_storage/call_lja2mOhr73bxmZazPMlBqetM.json'}

exec(code, env_args)
