code = """import json, pandas as pd, re

# Load sales totals
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

# normalize types
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
    # remove bracketed/parenthetical content and common separators, punctuation
    s = re.sub(r"\([^\)]*\)", " ", s)
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = re.sub(r"[-_/\\,:;\.!\?\"\'`]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def clean_title(title):
    s = norm_str(title)
    # if embedded ' - ' pattern originally, often 'artist - title'. keep last segment if multiple tokens suggest that
    # heuristic: if original had ' - ' and artist field empty, take substring after last hyphen
    return s

def norm_year(y):
    if y is None:
        return None
    s = str(y).strip()
    if s.lower() == 'none' or s == '':
        return None
    # extract 4-digit year if present
    m = re.search(r"(19\d{2}|20\d{2})", s)
    if m:
        return int(m.group(1))
    # 2-digit year
    m2 = re.search(r"\b(\d{2})\b", s)
    if m2:
        yy = int(m2.group(1))
        # guess century
        return 1900+yy if yy >= 30 else 2000+yy
    return None

tracks_df['title_n'] = tracks_df['title'].map(clean_title)
tracks_df['artist_n'] = tracks_df['artist'].map(norm_str)
tracks_df['album_n'] = tracks_df['album'].map(norm_str)
tracks_df['year_n'] = tracks_df['year'].map(norm_year)

# Build entity key: title+artist primarily; fallback to title+album when artist missing
tracks_df['entity_key'] = tracks_df.apply(lambda r: (r['title_n'] + '|' + (r['artist_n'] if r['artist_n'] else r['album_n'])), axis=1)

# Join sales totals to track metadata
df = sales_df.merge(tracks_df[['track_id','title','artist','album','year','title_n','artist_n','album_n','year_n','entity_key']], on='track_id', how='left')

# Aggregate by resolved entity key
agg = df.groupby('entity_key', as_index=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    track_ids=('track_id', lambda x: sorted(set(map(int, x)))),
    titles=('title', lambda x: sorted({t for t in x if t not in [None,'None']} )[:5]),
    artists=('artist', lambda x: sorted({a for a in x if a not in [None,'None']} )[:5]),
    albums=('album', lambda x: sorted({a for a in x if a not in [None,'None']} )[:5])
)

# pick top entity
top = agg.sort_values('total_revenue_usd', ascending=False).head(1).to_dict(orient='records')[0]

# Choose representative title/artist (most common among those track_ids)
top_ids = set(top['track_ids'])
sub = df[df['track_id'].isin(top_ids)].copy()
sub['title_clean'] = sub['title'].where(~sub['title'].isin([None,'None']), None)
sub['artist_clean'] = sub['artist'].where(~sub['artist'].isin([None,'None']), None)

rep_title = sub['title_clean'].mode(dropna=True)
rep_title = rep_title.iloc[0] if len(rep_title)>0 else (top['titles'][0] if top['titles'] else None)
rep_artist = sub['artist_clean'].mode(dropna=True)
rep_artist = rep_artist.iloc[0] if len(rep_artist)>0 else (top['artists'][0] if top['artists'] else None)

out = {
    'title': rep_title,
    'artist': rep_artist,
    'total_revenue_usd': round(float(top['total_revenue_usd']), 2),
    'track_ids_merged': top['track_ids']
}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_rYFKqIMu85ZZdvEKSFBVP03k': 'file_storage/call_rYFKqIMu85ZZdvEKSFBVP03k.json', 'var_call_dy8zIFVrdydMaNFB6ks0erVJ': 'file_storage/call_dy8zIFVrdydMaNFB6ks0erVJ.json'}

exec(code, env_args)
