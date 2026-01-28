code = """import json
import pandas as pd
import unicodedata
import re

# Load raw data
with open(var_call_SkrOIAlwXbrOAfb6RAv6HqY1, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_jpXV3hYazw6nDd2Nk7trJYC7, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# DataFrames
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Ensure types
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Normalizer
def normalize_text(s):
    if s is None:
        return ''
    s = str(s).strip()
    if s.lower() in ('none','nan','null',''):
        return ''
    s = s.lower()
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Merge
df_merged = df_sales.merge(df_tracks, on='track_id', how='left', suffixes=('_sale','_track'))

# Entity key
def make_key(row):
    t = normalize_text(row.get('title', ''))
    a = normalize_text(row.get('artist', ''))
    alb = normalize_text(row.get('album', ''))
    yr = normalize_text(row.get('year', ''))
    if a:
        return f"{t}|{a}"
    return f"{t}|{alb}|{yr}"

df_merged['entity_key'] = df_merged.apply(make_key, axis=1)

# Aggregate
agg = df_merged.groupby('entity_key').agg(
    total_revenue_usd=('revenue_usd', 'sum'),
    sales_count=('sale_id', 'count'),
    track_ids=('track_id', lambda x: sorted(set(x.astype(str))))
).reset_index()

# Find top
agg_sorted = agg.sort_values('total_revenue_usd', ascending=False).reset_index(drop=True)
if agg_sorted.empty:
    out = {"title": None, "artist": None, "total_revenue_usd": 0.0}
else:
    top = agg_sorted.iloc[0]
    track_ids = top['track_ids']
    # Find representative title/artist from df_tracks for these track_ids
    subset = df_tracks[df_tracks['track_id'].isin(track_ids)][['track_id','title','artist']]
    # pick most common non-empty title and artist
    def pick_most_common(series):
        vals = series.dropna().astype(str).str.strip()
        vals = vals[~vals.str.lower().isin(['none',''])]
        if vals.empty:
            return ''
        return vals.mode().iloc[0]
    rep_title = pick_most_common(subset['title'])
    rep_artist = pick_most_common(subset['artist'])
    out = {
        'title': rep_title if rep_title!='' else None,
        'artist': rep_artist if rep_artist!='' else None,
        'total_revenue_usd': round(float(top['total_revenue_usd']),2),
        'sales_count': int(top['sales_count']),
        'track_ids': track_ids
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SkrOIAlwXbrOAfb6RAv6HqY1': 'file_storage/call_SkrOIAlwXbrOAfb6RAv6HqY1.json', 'var_call_jpXV3hYazw6nDd2Nk7trJYC7': 'file_storage/call_jpXV3hYazw6nDd2Nk7trJYC7.json', 'var_call_2xtCUr9o1BtL8AWWppeCAXUR': {'title': '', 'artist': 'Песняры', 'total_revenue_usd': 9443.69, 'sales_count': 33, 'track_ids': ['10617', '13726', '14964', '1759', '18230', '202', '2556', '258', '3131', '4979'], 'entity_key': '||2006'}}

exec(code, env_args)
