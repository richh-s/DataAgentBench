code = """import json, re, unicodedata
import pandas as pd

# Load data from previous tool calls (file paths are stored in these variables)
tracks_path = var_call_B8095U14JmURn2eFqBveQ0Y8
sales_path = var_call_rlqCo86aIiX7lg6sTk8pFu95

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure proper types
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0)

# Sum revenue per track_id
rev_per_track = sales_df.groupby('track_id', as_index=False)['revenue_usd'].sum()
rev_per_track.rename(columns={'revenue_usd': 'total_revenue_usd'}, inplace=True)

# Merge with tracks
merged = pd.merge(tracks_df, rev_per_track, on='track_id', how='left')
merged['total_revenue_usd'] = merged['total_revenue_usd'].fillna(0.0)

# Normalization helpers
import unicodedata

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    # replace common tokens
    s = s.lower()
    s = s.replace('&', ' and ')
    # remove content in parentheses
    s = re.sub(r"\(.*?\)", "", s)
    # remove punctuation
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9\s]", ' ', s)
    # collapse whitespace
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# Create normalized fields
merged['norm_title'] = merged['title'].apply(normalize_text)
merged['norm_artist'] = merged['artist'].apply(normalize_text)
merged['norm_album'] = merged['album'].apply(normalize_text)

# Build entity key: prefer title+artist, but if artist missing use title+album
def entity_key(row):
    title = row['norm_title']
    artist = row['norm_artist']
    album = row['norm_album']
    if artist and artist not in ('none', '[unknown]') and artist.strip():
        key = f"{title}||{artist}"
    elif album and album.strip() and album not in ('none',''):
        key = f"{title}||album::{album}"
    else:
        key = f"{title}||artist::{artist}"
    return key

merged['entity_key'] = merged.apply(entity_key, axis=1)

# Group by entity_key and aggregate total revenue and collect track_ids
grouped = merged.groupby('entity_key').agg(
    total_revenue_usd=('total_revenue_usd','sum'),
    track_ids=('track_id', lambda x: sorted(list(set(x)))),
    titles=('title', lambda x: list(x.dropna()[:10])),
    artists=('artist', lambda x: list(x.dropna()[:10]))
).reset_index()

# Find the max
grouped['total_revenue_usd'] = grouped['total_revenue_usd'].astype(float)
max_row = grouped.loc[grouped['total_revenue_usd'].idxmax()]

# Choose representative title/artist: most common in group
rep_title = None
if max_row['titles']:
    # pick the longest non-empty title as representative
    rep_title = sorted(max_row['titles'], key=lambda x: (not x, len(str(x))), reverse=True)[0]
else:
    rep_title = ''
rep_artist = None
if max_row['artists']:
    rep_artist = sorted(max_row['artists'], key=lambda x: (not x, len(str(x))), reverse=True)[0]
else:
    rep_artist = ''

result = {
    'representative_title': rep_title,
    'representative_artist': rep_artist,
    'total_revenue_usd': round(float(max_row['total_revenue_usd']), 2),
    'contributing_track_ids': max_row['track_ids']
}

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rYOeJLEyroLP7V9l3t5i9Gy7': ['tracks'], 'var_call_lruJgmjMy3ZusA6AsEOVdeGf': ['sales'], 'var_call_B8095U14JmURn2eFqBveQ0Y8': 'file_storage/call_B8095U14JmURn2eFqBveQ0Y8.json', 'var_call_rlqCo86aIiX7lg6sTk8pFu95': 'file_storage/call_rlqCo86aIiX7lg6sTk8pFu95.json'}

exec(code, env_args)
