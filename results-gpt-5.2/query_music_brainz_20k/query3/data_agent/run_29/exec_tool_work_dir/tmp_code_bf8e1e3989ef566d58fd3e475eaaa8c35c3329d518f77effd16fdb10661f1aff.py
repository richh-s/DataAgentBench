code = """import json, pandas as pd, re

sales_src = var_call_rYFKqIMu85ZZdvEKSFBVP03k
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

tracks_src = var_call_dy8zIFVrdydMaNFB6ks0erVJ
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

sales_df = pd.DataFrame(sales)
tracks_df = pd.DataFrame(tracks)

sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

def norm_str(x):
    if x is None:
        return ''
    s = str(x)
    if s.lower() == 'none':
        return ''
    s = s.strip().lower()
    s = re.sub(r"\([^\)]*\)", " ", s)
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = re.sub(r"[^0-9a-z]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def norm_year(y):
    if y is None:
        return None
    s = str(y).strip()
    if s.lower() == 'none' or s == '':
        return None
    m = re.search(r"(19\d{2}|20\d{2})", s)
    if m:
        return int(m.group(1))
    m2 = re.search(r"\b(\d{2})\b", s)
    if m2:
        yy = int(m2.group(1))
        return 1900 + yy if yy >= 30 else 2000 + yy
    return None

tracks_df['title_n'] = tracks_df['title'].map(norm_str)
tracks_df['artist_n'] = tracks_df['artist'].map(norm_str)
tracks_df['album_n'] = tracks_df['album'].map(norm_str)
tracks_df['year_n'] = tracks_df['year'].map(norm_year)

tracks_df['entity_key'] = tracks_df.apply(lambda r: (r['title_n'] + '|' + (r['artist_n'] if r['artist_n'] else r['album_n'])), axis=1)

df = sales_df.merge(tracks_df[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

agg = df.groupby('entity_key', as_index=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    track_ids=('track_id', lambda x: sorted(set(map(int, x))))
)

top_ent = agg.sort_values('total_revenue_usd', ascending=False).head(1).iloc[0]
sub = df[df['entity_key'] == top_ent['entity_key']].copy()

def pick_mode(series):
    s = series.dropna()
    s = s[s.astype(str).str.lower() != 'none']
    if len(s) == 0:
        return None
    return s.mode().iloc[0]

out = {
    'title': pick_mode(sub['title']),
    'artist': pick_mode(sub['artist']),
    'total_revenue_usd': round(float(top_ent['total_revenue_usd']), 2),
    'track_ids_merged': sorted(set(map(int, sub['track_id'].tolist())))
}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_rYFKqIMu85ZZdvEKSFBVP03k': 'file_storage/call_rYFKqIMu85ZZdvEKSFBVP03k.json', 'var_call_dy8zIFVrdydMaNFB6ks0erVJ': 'file_storage/call_dy8zIFVrdydMaNFB6ks0erVJ.json'}

exec(code, env_args)
