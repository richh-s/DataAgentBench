code = """import json
import pandas as pd
import re
import unicodedata

# Load data from storage files
tracks_path = var_call_9ksKfgeBSeGqi6ZS3zfuGO9x
sales_path = var_call_N2XtFAzb2T8Xv7zyNtytDrnl

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure types
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Helper normalization functions

def remove_accents(s):
    if s is None:
        return ''
    s = str(s)
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s

remove_pattern = re.compile(r"\(.*?\)|\[.*?\]")

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = remove_accents(s)
    s = remove_pattern.sub('', s)  # remove bracketed content
    s = s.lower()
    # remove common descriptors
    s = re.sub(r"\b(live|remix|acoustic|version|edit|feat\.?|featuring|with)\b", ' ', s)
    # remove punctuation
    s = re.sub(r"[^a-z0-9\s]", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# Preprocess tracks: try to extract artist from title if artist missing or 'None' or blank

def extract_artist_title(row):
    title = row.get('title') or ''
    artist = row.get('artist') or ''
    title = str(title)
    artist = str(artist)
    # normalize missing indicators
    if artist.strip().lower() in ['', 'none', '[unknown]']:
        # if title contains ' - ' pattern, assume 'Artist - Title'
        if ' - ' in title:
            parts = title.split(' - ', 1)
            # Heuristic: if left part looks like an artist (contains letters)
            if len(parts[0].strip())>0 and re.search('[a-zA-Z]', parts[0]):
                artist = parts[0].strip()
                title = parts[1].strip()
    return title, artist

tracks_df[['clean_title', 'clean_artist']] = tracks_df.apply(lambda r: pd.Series(extract_artist_title(r)), axis=1)

# Create normalized fields
tracks_df['norm_title'] = tracks_df['clean_title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['clean_artist'].apply(normalize_text)

# If artist missing after extraction, try to infer from album or other fields
tracks_df.loc[tracks_df['norm_artist']=='', 'norm_artist'] = tracks_df.loc[tracks_df['norm_artist']=='', 'album'].fillna('').apply(normalize_text)

# Create grouping key
tracks_df['group_key'] = (tracks_df['norm_artist'] + '||' + tracks_df['norm_title']).fillna('')

# For any empty group_key (both missing), fallback to norm_title only
tracks_df.loc[tracks_df['group_key']=='||', 'group_key'] = tracks_df.loc[tracks_df['group_key']=='||', 'norm_title']

# Build mapping from track_id to group_key
trackid_to_group = tracks_df.set_index('track_id')['group_key'].to_dict()

# Map sales track_id to group_key; if track_id not found in tracks, use track_id itself
sales_df['group_key'] = sales_df['track_id'].map(trackid_to_group).fillna(sales_df['track_id'])

# Aggregate revenue by group_key
rev_by_group = sales_df.groupby('group_key', dropna=False)['revenue_usd'].sum().reset_index()

# Find top group
top = rev_by_group.sort_values('revenue_usd', ascending=False).iloc[0]

top_key = top['group_key']
top_revenue = float(top['revenue_usd'])

# Select representative title and artist for display: most common among tracks in group
rep_title = None
rep_artist = None
if top_key in tracks_df['group_key'].values:
    subset = tracks_df[tracks_df['group_key']==top_key]
    # choose the most frequent non-empty clean_title and clean_artist
    rep_title = subset['clean_title'].replace('', pd.NA).mode(dropna=True)
    rep_artist = subset['clean_artist'].replace('', pd.NA).mode(dropna=True)
    rep_title = rep_title.iloc[0] if not rep_title.empty else subset['title'].iat[0]
    rep_artist = rep_artist.iloc[0] if not rep_artist.empty else subset['artist'].iat[0]
else:
    # no mapping (track id only)
    rep_title = sales_df[sales_df['group_key']==top_key]['track_id'].iloc[0]
    rep_artist = ''

result = {
    'title': rep_title,
    'artist': rep_artist,
    'total_revenue_usd': round(top_revenue, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9ksKfgeBSeGqi6ZS3zfuGO9x': 'file_storage/call_9ksKfgeBSeGqi6ZS3zfuGO9x.json', 'var_call_N2XtFAzb2T8Xv7zyNtytDrnl': 'file_storage/call_N2XtFAzb2T8Xv7zyNtytDrnl.json'}

exec(code, env_args)
