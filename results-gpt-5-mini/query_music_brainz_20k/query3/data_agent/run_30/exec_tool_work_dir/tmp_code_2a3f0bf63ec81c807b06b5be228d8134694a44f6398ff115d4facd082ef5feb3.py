code = """import json
import pandas as pd
import unicodedata

# Load data from storage file paths
tracks_path = var_call_RAfzcMniRtILpJMnqiz5v0dY
sales_path = var_call_yUilCZyMgLaFRbRvyYDegxfL

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

# Normalization helpers
import re

def remove_diacritics(s):
    if s is None:
        return ''
    s = str(s)
    s = unicodedata.normalize('NFKD', s)
    s = ''.join([c for c in s if not unicodedata.combining(c)])
    return s


def normalize_text(s):
    if pd.isna(s):
        s = ''
    s = remove_diacritics(s)
    s = s.lower()
    # remove common annotations in parentheses
    s = re.sub(r"\([^)]*\)", "", s)
    # replace separators like '-' with space
    s = re.sub(r"[-_/]+", " ", s)
    # remove punctuation
    s = re.sub(r"[^0-9a-z ]+", "", s)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Preprocess titles: some titles include 'artist - title' pattern
# If artist is missing or 'None' or blank, try to extract from title
tracks_df['artist'] = tracks_df['artist'].replace({'None': None})
tracks_df['artist'] = tracks_df['artist'].fillna('')

# Extract possible artist from title if artist missing
extracted_artists = []
clean_titles = []
for _, row in tracks_df.iterrows():
    title = row['title'] if pd.notna(row['title']) else ''
    artist = row['artist'] if pd.notna(row['artist']) else ''
    t = str(title)
    # if artist is empty and title contains ' - ' or ': '
    if (not artist or artist.strip()=="") and ' - ' in t:
        parts = t.split(' - ', 1)
        possible_artist = parts[0].strip()
        possible_title = parts[1].strip()
        # simple heuristic: if possible_artist is short (not too long), accept
        if 1 <= len(possible_artist) <= 60:
            artist = possible_artist
            t = possible_title
    # also if title contains ' - ' and artist present but title starts with artist, remove duplication
    elif artist and ' - ' in t:
        parts = t.split(' - ', 1)
        if parts[0].strip().lower() == str(artist).strip().lower():
            t = parts[1].strip()
    extracted_artists.append(artist)
    clean_titles.append(t)

tracks_df['extracted_artist'] = extracted_artists
tracks_df['clean_title'] = clean_titles

# Now normalized fields
tracks_df['norm_title'] = tracks_df['clean_title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['extracted_artist'].apply(lambda x: normalize_text(x))

# Create grouping key
tracks_df['group_key'] = tracks_df['norm_title'] + '||' + tracks_df['norm_artist']

# For tracks with empty artist, try grouping by title only
# (group_key already has empty artist part)

# Map each track_id to group_key
track_to_group = tracks_df.set_index('track_id')['group_key'].to_dict()

# Map sales to groups
sales_df['group_key'] = sales_df['track_id'].map(track_to_group)

# For any sales rows with no matching track (shouldn't happen), set group_key to None
# Aggregate revenue by group_key
agg = sales_df.groupby('group_key', dropna=False)['revenue_usd'].sum().reset_index()

# Find top group by revenue
agg_sorted = agg.sort_values('revenue_usd', ascending=False).reset_index(drop=True)

if agg_sorted.empty:
    result = {
        'title': None,
        'artist': None,
        'total_revenue_usd': 0.0,
        'track_ids': [],
        'num_duplicate_records': 0
    }
else:
    top = agg_sorted.iloc[0]
    top_key = top['group_key']
    top_revenue = float(top['revenue_usd'])
    # get all track_ids in this group
    if pd.isna(top_key):
        track_ids = []
    else:
        tds = tracks_df[tracks_df['group_key'] == top_key]
        track_ids = tds['track_id'].astype(str).tolist()
        # pick representative title and artist (most common original)
        rep_title = tds['clean_title'].mode()
        rep_artist = tds['extracted_artist'].mode()
        rep_title = rep_title.iloc[0] if not rep_title.empty else ''
        rep_artist = rep_artist.iloc[0] if not rep_artist.empty else ''
        # count duplicates
        num_dup = len(tds)
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(top_revenue, 2),
        'track_ids': track_ids,
        'num_duplicate_records': num_dup
    }

# Print result in required format as a JSON string
print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print('print(\'' + json.dumps(result).replace("'", "\\'") + '\')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_b0IM0EzYO6gslJbjoyTEQPQ3': ['tracks'], 'var_call_qhSQBWJKNCnkbmAiLzforSbA': ['sales'], 'var_call_RAfzcMniRtILpJMnqiz5v0dY': 'file_storage/call_RAfzcMniRtILpJMnqiz5v0dY.json', 'var_call_yUilCZyMgLaFRbRvyYDegxfL': 'file_storage/call_yUilCZyMgLaFRbRvyYDegxfL.json'}

exec(code, env_args)
