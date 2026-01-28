code = """import json, pandas as pd

# Load sales totals per track_id
sales_src = var_call_DUvF87Mw4SnXBBbpX3PvBPRa
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

tracks_src = var_call_DsvHfe6XvcZL49Un9Zr2Lmrv
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

dfs = pd.DataFrame(sales)
dft = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    dfs[c] = pd.to_numeric(dfs[c], errors='coerce')
    dft[c] = pd.to_numeric(dft[c], errors='coerce')
dfs['total_revenue_usd'] = pd.to_numeric(dfs['total_revenue_usd'], errors='coerce').fillna(0.0)

# join to track attributes
df = dfs.merge(dft, on='track_id', how='left')

def norm_str(x):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return ''
    s = str(x).strip().lower()
    if s in {'none','null','[unknown]','unknown',''}:
        return ''
    return ' '.join(s.split())

def norm_year(y):
    y = norm_str(y)
    if not y:
        return ''
    # keep digits only
    digits = ''.join(ch for ch in y if ch.isdigit())
    if len(digits) == 4:
        return digits
    if len(digits) == 2:
        # assume 19xx for >=50 else 20xx? dataset seems 70s/90s etc; map 00-24 -> 2000s else 1900s
        v = int(digits)
        return str(2000+v) if v <= 24 else str(1900+v)
    return ''

# Build entity key: title/artist/album normalized; year optional
for col in ['title','artist','album','language','year']:
    if col not in df.columns:
        df[col] = None

df['n_title'] = df['title'].map(norm_str)
df['n_artist'] = df['artist'].map(norm_str)
df['n_album'] = df['album'].map(norm_str)
df['n_year'] = df['year'].map(norm_year)

# Some rows have artist embedded in title like "Artist - Track"; try split when artist missing
mask = (df['n_artist'] == '') & df['n_title'].str.contains(' - ')
parts = df.loc[mask, 'n_title'].str.split(' - ', n=1, expand=True)
df.loc[mask, 'n_artist'] = parts[0]
df.loc[mask, 'n_title'] = parts[1]

# entity key without year (robust) but include when present to reduce collisions
# We'll make two-level grouping: primarily by (title, artist, album), fallback album blank ok.
# Use album if present else blank.

df['entity_key'] = df['n_title'] + '||' + df['n_artist'] + '||' + df['n_album']

# Aggregate revenue across duplicates
agg = df.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
agg = agg.sort_values('total_revenue_usd', ascending=False)

top = agg.iloc[0]
key = top['entity_key']

# pick a representative row for reporting
cand = df[df['entity_key']==key].copy()
# prefer non-empty artist/title/album
cand['score'] = (cand['n_title']!='').astype(int) + (cand['n_artist']!='').astype(int) + (cand['n_album']!='').astype(int) + (cand['n_year']!='').astype(int)
rep = cand.sort_values(['score','total_revenue_usd'], ascending=[False, False]).iloc[0]

answer = {
    'title': rep.get('title'),
    'artist': rep.get('artist'),
    'album': rep.get('album'),
    'total_revenue_usd': float(top['total_revenue_usd'])
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_DUvF87Mw4SnXBBbpX3PvBPRa': 'file_storage/call_DUvF87Mw4SnXBBbpX3PvBPRa.json', 'var_call_DsvHfe6XvcZL49Un9Zr2Lmrv': 'file_storage/call_DsvHfe6XvcZL49Un9Zr2Lmrv.json'}

exec(code, env_args)
