code = """import json, pandas as pd

# load full results (may be file paths)
def load(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

sales_by_track = load(var_call_cOlkicCWSeQl9rCvHpkDLQyv)
tracks = load(var_call_P9jjKISSKQPNjUZ956TYwHvD)

df_sales = pd.DataFrame(sales_by_track)
df_tracks = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    df_sales[c] = pd.to_numeric(df_sales[c], errors='coerce')
    df_tracks[c] = pd.to_numeric(df_tracks[c], errors='coerce')
df_sales['total_revenue_usd'] = pd.to_numeric(df_sales['total_revenue_usd'], errors='coerce')

# merge sales revenue onto track attributes
m = df_sales.merge(df_tracks, on='track_id', how='left')

# canonicalization for entity resolution
import re

def norm_str(x):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return ''
    s = str(x).strip().lower()
    if s in {'none','null','nan','[unknown]','unknown',''}:
        return ''
    s = re.sub(r'\s+', ' ', s)
    return s

def norm_title(t):
    s = norm_str(t)
    # remove leading track number patterns like '012-' '007 ' etc
    s = re.sub(r'^\s*\d{1,3}\s*[-:]\s*', '', s)
    # remove artist prefix in title like 'artist - title'
    # if artist missing, still split on ' - ' first occurrence
    if ' - ' in s:
        parts = s.split(' - ', 1)
        # keep right side if left looks like a name (contains letters and spaces)
        if len(parts[0])>0 and re.search(r'[a-z]', parts[0]):
            s = parts[1]
    # remove parenthetical/live/location suffixes after ' - ' patterns already handled
    s = re.sub(r'\s*\(.*?\)\s*', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def norm_year(y):
    s = norm_str(y)
    s = s.replace("'", "")
    # extract 4-digit year if present
    m = re.search(r'(19\d{2}|20\d{2}|18\d{2})', s)
    if m:
        return m.group(1)
    # 2-digit year -> map 00-25 to 2000-2025 else 1900s
    m2 = re.search(r'\b(\d{2})\b', s)
    if m2:
        yy = int(m2.group(1))
        if yy <= 25:
            return str(2000+yy)
        return str(1900+yy)
    return ''

def norm_album(a):
    s = norm_str(a)
    s = re.sub(r'\s*\(\d{4}[^)]*\)\s*', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

m['t_title'] = m['title'].map(norm_title)
m['t_artist'] = m['artist'].map(norm_str)
m['t_album'] = m['album'].map(norm_album)
m['t_year'] = m['year'].map(norm_year)

# entity key: primarily title+artist; fallback title+album when artist missing
m['key1'] = m['t_title'] + '||' + m['t_artist']
m['key2'] = m['t_title'] + '||' + m['t_album']

# choose key: if artist present use key1 else key2
m['entity_key'] = m.apply(lambda r: r['key1'] if r['t_artist']!='' else r['key2'], axis=1)

# aggregate revenue by resolved entity
agg = (m.groupby('entity_key', dropna=False)
         .agg(total_revenue_usd=('total_revenue_usd','sum'),
              title=('title', lambda x: next((v for v in x if isinstance(v,str) and v not in [None,'None'] and str(v).strip()!=''), None)),
              artist=('artist', lambda x: next((v for v in x if isinstance(v,str) and v not in [None,'None'] and str(v).strip()!=''), None)),
              album=('album', lambda x: next((v for v in x if isinstance(v,str) and v not in [None,'None'] and str(v).strip()!=''), None)),
              year=('year', lambda x: next((v for v in x if isinstance(v,str) and v not in [None,'None'] and str(v).strip()!=''), None)),
              track_ids=('track_id', lambda x: sorted(set(int(v) for v in x if pd.notna(v))))
             )
         .reset_index())

best = agg.sort_values('total_revenue_usd', ascending=False).head(1).to_dict(orient='records')[0]

# format revenue to 2 decimals
best_out = {
    'title': best.get('title'),
    'artist': best.get('artist'),
    'album': best.get('album'),
    'year': best.get('year'),
    'total_revenue_usd': float(best['total_revenue_usd']),
    'track_ids_merged': best.get('track_ids')
}

print('__RESULT__:')
print(json.dumps(best_out, ensure_ascii=False))"""

env_args = {'var_call_cOlkicCWSeQl9rCvHpkDLQyv': 'file_storage/call_cOlkicCWSeQl9rCvHpkDLQyv.json', 'var_call_P9jjKISSKQPNjUZ956TYwHvD': 'file_storage/call_P9jjKISSKQPNjUZ956TYwHvD.json'}

exec(code, env_args)
