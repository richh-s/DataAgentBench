code = """import json, pandas as pd

tracks_path = var_call_2BApm1b8npyvVwlCFcOC15Wd
sales_path = var_call_qCgo4LOdtzU5zofOFGfR0cKt

with open(tracks_path, 'r') as f:
    tracks = json.load(f)
with open(sales_path, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

import re

def norm_text(s):
    if pd.isna(s):
        return None
    s = str(s).strip().lower()
    if s in ('none', '[unknown]', ''):
        return None
    return ' '.join(s.split())

for col in ['title', 'artist', 'album', 'year']:
    tracks_df[col + '_norm'] = tracks_df[col].apply(norm_text)


def norm_year(y):
    y = norm_text(y)
    if y is None:
        return None
    digits = re.findall(r"\d+", y)
    if not digits:
        return None
    d = digits[-1]
    if len(d) >= 4:
        return d[-4:]
    if len(d) == 2:
        return d
    return d

tracks_df['year_norm'] = tracks_df['year'].apply(norm_year)

keys = []
for idx, row in tracks_df.iterrows():
    t = row['title_norm']
    a = row['artist_norm']
    if not t and not a:
        key = None
    else:
        parts = []
        if t:
            parts.append(t)
        if a:
            parts.append(a)
        if row['album_norm']:
            parts.append(row['album_norm'])
        if row['year_norm']:
            parts.append(row['year_norm'])
        key = ' | '.join(parts)
    keys.append(key)

tracks_df['canonical_key'] = keys
tracks_df.loc[tracks_df['canonical_key'].isna() & tracks_df['title_norm'].notna(), 'canonical_key'] = tracks_df['title_norm']

sales_merged = sales_df.merge(tracks_df[['track_id', 'canonical_key', 'title', 'artist', 'album']], on='track_id', how='left')

agg = sales_merged.groupby('canonical_key', dropna=False)['revenue_usd'].sum().reset_index()

# Filter out rows where canonical_key is NaN to avoid issues
agg_non_null = agg[agg['canonical_key'].notna()].copy()

max_row = agg_non_null.loc[agg_non_null['revenue_usd'].idxmax()]
canonical = max_row['canonical_key']
max_revenue = float(max_row['revenue_usd'])

rep_candidates = tracks_df[tracks_df['canonical_key'] == canonical]
if len(rep_candidates) > 0:
    rep = rep_candidates.iloc[0]
    title = rep['title']
    artist = rep['artist']
    album = rep['album']
else:
    title = None
    artist = None
    album = None

result = {
    'title': title,
    'artist': artist,
    'album': album,
    'canonical_key': canonical,
    'total_revenue_usd': round(max_revenue, 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2BApm1b8npyvVwlCFcOC15Wd': 'file_storage/call_2BApm1b8npyvVwlCFcOC15Wd.json', 'var_call_qCgo4LOdtzU5zofOFGfR0cKt': 'file_storage/call_qCgo4LOdtzU5zofOFGfR0cKt.json'}

exec(code, env_args)
