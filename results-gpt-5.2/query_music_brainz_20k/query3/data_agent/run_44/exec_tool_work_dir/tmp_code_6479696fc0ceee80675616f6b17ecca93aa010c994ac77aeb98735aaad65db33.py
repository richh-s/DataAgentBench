code = """import json, pandas as pd, re

sales_src = var_call_zGCXTYXQrXKY82WZyVBGf3My
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

df_sales = pd.DataFrame(sales)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

tracks_src = var_call_TWQww3cgdlwfFir1zE8V0pUn
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

df_tracks = pd.DataFrame(tracks)
df_tracks['track_id'] = df_tracks['track_id'].astype(int)
for c in ['title','artist','album','year']:
    df_tracks[c] = df_tracks[c].astype(str)

def norm_str(s):
    s = '' if s is None else str(s)
    if s.lower()=='none' or s.strip()=='' or s.strip().lower()=='[unknown]':
        return ''
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s

def norm_title(t):
    t = norm_str(t)
    t = re.sub(r"^(\d{1,3}[-_. ]+)", "", t)
    return t

def year_bucket(y):
    y = norm_str(y)
    if not y:
        return ''
    y = re.sub(r"[^0-9]", "", y)
    if len(y)==4:
        return y
    if len(y)==2:
        return y
    return y

df_tracks['n_title'] = df_tracks['title'].map(norm_title)
df_tracks['n_artist'] = df_tracks['artist'].map(norm_str)
df_tracks['n_album'] = df_tracks['album'].map(norm_str)
df_tracks['y'] = df_tracks['year'].map(year_bucket)

split = df_tracks['n_title'].str.split(' - ', n=1, expand=True)
mask = (df_tracks['n_artist']=='') & (split.shape[1]==2)
df_tracks.loc[mask, 'n_artist'] = split.loc[mask,0].fillna('')
df_tracks.loc[mask, 'n_title'] = split.loc[mask,1].fillna('')

df_tracks['entity_key'] = (df_tracks['n_title']+'|'+df_tracks['n_artist']+'|'+df_tracks['n_album']+'|'+df_tracks['y'])

merged = df_sales.merge(df_tracks[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

agg = merged.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    title=('title','first'),
    artist=('artist','first'),
    album=('album','first'),
    year=('year','first'),
    n_track_ids=('track_id','nunique')
).reset_index()

best = agg.sort_values('total_revenue_usd', ascending=False).head(1).iloc[0].to_dict()
best['total_revenue_usd'] = float(round(best['total_revenue_usd'], 2))
best['n_track_ids'] = int(best['n_track_ids'])

print('__RESULT__:')
print(json.dumps(best, ensure_ascii=False))"""

env_args = {'var_call_zGCXTYXQrXKY82WZyVBGf3My': 'file_storage/call_zGCXTYXQrXKY82WZyVBGf3My.json', 'var_call_TWQww3cgdlwfFir1zE8V0pUn': 'file_storage/call_TWQww3cgdlwfFir1zE8V0pUn.json'}

exec(code, env_args)
