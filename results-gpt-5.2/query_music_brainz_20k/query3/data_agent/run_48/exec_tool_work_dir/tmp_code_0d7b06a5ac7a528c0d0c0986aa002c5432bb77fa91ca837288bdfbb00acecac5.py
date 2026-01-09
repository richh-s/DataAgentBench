code = """import json, pandas as pd

# load sales totals per track_id
p_sales = var_call_rM1JkljrGEfhZ2MiINMCiiXl
if isinstance(p_sales, str):
    with open(p_sales, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = p_sales

p_tracks = var_call_TmpeRs8l1oA7AyUA70FZfWbQ
if isinstance(p_tracks, str):
    with open(p_tracks, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = p_tracks

df_sales = pd.DataFrame(sales)
df_tracks = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    df_sales[c] = pd.to_numeric(df_sales[c], errors='coerce')
    df_tracks[c] = pd.to_numeric(df_tracks[c], errors='coerce')
df_sales['total_revenue_usd'] = pd.to_numeric(df_sales['total_revenue_usd'], errors='coerce').fillna(0.0)

# basic normalization for entity resolution
import re

def norm_str(x):
    if x is None:
        return ''
    x = str(x).strip().lower()
    if x in ['none', 'null', '[unknown]']:
        return ''
    x = re.sub(r"\s+", " ", x)
    return x

def norm_title(t):
    t = norm_str(t)
    # remove leading track number patterns like '012-' '007' etc
    t = re.sub(r'^\d{1,3}[-_\s]+', '', t)
    t = re.sub(r'^\d{2,3}$', '', t)
    # remove artist prefix in title like 'artist - title'
    if ' - ' in t:
        parts = t.split(' - ', 1)
        # if artist field is missing often encoded in title; keep rhs as title
        t = parts[1].strip()
    # remove live/date/location annotations in parentheses that vary a lot
    t = re.sub(r'\(live\)', '', t)
    t = re.sub(r'\s*\(.*?\)$', '', t)  # trailing parens
    t = re.sub(r"[^a-z0-9]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def norm_artist(a, title):
    a0 = norm_str(a)
    if a0:
        a0 = re.sub(r"[^a-z0-9]+", " ", a0)
        a0 = re.sub(r"\s+", " ", a0).strip()
        return a0
    # try infer from title prefix 'artist - title'
    tt = norm_str(title)
    if ' - ' in tt:
        left = tt.split(' - ', 1)[0].strip()
        left = re.sub(r"[^a-z0-9]+", " ", left)
        left = re.sub(r"\s+", " ", left).strip()
        return left
    return ''

def norm_album(alb):
    alb = norm_str(alb)
    alb = re.sub(r'\(\d{4}\)$', '', alb).strip()
    alb = re.sub(r"[^a-z0-9]+", " ", alb)
    alb = re.sub(r"\s+", " ", alb).strip()
    return alb

def norm_year(y):
    y = norm_str(y)
    y = y.replace("'", "")
    m = re.search(r'(19\d{2}|20\d{2})', y)
    return m.group(1) if m else ''

df_tracks['n_title'] = df_tracks['title'].apply(norm_title)
df_tracks['n_artist'] = [norm_artist(a,t) for a,t in zip(df_tracks['artist'], df_tracks['title'])]
df_tracks['n_album'] = df_tracks['album'].apply(norm_album)
df_tracks['n_year'] = df_tracks['year'].apply(norm_year)

# define entity key. prefer (title, artist) else (title, album)
# This is heuristic; adequate to group duplicates.

def make_key(row):
    t = row['n_title']
    a = row['n_artist']
    alb = row['n_album']
    y = row['n_year']
    if t == '':
        return ''
    if a != '':
        return f"ta|{t}|{a}|{y}"
    if alb != '':
        return f"tl|{t}|{alb}|{y}"
    return f"t|{t}|{y}"

df_tracks['entity_key'] = df_tracks.apply(make_key, axis=1)

# join sales to tracks then aggregate by entity_key
j = df_sales.merge(df_tracks[['track_id','entity_key','title','artist','album','year']], on='track_id', how='left')
# if entity_key missing, fallback to unique per track_id
j['entity_key'] = j.apply(lambda r: r['entity_key'] if isinstance(r['entity_key'], str) and r['entity_key']!='' else f"track_id|{int(r['track_id'])}" , axis=1)

agg = j.groupby('entity_key', as_index=False)['total_revenue_usd'].sum()
# pick representative metadata: highest revenue track_id within entity
rep = j.sort_values(['entity_key','total_revenue_usd'], ascending=[True,False]).drop_duplicates('entity_key')
res = agg.merge(rep[['entity_key','track_id','title','artist','album','year']], on='entity_key', how='left')
res = res.sort_values('total_revenue_usd', ascending=False)

top = res.iloc[0].to_dict()
# format revenue
ans = {
    'title': None if pd.isna(top.get('title')) else str(top.get('title')),
    'artist': None if pd.isna(top.get('artist')) else str(top.get('artist')),
    'album': None if pd.isna(top.get('album')) else str(top.get('album')),
    'year': None if pd.isna(top.get('year')) else str(top.get('year')),
    'total_revenue_usd': float(top['total_revenue_usd'])
}

print('__RESULT__:')
print(json.dumps(ans, ensure_ascii=False))"""

env_args = {'var_call_rM1JkljrGEfhZ2MiINMCiiXl': 'file_storage/call_rM1JkljrGEfhZ2MiINMCiiXl.json', 'var_call_TmpeRs8l1oA7AyUA70FZfWbQ': 'file_storage/call_TmpeRs8l1oA7AyUA70FZfWbQ.json'}

exec(code, env_args)
