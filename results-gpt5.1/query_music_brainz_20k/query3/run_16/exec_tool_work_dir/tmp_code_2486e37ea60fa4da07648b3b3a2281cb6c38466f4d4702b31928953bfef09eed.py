code = """import json, pandas as pd
from pathlib import Path

tracks_path = Path(var_call_90VZqrCG9zneNKtCSuw1LRqJ)
sales_path = Path(var_call_880l7oRLUOkqjQJO81hFoYju)

tracks = pd.read_json(tracks_path)
sales = pd.read_json(sales_path)

tracks['norm_title'] = tracks['title'].str.strip().str.lower()
tracks['norm_artist'] = tracks['artist'].fillna('').str.strip().str.lower()
tracks['norm_album'] = tracks['album'].fillna('').str.strip().str.lower()

# basic entity key using title+artist; fallback to title+album where artist missing
tracks['entity_key'] = tracks['norm_title'] + '||' + tracks['norm_artist']
missing_artist = tracks['norm_artist'].eq('')
tracks.loc[missing_artist, 'entity_key'] = tracks.loc[missing_artist, 'norm_title'] + '||' + tracks.loc[missing_artist, 'norm_album']

# Map track_id to entity_key
track_to_entity = tracks.set_index('track_id')['entity_key']

sales = sales.merge(track_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

entity_revenue = sales.groupby('entity_key', as_index=False)['revenue_usd'].sum()

# Attach a representative title/artist for each entity
rep = tracks.groupby('entity_key').agg({'title':'first','artist':'first'})
entity_revenue = entity_revenue.merge(rep, on='entity_key', how='left')

best = entity_revenue.sort_values('revenue_usd', ascending=False).iloc[0]

result = {
  'title': best['title'],
  'artist': best['artist'],
  'total_revenue_usd': float(best['revenue_usd'])
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_90VZqrCG9zneNKtCSuw1LRqJ': 'file_storage/call_90VZqrCG9zneNKtCSuw1LRqJ.json', 'var_call_880l7oRLUOkqjQJO81hFoYju': 'file_storage/call_880l7oRLUOkqjQJO81hFoYju.json'}

exec(code, env_args)
