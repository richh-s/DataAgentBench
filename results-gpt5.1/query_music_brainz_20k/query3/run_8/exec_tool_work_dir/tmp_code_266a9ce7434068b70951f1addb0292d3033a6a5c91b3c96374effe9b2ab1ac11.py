code = """import json, pandas as pd, os

# Load full results from JSON files
tracks_path = var_call_8gTMQ3y4zUoZezISwxH7DRD1
sales_path = var_call_EINYfg5S7IoSUpmlURoxxxSu

with open(tracks_path, 'r') as f:
    tracks = json.load(f)
with open(sales_path, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert numeric fields
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Basic entity key: normalized title + artist + album (casefold, strip). Handle None/'None'.
for col in ['title','artist','album']:
    tracks_df[col] = tracks_df[col].fillna('')
    tracks_df[col] = tracks_df[col].replace('None','').replace('[unknown]','')

def norm(s):
    return ''.join(s.casefold().split())

tracks_df['entity_key'] = tracks_df.apply(lambda r: norm(r['title'])+'||'+norm(r['artist'])+'||'+norm(r['album']), axis=1)

# Map each track_id to entity_key
track_to_entity = tracks_df.set_index('track_id')['entity_key']

sales_df = sales_df.merge(track_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

# Aggregate revenue by entity_key
agg = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()

# Find max revenue entity
max_row = agg.loc[agg['revenue_usd'].idxmax()]
max_key = max_row['entity_key']
max_revenue = float(max_row['revenue_usd'])

# For that entity, pick a representative track (first occurrence) to get a readable title/artist/album
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

env_args = {'var_call_8gTMQ3y4zUoZezISwxH7DRD1': 'file_storage/call_8gTMQ3y4zUoZezISwxH7DRD1.json', 'var_call_EINYfg5S7IoSUpmlURoxxxSu': 'file_storage/call_EINYfg5S7IoSUpmlURoxxxSu.json'}

exec(code, env_args)
