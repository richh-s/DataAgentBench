code = """import json
import pandas as pd
import re

# Load data from storage files
with open(var_call_Qq3uYCvFVq9SjPBO6u0xeXHr, 'r') as f:
    tracks = json.load(f)
with open(var_call_hjWhgU2NMfuN49EmmucEhqrK, 'r') as f:
    sales = json.load(f)

# Create DataFrames
df_t = pd.DataFrame(tracks)
df_s = pd.DataFrame(sales)

# Convert types
df_t['track_id'] = df_t['track_id'].astype(int)
# Normalize missing-like strings to empty
for col in ['title','artist','album','year']:
    if col in df_t.columns:
        df_t[col] = df_t[col].fillna('').astype(str)

# sales types
df_s['track_id'] = df_s['track_id'].astype(int)
# revenue may be stored as strings
df_s['revenue_usd'] = df_s['revenue_usd'].astype(float)

# Normalization helpers
_nonmeaning = set(['none','[none]','[unknown]','unknown','nan',''])

def clean_text(s):
    if s is None:
        return ''
    s = str(s).strip()
    low = s.lower()
    if low in _nonmeaning:
        return ''
    # Remove parenthetical and bracketed content
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # If title looks like "Artist - Title" and artist field missing, take the part after last '-'
    s = s.strip()
    # Replace ampersand
    s = s.replace('&', 'and')
    # Remove common remix/live indicators after hyphen
    # We'll split on ' - ' and if left part contains no space (or is all caps) it might be artist; but safer: take last part
    parts = [p.strip() for p in s.split(' - ')]
    if len(parts) > 1:
        s = parts[-1]
    # Remove punctuation except spaces and alphanum
    s = re.sub(r"[^0-9a-zA-Z \']+", " ", s)
    # collapse spaces
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

# Normalize album and year similarly but simpler

def clean_simple(s):
    if s is None:
        return ''
    s = str(s).strip()
    if s.lower() in _nonmeaning:
        return ''
    s = re.sub(r"[^0-9a-zA-Z ]+", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

# Build canonical key for each track_id
keys = {}
for _, row in df_t.iterrows():
    tid = int(row['track_id'])
    title_norm = clean_text(row.get('title', ''))
    artist_norm = clean_text(row.get('artist', ''))
    album_norm = clean_simple(row.get('album', ''))
    year_norm = clean_simple(row.get('year', ''))
    if title_norm == '':
        # if no title, fallback to combination of other fields
        composite = ' '.join([artist_norm, album_norm, year_norm]).strip()
        key = composite if composite else f'unknown_{tid}'
    else:
        if artist_norm:
            key = title_norm + '||' + artist_norm
        elif album_norm:
            key = title_norm + '||' + album_norm
        elif year_norm:
            key = title_norm + '||' + year_norm
        else:
            key = title_norm
    keys[tid] = key

# Map keys to sales
df_s['canonical_key'] = df_s['track_id'].map(keys)

# Some sales may reference track_ids not in tracks; drop those
df_s = df_s[df_s['canonical_key'].notna()]

# Aggregate revenue by canonical_key
agg = df_s.groupby('canonical_key', dropna=False)['revenue_usd'].sum().reset_index()
# Find max
if agg.shape[0] == 0:
    result = {'title': None, 'artist': None, 'total_revenue_usd': 0.0, 'track_ids': []}
else:
    max_row = agg.loc[agg['revenue_usd'].idxmax()]
    top_key = max_row['canonical_key']
    total_revenue = float(max_row['revenue_usd'])
    # Find all track_ids for this key
    track_ids = [int(tid) for tid, k in keys.items() if k == top_key]
    # From tracks, pick representative title and artist (most common non-empty)
    subset = df_t[df_t['track_id'].isin(track_ids)]
    # choose artist: most common non-empty cleaned artist
    def first_nonempty(series):
        for v in series:
            vv = str(v).strip()
            if vv.lower() not in _nonmeaning and vv != '':
                return vv
        return ''
    rep_title = first_nonempty(subset['title'].tolist())
    rep_artist = first_nonempty(subset['artist'].tolist())
    # If rep_title still empty, try to parse from key
    if not rep_title:
        rep_title = top_key.split('||')[0]
    if not rep_artist:
        parts = top_key.split('||')
        rep_artist = parts[1] if len(parts) > 1 else ''
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(total_revenue, 2),
        'track_ids': track_ids,
        'canonical_key': top_key
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Qq3uYCvFVq9SjPBO6u0xeXHr': 'file_storage/call_Qq3uYCvFVq9SjPBO6u0xeXHr.json', 'var_call_hjWhgU2NMfuN49EmmucEhqrK': 'file_storage/call_hjWhgU2NMfuN49EmmucEhqrK.json'}

exec(code, env_args)
