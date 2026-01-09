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

# Simple entity resolution key: normalized title + normalized artist (fallback album)

def norm_str(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none' or s.strip() == '':
        return ''
    return re.sub(r'\s+', ' ', s.lower().strip())

def norm_title(s):
    s = norm_str(s)
    # remove leading 'something - '
    s = re.sub(r'^[^-]{1,40}\s-\s', '', s)
    return s

tracks['n_title'] = tracks['title'].map(norm_title)
tracks['n_artist'] = tracks['artist'].map(norm_str)
tracks['n_album'] = tracks['album'].map(norm_str)
tracks['entity_key'] = tracks.apply(lambda r: (r['n_title'] + '|' + (r['n_artist'] if r['n_artist'] else r['n_album'])), axis=1)

st = sales_by_track.merge(tracks[['track_id','title','artist','album','entity_key']], on='track_id', how='left')

grp = st.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index().sort_values('total_revenue_usd', ascending=False)

top_key = grp.iloc[0]['entity_key']
top_total = float(grp.iloc[0]['total_revenue_usd'])

rep = st[st['entity_key']==top_key].iloc[0]

answer = {
    'title': rep['title'],
    'artist': None if str(rep['artist'])=='None' else rep['artist'],
    'album': None if str(rep['album'])=='None' else rep['album'],
    'total_revenue_usd': round(top_total, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_Bh6o9xyvFYt9CAbH7p3IrHkS': 'file_storage/call_Bh6o9xyvFYt9CAbH7p3IrHkS.json', 'var_call_AwoLIqBQSiCYveajJZTkNM2p': 'file_storage/call_AwoLIqBQSiCYveajJZTkNM2p.json'}

exec(code, env_args)
