code = """import json
import pandas as pd
import re
import unicodedata

# Load data from previous tool calls (file paths)
with open(var_call_K3MuIleYHcghA84esTNp1DKh, 'r', encoding='utf-8') as f:
    sales_agg = json.load(f)
with open(var_call_BwfSWEiUBgJ9nQIzuZ3Hk0Ca, 'r', encoding='utf-8') as f:
    tracks = json.load(f)

# Create DataFrames
df_sales = pd.DataFrame(sales_agg)
df_tracks = pd.DataFrame(tracks)

# Normalize columns and types
# track_id may be string in both; keep as string for merge
df_sales['track_id'] = df_sales['track_id'].astype(str)
# revenue might be string, convert to float
df_sales['total_revenue_usd'] = df_sales['total_revenue_usd'].astype(float)

def normalize_text(s):
    if s is None:
        return ''
    if not isinstance(s, str):
        s = str(s)
    s = s.strip()
    if s.lower() in ('none', 'nan', '[unknown]', ''):
        return ''
    # remove content inside parentheses
    s = re.sub(r"\(.*?\)", "", s)
    # transliterate unicode
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', 'ignore').decode('ascii')
    # remove punctuation except ampersand and plus and apostrophe? remove most punctuation
    s = re.sub(r"[^0-9a-zA-Z\s&'+-]", ' ', s)
    # replace dashes with space
    s = s.replace('-', ' ')
    # collapse whitespace
    s = re.sub(r"\s+", ' ', s)
    s = s.strip().lower()
    return s

# Preprocess tracks: fill artist if missing by parsing title 'Artist - Title' pattern
tracks_processed = df_tracks.copy()

# Replace string 'None' with actual None for easier checks
tracks_processed['artist'] = tracks_processed['artist'].replace({None: '', 'None': '', "[unknown]": ''})
tracks_processed['title'] = tracks_processed['title'].replace({None: ''})

# Parse title to extract artist if artist missing and title contains ' - '
def extract_from_title(row):
    artist = row['artist']
    title = row['title'] if isinstance(row['title'], str) else ''
    if (not artist) and ' - ' in title:
        parts = title.split(' - ', 1)
        left = parts[0].strip()
        right = parts[1].strip()
        # Heuristic: if left looks like an artist (contains letters and not just numbers), use it
        if re.search(r'[A-Za-z]', left):
            return pd.Series([left, right])
    return pd.Series([artist, title])

tracks_processed[['artist_ex', 'title_ex']] = tracks_processed.apply(extract_from_title, axis=1)

# Use extracted values if present
tracks_processed['artist_final'] = tracks_processed.apply(lambda r: r['artist_ex'] if r['artist_ex'] else r['artist'], axis=1)
tracks_processed['title_final'] = tracks_processed.apply(lambda r: r['title_ex'] if r['title_ex'] else r['title'], axis=1)

# Normalize fields
tracks_processed['title_norm'] = tracks_processed['title_final'].apply(normalize_text)
tracks_processed['artist_norm'] = tracks_processed['artist_final'].apply(normalize_text)
tracks_processed['album_norm'] = tracks_processed['album'].fillna('').apply(normalize_text)
tracks_processed['year_norm'] = tracks_processed['year'].fillna('').astype(str).apply(lambda x: x.strip().lower() if x and x.lower()!='none' else '')

# Create entity key using title and artist primarily, include album and year when available
tracks_processed['entity_key'] = tracks_processed['title_norm'] + '|' + tracks_processed['artist_norm']
# If album and year exist, append to key to reduce false positives
tracks_processed.loc[tracks_processed['album_norm']!='', 'entity_key'] = (
    tracks_processed['entity_key'] + '|' + tracks_processed['album_norm']
)
tracks_processed.loc[tracks_processed['year_norm']!='', 'entity_key'] = (
    tracks_processed['entity_key'] + '|' + tracks_processed['year_norm']
)

# Merge sales aggregated with tracks
merged = pd.merge(tracks_processed, df_sales, on='track_id', how='left')
merged['total_revenue_usd'] = merged['total_revenue_usd'].fillna(0.0)

# Group by entity_key
grouped = merged.groupby('entity_key').agg(
    total_revenue_usd=('total_revenue_usd', 'sum'),
    titles=('title_final', lambda x: list(x.dropna().unique())[:5]),
    artists=('artist_final', lambda x: list(x.dropna().unique())[:5]),
    track_ids=('track_id', lambda x: list(x.unique())[:200]),
    albums=('album', lambda x: list(x.dropna().unique())[:5]),
    years=('year', lambda x: list(x.dropna().unique())[:5])
).reset_index()

# Find max revenue entity
if grouped.shape[0] == 0:
    result = {"error": "No data available"}
else:
    top = grouped.sort_values('total_revenue_usd', ascending=False).iloc[0]
    # Pick representative title and artist (first in lists) or fallback to normalized
    rep_title = top['titles'][0] if top['titles'] else ''
    rep_artist = top['artists'][0] if top['artists'] else ''
    # Format revenue to 2 decimals
    total_revenue = float(top['total_revenue_usd'])
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(total_revenue, 2),
        'track_ids': top['track_ids'],
        'albums': top['albums'],
        'years': top['years']
    }

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_K3MuIleYHcghA84esTNp1DKh': 'file_storage/call_K3MuIleYHcghA84esTNp1DKh.json', 'var_call_BwfSWEiUBgJ9nQIzuZ3Hk0Ca': 'file_storage/call_BwfSWEiUBgJ9nQIzuZ3Hk0Ca.json'}

exec(code, env_args)
