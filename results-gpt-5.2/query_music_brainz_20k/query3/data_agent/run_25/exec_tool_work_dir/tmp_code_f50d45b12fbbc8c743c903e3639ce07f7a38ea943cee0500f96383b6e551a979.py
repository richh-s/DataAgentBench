code = """import json, pandas as pd, re

def load_tool_result(var):
    # if var is a path string to json file
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

sales_by_track = load_tool_result(var_call_gHyKaP3bXtwRZqOGUdbox58X)
tracks = load_tool_result(var_call_DipWTOrnih4S2CyMfJaHM3QF)

sales_df = pd.DataFrame(sales_by_track)
tracks_df = pd.DataFrame(tracks)

# coerce types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# join to get attributes
df = sales_df.merge(tracks_df, on='track_id', how='left')

def norm_text(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() in ['none', 'null', 'nan']:
        return ''
    s = s.lower().strip()
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r"[^a-z0-9 '\-]", '', s)
    return s

def norm_year(y):
    if y is None:
        return None
    y = str(y).strip()
    if y.lower() in ['none','null','nan','']:
        return None
    # extract 4-digit year
    m = re.search(r'(19\d{2}|20\d{2})', y)
    if m:
        return int(m.group(1))
    # 2-digit year heuristic
    m2 = re.search(r'\b(\d{2})\b', y)
    if m2:
        yy = int(m2.group(1))
        return 1900+yy if yy >= 50 else 2000+yy
    return None

# normalize fields
for col in ['title','artist','album']:
    df[col] = df[col].apply(norm_text)
df['year_n'] = df['year'].apply(norm_year)

# entity key: title+artist+album; if artist missing, try parse from title prefix "artist - title"

def split_artist_title(title, artist):
    if artist:
        return artist, title
    # parse patterns like "artist - song" possibly with en dash
    m = re.match(r"^(.{2,60})\s*[-–]\s*(.{1,200})$", title)
    if m:
        a = m.group(1).strip()
        t = m.group(2).strip()
        # avoid cases where left looks like track number
        if not re.match(r'^\d+$', a):
            return a, t
    return artist, title

parsed = df.apply(lambda r: split_artist_title(r['title'], r['artist']), axis=1, result_type='expand')
df['artist_p'] = parsed[0].fillna('')
df['title_p'] = parsed[1].fillna('')

# build key

def make_key(r):
    # include album if present
    parts = [r['title_p'], r['artist_p']]
    if r['album']:
        parts.append(r['album'])
    return '||'.join([p for p in parts if p])

df['entity_key'] = df.apply(make_key, axis=1)

# aggregate revenue by entity
agg = df.groupby('entity_key', dropna=False).agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    track_ids=('track_id', lambda x: sorted(set(map(int,x)))),
    title=('title_p','first'),
    artist=('artist_p','first'),
    album=('album','first')
).reset_index()

# pick max
best = agg.sort_values('total_revenue_usd', ascending=False).head(1).to_dict(orient='records')[0]

# format answer components
best_title = best.get('title','').strip() or '(unknown title)'
best_artist = best.get('artist','').strip() or '(unknown artist)'
best_album = best.get('album','').strip() or None
best_rev = round(float(best['total_revenue_usd']), 2)

out = {
    'title': best_title,
    'artist': best_artist,
    'album': best_album,
    'total_revenue_usd': best_rev,
    'track_ids_merged': best['track_ids']
}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_gHyKaP3bXtwRZqOGUdbox58X': 'file_storage/call_gHyKaP3bXtwRZqOGUdbox58X.json', 'var_call_DipWTOrnih4S2CyMfJaHM3QF': 'file_storage/call_DipWTOrnih4S2CyMfJaHM3QF.json'}

exec(code, env_args)
