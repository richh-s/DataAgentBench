code = """import json, pandas as pd

# Load sales totals per track_id
sales_src = var_call_cNaX5SM8vfVktYPzIPqqCFYP
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

tracks_src = var_call_ZUTtDcINw698GKg2naNriqP2
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

sales_df = pd.DataFrame(sales)
tracks_df = pd.DataFrame(tracks)

# types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# join
df = sales_df.merge(tracks_df, on='track_id', how='left')

def norm_str(x):
    if x is None:
        return ''
    x = str(x)
    if x.lower() == 'none' or x.strip() == '':
        return ''
    return ' '.join(x.lower().strip().split())

def norm_year(y):
    if y is None:
        return ''
    y = str(y).strip().strip("'").strip()
    if y.lower() == 'none' or y == '':
        return ''
    # keep digits only
    digits = ''.join(ch for ch in y if ch.isdigit())
    if len(digits) == 4:
        return digits
    if len(digits) == 2:
        # heuristic: 00-25 => 2000-2025 else 1900-1999
        yy = int(digits)
        return str(2000 + yy) if yy <= 25 else str(1900 + yy)
    return digits

# normalize fields for entity resolution key
for col in ['title','artist','album','year']:
    if col not in df.columns:
        df[col] = None

df['n_title'] = df['title'].map(norm_str)
df['n_artist'] = df['artist'].map(norm_str)
df['n_album'] = df['album'].map(norm_str)
df['n_year'] = df['year'].map(norm_year)

# basic cleanup: remove common prefix patterns like "artist - title" inside title when artist missing
# If artist is blank and title has ' - ', split once and treat left as artist candidate
mask = (df['n_artist'] == '') & (df['n_title'].str.contains(' - '))
left = df.loc[mask, 'n_title'].str.split(' - ', n=1, expand=True)[0]
right = df.loc[mask, 'n_title'].str.split(' - ', n=1, expand=True)[1]
# update normalized artist/title for those rows
if mask.any():
    df.loc[mask, 'n_artist'] = left
    df.loc[mask, 'n_title'] = right

# entity key: prioritize title+artist; include album/year when present to reduce false merges
# if album missing, don't include it

def make_key(r):
    parts = [r['n_title'], r['n_artist']]
    if r['n_album']:
        parts.append(r['n_album'])
    if r['n_year']:
        parts.append(r['n_year'])
    return '||'.join(parts)

df['entity_key'] = df.apply(make_key, axis=1)

entity_rev = df.groupby('entity_key', as_index=False)['total_revenue_usd'].sum()
# pick top
best = entity_rev.sort_values('total_revenue_usd', ascending=False).head(1)
best_key = best.iloc[0]['entity_key']
best_rev = float(best.iloc[0]['total_revenue_usd'])

# representative song metadata: choose row within entity with max revenue track_id total (or first non-empty)
ent_rows = df[df['entity_key'] == best_key].copy()
# choose best representative: most complete metadata (non-empty artist/title)
ent_rows['meta_score'] = (ent_rows['n_title'].ne('').astype(int) + ent_rows['n_artist'].ne('').astype(int) + ent_rows['n_album'].ne('').astype(int) + ent_rows['n_year'].ne('').astype(int))
rep = ent_rows.sort_values(['meta_score','total_revenue_usd'], ascending=[False, False]).iloc[0]

answer_obj = {
    'title': None if rep['n_title']=='' else rep['title'],
    'artist': None if rep['n_artist']=='' else rep['artist'],
    'album': None if rep['n_album']=='' else rep['album'],
    'year': None if rep['n_year']=='' else rep['year'],
    'total_revenue_usd': round(best_rev, 2)
}

print('__RESULT__:')
print(json.dumps(answer_obj, ensure_ascii=False))"""

env_args = {'var_call_cNaX5SM8vfVktYPzIPqqCFYP': 'file_storage/call_cNaX5SM8vfVktYPzIPqqCFYP.json', 'var_call_ZUTtDcINw698GKg2naNriqP2': 'file_storage/call_ZUTtDcINw698GKg2naNriqP2.json'}

exec(code, env_args)
