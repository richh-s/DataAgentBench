code = """import json, pandas as pd

# load full results
sales_path = var_call_YqjDHCNVvs0V8gcSDal0hBnK
tracks_path = var_call_JNfIFX1RmPiVoi0htj6N8OWG

with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)
with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

df_sales = pd.DataFrame(sales)
df_tracks = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    df_sales[c] = pd.to_numeric(df_sales[c], errors='coerce').astype('Int64')
    df_tracks[c] = pd.to_numeric(df_tracks[c], errors='coerce').astype('Int64')
df_sales['total_revenue_usd'] = pd.to_numeric(df_sales['total_revenue_usd'], errors='coerce').fillna(0.0)

# join to get metadata per track_id
df = df_sales.merge(df_tracks[['track_id','title','artist','album','year']], on='track_id', how='left')

def norm_str(x):
    if x is None:
        return ''
    x = str(x)
    if x.lower() == 'none' or x.strip() == '':
        return ''
    return ' '.join(x.strip().lower().split())

def norm_title(t):
    t = norm_str(t)
    # remove leading track numbers like "016-" "011-" etc
    import re
    t = re.sub(r'^\d{1,3}\s*[-._]+\s*', '', t)
    return t

def norm_artist(a):
    a = norm_str(a)
    if a in ['[unknown]','unknown','various artists']:
        return ''
    return a

def norm_album(a):
    return norm_str(a)

def norm_year(y):
    import re
    y = norm_str(y)
    if y == '':
        return ''
    # extract 4-digit year if present
    m = re.search(r'(19\d{2}|20\d{2})', y)
    if m:
        return m.group(1)
    # handle 2-digit years like '05 or 05 -> 2005 if <=25 else 19xx heuristic
    m2 = re.search(r"\b'?([0-9]{2})\b", y)
    if m2:
        yy = int(m2.group(1))
        return str(2000+yy) if yy <= 25 else str(1900+yy)
    return ''

# build entity key
keys = []
for _, r in df.iterrows():
    k = (norm_title(r.get('title')), norm_artist(r.get('artist')), norm_album(r.get('album')), norm_year(r.get('year')))
    keys.append('|'.join(k))

df['entity_key'] = keys

# if artist missing, fall back to title+album+year
mask_missing_artist = df['entity_key'].str.split('|').str[1].eq('')
# create alt key
alt_keys=[]
for _, r in df.iterrows():
    k = (norm_title(r.get('title')), norm_album(r.get('album')), norm_year(r.get('year')))
    alt_keys.append('|'.join(k))
df['alt_key'] = alt_keys

df['final_key'] = df['entity_key']
df.loc[mask_missing_artist, 'final_key'] = df.loc[mask_missing_artist, 'alt_key']

# aggregate revenue by resolved entity
agg = df.groupby('final_key', dropna=False)['total_revenue_usd'].sum().reset_index()
agg = agg.sort_values('total_revenue_usd', ascending=False)

best_key = agg.iloc[0]['final_key']
best_rev = float(agg.iloc[0]['total_revenue_usd'])

# pick a representative track row (highest revenue among track_ids in that entity)
df_best = df[df['final_key'] == best_key].copy()
rep = df_best.sort_values('total_revenue_usd', ascending=False).iloc[0]

answer = {
    'title': None if pd.isna(rep.get('title')) else str(rep.get('title')),
    'artist': None if pd.isna(rep.get('artist')) else str(rep.get('artist')),
    'album': None if pd.isna(rep.get('album')) else str(rep.get('album')),
    'year': None if pd.isna(rep.get('year')) else str(rep.get('year')),
    'total_revenue_usd': round(best_rev, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_YqjDHCNVvs0V8gcSDal0hBnK': 'file_storage/call_YqjDHCNVvs0V8gcSDal0hBnK.json', 'var_call_JNfIFX1RmPiVoi0htj6N8OWG': 'file_storage/call_JNfIFX1RmPiVoi0htj6N8OWG.json'}

exec(code, env_args)
