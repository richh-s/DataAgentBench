code = """import json
import pandas as pd
import re

# Load the query results from storage variables (file paths)
tracks_path = var_call_bGXbbzXG6Kylz5HNVEKLkG0X
sales_path = var_call_UtvtrCWj8kAq9IfynK3X70fU

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# Create DataFrames
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Ensure track_id types are consistent
# Some values may be strings; convert to string
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

# Convert revenue to numeric
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce').fillna(0.0)

# Normalization function
_non_alnum = re.compile(r'[^0-9a-zA-Z]+')

def normalize(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ('none', 'nan', 'null', "[unknown]", ''):
        return ''
    # lowercase
    s = s.lower()
    # replace non-alphanumeric with space
    s = _non_alnum.sub(' ', s)
    # collapse spaces
    s = ' '.join(s.split())
    return s

# Apply normalization to tracks
for col in ['title', 'artist']:
    if col not in df_tracks.columns:
        df_tracks[col] = ''
    df_tracks[col + '_norm'] = df_tracks[col].apply(normalize)

# Create entity key primarily using title + artist
# If artist is missing, rely on title only

def make_entity_key(row):
    title = row.get('title_norm', '')
    artist = row.get('artist_norm', '')
    if artist:
        return title + ' ||| ' + artist
    else:
        return title


df_tracks['entity_key'] = df_tracks.apply(make_entity_key, axis=1)

# Merge sales with tracks to attach entity_key
# Some sales may refer to track_ids not in tracks; keep them with entity_key = '<unknown>'
df_merged = pd.merge(df_sales, df_tracks[['track_id', 'entity_key', 'title', 'artist']], on='track_id', how='left')
df_merged['entity_key'] = df_merged['entity_key'].fillna('__UNKNOWN__')

# Group by entity_key and sum revenue
grouped = df_merged.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()

# Find entity with max revenue
idx_max = grouped['revenue_usd'].idxmax()
max_row = grouped.loc[idx_max]
max_entity = max_row['entity_key']
max_revenue = float(max_row['revenue_usd'])

# For the winning entity, collect representative titles and artists and track_ids
wins = df_merged[df_merged['entity_key'] == max_entity]
unique_track_ids = sorted(wins['track_id'].astype(str).unique().tolist())
# choose most common title/artist (non-empty)

# Helper to pick best representative
def best_value(series):
    # prefer non-empty and not None
    vals = [v for v in series.fillna('').astype(str).tolist() if v.strip().lower() not in ('', 'none', '[unknown]')]
    if not vals:
        return ''
    # return most common
    from collections import Counter
    return Counter(vals).most_common(1)[0][0]

rep_title = best_value(wins['title'])
rep_artist = best_value(wins['artist'])

result = {
    'title': rep_title,
    'artist': rep_artist,
    'total_revenue_usd': round(max_revenue, 2),
    'track_ids': unique_track_ids,
    'entity_key': max_entity,
    'num_sales_records': int(len(wins))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2pqsS7Cv4KiFRvTUFZtXTxlI': ['tracks'], 'var_call_wyt8VXLuev3pUq8FfugPJlH1': ['sales'], 'var_call_bGXbbzXG6Kylz5HNVEKLkG0X': 'file_storage/call_bGXbbzXG6Kylz5HNVEKLkG0X.json', 'var_call_UtvtrCWj8kAq9IfynK3X70fU': 'file_storage/call_UtvtrCWj8kAq9IfynK3X70fU.json'}

exec(code, env_args)
