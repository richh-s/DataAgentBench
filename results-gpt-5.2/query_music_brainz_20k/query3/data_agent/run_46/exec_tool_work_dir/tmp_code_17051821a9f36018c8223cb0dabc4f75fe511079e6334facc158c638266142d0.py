code = """import json, pandas as pd, re

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

sales_by_track = pd.DataFrame(load_records(var_call_Bh6o9xyvFYt9CAbH7p3IrHkS))
tracks = pd.DataFrame(load_records(var_call_AwoLIqBQSiCYveajJZTkNM2p))

# types
sales_by_track['track_id'] = sales_by_track['track_id'].astype(int)
sales_by_track['total_revenue_usd'] = sales_by_track['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# normalize title/artist/album/year for entity resolution

def norm_str(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none' or s.strip() == '':
        return ''
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s

def norm_title(s):
    s = norm_str(s)
    # strip common prefixes like 'artist - title'
    s = re.sub(r"^[^-]{1,40}\s-\s", "", s)
    # remove bracketed/parenthetical descriptors and live/remix annotations crudely
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"\[[^\]]*\]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def norm_year(y):
    y = norm_str(y)
    y = y.strip("'\"")
    if y == '':
        return ''
    # keep 4-digit years only; if 2-digit, leave blank (ambiguous)
    m = re.search(r"(19\d{2}|20\d{2})", y)
    return m.group(1) if m else ''

tracks['n_title'] = tracks['title'].map(norm_title)
tracks['n_artist'] = tracks['artist'].map(norm_str)
tracks['n_album'] = tracks['album'].map(norm_str)
tracks['n_year'] = tracks['year'].map(norm_year)

# entity key: title+artist if present else title+album; include year if available
tracks['entity_key'] = tracks.apply(lambda r: '|'.join([
    r['n_title'],
    r['n_artist'] if r['n_artist'] else r['n_album'],
    r['n_year']
]), axis=1)

# join sales and tracks
st = sales_by_track.merge(tracks[['track_id','title','artist','album','year','entity_key','n_title','n_artist','n_album','n_year']], on='track_id', how='left')

# group by resolved entity
grp = st.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index().sort_values('total_revenue_usd', ascending=False)

top_key = grp.iloc[0]['entity_key']
top_total = float(grp.iloc[0]['total_revenue_usd'])

top_rows = st[st['entity_key']==top_key].copy()
# pick a representative with non-empty artist and cleanest title

def score_row(r):
    return (1 if norm_str(r['artist']) not in ['', 'none', '[unknown]'] else 0,
            1 if norm_str(r['album']) else 0,
            len(str(r['title'])) if r['title'] is not None else 9999)

rep = top_rows.sort_values(by=['artist','album','title'], key=lambda col: col.map(lambda x: 0)).head(1)
# better: compute score explicitly
rep = top_rows.assign(_score=top_rows.apply(score_row, axis=1).map(lambda t: t[0]*1000 + t[1]*10 - t[2]/1000)).sort_values('_score', ascending=False).iloc[0]

answer = {
    'title': rep['title'],
    'artist': None if str(rep['artist'])=='None' else rep['artist'],
    'album': None if str(rep['album'])=='None' else rep['album'],
    'total_revenue_usd': round(top_total, 2)
}

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_Bh6o9xyvFYt9CAbH7p3IrHkS': 'file_storage/call_Bh6o9xyvFYt9CAbH7p3IrHkS.json', 'var_call_AwoLIqBQSiCYveajJZTkNM2p': 'file_storage/call_AwoLIqBQSiCYveajJZTkNM2p.json'}

exec(code, env_args)
