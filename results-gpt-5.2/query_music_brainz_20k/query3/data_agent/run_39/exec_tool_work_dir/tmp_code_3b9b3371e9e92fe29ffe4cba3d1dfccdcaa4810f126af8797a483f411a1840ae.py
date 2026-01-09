code = """import json, pandas as pd

# load full results
sales_path = var_call_TkvEN2aCkWkKY1on1fqDZGnO
tracks_path = var_call_xOVbykd8Tc6PGE75e3qdA0xj

with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)
with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

dfs = pd.DataFrame(sales)
dft = pd.DataFrame(tracks)

# types
for c in ['track_id']:
    dfs[c] = pd.to_numeric(dfs[c], errors='coerce')
    dft[c] = pd.to_numeric(dft[c], errors='coerce')
dfs['total_revenue_usd'] = pd.to_numeric(dfs['total_revenue_usd'], errors='coerce').fillna(0.0)

# basic normalization for entity resolution
import re

def norm_str(x):
    if x is None:
        return ''
    x = str(x)
    if x.lower() == 'none':
        return ''
    x = x.lower().strip()
    x = re.sub(r"\s+", " ", x)
    x = re.sub(r"[\u2018\u2019\u201c\u201d]", "'", x)
    x = re.sub(r"[^a-z0-9' ]+", " ", x)
    x = re.sub(r"\s+", " ", x).strip()
    return x

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
    # handle 2-digit years like '05, 75
    m2 = re.search(r"\b(\d{2})\b", y)
    if m2:
        yy = int(m2.group(1))
        # heuristic: 00-25 => 2000s else 1900s
        return str(2000+yy) if yy <= 25 else str(1900+yy)
    return ''

dft['n_title'] = dft['title'].map(norm_str)
dft['n_artist'] = dft['artist'].map(norm_str)
dft['n_album'] = dft['album'].map(norm_str)
dft['n_year'] = dft['year'].map(norm_year)

# build entity key; if artist missing, fall back to title+album+year
# also strip leading patterns like 'artist - title' found in title when artist is None

def split_artist_title(row):
    t = '' if row['title'] is None else str(row['title'])
    if row['artist'] is None or str(row['artist']).lower()=='none' or str(row['artist']).strip()=='':
        if ' - ' in t:
            left, right = t.split(' - ', 1)
            # treat left as artist and right as title if left looks like name
            if len(left) <= 60 and len(right) > 0:
                return norm_str(right), norm_str(left)
    return row['n_title'], row['n_artist']

split = dft.apply(split_artist_title, axis=1, result_type='expand')
dft['k_title'] = split[0]
dft['k_artist'] = split[1]

# entity key
def make_key(r):
    parts = [r['k_title']]
    if r['k_artist']:
        parts.append(r['k_artist'])
    if r['n_album']:
        parts.append(r['n_album'])
    if r['n_year']:
        parts.append(r['n_year'])
    return ' | '.join(parts)

dft['entity_key'] = dft.apply(make_key, axis=1)

# join revenues to tracks, then aggregate by entity
m = dfs.merge(dft[['track_id','entity_key','title','artist','album','year']], on='track_id', how='left')
agg = m.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
agg = agg.sort_values('total_revenue_usd', ascending=False)

top_key = agg.iloc[0]['entity_key']
top_rev = float(agg.iloc[0]['total_revenue_usd'])

# pick a representative track record for display (highest revenue within entity)
rep = m[m['entity_key']==top_key].copy()
rep = rep.sort_values('total_revenue_usd', ascending=False)
rep_row = rep.iloc[0]

answer = {
    'title': None if pd.isna(rep_row.get('title')) else str(rep_row.get('title')),
    'artist': None if pd.isna(rep_row.get('artist')) else str(rep_row.get('artist')),
    'album': None if pd.isna(rep_row.get('album')) else str(rep_row.get('album')),
    'year': None if pd.isna(rep_row.get('year')) else str(rep_row.get('year')),
    'total_revenue_usd': round(top_rev, 2),
    'entity_key': top_key
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_TkvEN2aCkWkKY1on1fqDZGnO': 'file_storage/call_TkvEN2aCkWkKY1on1fqDZGnO.json', 'var_call_xOVbykd8Tc6PGE75e3qdA0xj': 'file_storage/call_xOVbykd8Tc6PGE75e3qdA0xj.json'}

exec(code, env_args)
