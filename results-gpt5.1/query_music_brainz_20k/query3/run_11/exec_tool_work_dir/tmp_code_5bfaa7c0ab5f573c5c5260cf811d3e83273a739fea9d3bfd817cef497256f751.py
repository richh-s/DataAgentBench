code = """import json, pandas as pd
from pathlib import Path

# Load full data from files
tracks_path = Path(var_call_jAwNxDrGp2sgv5eYqCfGqwqV)
sales_path = Path(var_call_U8943rlir7BWccxDXCHDSvUU)

tracks = json.loads(tracks_path.read_text())
sales = json.loads(sales_path.read_text())

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Naive entity resolution: match on normalized (title, artist, album, year)
for col in ['title','artist','album','year']:
    tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()

tracks_df['entity_key'] = (tracks_df['title'] + '|' + tracks_df['artist'] + '|' + tracks_df['album'] + '|' + tracks_df['year'])

# Map track_id -> entity_key
id_to_entity = tracks_df.set_index('track_id')['entity_key']

sales_df = sales_df.merge(id_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

# Aggregate revenue by entity
entity_revenue = sales_df.groupby('entity_key', as_index=False)['revenue_usd'].sum()

# Attach representative track (first) for labeling
rep_tracks = tracks_df.groupby('entity_key').agg({'title':'first','artist':'first','album':'first','year':'first'}).reset_index()

summary = entity_revenue.merge(rep_tracks, on='entity_key', how='left')

# Find max revenue
max_row = summary.sort_values('revenue_usd', ascending=False).iloc[0]

result = {
    'title': max_row['title'],
    'artist': max_row['artist'],
    'album': max_row['album'],
    'year': max_row['year'],
    'total_revenue_usd': max_row['revenue_usd']
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_jAwNxDrGp2sgv5eYqCfGqwqV': 'file_storage/call_jAwNxDrGp2sgv5eYqCfGqwqV.json', 'var_call_U8943rlir7BWccxDXCHDSvUU': 'file_storage/call_U8943rlir7BWccxDXCHDSvUU.json', 'var_call_3VkYuDJg0GxJfTWHFuGtHfU1': ['tracks'], 'var_call_9T7FYC4hfwnY41YmgqWYduev': ['sales']}

exec(code, env_args)
