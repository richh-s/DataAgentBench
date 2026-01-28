code = """import json
import pandas as pd
import re

# Load data from previous query results stored as file paths
tracks_path = var_call_wiMjCcYdft0iwjNPcqKfYDW6
sales_path = var_call_2lbDhdSpbMrwCQJkrygNidFh

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure correct dtypes
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
if 'revenue_usd_total' in sales_df.columns:
    sales_df['track_id'] = sales_df['track_id'].astype(str)
    sales_df['revenue_usd_total'] = sales_df['revenue_usd_total'].astype(float)
else:
    # fallback
    sales_df['revenue_usd_total'] = sales_df.get('revenue_usd', 0.0).astype(float)

# Normalization functions

def normalize_text(s):
    if s is None:
        return None
    if not isinstance(s, str):
        s = str(s)
    s = s.strip()
    if s.lower() in ('none', "\'none\'", ''):
        return None
    # remove content in parentheses or brackets
    s = re.sub(r"\(.*?\)|\[.*?\]", "", s)
    # replace punctuation with space, keep alphanum
    s = s.lower()
    s = re.sub(r"[^0-9a-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    s = s.strip()
    if s == '':
        return None
    return s

tracks_df['norm_title'] = tracks_df['title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)

# If artist missing, set to special token to group by title only
tracks_df['norm_artist_filled'] = tracks_df['norm_artist'].fillna('@@UNKNOWN@@')

# Create group key
tracks_df['entity_key'] = tracks_df['norm_title'].fillna('@@NO_TITLE@@') + '||' + tracks_df['norm_artist_filled']

# Merge revenue per track
merged = tracks_df.merge(sales_df[['track_id', 'revenue_usd_total']], on='track_id', how='left')
merged['revenue_usd_total'] = merged['revenue_usd_total'].fillna(0.0)

# Aggregate revenue by entity_key
agg = merged.groupby('entity_key').agg(
    total_revenue_usd=('revenue_usd_total', 'sum'),
    count_tracks=('track_id', 'nunique')
).reset_index()

# Find entity with max revenue
max_row = agg.loc[agg['total_revenue_usd'].idxmax()]
max_key = max_row['entity_key']
max_total = float(max_row['total_revenue_usd'])

# Extract representative title and artist: choose most common original among group
group_df = merged[merged['entity_key'] == max_key]
# pick mode of title and artist (first if multiple)
rep_title = None
rep_artist = None
if not group_df.empty:
    rep_title = group_df['title'].mode().iloc[0] if group_df['title'].mode().size>0 else None
    rep_artist = group_df['artist'].mode().iloc[0] if group_df['artist'].mode().size>0 else None

# Collect member track_ids
member_track_ids = sorted(group_df['track_id'].astype(str).unique(), key=lambda x: int(x))

result = {
    'title': rep_title,
    'artist': rep_artist,
    'total_revenue_usd': round(max_total, 2),
    'member_track_ids': member_track_ids,
    'entity_key': max_key
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2lbDhdSpbMrwCQJkrygNidFh': 'file_storage/call_2lbDhdSpbMrwCQJkrygNidFh.json', 'var_call_wiMjCcYdft0iwjNPcqKfYDW6': 'file_storage/call_wiMjCcYdft0iwjNPcqKfYDW6.json'}

exec(code, env_args)
