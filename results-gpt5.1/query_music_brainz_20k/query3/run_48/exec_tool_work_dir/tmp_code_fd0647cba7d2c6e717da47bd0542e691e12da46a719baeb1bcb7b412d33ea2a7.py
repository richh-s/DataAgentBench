code = """import json, pandas as pd
from pathlib import Path

with open(var_call_Ejq1FrwKjO0IbB22Ct7jYP16, 'r') as f:
    tracks = json.load(f)
with open(var_call_Mza345ZCpMkxBpbJAEr4jCdz, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

for col in ['title','artist','album','year']:
    tracks_df[col] = tracks_df[col].astype(str).str.strip().str.lower()

tracks_df['year_norm'] = tracks_df['year'].astype(str).str.extract(r'(\d{2,4})', expand=False).fillna('')

tracks_df['entity_key'] = tracks_df[['title','artist','album','year_norm']].astype(str).agg('|'.join, axis=1)

track_to_entity = tracks_df.set_index('track_id')['entity_key']

sales_df = sales_df.merge(track_to_entity.rename('entity_key'), left_on='track_id', right_index=True, how='left')

entity_revenue = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()

entity_revenue = entity_revenue[entity_revenue['entity_key'].notna()]

top_entity = entity_revenue.sort_values('revenue_usd', ascending=False).iloc[0]

rep_track = tracks_df[tracks_df['entity_key'] == top_entity['entity_key']].iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'year': rep_track['year'],
    'total_revenue_usd': round(float(top_entity['revenue_usd']), 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Ejq1FrwKjO0IbB22Ct7jYP16': 'file_storage/call_Ejq1FrwKjO0IbB22Ct7jYP16.json', 'var_call_Mza345ZCpMkxBpbJAEr4jCdz': 'file_storage/call_Mza345ZCpMkxBpbJAEr4jCdz.json'}

exec(code, env_args)
