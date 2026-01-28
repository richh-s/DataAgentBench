code = """import json, pandas as pd, re

# Load aggregated revenue by track_id
path_sales = var_call_9AMfEJA7K1KN9D0luiCWuLAJ
with open(path_sales, 'r', encoding='utf-8') as f:
    sales_agg = json.load(f)

# Load tracks metadata
path_tracks = var_call_ccqcpOtYt6lZDLbTJUqPswi4
with open(path_tracks, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

df_sales = pd.DataFrame(sales_agg)
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

df_tracks = pd.DataFrame(tracks)
df_tracks['track_id'] = df_tracks['track_id'].astype(int)

# Basic cleanup / canonicalization for entity resolution

def norm_str(x):
    if x is None:
        return ''
    s = str(x)
    if s.lower() == 'none':
        s = ''
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s

def norm_title(t):
    s = norm_str(t)
    # Remove leading track numbers like '012-' or '001-' etc
    s = re.sub(r'^[0-9]{1,3}\s*-\s*', '', s)
    # Remove artist prefix like 'artist - title'
    # If title contains ' - ' and artist field missing, keep last segment as title candidate
    parts = [p.strip() for p in s.split(' - ') if p.strip()]
    if len(parts) >= 2:
        s = parts[-1]
    # Remove parenthetical live/remaster tags
    s = re.sub(r'\([^)]*\)', '', s).strip()
    s = re.sub(r"[^a-z0-9' ]+", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

def norm_artist(a, title=None):
    s = norm_str(a)
    if s in ('[unknown]', 'unknown'):
        s = ''
    if not s and title is not None:
        tt = norm_str(title)
        parts = [p.strip() for p in tt.split(' - ') if p.strip()]
        # if looks like 'artist - title'
        if len(parts) >= 2:
            s = parts[0]
    s = re.sub(r"[^a-z0-9' ]+", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

def norm_album(alb):
    s = norm_str(alb)
    s = re.sub(r'\([^)]*\)', '', s).strip()
    s = re.sub(r"[^a-z0-9' ]+", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

def norm_year(y):
    s = norm_str(y)
    if not s:
        return ''
    # extract 4-digit year if present
    m = re.search(r'(19\d{2}|20\d{2})', s)
    if m:
        return m.group(1)
    # handle 2-digit years like '05' or "'89"
    m2 = re.search(r"\b'?([0-9]{2})\b", s)
    if m2:
        yy = int(m2.group(1))
        # heuristic: >=30 => 1900s else 2000s
        return str(1900+yy if yy >= 30 else 2000+yy)
    return ''

df_tracks['title_n'] = df_tracks['title'].apply(norm_title)
df_tracks['artist_n'] = [norm_artist(a,t) for a,t in zip(df_tracks['artist'], df_tracks['title'])]
df_tracks['album_n'] = df_tracks['album'].apply(norm_album)
df_tracks['year_n'] = df_tracks['year'].apply(norm_year)

# Join sales revenue onto track records
m = df_tracks.merge(df_sales, on='track_id', how='inner')

# Entity key: prefer title+artist; if artist missing, use title+album
m['entity_key'] = m.apply(lambda r: (r['title_n']+'||'+r['artist_n']) if r['artist_n'] else (r['title_n']+'||'+r['album_n']), axis=1)

# Aggregate revenue by entity
ent = m.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    track_ids=('track_id', lambda x: sorted(set(map(int,x)))),
    titles=('title', lambda x: sorted({str(v) for v in x if v is not None and str(v).lower()!='none'})),
    artists=('artist', lambda x: sorted({str(v) for v in x if v is not None and str(v).lower()!='none'})),
    albums=('album', lambda x: sorted({str(v) for v in x if v is not None and str(v).lower()!='none'})),
    years=('year', lambda x: sorted({str(v) for v in x if v is not None and str(v).lower()!='none'})),
).reset_index()

# pick top entity
ent_sorted = ent.sort_values('total_revenue_usd', ascending=False).head(1)
row = ent_sorted.iloc[0].to_dict()

# Choose display title/artist
best_title = row['titles'][0] if row['titles'] else ''
best_artist = row['artists'][0] if row['artists'] else ''

out = {
    'title': best_title,
    'artist': best_artist,
    'total_revenue_usd': float(row['total_revenue_usd']),
    'track_ids_merged': row['track_ids']
}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_9AMfEJA7K1KN9D0luiCWuLAJ': 'file_storage/call_9AMfEJA7K1KN9D0luiCWuLAJ.json', 'var_call_ccqcpOtYt6lZDLbTJUqPswi4': 'file_storage/call_ccqcpOtYt6lZDLbTJUqPswi4.json'}

exec(code, env_args)
