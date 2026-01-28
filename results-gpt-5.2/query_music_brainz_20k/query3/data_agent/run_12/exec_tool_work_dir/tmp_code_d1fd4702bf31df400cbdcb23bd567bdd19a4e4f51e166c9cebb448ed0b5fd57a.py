code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

sales = pd.DataFrame(load_records(var_call_Fjf7qF4k8k1usFZ1YKXE3NEy))
tracks = pd.DataFrame(load_records(var_call_gug2ZSWQqNLOoffgdZAeS4xO))

# types
sales['track_id'] = sales['track_id'].astype(int)
sales['total_revenue_usd'] = sales['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# choose max revenue track_id (single)
max_row = sales.loc[sales['total_revenue_usd'].idxmax()]
max_track_id = int(max_row['track_id'])
max_rev = float(max_row['total_revenue_usd'])

row = tracks.loc[tracks['track_id']==max_track_id].iloc[0].to_dict() if (tracks['track_id']==max_track_id).any() else {'title': None,'artist':None,'album':None,'year':None}

title = row.get('title')
artist = row.get('artist')
album = row.get('album')
year = row.get('year')

# output
out = {
    'track_id': max_track_id,
    'title': title,
    'artist': artist,
    'album': album,
    'year': year,
    'total_revenue_usd': round(max_rev, 2)
}
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_Fjf7qF4k8k1usFZ1YKXE3NEy': 'file_storage/call_Fjf7qF4k8k1usFZ1YKXE3NEy.json', 'var_call_gug2ZSWQqNLOoffgdZAeS4xO': 'file_storage/call_gug2ZSWQqNLOoffgdZAeS4xO.json'}

exec(code, env_args)
