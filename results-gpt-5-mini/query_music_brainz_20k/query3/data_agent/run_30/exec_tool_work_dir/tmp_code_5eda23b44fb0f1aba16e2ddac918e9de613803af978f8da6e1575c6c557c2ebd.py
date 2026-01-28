code = """import json
import pandas as pd
import unicodedata
import re

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
def remove_diacritics(s):
    if s is None:
        return ''
    s = str(s)
    s = unicodedata.normalize('NFKD', s)
    s = ''.join([c for c in s if not unicodedata.combining(c)])
    return s

def normalize_text(s):
    if s is None:
        s = ''
    s = str(s)
    s = remove_diacritics(s)
    s = s.lower()
    # remove common annotations in parentheses
    s = re.sub(r"\([^)]*\)", "", s)
    # replace separators like '-' with space
    s = re.sub(r"[-_/]+", " ", s)
    # remove punctuation except spaces and alphanumerics
    s = re.sub(r"[^0-9a-z ]+", "", s)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Preprocess titles: some titles include 'artist - title' pattern
tracks_df['artist'] = tracks_df['artist'].replace({'None': None})
tracks_df['artist'] = tracks_df['artist'].fillna('')

extracted_artists = []
clean_titles = []
for _, row in tracks_df.iterrows():
    title = row.get('title', '') if pd.notna(row.get('title', '')) else ''
    artist = row.get('artist', '') if pd.notna(row.get('artist', '')) else ''
    t = str(title)
    if (not artist or artist.strip() == "") and ' - ' in t:
        parts = t.split(' - ', 1)
        possible_artist = parts[0].strip()
        possible_title = parts[1].strip()
        if 1 <= len(possible_artist) <= 60:
            artist = possible_artist
            t = possible_title
    elif artist and ' - ' in t:
        parts = t.split(' - ', 1)
        if parts[0].strip().lower() == str(artist).strip().lower():
            t = parts[1].strip()
    extracted_artists.append(artist)
    clean_titles.append(t)

tracks_df['extracted_artist'] = extracted_artists
tracks_df['clean_title'] = clean_titles

tracks_df['norm_title'] = tracks_df['clean_title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['extracted_artist'].apply(normalize_text)

tracks_df['group_key'] = tracks_df['norm_title'] + '||' + tracks_df['norm_artist']

# Map each track_id to group_key
track_to_group = tracks_df.set_index('track_id')['group_key'].to_dict()

# Map sales to groups
sales_df['group_key'] = sales_df['track_id'].map(track_to_group)

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
    if pd.isna(top_key):
        track_ids = []
        rep_title = None
        rep_artist = None
        num_dup = 0
    else:
        tds = tracks_df[tracks_df['group_key'] == top_key]
        track_ids = tds['track_id'].astype(str).tolist()
        rep_title_series = tds['clean_title'].dropna()
        rep_artist_series = tds['extracted_artist'].dropna()
        rep_title = rep_title_series.mode().iloc[0] if not rep_title_series.empty else ''
        rep_artist = rep_artist_series.mode().iloc[0] if not rep_artist_series.empty else ''
        num_dup = len(tds)
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(top_revenue, 2),
        'track_ids': track_ids,
        'num_duplicate_records': int(num_dup)
    }

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_b0IM0EzYO6gslJbjoyTEQPQ3': ['tracks'], 'var_call_qhSQBWJKNCnkbmAiLzforSbA': ['sales'], 'var_call_RAfzcMniRtILpJMnqiz5v0dY': 'file_storage/call_RAfzcMniRtILpJMnqiz5v0dY.json', 'var_call_yUilCZyMgLaFRbRvyYDegxfL': 'file_storage/call_yUilCZyMgLaFRbRvyYDegxfL.json'}

exec(code, env_args)
