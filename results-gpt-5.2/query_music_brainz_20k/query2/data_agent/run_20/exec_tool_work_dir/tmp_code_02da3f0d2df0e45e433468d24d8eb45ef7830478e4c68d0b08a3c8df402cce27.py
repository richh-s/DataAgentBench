code = """import json, pandas as pd, re

def norm(s):
    if s is None:
        return ''
    s=str(s).strip().lower()
    if s in ('none','null','nan'):
        return ''
    return s

def norm_artist(a):
    a=norm(a)
    a=re.sub(r'[^a-z0-9 ]+','',a)
    a=re.sub(r'\s+',' ',a).strip()
    # accept common misspelling brucqe vs bruce
    a=a.replace('brucqe','bruce')
    return a

def norm_title(t):
    t=norm(t)
    t=re.sub(r'[^a-z0-9 ]+',' ',t)
    t=re.sub(r'\s+',' ',t).strip()
    # remove track number prefixes like 011
    t=re.sub(r'^\d+\s+','',t)
    return t

candidates = pd.DataFrame(var_call_uIEFxXYXzwXjaFO1bNMeOzBz)
if not candidates.empty:
    candidates['artist_n']=candidates['artist'].apply(norm_artist)
    candidates['title_n']=candidates['title'].apply(norm_title)
    # keep those matching street hype and bruce maginnis after normalization
    matched = candidates[(candidates['title_n'].str.contains('street hype')) & (candidates['artist_n'].eq('bruce maginnis'))]
    track_ids = matched['track_id'].astype(int).tolist()
else:
    track_ids=[]

print('__RESULT__:')
print(json.dumps({'resolved_track_ids': track_ids}))"""

env_args = {'var_call_G6XL2uNLXftEOgQMZnjL9rwb': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_uIEFxXYXzwXjaFO1bNMeOzBz': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_call_sgLIQIJWeM8z3U29eSNgz5YL': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}]}

exec(code, env_args)
