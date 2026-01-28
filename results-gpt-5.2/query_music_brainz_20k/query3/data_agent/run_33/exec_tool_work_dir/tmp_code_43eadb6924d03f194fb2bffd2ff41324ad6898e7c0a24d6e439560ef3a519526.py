code = """import json, pandas as pd, re

# Load sales totals per track_id
path_sales = var_call_s82FdyDgawQaMtEf0uhrmQpp
with open(path_sales, 'r', encoding='utf-8') as f:
    sales_totals = json.load(f)
df_sales = pd.DataFrame(sales_totals)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

# Load track metadata
path_tracks = var_call_kNCWc5Ixl66wAAqj8IJpDlGC
with open(path_tracks, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
df_tracks = pd.DataFrame(tracks)
df_tracks['track_id'] = df_tracks['track_id'].astype(int)

# Basic normalization for entity resolution
na_vals = {'none','[unknown]','unknown','', '   ', None}

def norm_str(s):
    if s is None:
        return None
    s = str(s)
    if s.strip().lower() in na_vals:
        return None
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[\u2018\u2019]", "'", s)
    return s

def clean_title(t):
    t = norm_str(t)
    if t is None:
        return None
    # remove leading track numbers like '011-' '007-' '016-' etc
    t = re.sub(r"^\s*\d{1,3}\s*[-._ ]+\s*", "", t)
    # drop trailing parenthetical live/mix info for rough entity resolution
    t = re.sub(r"\s*\((?:live|remix|demo|acoustic|radio edit|edit|version)[^)]*\)\s*$", "", t)
    return t.strip()

def parse_year(y):
    y = norm_str(y)
    if y is None:
        return None
    # extract 4-digit year if present
    m = re.search(r"(19\d{2}|20\d{2})", y)
    if m:
        return int(m.group(1))
    # handle two-digit years like '05', '75'
    m2 = re.fullmatch(r"'?\s*(\d{2})\s*", y)
    if m2:
        yy = int(m2.group(1))
        # heuristic: 00-25 -> 2000-2025 else 1900s
        return 2000+yy if yy <= 25 else 1900+yy
    return None

for col, func in [('title', clean_title), ('artist', norm_str), ('album', norm_str)]:
    df_tracks[col+'_n'] = df_tracks[col].map(func)

df_tracks['year_n'] = df_tracks['year'].map(parse_year)

# Build entity key: title+artist; fallback to title only when artist missing.
# Include album when available to reduce collisions.

def make_key(r):
    t,a,al = r['title_n'], r['artist_n'], r['album_n']
    if t is None:
        return None
    if a is None:
        base = f"t:{t}"
    else:
        base = f"t:{t}|a:{a}"
    if al is not None:
        base += f"|al:{al}"
    return base

df_tracks['entity_key'] = df_tracks.apply(make_key, axis=1)

# Join sales totals to tracks and aggregate revenue by entity_key
merged = df_sales.merge(df_tracks[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')
merged = merged[~merged['entity_key'].isna()].copy()
agg = merged.groupby('entity_key', as_index=False)['total_revenue_usd'].sum()

# Pick top entity
top = agg.sort_values('total_revenue_usd', ascending=False).head(1)
entity_key = top.iloc[0]['entity_key']
entity_revenue = float(top.iloc[0]['total_revenue_usd'])

# Choose a representative track row: highest revenue track_id within entity
cand = merged[merged['entity_key']==entity_key].copy().sort_values('total_revenue_usd', ascending=False)
rep = cand.iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'year': rep['year'],
    'total_revenue_usd': round(entity_revenue, 2)
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_s82FdyDgawQaMtEf0uhrmQpp': 'file_storage/call_s82FdyDgawQaMtEf0uhrmQpp.json', 'var_call_kNCWc5Ixl66wAAqj8IJpDlGC': 'file_storage/call_kNCWc5Ixl66wAAqj8IJpDlGC.json'}

exec(code, env_args)
