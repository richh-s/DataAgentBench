code = """import json, pandas as pd, re

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

sales = load_records(var_call_7GkqSENslPJAjJzCjB1HtXOk)
tracks = load_records(var_call_hVzBh01BZIiBdQP0BsvEEcba)

dfs = pd.DataFrame(sales)
dft = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    dfs[c] = pd.to_numeric(dfs[c], errors='coerce')
    dft[c] = pd.to_numeric(dft[c], errors='coerce')
dfs['total_revenue_usd'] = pd.to_numeric(dfs['total_revenue_usd'], errors='coerce').fillna(0.0)

# normalize helpers
stop = set(['the','a','an','and','feat','featuring','ft','remaster','remastered','live','demo','mix','edit','version'])

def norm_text(s):
    if s is None or (isinstance(s,float) and pd.isna(s)):
        return ''
    s = str(s).lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"\[.*?\]", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    toks = [t for t in s.split() if t and t not in stop]
    return ' '.join(toks)

def norm_year(y):
    if y is None or (isinstance(y,float) and pd.isna(y)):
        return None
    s = str(y).strip()
    m = re.search(r"(\d{4})", s)
    if m:
        return int(m.group(1))
    m = re.search(r"(\d{2})", s)
    if m:
        yy = int(m.group(1))
        # heuristic: 00-25 => 2000+, else 1900+
        return 2000+yy if yy <= 25 else 1900+yy
    return None

# build canonical song key: title+artist with cleanup; fallback artist parsed from title prefix 'Artist - Title'
artist = dft['artist'].fillna('')
title = dft['title'].fillna('')

parsed_artist = []
parsed_title = []
for a,t in zip(artist.tolist(), title.tolist()):
    a2 = a
    t2 = t
    if (a2 is None) or (str(a2).lower()=='none') or (str(a2).strip()==""):
        if isinstance(t2,str) and ' - ' in t2:
            left,right = t2.split(' - ',1)
            if len(left) <= 60:
                a2 = left
                t2 = right
    parsed_artist.append(None if a2 is None else str(a2))
    parsed_title.append(None if t2 is None else str(t2))

dft['artist2'] = parsed_artist
nd = dft.copy()
nd['title2'] = parsed_title
nd['n_title'] = nd['title2'].apply(norm_text)
nd['n_artist'] = nd['artist2'].apply(norm_text)
nd['year_n'] = nd['year'].apply(norm_year)

nd['song_key'] = nd['n_title'] + '|' + nd['n_artist']
# if artist missing after parse, key only title
nd.loc[nd['n_artist'].eq(''), 'song_key'] = nd.loc[nd['n_artist'].eq(''), 'n_title'] + '|'

# join sales to tracks, aggregate by song_key
m = dfs.merge(nd[['track_id','song_key','title2','artist2']], on='track_id', how='left')
agg = m.groupby('song_key', dropna=False)['total_revenue_usd'].sum().reset_index()
agg = agg.sort_values('total_revenue_usd', ascending=False)

best_key = agg.iloc[0]['song_key']
best_rev = float(agg.iloc[0]['total_revenue_usd'])

# pick a representative title/artist for best_key (most frequent / non-empty)
rep = m[m['song_key']==best_key].copy()
# choose first non-null title/artist
rep_title = rep['title2'].dropna().astype(str)
rep_artist = rep['artist2'].dropna().astype(str)
rep_title = rep_title[rep_title.str.lower()!='none']
rep_artist = rep_artist[rep_artist.str.lower()!='none']

title_out = rep_title.iloc[0] if len(rep_title)>0 else ''
artist_out = rep_artist.iloc[0] if len(rep_artist)>0 else ''

out = {
    'title': title_out,
    'artist': artist_out if artist_out.strip()!='' else None,
    'total_revenue_usd': round(best_rev, 2)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7GkqSENslPJAjJzCjB1HtXOk': 'file_storage/call_7GkqSENslPJAjJzCjB1HtXOk.json', 'var_call_hVzBh01BZIiBdQP0BsvEEcba': 'file_storage/call_hVzBh01BZIiBdQP0BsvEEcba.json'}

exec(code, env_args)
