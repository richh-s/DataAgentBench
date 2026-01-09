code = """import json, pandas as pd, re

# load sales totals per track_id
sales_src = var_call_GWizbNKax2gMcFXSkwzKQUwv
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

tracks_src = var_call_YcRYPW2guztRvJpNEeR2mVvt
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

sales_df = pd.DataFrame(sales)
tracks_df = pd.DataFrame(tracks)

# types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# helper normalization
stop_words = set(['the','a','an','and','feat','ft','featuring','live','remix','edit','version','radio'])

def norm_text(x):
    if x is None:
        return ''
    x = str(x)
    if x.lower() == 'none':
        return ''
    x = x.lower()
    x = re.sub(r"\([^\)]*\)", " ", x)  # remove parenthetical
    x = re.sub(r"\[[^\]]*\]", " ", x)
    x = re.sub(r"[^a-z0-9]+", " ", x)
    toks = [t for t in x.split() if t and t not in stop_words]
    return ' '.join(toks)

def extract_year(y):
    if y is None:
        return None
    s = str(y)
    if s.lower()=='none' or s.strip()=='' :
        return None
    m = re.search(r"(19\d{2}|20\d{2})", s)
    if m:
        return int(m.group(1))
    # 2-digit year
    m2 = re.search(r"\b(\d{2})\b", s)
    if m2:
        yy = int(m2.group(1))
        return 2000+yy if yy<=26 else 1900+yy
    return None

tracks_df['title_n'] = tracks_df['title'].apply(norm_text)
tracks_df['artist_n'] = tracks_df['artist'].apply(norm_text)
tracks_df['album_n'] = tracks_df['album'].apply(norm_text)
tracks_df['year_i'] = tracks_df['year'].apply(extract_year)

# entity key: prefer (title, artist) if artist present else (title, album)
tracks_df['entity_key'] = tracks_df.apply(
    lambda r: ('ta', r['title_n'], r['artist_n']) if r['artist_n'] else ('tl', r['title_n'], r['album_n']),
    axis=1
)

# join sales onto tracks
df = sales_df.merge(tracks_df[['track_id','title','artist','album','year','title_n','artist_n','album_n','year_i','entity_key']], on='track_id', how='left')

# aggregate by entity_key
agg = df.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    track_ids=('track_id', lambda x: sorted(set(map(int,x)))),
    rep_title=('title', lambda x: next((v for v in x if v not in [None,'None'] and str(v).strip()!=''), None)),
    rep_artist=('artist', lambda x: next((v for v in x if v not in [None,'None'] and str(v).strip()!=''), None)),
    rep_album=('album', lambda x: next((v for v in x if v not in [None,'None'] and str(v).strip()!=''), None)),
    rep_year=('year_i','max')
).reset_index()

best = agg.sort_values('total_revenue_usd', ascending=False).head(1).iloc[0]

ans = {
    'title': best['rep_title'],
    'artist': best['rep_artist'],
    'album': best['rep_album'],
    'year': None if pd.isna(best['rep_year']) else int(best['rep_year']),
    'total_revenue_usd': round(float(best['total_revenue_usd']), 2),
    'track_ids_merged': best['track_ids']
}

print('__RESULT__:')
print(json.dumps(ans, ensure_ascii=False))"""

env_args = {'var_call_GWizbNKax2gMcFXSkwzKQUwv': 'file_storage/call_GWizbNKax2gMcFXSkwzKQUwv.json', 'var_call_YcRYPW2guztRvJpNEeR2mVvt': 'file_storage/call_YcRYPW2guztRvJpNEeR2mVvt.json'}

exec(code, env_args)
