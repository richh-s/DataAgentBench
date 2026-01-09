code = """import json, pandas as pd

# load sales per track_id
sales_src = var_call_R66XYMv85Ax4pyxZLUmhCmG8
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

tracks_src = var_call_RGtmPZxMu8sLUYkT8emnUMqm
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

sdf = pd.DataFrame(sales)
tdf = pd.DataFrame(tracks)

# types
sdf['track_id'] = sdf['track_id'].astype(int)
sdf['total_revenue_usd'] = sdf['total_revenue_usd'].astype(float)
tdf['track_id'] = tdf['track_id'].astype(int)

# entity resolution: canonical key based on normalized title+artist (fallback parsing when artist is missing but title contains ' - ')
import re

def norm_text(x):
    if x is None:
        return ''
    x = str(x).strip().lower()
    if x in ['none', 'null', 'nan']:
        return ''
    x = re.sub(r"\s+", " ", x)
    # remove punctuation except spaces/alphanum
    x = re.sub(r"[^a-z0-9\s]", "", x)
    x = re.sub(r"\s+", " ", x).strip()
    return x

def split_title_artist(row):
    title = row.get('title', None)
    artist = row.get('artist', None)
    nt = norm_text(title)
    na = norm_text(artist)
    # if artist missing and title looks like 'artist - title'
    if na == '' and isinstance(title, str) and ' - ' in title:
        left, right = title.split(' - ', 1)
        nleft, nright = norm_text(left), norm_text(right)
        # heuristic: if left is not too short, treat left as artist
        if len(nleft) >= 2 and len(nright) >= 2:
            na = nleft
            nt = nright
    return pd.Series({'norm_title': nt, 'norm_artist': na})

norms = tdf.apply(split_title_artist, axis=1)
tdf = pd.concat([tdf, norms], axis=1)

# build entity key
# use (title, artist) primarily; if artist missing, include album to reduce collisions
album_norm = tdf['album'].map(norm_text)
tdf['entity_key'] = tdf['norm_title'] + '||' + tdf['norm_artist']
missing_artist = tdf['norm_artist'].eq('')
tdf.loc[missing_artist, 'entity_key'] = tdf.loc[missing_artist, 'norm_title'] + '||' + album_norm[missing_artist]

# join revenue to tracks
j = sdf.merge(tdf[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

# aggregate by resolved entity
agg = j.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    any_title=('title', lambda x: next((v for v in x if v not in [None,'None',''] ), None)),
    any_artist=('artist', lambda x: next((v for v in x if v not in [None,'None',''] ), None)),
    any_album=('album', lambda x: next((v for v in x if v not in [None,'None',''] ), None)),
).reset_index()

best = agg.sort_values(['total_revenue_usd'], ascending=False).head(1)
rec = best.to_dict(orient='records')[0]

# format revenue to 2 decimals
rec['total_revenue_usd'] = round(float(rec['total_revenue_usd']), 2)

print('__RESULT__:')
print(json.dumps(rec, ensure_ascii=False))"""

env_args = {'var_call_R66XYMv85Ax4pyxZLUmhCmG8': 'file_storage/call_R66XYMv85Ax4pyxZLUmhCmG8.json', 'var_call_RGtmPZxMu8sLUYkT8emnUMqm': 'file_storage/call_RGtmPZxMu8sLUYkT8emnUMqm.json'}

exec(code, env_args)
