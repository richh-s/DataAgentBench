code = """import json, pandas as pd, re

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

sales_by_track = pd.DataFrame(load_records(var_call_Bh6o9xyvFYt9CAbH7p3IrHkS))
tracks = pd.DataFrame(load_records(var_call_AwoLIqBQSiCYveajJZTkNM2p))

sales_by_track['track_id'] = sales_by_track['track_id'].astype(int)
sales_by_track['total_revenue_usd'] = sales_by_track['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# normalization helpers

def norm_str(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none' or s.strip() == '':
        return ''
    s = s.lower().strip()
    s = re.sub(r'\s+', ' ', s)
    return s

def norm_title(s):
    s = norm_str(s)
    # strip common 'artist - title' prefix
    s = re.sub(r'^[^-]{1,40}\s-\s', '', s)
    # remove parenthetical/bracketed descriptors
    s = re.sub(r'\([^)]*\)', '', s)
    s = re.sub(r'\[[^\]]*\]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def norm_year(y):
    y = norm_str(y)
    y = y.strip("'\"")
    if y == '':
        return ''
    m = re.search(r'(19\d{2}|20\d{2})', y)
    return m.group(1) if m else ''

tracks['n_title'] = tracks['title'].map(norm_title)
tracks['n_artist'] = tracks['artist'].map(norm_str)
tracks['n_album'] = tracks['album'].map(norm_str)
tracks['n_year'] = tracks['year'].map(norm_year)

tracks['entity_key'] = tracks.apply(lambda r: '|'.join([
    r['n_title'],
    r['n_artist'] if r['n_artist'] else r['n_album'],
    r['n_year']
]), axis=1)

st = sales_by_track.merge(tracks[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

grp = st.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
grp = grp.sort_values('total_revenue_usd', ascending=False)

top_key = grp.iloc[0]['entity_key']
top_total = float(grp.iloc[0]['total_revenue_usd'])

top_rows = st[st['entity_key'] == top_key].copy()

# choose representative row: prefer non-empty artist and shorter title

def rep_rank(r):
    artist_ok = 0 if norm_str(r['artist']) in ['', '[unknown]'] else 1
    album_ok = 1 if norm_str(r['album']) else 0
    title_len = len(str(r['title'])) if r['title'] is not None else 10**9
    return (-artist_ok, -album_ok, title_len)

rep = top_rows.assign(_rank=top_rows.apply(rep_rank, axis=1)).sort_values('_rank').iloc[0]

answer = {
    'title': rep['title'],
    'artist': None if str(rep['artist']) == 'None' else rep['artist'],
    'album': None if str(rep['album']) == 'None' else rep['album'],
    'total_revenue_usd': round(top_total, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_Bh6o9xyvFYt9CAbH7p3IrHkS': 'file_storage/call_Bh6o9xyvFYt9CAbH7p3IrHkS.json', 'var_call_AwoLIqBQSiCYveajJZTkNM2p': 'file_storage/call_AwoLIqBQSiCYveajJZTkNM2p.json'}

exec(code, env_args)
