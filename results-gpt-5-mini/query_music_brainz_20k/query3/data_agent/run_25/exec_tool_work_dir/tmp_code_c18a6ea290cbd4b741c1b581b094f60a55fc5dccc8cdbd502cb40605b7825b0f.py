code = """import pandas as pd
import json
import re

# Load data from provided storage file paths
tracks_path = var_call_5Q7HgraK06JCwFWbIBQK9ohq
sales_path = var_call_hQ1UbUfqJypgdCSPGeCPYfJj

df_tracks = pd.read_json(tracks_path)
df_sales = pd.read_json(sales_path)

# Ensure numeric types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Normalization helper
def normalize_text(s):
    if s is None:
        return ""
    s = str(s)
    s = s.lower()
    # remove parenthetical/bracketed content
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # replace non-alphanumeric with space
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()

# Normalize year to digits only (first 4-digit group)
def normalize_year(y):
    if y is None:
        return ""
    s = str(y)
    m = re.search(r"(\d{4})", s)
    if m:
        return m.group(1)
    m2 = re.search(r"(\d{2,4})", s)
    if m2:
        return m2.group(1)
    return ""

# Create normalized fields
for col in ['title','artist','album','year']:
    if col not in df_tracks.columns:
        df_tracks[col] = ""

df_tracks['title_norm'] = df_tracks['title'].apply(normalize_text)
# For artist, if it's 'None' string, treat as empty
df_tracks['artist_norm'] = df_tracks['artist'].replace('None','').apply(normalize_text)
# album may be None or 'None'
df_tracks['album_norm'] = df_tracks['album'].replace('None','').apply(normalize_text)
df_tracks['year_norm'] = df_tracks['year'].apply(normalize_year)

# Build canonical key using title + artist + album + year (but allow missing artist/album)

def canonical_key(row):
    parts = [row['title_norm'], row['artist_norm']]
    # include album only if present
    if row['album_norm']:
        parts.append(row['album_norm'])
    if row['year_norm']:
        parts.append(row['year_norm'])
    return '|'.join(parts)

df_tracks['canon'] = df_tracks.apply(canonical_key, axis=1)

# Map canonical to representative metadata (choose the longest non-empty original title/artist)
canon_groups = {}
for _, r in df_tracks.iterrows():
    c = r['canon']
    if c not in canon_groups:
        canon_groups[c] = {
            'track_ids': [],
            'titles': [],
            'artists': [],
            'albums': [],
            'years': []
        }
    canon_groups[c]['track_ids'].append(str(r['track_id']))
    if r['title'] and r['title'] != 'None':
        canon_groups[c]['titles'].append(r['title'])
    if r['artist'] and r['artist'] != 'None':
        canon_groups[c]['artists'].append(r['artist'])
    if r['album'] and r['album'] != 'None':
        canon_groups[c]['albums'].append(r['album'])
    if r['year'] and r['year'] != 'None':
        canon_groups[c]['years'].append(r['year'])

# For each canonical entity compute total revenue by summing sales of all track_ids in it
results = []
for c, info in canon_groups.items():
    ids = info['track_ids']
    # sales track_id may be string; ensure comparison as strings
    mask = df_sales['track_id'].astype(str).isin(ids)
    total_revenue = float(df_sales.loc[mask, 'revenue_usd'].sum())
    # choose representative title/artist
    rep_title = ''
    rep_artist = ''
    if info['titles']:
        # choose most common or longest
        rep_title = max(info['titles'], key=lambda x: len(x))
    if info['artists']:
        rep_artist = max(info['artists'], key=lambda x: len(x))
    results.append({
        'canon': c,
        'rep_title': rep_title,
        'rep_artist': rep_artist,
        'track_ids': ids,
        'total_revenue_usd': round(total_revenue, 2)
    })

# Find max revenue entity
if results:
    best = max(results, key=lambda x: x['total_revenue_usd'])
else:
    best = None

output = best if best is not None else {}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_5Q7HgraK06JCwFWbIBQK9ohq': 'file_storage/call_5Q7HgraK06JCwFWbIBQK9ohq.json', 'var_call_hQ1UbUfqJypgdCSPGeCPYfJj': 'file_storage/call_hQ1UbUfqJypgdCSPGeCPYfJj.json'}

exec(code, env_args)
