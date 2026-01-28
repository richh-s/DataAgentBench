code = """import json, pandas as pd

# load sales totals by track_id
path_sales = var_call_SPjCrAahIeBnaDMlcqBcuEGI
with open(path_sales, 'r', encoding='utf-8') as f:
    sales_totals = json.load(f)
df_sales = pd.DataFrame(sales_totals)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

# load tracks
path_tracks = var_call_OVuYNllfr1TbhtQBQ74XFLfY
with open(path_tracks, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
df_tracks = pd.DataFrame(tracks)
df_tracks['track_id'] = df_tracks['track_id'].astype(int)

# merge
df = df_sales.merge(df_tracks, on='track_id', how='left')

# entity resolution key (title+artist), cleaning
import re

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() in ['none','[unknown]','unknown','']:
        return ''
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^a-z0-9\s']+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def split_title_artist(title, artist):
    t = '' if title is None else str(title)
    a = '' if artist is None else str(artist)
    if norm(a) != '':
        return t, a
    # if title has pattern 'Artist - Title'
    if ' - ' in t:
        left, right = t.split(' - ', 1)
        if norm(left) != '' and norm(right) != '':
            return right, left
    return t, a

fixed = df.apply(lambda r: split_title_artist(r.get('title'), r.get('artist')), axis=1, result_type='expand')
df['title_fixed'] = fixed[0]
df['artist_fixed'] = fixed[1]

df['entity_key'] = df['title_fixed'].map(norm) + '||' + df['artist_fixed'].map(norm)
# if artist empty, fall back to title only
mask_empty_artist = df['artist_fixed'].map(lambda x: norm(x)== '')
df.loc[mask_empty_artist, 'entity_key'] = df.loc[mask_empty_artist, 'title_fixed'].map(norm)

# aggregate revenue by entity
agg = df.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    any_title=('title_fixed','first'),
    any_artist=('artist_fixed','first')
).reset_index()

best = agg.sort_values('total_revenue_usd', ascending=False).head(1)
res = {
    'title': None if best.iloc[0]['any_title'] is None else str(best.iloc[0]['any_title']),
    'artist': None if best.iloc[0]['any_artist'] is None else str(best.iloc[0]['any_artist']),
    'total_revenue_usd': float(best.iloc[0]['total_revenue_usd'])
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_SPjCrAahIeBnaDMlcqBcuEGI': 'file_storage/call_SPjCrAahIeBnaDMlcqBcuEGI.json', 'var_call_OVuYNllfr1TbhtQBQ74XFLfY': 'file_storage/call_OVuYNllfr1TbhtQBQ74XFLfY.json'}

exec(code, env_args)
