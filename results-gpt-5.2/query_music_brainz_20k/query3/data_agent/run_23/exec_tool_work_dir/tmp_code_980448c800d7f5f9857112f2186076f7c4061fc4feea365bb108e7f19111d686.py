code = """import json, pandas as pd

# Load sales top per track_id
sales_path = var_call_Rzf9UaLmRuFht5A8rJ0XvPa4
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)
sales_df = pd.DataFrame(sales)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)

# Load tracks
tracks_path = var_call_tYspsuJLH9wPpzBTOwJEuh8r
with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
tracks_df = pd.DataFrame(tracks)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Join for those top track_ids
top_ids = set(sales_df['track_id'].tolist())
sub_tracks = tracks_df[tracks_df['track_id'].isin(top_ids)].copy()
merged = sales_df.merge(sub_tracks, on='track_id', how='left')

# Entity resolution: canonical key based on normalized title/artist/album
import re

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^a-z0-9\s]", "", s)
    return s

merged['k_title'] = merged['title'].map(norm)
merged['k_artist'] = merged['artist'].map(norm)
merged['k_album'] = merged['album'].map(norm)
merged['entity_key'] = merged['k_title'] + '|' + merged['k_artist'] + '|' + merged['k_album']

# For each entity_key, sum revenue across track_ids in top set (approx; assumes winner in top 200)
ent = merged.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    title=('title', lambda x: x.dropna().iloc[0] if len(x.dropna()) else None),
    artist=('artist', lambda x: x.dropna().iloc[0] if len(x.dropna()) else None),
    album=('album', lambda x: x.dropna().iloc[0] if len(x.dropna()) else None),
    track_ids=('track_id', lambda x: sorted(set(map(int,x.tolist()))))
).reset_index()

ent = ent.sort_values('total_revenue_usd', ascending=False).reset_index(drop=True)
winner = ent.iloc[0].to_dict()
winner['total_revenue_usd'] = round(float(winner['total_revenue_usd']), 2)

print('__RESULT__:')
print(json.dumps(winner, ensure_ascii=False))"""

env_args = {'var_call_Rzf9UaLmRuFht5A8rJ0XvPa4': 'file_storage/call_Rzf9UaLmRuFht5A8rJ0XvPa4.json', 'var_call_tYspsuJLH9wPpzBTOwJEuh8r': 'file_storage/call_tYspsuJLH9wPpzBTOwJEuh8r.json'}

exec(code, env_args)
