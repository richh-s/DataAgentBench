code = """import json
import pandas as pd
import re
import unicodedata

# Load data from storage variables provided by previous query_db calls
# var_call_8RoigwBxI9nMjK0GGzl0L4S9 and var_call_qqFX8aEUMlZuOklVKwp9gg38 are file paths
tracks_path = var_call_8RoigwBxI9nMjK0GGzl0L4S9
sales_path = var_call_qqFX8aEUMlZuOklVKwp9gg38

tracks = pd.read_json(tracks_path)
sales = pd.read_json(sales_path)

# Ensure proper types
tracks['track_id'] = tracks['track_id'].astype(str)
sales['track_id'] = sales['track_id'].astype(str)
sales['revenue_usd'] = pd.to_numeric(sales['revenue_usd'], errors='coerce').fillna(0.0)

# Normalization helpers
REMOVE_WORDS = ['live', 'remix', 'acoustic', 'version', 'feat', 'featuring', 'ft', 'remastered', 'edit', 'demo', 'instrumental']

def strip_parenthetical(s):
    return re.sub(r"\(.*?\)", "", s)

def normalize_string(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ['none', 'nan', 'null', '[unknown]', '']:
        return ''
    # unicode normalize
    s = unicodedata.normalize('NFKD', s)
    # remove parenthetical
    s = strip_parenthetical(s)
    # remove dates like 2008-02-15 or '2008' or quoted year patterns
    s = re.sub(r"\d{4}(-\d{2}-\d{2})?", "", s)
    # replace common separators with space
    s = s.replace('_', ' ').replace('/', ' ').replace('-', ' ')
    # remove punctuation
    s = re.sub(r"[^\w\s]", "", s)
    s = s.lower()
    # remove common words
    tokens = [t for t in s.split() if t not in REMOVE_WORDS]
    s = ' '.join(tokens)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# If title contains ' - ' and artist is missing or invalid, extract artist and title
def fix_title_artist(row):
    title = row.get('title') or ''
    artist = row.get('artist') or ''
    title_str = str(title)
    artist_str = str(artist)
    if (artist_str.strip().lower() in ['', 'none', '[unknown]']) and ' - ' in title_str:
        parts = title_str.split(' - ', 1)
        # Heuristic: left is artist, right is title
        left = parts[0].strip()
        right = parts[1].strip()
        # Only apply if left looks like an artist (contains letters)
        if re.search(r'[A-Za-z]', left):
            return pd.Series({'title': right, 'artist': left})
    return pd.Series({'title': title, 'artist': artist})

fixed = tracks.apply(fix_title_artist, axis=1)
tracks['title_fixed'] = fixed['title']
tracks['artist_fixed'] = fixed['artist']

# Create normalized fields
tracks['title_norm'] = tracks['title_fixed'].apply(normalize_string)
tracks['artist_norm'] = tracks['artist_fixed'].apply(normalize_string)

# Create fingerprint
tracks['fingerprint'] = tracks.apply(lambda r: (r['title_norm'] + '||' + r['artist_norm']).strip('||'), axis=1)

# Build mapping from fingerprint to list of track_ids and choose canonical display title/artist
groups = {}
for _, row in tracks.iterrows():
    fp = row['fingerprint']
    if fp == '':
        continue
    if fp not in groups:
        groups[fp] = {'track_ids': [], 'titles': [], 'artists': []}
    groups[fp]['track_ids'].append(row['track_id'])
    if row['title_fixed'] and str(row['title_fixed']).strip().lower() not in ['none', 'nan']:
        groups[fp]['titles'].append(row['title_fixed'])
    if row['artist_fixed'] and str(row['artist_fixed']).strip().lower() not in ['none', 'nan', '[unknown]']:
        groups[fp]['artists'].append(row['artist_fixed'])

# Sum revenue per track_id
revenue_per_track = sales.groupby('track_id', as_index=False)['revenue_usd'].sum()
revenue_map = dict(zip(revenue_per_track['track_id'], revenue_per_track['revenue_usd']))

# Aggregate revenue per fingerprint
agg = []
for fp, info in groups.items():
    total = 0.0
    for tid in info['track_ids']:
        total += float(revenue_map.get(tid, 0.0))
    if total <= 0:
        continue
    # pick canonical title/artist
    title_canon = info['titles'][0] if info['titles'] else ''
    artist_canon = info['artists'][0] if info['artists'] else ''
    agg.append({'fingerprint': fp, 'title': title_canon, 'artist': artist_canon, 'track_ids': info['track_ids'], 'total_revenue_usd': round(total, 2)})

# If no aggregated groups (unlikely), fallback to per-track revenue
if not agg:
    for tid, rev in revenue_map.items():
        title = tracks.loc[tracks['track_id'] == tid, 'title'].iloc[0] if tid in list(tracks['track_id']) else ''
        artist = tracks.loc[tracks['track_id'] == tid, 'artist'].iloc[0] if tid in list(tracks['track_id']) else ''
        agg.append({'fingerprint': tid, 'title': title, 'artist': artist, 'track_ids': [tid], 'total_revenue_usd': round(float(rev),2)})

# Find max
agg_sorted = sorted(agg, key=lambda x: x['total_revenue_usd'], reverse=True)
best = agg_sorted[0]

result = {
    'title': best['title'],
    'artist': best['artist'],
    'total_revenue_usd': best['total_revenue_usd'],
    'track_ids_merged': best['track_ids']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8RoigwBxI9nMjK0GGzl0L4S9': 'file_storage/call_8RoigwBxI9nMjK0GGzl0L4S9.json', 'var_call_qqFX8aEUMlZuOklVKwp9gg38': 'file_storage/call_qqFX8aEUMlZuOklVKwp9gg38.json'}

exec(code, env_args)
