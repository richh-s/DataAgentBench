code = """import json, pandas as pd, re

# Load track attributes
tracks_src = var_call_Ot2tX98ibtgzHRU4kYkTtSdL
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

# Load top track revenues (per track_id)
top_src = var_call_Vac8insFi8bEb0OrUOmN3oiB
if isinstance(top_src, str):
    with open(top_src, 'r', encoding='utf-8') as f:
        top = json.load(f)
else:
    top = top_src

df_tracks = pd.DataFrame(tracks)
df_top = pd.DataFrame(top)

# Normalize
for c in ['track_id']:
    df_tracks[c] = pd.to_numeric(df_tracks[c], errors='coerce')
    df_top[c] = pd.to_numeric(df_top[c], errors='coerce')

df_top['total_revenue_usd'] = pd.to_numeric(df_top['total_revenue_usd'], errors='coerce')

# entity resolution key: title+artist (fallback to parsing artist from title when artist is None)

def norm_text(s):
    if s is None or (isinstance(s, float) and pd.isna(s)):
        return ''
    s = str(s).strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = s.replace('’', "'")
    return s

def split_artist_title(title):
    # pattern: "Artist - Title" frequently used
    if title is None:
        return ('', '')
    t = str(title)
    if ' - ' in t:
        a, rest = t.split(' - ', 1)
        return (a.strip(), rest.strip())
    return ('', t.strip())

def canon_row(row):
    artist = row.get('artist', None)
    title = row.get('title', None)
    album = row.get('album', None)
    a = None if artist in (None, 'None') else artist
    if a is None:
        a2, t2 = split_artist_title(title)
        if a2:
            a = a2
            title = t2
    return {
        'track_id': row['track_id'],
        'title_c': norm_text(title),
        'artist_c': norm_text(a),
        'album_c': norm_text(None if album in (None, 'None') else album),
        'title_raw': None if title in (None, 'None') else title,
        'artist_raw': None if (a in (None, 'None')) else a,
        'album_raw': None if album in (None, 'None') else album,
        'year_raw': row.get('year', None)
    }

canon = pd.DataFrame([canon_row(r) for r in df_tracks.to_dict('records')])

# Merge top revenues with canonicalized tracks
m = df_top.merge(canon, on='track_id', how='left')

# Create entity key. Prefer title+artist; if artist missing, include album to reduce collisions.
# If artist empty, key on title+album.

def make_key(r):
    if r['artist_c']:
        return f"t:{r['title_c']}|a:{r['artist_c']}"
    else:
        return f"t:{r['title_c']}|al:{r['album_c']}"

m['entity_key'] = m.apply(make_key, axis=1)

# Aggregate revenues by entity
agg = m.groupby('entity_key', as_index=False).agg(total_revenue_usd=('total_revenue_usd','sum'))
agg = agg.sort_values('total_revenue_usd', ascending=False)

top_entity = agg.iloc[0].to_dict()

# Find representative metadata: pick highest-revenue track_id within the entity
m_ent = m[m['entity_key'] == top_entity['entity_key']].sort_values('total_revenue_usd', ascending=False)
rep = m_ent.iloc[0]

answer = {
    'title': rep['title_raw'],
    'artist': rep['artist_raw'],
    'album': rep['album_raw'],
    'total_revenue_usd': round(float(top_entity['total_revenue_usd']), 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_Vac8insFi8bEb0OrUOmN3oiB': 'file_storage/call_Vac8insFi8bEb0OrUOmN3oiB.json', 'var_call_Ot2tX98ibtgzHRU4kYkTtSdL': 'file_storage/call_Ot2tX98ibtgzHRU4kYkTtSdL.json', 'var_call_XB7kbmm7VlFPfeNSj6eCF4lG': [{'n_sales': '58049', 'n_tracks': '19375'}], 'var_call_SgBv7QBSNeqitaWSx2iSJ6kD': [{'n_tracks_rows': '19375', 'n_track_ids': '19375'}]}

exec(code, env_args)
