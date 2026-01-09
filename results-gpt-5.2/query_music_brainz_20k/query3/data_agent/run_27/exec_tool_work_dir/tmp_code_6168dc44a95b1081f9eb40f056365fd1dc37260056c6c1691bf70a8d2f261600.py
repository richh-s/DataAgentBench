code = """import json, pandas as pd, re

# Load full results (they were stored as file paths)

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

sales_by_track = load_maybe_path(var_call_iOhQ46EoAcBklu0xy41F1tds)
tracks = load_maybe_path(var_call_EcfKpRXAXqevgyzvRew3drea)

dfs = pd.DataFrame(sales_by_track)
dft = pd.DataFrame(tracks)

# Normalize
for c in ['track_id']:
    dfs[c] = pd.to_numeric(dfs[c], errors='coerce')
    dft[c] = pd.to_numeric(dft[c], errors='coerce')

dfs['total_revenue_usd'] = pd.to_numeric(dfs['total_revenue_usd'], errors='coerce')

# Basic cleanup for entity resolution keys

def norm_text(x):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return ''
    x = str(x)
    x = x.strip().lower()
    x = re.sub(r'\s+', ' ', x)
    return x

# Attempt to extract artist if embedded in title like "Artist - Title"

def split_title_artist(title, artist):
    t = norm_text(title)
    a = norm_text(artist)
    if (a == '' or a == 'none' or a == '[unknown]') and ' - ' in t:
        left, right = t.split(' - ', 1)
        # if left looks like an artist name and right looks like song title
        if len(left) > 0 and len(right) > 0:
            # keep original capitalization? we'll store normalized
            return right, left
    return t, a

keys = []
for _, row in dft.iterrows():
    title = row.get('title')
    artist = row.get('artist')
    album = row.get('album')
    year = row.get('year')
    nt, na = split_title_artist(title, artist)
    nalb = norm_text(album)
    # normalize year to 4-digit when possible
    y = norm_text(year)
    y4 = ''
    m = re.search(r'(\d{4})', y)
    if m:
        y4 = m.group(1)
    else:
        # handle 2-digit years like '96 or 96
        m2 = re.search(r"(?:^|\D)(\d{2})(?:$|\D)", y)
        if m2:
            yy = int(m2.group(1))
            y4 = str(1900+yy if yy >= 30 else 2000+yy)
    # entity key: title+artist primarily; album as tie-breaker
    key = (nt, na, nalb)
    keys.append(key)

dft = dft.copy()
dft['entity_key'] = keys

# Join sales totals to track metadata
merged = dfs.merge(dft[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

# Aggregate revenue by entity_key to resolve duplicates
agg = (merged.groupby('entity_key', dropna=False)
       .agg(total_revenue_usd=('total_revenue_usd','sum'),
            any_title=('title', lambda s: s.dropna().iloc[0] if len(s.dropna()) else None),
            any_artist=('artist', lambda s: s.dropna().iloc[0] if len(s.dropna()) else None),
            any_album=('album', lambda s: s.dropna().iloc[0] if len(s.dropna()) else None),
            any_year=('year', lambda s: s.dropna().iloc[0] if len(s.dropna()) else None),
            track_ids=('track_id', lambda s: sorted(set([int(x) for x in s.dropna().tolist()]))))
       .reset_index())

# Get max
max_row = agg.sort_values('total_revenue_usd', ascending=False).iloc[0].to_dict()

# Format revenue to 2 decimals
max_row['total_revenue_usd'] = float(max_row['total_revenue_usd'])

out = {
    'title': max_row.get('any_title'),
    'artist': max_row.get('any_artist'),
    'album': max_row.get('any_album'),
    'year': max_row.get('any_year'),
    'total_revenue_usd': round(max_row['total_revenue_usd'], 2),
    'track_ids_combined': max_row.get('track_ids')
}

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_iOhQ46EoAcBklu0xy41F1tds': 'file_storage/call_iOhQ46EoAcBklu0xy41F1tds.json', 'var_call_EcfKpRXAXqevgyzvRew3drea': 'file_storage/call_EcfKpRXAXqevgyzvRew3drea.json'}

exec(code, env_args)
