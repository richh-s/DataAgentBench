code = """import json
import pandas as pd
import unicodedata
import re

# Load data from storage files
with open(var_call_16yYkmcPA7ZfI7daqCqWZQBX, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_eHkOMtdguz2RHb3VQOJ4XEHG, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# Create dataframes
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Clean tracks columns
for col in ['title','artist','album','year','language','source_track_id']:
    if col in df_tracks.columns:
        df_tracks[col] = df_tracks[col].fillna('').astype(str)
        df_tracks[col] = df_tracks[col].replace({'None':'', '[unknown]':''})

# Clean sales dataframe
# Remove commas and convert to float
if 'revenue_usd' in df_sales.columns:
    df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(str).str.replace(',', '').astype(float)

# Ensure track_id types align as strings
if 'track_id' in df_tracks.columns:
    df_tracks['track_id'] = df_tracks['track_id'].astype(str)
if 'track_id' in df_sales.columns:
    df_sales['track_id'] = df_sales['track_id'].astype(str)

# Heuristic: if artist empty but title contains ' - ' or ' – ' or ':' or '|' split
def split_artist_title(row):
    title = row.get('title','')
    artist = row.get('artist','')
    if (not artist or artist.strip()=='' ) and isinstance(title, str):
        parts = re.split(r"\s[-–:\|]\s", title, maxsplit=1)
        if len(parts)==2:
            row['artist'] = parts[0].strip()
            row['title'] = parts[1].strip()
    return row

if not df_tracks.empty:
    df_tracks = df_tracks.apply(split_artist_title, axis=1)

# Normalization function: lowercase, remove accents, remove punctuation except spaces
def normalize_text(s):
    if not isinstance(s, str):
        s = str(s)
    s = s.strip().lower()
    s = unicodedata.normalize('NFKD', s)
    s = ''.join([c for c in s if not unicodedata.combining(c)])
    # replace non-alphanumeric characters with space
    s = re.sub(r'[^0-9a-z ]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

for col in ['title','artist','album','year']:
    if col in df_tracks.columns:
        df_tracks[col + '_norm'] = df_tracks[col].fillna('').astype(str).apply(normalize_text)

# Build canonical key: prefer title+artist; if artist missing, include album and year
def make_key(row):
    t = row.get('title_norm','')
    a = row.get('artist_norm','')
    alb = row.get('album_norm','')
    year = row.get('year_norm','')
    if a:
        return f"{t}||{a}"
    else:
        return f"{t}||{alb}||{year}"

if not df_tracks.empty:
    df_tracks['canonical_key'] = df_tracks.apply(make_key, axis=1)
else:
    df_tracks['canonical_key'] = []

# Map track_id to canonical_key
track_to_key = {}
if 'track_id' in df_tracks.columns and 'canonical_key' in df_tracks.columns:
    track_to_key = df_tracks.set_index('track_id')['canonical_key'].to_dict()

# Map sales track_id to canonical_key
def map_key(tid):
    return track_to_key.get(tid, f"missing_track||{tid}")

if not df_sales.empty:
    df_sales['canonical_key'] = df_sales['track_id'].astype(str).apply(map_key)
else:
    df_sales['canonical_key'] = []

# Aggregate revenue by canonical_key
if not df_sales.empty:
    agg = df_sales.groupby('canonical_key', as_index=False)['revenue_usd'].sum()
else:
    agg = pd.DataFrame(columns=['canonical_key','revenue_usd'])

# Get track ids per canonical key
tracks_grouped = {}
if not df_tracks.empty:
    tracks_grouped = df_tracks.groupby('canonical_key')['track_id'].apply(list).to_dict()

# Ensure sales-only keys have track ids
for k in agg['canonical_key']:
    if k not in tracks_grouped:
        if k.startswith('missing_track||'):
            tracks_grouped[k] = [k.split('||',1)[1]]
        else:
            tracks_grouped[k] = []

# Find max revenue
agg_sorted = agg.sort_values('revenue_usd', ascending=False).reset_index(drop=True)
if agg_sorted.shape[0] == 0:
    result = {'title': None, 'artist': None, 'total_revenue_usd': 0.0, 'track_ids': []}
else:
    top = agg_sorted.iloc[0]
    top_key = top['canonical_key']
    total_rev = float(top['revenue_usd'])
    tids = tracks_grouped.get(top_key, [])
    rep_title = ''
    rep_artist = ''
    if tids:
        sub = df_tracks[df_tracks['track_id'].isin(tids)]
        titles = sub['title'].replace('', pd.NA).dropna()
        artists = sub['artist'].replace('', pd.NA).dropna()
        if not titles.empty:
            rep_title = titles.mode().iloc[0]
        if not artists.empty:
            rep_artist = artists.mode().iloc[0]
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(total_rev,2),
        'track_ids': tids
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_16yYkmcPA7ZfI7daqCqWZQBX': 'file_storage/call_16yYkmcPA7ZfI7daqCqWZQBX.json', 'var_call_eHkOMtdguz2RHb3VQOJ4XEHG': 'file_storage/call_eHkOMtdguz2RHb3VQOJ4XEHG.json'}

exec(code, env_args)
