code = """import json, pandas as pd

def load_result(var):
    if isinstance(var, str):
        # file path
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

sales_totals = load_result(var_call_TOivwrHq1HGu5scosMAzytnz)
tracks = load_result(var_call_BMvlTP0eXD2Yk4WeYubLDl6G)

df_sales = pd.DataFrame(sales_totals)
df_tracks = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    df_sales[c] = pd.to_numeric(df_sales[c])
    df_tracks[c] = pd.to_numeric(df_tracks[c])
df_sales['total_revenue_usd'] = pd.to_numeric(df_sales['total_revenue_usd'])

# canonicalize strings for entity resolution
import re

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.strip().lower()
    s = re.sub(r'\s+', ' ', s)
    # remove common punctuation
    s = re.sub(r"[\'\"\(\)\[\]\{\}\\/\-_:;,.!?]", ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

df_tracks['n_title'] = df_tracks['title'].map(norm)
df_tracks['n_artist'] = df_tracks['artist'].map(norm)
df_tracks['n_album'] = df_tracks['album'].map(norm)

def norm_year(y):
    if y is None:
        return None
    y = str(y).strip()
    if y.lower() == 'none' or y == '':
        return None
    # extract 4-digit year if present
    m = re.search(r'(19\d{2}|20\d{2})', y)
    if m:
        return int(m.group(1))
    # 2-digit year: assume 19xx if >=50 else 20xx
    m = re.search(r'\b(\d{2})\b', y)
    if m:
        yy = int(m.group(1))
        return 1900+yy if yy >= 50 else 2000+yy
    return None

df_tracks['n_year'] = df_tracks['year'].map(norm_year)

# entity key: title+artist primarily; fall back to title+album if artist missing
# choose best representative record: prefer non-empty artist, album, and plausible year

def entity_key(row):
    t = row['n_title']
    a = row['n_artist']
    al = row['n_album']
    if a:
        return f"ta::{t}::{a}"
    if al:
        return f"tl::{t}::{al}"
    return f"t::{t}"

df_tracks['entity_key'] = df_tracks.apply(entity_key, axis=1)

# aggregate revenue by entity_key via track_id mapping
rev_by_tid = df_sales.set_index('track_id')['total_revenue_usd']
df_tracks['revenue'] = df_tracks['track_id'].map(rev_by_tid).fillna(0.0)
entity_rev = df_tracks.groupby('entity_key', as_index=False)['revenue'].sum().sort_values('revenue', ascending=False)

top = entity_rev.iloc[0]
key = top['entity_key']

cands = df_tracks[df_tracks['entity_key']==key].copy()
# scoring for representative
cands['score'] = (
    (cands['n_artist'].str.len()>0).astype(int)*3 +
    (cands['n_album'].str.len()>0).astype(int)*2 +
    (cands['n_year'].notna()).astype(int)*1
)
rep = cands.sort_values(['score','track_id'], ascending=[False, True]).iloc[0]

answer = {
    'title': None if rep['title'] in [None,'None'] else rep['title'],
    'artist': None if rep['artist'] in [None,'None'] else rep['artist'],
    'album': None if rep['album'] in [None,'None'] else rep['album'],
    'year': rep['n_year'],
    'total_revenue_usd': float(top['revenue']),
    'num_track_ids_merged': int(len(cands)),
    'track_ids': [int(x) for x in sorted(cands['track_id'].tolist())]
}

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_TOivwrHq1HGu5scosMAzytnz': 'file_storage/call_TOivwrHq1HGu5scosMAzytnz.json', 'var_call_BMvlTP0eXD2Yk4WeYubLDl6G': 'file_storage/call_BMvlTP0eXD2Yk4WeYubLDl6G.json'}

exec(code, env_args)
