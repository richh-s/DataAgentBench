code = """import json
import pandas as pd
import re
from collections import Counter

# Load data from storage variables (file paths)
tracks_path = var_call_cK5n4wM5jrZB75fJSyCnJpyG
sales_path = var_call_AQSM4HDagd2FfavgOhDgBg8A

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# Convert to DataFrame
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Clean revenue and numeric fields
df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)
# Ensure track_id types
# Some track_id values may be strings; normalize to string for join
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)

# Aggregate revenue per track_id
rev_per_track = df_sales.groupby('track_id', as_index=False)['revenue_usd'].sum()
rev_per_track.rename(columns={'revenue_usd': 'total_revenue_usd'}, inplace=True)

# Merge revenue into tracks; some track_ids in sales may not be in tracks and vice versa
df_merged = pd.merge(df_tracks, rev_per_track, on='track_id', how='inner')

# Normalization helpers
remove_tokens = ['live', 'remix', 'acoustic', 'version', "feat", "featuring", "ft", "- live", "(live)", "original", "remastered"]

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ['none', '', 'nan', 'na', '[unknown]']:
        return ''
    # remove parenthetical content
    s = re.sub(r"\(.*?\)", "", s)
    # remove common tokens
    for tok in remove_tokens:
        s = re.sub(re.escape(tok), ' ', s, flags=re.I)
    # remove punctuation
    s = re.sub(r"[^0-9a-zA-Z\s]", ' ', s)
    # collapse whitespace
    s = re.sub(r"\s+", ' ', s)
    s = s.lower().strip()
    return s

# Create normalized fields
df_merged['norm_title'] = df_merged['title'].apply(normalize_text)
# artist may contain multiple artists; pick as-is then normalize
# if artist field is empty, try to extract artist from title if title formatted like 'Artist - Title'
def extract_artist_from_title(title):
    if not title:
        return ''
    if '-' in title:
        parts = title.split('-')
        # heuristic: if left part shorter than right, treat left as artist
        left = parts[0].strip()
        right = '-'.join(parts[1:]).strip()
        # if left contains spaces but not too long
        if len(left) < len(right):
            return left
    return ''

# Fill missing artist from title heuristics
df_merged['artist_filled'] = df_merged['artist'].replace({None: ''}).astype(str).str.strip()
mask_missing_artist = df_merged['artist_filled'].isin(['', 'None', 'nan', 'None'])
extracted = df_merged.loc[mask_missing_artist, 'title'].apply(extract_artist_from_title)
df_merged.loc[mask_missing_artist, 'artist_filled'] = extracted.fillna('')

# Normalize artist
df_merged['norm_artist'] = df_merged['artist_filled'].apply(normalize_text)

# Group by normalized title+artist as entity resolution
group_cols = ['norm_title', 'norm_artist']
agg = df_merged.groupby(group_cols).agg({
    'total_revenue_usd': 'sum',
    'track_id': lambda ids: list(ids),
    'title': lambda vals: list(vals),
    'artist_filled': lambda vals: list(vals),
    'album': lambda vals: list(vals)
}).reset_index()

# Find top group by revenue
top_idx = agg['total_revenue_usd'].idxmax()
top_group = agg.loc[top_idx]

# Choose representative title/artist/album by most common non-empty value
def most_common_nonempty(lst):
    cnt = Counter([x for x in lst if x and str(x).strip().lower() not in ['none', 'nan']])
    if not cnt:
        return ''
    return cnt.most_common(1)[0][0]

rep_title = most_common_nonempty(top_group['title'])
rep_artist = most_common_nonempty(top_group['artist_filled'])
rep_album = most_common_nonempty(top_group['album'])

result = {
    'title': rep_title,
    'artist': rep_artist,
    'representative_album': rep_album,
    'total_revenue_usd': round(float(top_group['total_revenue_usd']), 2),
    'track_ids': top_group['track_id'],
    'member_count': len(top_group['track_id'])
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cK5n4wM5jrZB75fJSyCnJpyG': 'file_storage/call_cK5n4wM5jrZB75fJSyCnJpyG.json', 'var_call_AQSM4HDagd2FfavgOhDgBg8A': 'file_storage/call_AQSM4HDagd2FfavgOhDgBg8A.json'}

exec(code, env_args)
