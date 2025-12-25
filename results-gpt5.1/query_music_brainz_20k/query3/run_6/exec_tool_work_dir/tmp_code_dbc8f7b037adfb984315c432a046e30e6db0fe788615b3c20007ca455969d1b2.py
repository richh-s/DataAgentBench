code = """import json, pandas as pd
from pathlib import Path

# Load full data from JSON files
tracks_path = Path(var_call_nZJnIidE8vMfDRQREcijDRz5)
sales_path = Path(var_call_1y5yMfm2ceLGM8WobRtzudRT)

with tracks_path.open() as f:
    tracks = json.load(f)
with sales_path.open() as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Basic cleaning: normalize title and artist for rough entity resolution
for col in ['title','artist','album']:
    if col in tracks_df.columns:
        tracks_df[col] = tracks_df[col].astype(str).str.strip().str.lower()

# Convert track_id and revenue to numeric
sales_df['track_id'] = pd.to_numeric(sales_df['track_id'])
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
tracks_df['track_id'] = pd.to_numeric(tracks_df['track_id'])

# Heuristic: consider exact match on normalized title AND artist AND album as same real-world song
key_cols = ['title','artist','album']
tracks_df['entity_key'] = tracks_df[key_cols].agg(' | '.join, axis=1)

# Map each track_id to its entity_key
track_to_entity = tracks_df.set_index('track_id')['entity_key']

sales_df = sales_df.merge(track_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

# Aggregate revenue by entity_key
entity_revenue = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()

# Find entity with max revenue
top_entity = entity_revenue.sort_values('revenue_usd', ascending=False).iloc[0]

# Get a representative track (first one) for this entity_key
rep_track = tracks_df[tracks_df['entity_key'] == top_entity['entity_key']].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'total_revenue_usd': float(top_entity['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nZJnIidE8vMfDRQREcijDRz5': 'file_storage/call_nZJnIidE8vMfDRQREcijDRz5.json', 'var_call_1y5yMfm2ceLGM8WobRtzudRT': 'file_storage/call_1y5yMfm2ceLGM8WobRtzudRT.json'}

exec(code, env_args)
