code = """import json, pandas as pd, re

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

sales_top = pd.DataFrame(load_result(var_call_sZ4ZFbjRg0zXq75PL272js83))
tracks = pd.DataFrame(load_result(var_call_ZlX7KZR1j0NTosuHef7MZ06W))

sales_top['track_id'] = sales_top['track_id'].astype(int)
sales_top['total_revenue_usd'] = sales_top['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# Normalize for entity resolution

def norm_str(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        s = ''
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", "", s)
    return s

def norm_year(y):
    if y is None:
        return ''
    y = str(y).strip().strip("'")
    if y.lower() == 'none' or y=='':
        return ''
    # take first 4-digit year if present
    m = re.search(r"(19\d{2}|20\d{2}|18\d{2})", y)
    if m:
        return m.group(1)
    # two-digit year heuristics
    m2 = re.search(r"\b(\d{2})\b", y)
    if m2:
        yy = int(m2.group(1))
        return str(1900+yy if yy>=30 else 2000+yy)
    return ''

tracks['n_title'] = tracks['title'].apply(norm_str)
tracks['n_artist'] = tracks['artist'].apply(norm_str)
tracks['n_album'] = tracks['album'].apply(norm_str)
tracks['n_year'] = tracks['year'].apply(norm_year)

# join with track attributes for top revenue track_ids
st = sales_top.merge(tracks[['track_id','title','artist','album','year','n_title','n_artist','n_album','n_year']], on='track_id', how='left')

# Build entity key primarily by title+artist; fallback to title only if artist missing
st['entity_key'] = st.apply(lambda r: (r['n_title'] + '||' + r['n_artist']) if r['n_artist'] else (r['n_title'] + '||'), axis=1)

# Aggregate revenue by entity_key among top 200 only (may miss duplicates not in top list)
agg = st.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index().sort_values('total_revenue_usd', ascending=False)

# pick best entity and representative metadata from highest single track within that entity
best_key = agg.iloc[0]['entity_key']
best_rows = st[st['entity_key']==best_key].sort_values('total_revenue_usd', ascending=False)
rep = best_rows.iloc[0]

result = {
    'entity_key': best_key,
    'representative_track_id': int(rep['track_id']) if pd.notna(rep['track_id']) else None,
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'year': rep['year'],
    'total_revenue_usd_top200_only': float(agg.iloc[0]['total_revenue_usd'])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_sZ4ZFbjRg0zXq75PL272js83': 'file_storage/call_sZ4ZFbjRg0zXq75PL272js83.json', 'var_call_ZlX7KZR1j0NTosuHef7MZ06W': 'file_storage/call_ZlX7KZR1j0NTosuHef7MZ06W.json'}

exec(code, env_args)
