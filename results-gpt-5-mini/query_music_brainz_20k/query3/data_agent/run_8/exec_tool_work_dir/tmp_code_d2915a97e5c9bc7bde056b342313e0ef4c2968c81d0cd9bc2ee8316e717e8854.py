code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
tracks_path = var_call_0EFqDgxNqQ6X0xE9QW7vjByT
sales_path = var_call_bBRQ807lj8KMrwGizJIPMcPu

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure proper types
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)

# convert revenue to float
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Sum revenue per track_id
revenue_per_track = sales_df.groupby('track_id', dropna=False)['revenue_usd'].sum().reset_index()
revenue_per_track.columns = ['track_id', 'total_revenue']

# Merge with tracks
merged = pd.merge(tracks_df, revenue_per_track, on='track_id', how='left')
merged['total_revenue'] = merged['total_revenue'].fillna(0.0)

# Normalization helpers
placeholder_artist = set(['none', "[unknown]", '', '   ', 'unknown', 'n/a', 'none'])

def clean_text(s):
    if s is None:
        return ''
    s = str(s)
    # Replace common separators
    s = s.replace('\u2013', '-').replace('\u2014', '-')
    # Remove content in parentheses or brackets
    s = re.sub(r"\[.*?\]", "", s)
    s = re.sub(r"\(.*?\)", "", s)
    # Lowercase
    s = s.lower()
    # Remove punctuation except spaces and alphanum
    s = re.sub(r"[^a-z0-9\s]", "", s)
    # Collapse whitespace
    s = re.sub(r"\s+", " ", s)
    return s.strip()

# Attempt to parse titles that begin with 'Artist - Title' when artist field is missing or placeholder
parsed_titles = []
for _, row in merged.iterrows():
    title = row.get('title') if row.get('title') is not None else ''
    artist = row.get('artist') if row.get('artist') is not None else ''
    t = str(title)
    a = str(artist)
    # Normalize artist placeholder check
    a_clean = a.strip().lower()
    if (' - ' in t) and (a_clean in placeholder_artist):
        parts = t.split(' - ', 1)
        # Heuristic: if left part doesn't contain numbers and is reasonably short, treat as artist
        left = parts[0].strip()
        right = parts[1].strip()
        if len(left) > 0 and len(left.split()) <= 6:
            # Assign
            artist = left
            title = right
    # As further heuristic, if title contains ' - ' and left equals artist token (case-insensitive), split
    else:
        if ' - ' in t and a_clean not in placeholder_artist:
            left = t.split(' - ', 1)[0].strip().lower()
            if left == a_clean:
                title = t.split(' - ', 1)[1].strip()
    parsed_titles.append((str(title), str(artist)))

merged[['parsed_title', 'parsed_artist']] = pd.DataFrame(parsed_titles, index=merged.index)

# Create normalized keys
merged['norm_title'] = merged['parsed_title'].apply(clean_text)
merged['norm_artist'] = merged['parsed_artist'].apply(clean_text)

# For records still with empty artist, try to extract artist from title if title contains ' - '
def extract_from_title(title, artist):
    if artist.strip() == '':
        if ' - ' in title:
            left, right = title.split(' - ', 1)
            # if left looks like name (no digits), use it
            if re.search(r"\d", left) is None:
                return left.strip()
    return artist

merged['parsed_artist'] = merged.apply(lambda r: extract_from_title(r['parsed_title'], r['parsed_artist']), axis=1)
merged['norm_artist'] = merged['parsed_artist'].apply(clean_text)

# Build resolved key
merged['resolved_key'] = merged['norm_title'] + '||' + merged['norm_artist']

# Group by resolved entity
grouped = merged.groupby('resolved_key').agg({
    'total_revenue': 'sum',
    'track_id': lambda ids: list(ids.astype(str).unique()),
    'parsed_title': lambda vals: list(vals.dropna().unique()),
    'parsed_artist': lambda vals: list(vals.dropna().unique())
}).reset_index()

# Find max revenue
grouped['total_revenue'] = grouped['total_revenue'].astype(float)
max_row = grouped.loc[grouped['total_revenue'].idxmax()]

# Choose representative title and artist: pick the most common non-empty
def choose_rep(lst):
    lst = [x for x in lst if x not in [None, '', 'None']]
    if not lst:
        return ''
    # pick the shortest non-empty (to avoid verbose album-like titles), then the first
    lst_sorted = sorted(lst, key=lambda s: (len(s), lst.index(s)))
    return lst_sorted[0]

rep_title = choose_rep(max_row['parsed_title'])
rep_artist = choose_rep(max_row['parsed_artist'])

result = {
    'title': rep_title,
    'artist': rep_artist,
    'total_revenue_usd': round(float(max_row['total_revenue']), 2),
    'contributing_track_ids': max_row['track_id']
}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_0EFqDgxNqQ6X0xE9QW7vjByT': 'file_storage/call_0EFqDgxNqQ6X0xE9QW7vjByT.json', 'var_call_bBRQ807lj8KMrwGizJIPMcPu': 'file_storage/call_bBRQ807lj8KMrwGizJIPMcPu.json'}

exec(code, env_args)
