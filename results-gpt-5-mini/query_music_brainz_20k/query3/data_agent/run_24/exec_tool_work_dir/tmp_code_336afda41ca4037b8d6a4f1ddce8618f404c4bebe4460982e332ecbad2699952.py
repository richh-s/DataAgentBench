code = """import json
import pandas as pd
import unicodedata
import re

# Load data from storage files
with open(var_call_16yYkmcPA7ZfI7daqCqWZQBX, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_eHkOMtdguz2RHb3VQOJ4XEHG, 'r', encoding='utf-8') as f:
    sales = json.load(f)

df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Normalize missing-like strings
missing_vals = set(['None', 'None', '', '   ', None, '[unknown]'])
for col in ['title','artist','album','year','language','source_track_id']:
    if col in df_tracks.columns:
        df_tracks[col] = df_tracks[col].fillna('')
        df_tracks[col] = df_tracks[col].astype(str).replace({'None': '', '[unknown]': '', 'nan': ''})

# Clean sales dataframe
df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(str).str.replace(',', '').astype(float)
# Ensure track_id types align
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

# Heuristic: if artist is empty but title contains " - ", split
def split_artist_title(row):
    title = row['title']
    artist = row['artist']
    if (not artist or artist.strip()=='' ) and isinstance(title, str):
        # split on ' - ' or ' – ' or ':'
        m = re.split(r"\s[-–:\|]\s", title, maxsplit=1)
        if len(m)==2:
            # assign
            row['artist'] = m[0].strip()
            row['title'] = m[1].strip()
    return row

df_tracks = df_tracks.apply(split_artist_title, axis=1)

# Normalization function
def normalize_text(s):
    if not isinstance(s, str):
        s = str(s)
    s = s.strip().lower()
    # remove accents
    s = unicodedata.normalize('NFKD', s)
    s = ''.join([c for c in s if not unicodedata.combining(c)])
    # replace common punctuation with space
    s = re.sub(r"[\"'\\/\(\)\[\]\{\},.!?;:@#$%^&*_+=<>~`\\-]+", ' ', s)
    # collapse multiple spaces
    s = re.sub(r"\s+", ' ', s).strip()
    return s

for col in ['title','artist','album','year']:
    if col in df_tracks.columns:
        df_tracks[col+'_norm'] = df_tracks[col].fillna('').astype(str).apply(normalize_text)

# Build canonical key: prefer title+artist; if artist missing, include album
def make_key(row):
    t = row.get('title_norm', '')
    a = row.get('artist_norm', '')
    alb = row.get('album_norm', '')
    year = row.get('year_norm', '')
    if a:
        return f"{t}||{a}"
    else:
        # if artist missing, include album and year to disambiguate
        return f"{t}||{alb}||{year}"

df_tracks['canonical_key'] = df_tracks.apply(make_key, axis=1)

# Map track_id to canonical_key
track_to_key = df_tracks.set_index('track_id')['canonical_key'].to_dict()

# For sales entries with track_ids not in tracks, set key to track_id itself

def map_key(tid):
    return track_to_key.get(tid, f"missing_track||{tid}")

df_sales['canonical_key'] = df_sales['track_id'].astype(str).apply(map_key)

# Aggregate revenue by canonical_key
agg = df_sales.groupby('canonical_key', as_index=False)['revenue_usd'].sum()

# Get track ids per canonical key
tracks_grouped = df_tracks.groupby('canonical_key')['track_id'].apply(list).to_dict()

# For keys missing in tracks_grouped (sales-only), add track id from sales
for k in agg['canonical_key']:
    if k not in tracks_grouped:
        # extract track id from key suffix if our map used missing_track||{tid}
        if k.startswith('missing_track||'):
            tracks_grouped[k] = [k.split('||',1)[1]]
        else:
            tracks_grouped[k] = []

# Find max revenue
agg_sorted = agg.sort_values('revenue_usd', ascending=False).reset_index(drop=True)
if agg_sorted.shape[0]==0:
    result = {
        'title': None,
        'artist': None,
        'total_revenue_usd': 0.0,
        'track_ids': []
    }
else:
    top = agg_sorted.iloc[0]
    top_key = top['canonical_key']
    total_rev = float(top['revenue_usd'])
    # choose representative title/artist from tracks in that group
    tids = tracks_grouped.get(top_key, [])
    rep_title = None
    rep_artist = None
    if tids:
        sub = df_tracks[df_tracks['track_id'].isin(tids)]
        # choose most common non-empty title and artist
        titles = sub['title'].replace('', pd.NA).dropna()
        artists = sub['artist'].replace('', pd.NA).dropna()
        rep_title = titles.mode().iloc[0] if not titles.empty else ''
        rep_artist = artists.mode().iloc[0] if not artists.empty else ''
    else:
        rep_title = ''
        rep_artist = ''
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(total_rev, 2),
        'track_ids': tids
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_16yYkmcPA7ZfI7daqCqWZQBX': 'file_storage/call_16yYkmcPA7ZfI7daqCqWZQBX.json', 'var_call_eHkOMtdguz2RHb3VQOJ4XEHG': 'file_storage/call_eHkOMtdguz2RHb3VQOJ4XEHG.json'}

exec(code, env_args)
