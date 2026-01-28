code = """import json, pandas as pd, re

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

sales_tot = pd.DataFrame(load_records(var_call_XUmPxhntsgzSuzFbjhSOjvdl))
tracks = pd.DataFrame(load_records(var_call_CwXYMEjUMGUVx1zRmWNJn7R7))

sales_tot['track_id'] = sales_tot['track_id'].astype(int)
sales_tot['total_revenue_usd'] = sales_tot['total_revenue_usd'].astype(float)
tracks['track_id'] = tracks['track_id'].astype(int)

# Normalize for entity resolution

def norm_text(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() == 'none':
        return ''
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^a-z0-9\s]", "", s)
    return s

def norm_year(y):
    if y is None:
        return ''
    y = str(y).strip()
    if y.lower() == 'none' or y == '':
        return ''
    # extract 4-digit year if present
    m = re.search(r"(19\d{2}|20\d{2})", y)
    if m:
        return m.group(1)
    # handle 2-digit years like '05, 75 etc. Map 00-25->2000-2025 else->1900s
    m2 = re.search(r"\b(\d{2})\b", y)
    if m2:
        yy = int(m2.group(1))
        return str(2000+yy) if yy <= 25 else str(1900+yy)
    return ''

tracks['n_title'] = tracks['title'].apply(norm_text)
tracks['n_artist'] = tracks['artist'].apply(norm_text)
tracks['n_album'] = tracks['album'].apply(norm_text)
tracks['n_year'] = tracks['year'].apply(norm_year)

# entity key: primarily title+artist; fall back to title+album when artist missing
tracks['entity_key'] = tracks.apply(lambda r: (r['n_title']+'|'+r['n_artist']) if r['n_artist']!='' else (r['n_title']+'|'+r['n_album']), axis=1)

# join sales with track metadata
df = sales_tot.merge(tracks[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

# aggregate across resolved entities
ent = df.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    any_title=('title', lambda s: next((x for x in s if x not in [None,'None']), None)),
    any_artist=('artist', lambda s: next((x for x in s if x not in [None,'None']), None)),
    any_album=('album', lambda s: next((x for x in s if x not in [None,'None']), None)),
    any_year=('year', lambda s: next((x for x in s if x not in [None,'None']), None)),
).reset_index()

ent_sorted = ent.sort_values('total_revenue_usd', ascending=False)
Top = ent_sorted.iloc[0].to_dict()
Top['total_revenue_usd'] = float(Top['total_revenue_usd'])

result = {
    'title': Top.get('any_title'),
    'artist': Top.get('any_artist'),
    'album': Top.get('any_album'),
    'year': Top.get('any_year'),
    'total_revenue_usd': round(Top['total_revenue_usd'], 2)
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_XUmPxhntsgzSuzFbjhSOjvdl': 'file_storage/call_XUmPxhntsgzSuzFbjhSOjvdl.json', 'var_call_CwXYMEjUMGUVx1zRmWNJn7R7': 'file_storage/call_CwXYMEjUMGUVx1zRmWNJn7R7.json'}

exec(code, env_args)
