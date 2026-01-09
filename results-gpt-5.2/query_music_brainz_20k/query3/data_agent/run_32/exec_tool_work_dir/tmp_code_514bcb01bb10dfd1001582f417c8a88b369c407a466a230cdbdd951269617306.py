code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

sales = pd.DataFrame(load_records(var_call_xqRDbITwz5hYj3XMCXQx1elJ))
tracks = pd.DataFrame(load_records(var_call_lLDJyUvNn9vorJUACyRuYqfz))

sales['track_id'] = sales['track_id'].astype(int)
sales['total_revenue_usd'] = sales['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

def norm_str(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.lower().strip()
    s = re.sub(r"\s*\([^)]*\)", " ", s)
    s = re.sub(r"\s*-\s*.*$", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def norm_year(y):
    if y is None:
        return None
    y = str(y)
    if y.lower() == 'none':
        return None
    m = re.search(r"(19\d{2}|20\d{2})", y)
    if m:
        return int(m.group(1))
    m2 = re.search(r"\b(\d{2})\b", y)
    if m2:
        yy = int(m2.group(1))
        return 1900 + yy if yy >= 40 else 2000 + yy
    return None

tracks['n_title'] = tracks['title'].map(norm_str)
tracks['n_artist'] = tracks['artist'].map(norm_str)
tracks['n_album'] = tracks['album'].map(norm_str)
tracks['n_year'] = tracks['year'].map(norm_year)

def build_key(r):
    t = r['n_title']
    a = r['n_artist']
    alb = r['n_album']
    y = r['n_year']
    part2 = a if a else ('alb:' + alb)
    part3 = str(int(y)) if pd.notnull(y) else ''
    return '|'.join([t, part2, part3])

tracks['entity_key'] = tracks.apply(build_key, axis=1)

st = sales.merge(tracks[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')
agg = st.groupby('entity_key', as_index=False)['total_revenue_usd'].sum().sort_values('total_revenue_usd', ascending=False)

top = agg.iloc[0]
key = top['entity_key']
st_ent = st[st['entity_key'] == key].copy()
rep = st_ent.groupby('track_id', as_index=False)['total_revenue_usd'].sum().sort_values('total_revenue_usd', ascending=False).iloc[0]
rep_track = tracks[tracks['track_id'] == int(rep['track_id'])].iloc[0]

answer = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'year': rep_track['year'],
    'total_revenue_usd': float(top['total_revenue_usd'])
}

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_xqRDbITwz5hYj3XMCXQx1elJ': 'file_storage/call_xqRDbITwz5hYj3XMCXQx1elJ.json', 'var_call_lLDJyUvNn9vorJUACyRuYqfz': 'file_storage/call_lLDJyUvNn9vorJUACyRuYqfz.json'}

exec(code, env_args)
