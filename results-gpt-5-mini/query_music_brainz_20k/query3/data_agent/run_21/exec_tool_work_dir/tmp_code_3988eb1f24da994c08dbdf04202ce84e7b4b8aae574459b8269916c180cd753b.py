code = """import json
import pandas as pd

# Load the previously computed result for context
res = json.loads(open(var_call_2xtCUr9o1BtL8AWWppeCAXUR, 'r', encoding='utf-8').read().strip().split('\n',1)[1])

# Load full merged data to inspect representative titles/artists for the top entity
with open(var_call_SkrOIAlwXbrOAfb6RAv6HqY1, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_jpXV3hYazw6nDd2Nk7trJYC7, 'r', encoding='utf-8') as f:
    sales = json.load(f)

df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

df_merged = df_sales.merge(df_tracks, on='track_id', how='left', suffixes=('_sale','_track'))

# Filter merged rows for the top entity's track_ids
top_track_ids = res['track_ids']
filtered = df_merged[df_merged['track_id'].isin(top_track_ids)].copy()

# Show unique combinations of title, artist, album, year
combos = filtered[['track_id','title','artist','album','year']].drop_duplicates().to_dict(orient='records')

output = {
    'top_entity_key': res['entity_key'],
    'total_revenue_usd': res['total_revenue_usd'],
    'sales_count': res['sales_count'],
    'track_id_records': combos
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_SkrOIAlwXbrOAfb6RAv6HqY1': 'file_storage/call_SkrOIAlwXbrOAfb6RAv6HqY1.json', 'var_call_jpXV3hYazw6nDd2Nk7trJYC7': 'file_storage/call_jpXV3hYazw6nDd2Nk7trJYC7.json', 'var_call_2xtCUr9o1BtL8AWWppeCAXUR': {'title': '', 'artist': 'Песняры', 'total_revenue_usd': 9443.69, 'sales_count': 33, 'track_ids': ['10617', '13726', '14964', '1759', '18230', '202', '2556', '258', '3131', '4979'], 'entity_key': '||2006'}}

exec(code, env_args)
