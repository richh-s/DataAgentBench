code = """import json, pandas as pd, re

def load_result(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

sales_by_track = load_result(var_call_fvYH6tNQh7IowQu3j61Dwpps)
tracks = load_result(var_call_gSiKydDee8Rme6zzgi6iEujP)

df_sales = pd.DataFrame(sales_by_track)
df_tracks = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    df_sales[c] = df_sales[c].astype(int)
    df_tracks[c] = df_tracks[c].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

# entity resolution: canonical key from title/artist (+album) using normalization

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.lower().strip()
    # remove parenthetical / bracketed content
    s = re.sub(r'\([^)]*\)', ' ', s)
    s = re.sub(r'\[[^]]*\]', ' ', s)
    # replace separators with space
    s = re.sub(r"[-_/,:;]+", ' ', s)
    # collapse whitespace and remove non-alnum
    s = re.sub(r"[^a-z0-9\s]", '', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# If title embeds artist like 'Artist - Title', try to split when artist missing

def extract_artist_title(title, artist):
    t = '' if title is None or str(title).lower()=='none' else str(title)
    a = '' if artist is None or str(artist).lower()=='none' else str(artist)
    if a.strip() != '':
        return a, t
    # pattern 'X - Y'
    if ' - ' in t:
        left, right = t.split(' - ', 1)
        # heuristic: left is artist if it's not like track numbering
        if len(left) <= 60 and len(right) > 0:
            return left.strip(), right.strip()
    return a, t

artists=[]
titles=[]
for _, r in df_tracks.iterrows():
    a,t = extract_artist_title(r.get('title'), r.get('artist'))
    artists.append(a)
    titles.append(t)

df_tracks['artist_fixed']=artists
df_tracks['title_fixed']=titles

# create canonical key; include album only if present to reduce collisions
album_norm = df_tracks['album'].map(norm)
title_norm = df_tracks['title_fixed'].map(norm)
artist_norm = df_tracks['artist_fixed'].map(norm)

def make_key(tn, an, aln):
    base = tn + '|' + an
    if aln:
        base = base + '|' + aln
    return base

keys=[]
for tn, an, aln in zip(title_norm, artist_norm, album_norm):
    keys.append(make_key(tn, an, aln))

df_tracks['entity_key']=keys

# join sales with tracks, then aggregate by entity_key
joined = df_sales.merge(df_tracks[['track_id','entity_key','title_fixed','artist_fixed','album','year']], on='track_id', how='left')
agg = joined.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
agg = agg.sort_values('total_revenue_usd', ascending=False)

best_key = agg.iloc[0]['entity_key']
best_rev = float(agg.iloc[0]['total_revenue_usd'])

# pick a representative track for that entity_key: highest revenue track_id within entity
rep = joined[joined['entity_key']==best_key].sort_values('total_revenue_usd', ascending=False).iloc[0]
result = {
    'title': None if pd.isna(rep['title_fixed']) else str(rep['title_fixed']),
    'artist': None if pd.isna(rep['artist_fixed']) else str(rep['artist_fixed']),
    'album': None if pd.isna(rep['album']) else str(rep['album']),
    'year': None if pd.isna(rep['year']) else str(rep['year']),
    'total_revenue_usd': round(best_rev, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fvYH6tNQh7IowQu3j61Dwpps': 'file_storage/call_fvYH6tNQh7IowQu3j61Dwpps.json', 'var_call_gSiKydDee8Rme6zzgi6iEujP': 'file_storage/call_gSiKydDee8Rme6zzgi6iEujP.json'}

exec(code, env_args)
