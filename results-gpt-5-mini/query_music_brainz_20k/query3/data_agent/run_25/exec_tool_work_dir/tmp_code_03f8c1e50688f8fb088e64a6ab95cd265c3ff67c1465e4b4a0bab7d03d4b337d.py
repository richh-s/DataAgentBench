code = """import pandas as pd
import json
import re

tracks_path = var_call_5Q7HgraK06JCwFWbIBQK9ohq
sales_path = var_call_hQ1UbUfqJypgdCSPGeCPYfJj

# Read JSON files
df_tracks = pd.read_json(tracks_path)
df_sales = pd.read_json(sales_path)

# Convert revenue to numeric
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Precompute revenue per track_id (as string)
sales_rev = df_sales.groupby(df_sales['track_id'].astype(str), dropna=False)['revenue_usd'].sum().reset_index()
sales_rev.columns = ['track_id','revenue_usd']

# Normalize text using vectorized operations
def normalize_series(s):
    s = s.fillna('').astype(str).str.lower()
    s = s.str.replace(r"\(.*?\)", "", regex=True)
    s = s.str.replace(r"\[.*?\]", "", regex=True)
    s = s.str.replace(r"[^a-z0-9]+", " ", regex=True)
    s = s.str.replace(r"\s+", " ", regex=True)
    return s.str.strip()

df_tracks['title_norm'] = normalize_series(df_tracks['title'])
# replace literal 'None' tokens
artist_series = df_tracks['artist'].replace(['None', None, ''], '')
df_tracks['artist_norm'] = normalize_series(artist_series)
album_series = df_tracks['album'].replace(['None', None, ''], '')
df_tracks['album_norm'] = normalize_series(album_series)

# Normalize year: extract first 4-digit or 2-4 digit group
def extract_year(s):
    s = '' if pd.isna(s) else str(s)
    m = re.search(r"(\d{4})", s)
    if m:
        return m.group(1)
    m = re.search(r"(\d{2,4})", s)
    return m.group(1) if m else ''

df_tracks['year_norm'] = df_tracks['year'].apply(extract_year)

# Build canonical key
parts = df_tracks['title_norm'] + '|' + df_tracks['artist_norm']
# include album if present
parts = parts + '|' + df_tracks['album_norm']
parts = parts + '|' + df_tracks['year_norm']
# collapse multiple trailing separators
df_tracks['canon'] = parts.str.strip('|')

# Merge revenue per track
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df = df_tracks.merge(sales_rev, left_on='track_id', right_on='track_id', how='left')
df['revenue_usd'] = df['revenue_usd'].fillna(0.0)

# Aggregate by canon: sum revenue, collect track_ids, choose representative title/artist
agg = df.groupby('canon', dropna=False).agg(
    total_revenue_usd=('revenue_usd','sum'),
    track_ids=('track_id', lambda x: list(x.astype(str).unique())),
    rep_title=('title', lambda x: max([t for t in x if t not in (None,'None','')], key=lambda s: len(str(s))) if any([t not in (None,'None','') for t in x]) else ''),
    rep_artist=('artist', lambda x: max([t for t in x if t not in (None,'None','')], key=lambda s: len(str(s))) if any([t not in (None,'None','') for t in x]) else '')
).reset_index()

# Round revenue
agg['total_revenue_usd'] = agg['total_revenue_usd'].astype(float).round(2)

# Select best
best_row = agg.loc[agg['total_revenue_usd'].idxmax()] if not agg.empty else None

if best_row is not None:
    result = {
        'canon': best_row['canon'],
        'rep_title': best_row['rep_title'],
        'rep_artist': best_row['rep_artist'],
        'track_ids': best_row['track_ids'],
        'total_revenue_usd': float(best_row['total_revenue_usd'])
    }
else:
    result = {}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5Q7HgraK06JCwFWbIBQK9ohq': 'file_storage/call_5Q7HgraK06JCwFWbIBQK9ohq.json', 'var_call_hQ1UbUfqJypgdCSPGeCPYfJj': 'file_storage/call_hQ1UbUfqJypgdCSPGeCPYfJj.json'}

exec(code, env_args)
