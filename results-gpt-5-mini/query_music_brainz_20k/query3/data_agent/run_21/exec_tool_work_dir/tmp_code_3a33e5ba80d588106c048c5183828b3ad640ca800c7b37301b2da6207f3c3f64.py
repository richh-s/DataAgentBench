code = """import json
import pandas as pd
import unicodedata
import re

# Load data from previous query_db calls (file paths are stored in variables)
with open(var_call_SkrOIAlwXbrOAfb6RAv6HqY1, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_jpXV3hYazw6nDd2Nk7trJYC7, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# Create DataFrames
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Ensure track_id types match
# Some fields may be strings; convert to string for consistency
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

# Convert revenue to float
# Handle possible non-numeric by coercing
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Normalization function for entity resolution
import math

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ('none', 'nan', 'null', ''):
        return ''
    s = s.lower()
    s = unicodedata.normalize('NFKD', s)
    # remove diacritics
    s = ''.join(c for c in s if not unicodedata.combining(c))
    # remove punctuation except alphanumerics and spaces
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Merge sales with tracks to get track attributes
df_merged = df_sales.merge(df_tracks, on='track_id', how='left', suffixes=('_sale','_track'))

# Create normalized grouping key using title and artist (and album as fallback)
# If artist missing, include album to help disambiguate

def make_key(row):
    t = normalize_text(row.get('title', ''))
    a = normalize_text(row.get('artist', ''))
    alb = normalize_text(row.get('album', ''))
    yr = normalize_text(row.get('year', ''))
    # Compose key giving priority to title+artist; if artist missing, include album and year
    if a:
        key = f"{t}|{a}"
    else:
        key = f"{t}|{alb}|{yr}"
    return key

# Apply
keys = df_merged.apply(make_key, axis=1)
df_merged = df_merged.copy()
df_merged['entity_key'] = keys

# Aggregate revenue by entity_key
agg = df_merged.groupby('entity_key').agg(
    total_revenue_usd=('revenue_usd', 'sum'),
    sales_count=('sale_id', 'count'),
    unique_track_ids=('track_id', lambda x: sorted(set(x.astype(str))))
).reset_index()

# For human-readable title/artist, pick the most common original title and artist per group
rep_titles = df_merged.groupby('entity_key')['title'].agg(lambda x: x.dropna().mode().iloc[0] if not x.dropna().empty else '')
rep_artists = df_merged.groupby('entity_key')['artist'].agg(lambda x: x.dropna().mode().iloc[0] if not x.dropna().empty else '')

agg = agg.merge(rep_titles.rename('rep_title'), left_on='entity_key', right_index=True)
agg = agg.merge(rep_artists.rename('rep_artist'), left_on='entity_key', right_index=True)

# Find top by total_revenue_usd
agg_sorted = agg.sort_values('total_revenue_usd', ascending=False).reset_index(drop=True)
if agg_sorted.shape[0] == 0:
    result = {"title": None, "artist": None, "total_revenue_usd": 0.0, "sales_count": 0, "track_ids": []}
else:
    top = agg_sorted.iloc[0]
    # Clean up representative fields
    title = top['rep_title'] if pd.notna(top['rep_title']) and str(top['rep_title']).strip().lower() not in ('none','') else ''
    artist = top['rep_artist'] if pd.notna(top['rep_artist']) and str(top['rep_artist']).strip().lower() not in ('none','') else ''
    total = float(top['total_revenue_usd'])
    sales_count = int(top['sales_count'])
    track_ids = top['unique_track_ids']
    result = {
        "title": title,
        "artist": artist,
        "total_revenue_usd": round(total, 2),
        "sales_count": sales_count,
        "track_ids": track_ids,
        "entity_key": top['entity_key']
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SkrOIAlwXbrOAfb6RAv6HqY1': 'file_storage/call_SkrOIAlwXbrOAfb6RAv6HqY1.json', 'var_call_jpXV3hYazw6nDd2Nk7trJYC7': 'file_storage/call_jpXV3hYazw6nDd2Nk7trJYC7.json'}

exec(code, env_args)
