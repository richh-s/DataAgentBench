code = """import json
import pandas as pd
import re

# Load data from storage files
with open(var_call_6eTCEOL6hs0fbxjmLYCydlti, 'r') as f:
    tracks = json.load(f)
with open(var_call_5eGlZXLVm09aaTZvmhws2SNS, 'r') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize column types
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Basic cleaning of text fields
def clean_text(x):
    if x is None:
        return ''
    if not isinstance(x, str):
        x = str(x)
    x = x.strip()
    if x.lower() in ('none', 'nan', 'null', '[unknown]'):
        return ''
    return x

tracks_df['title_raw'] = tracks_df['title'].apply(clean_text)
tracks_df['artist_raw'] = tracks_df['artist'].apply(clean_text)
tracks_df['album_raw'] = tracks_df['album'].apply(clean_text)
tracks_df['year_raw'] = tracks_df['year'].apply(clean_text)

# Heuristic normalization for entity resolution
paren_re = re.compile(r"\(.*?\)")
non_alnum_re = re.compile(r"[^0-9a-zA-Z ]+")
mult_space_re = re.compile(r"\s+")

def normalize_title(title, artist):
    t = title
    # If title contains ' - ' and artist missing, assume format 'Artist - Title'
    if (not artist) and ' - ' in t:
        parts = t.split(' - ', 1)
        t = parts[1]
    # remove parenthetical content
    t = paren_re.sub('', t)
    # remove punctuation
    t = non_alnum_re.sub(' ', t)
    t = t.lower()
    t = mult_space_re.sub(' ', t).strip()
    return t

def normalize_artist(artist):
    a = artist
    if not a:
        return ''
    a = paren_re.sub('', a)
    a = non_alnum_re.sub(' ', a)
    a = a.lower()
    a = mult_space_re.sub(' ', a).strip()
    return a

tracks_df['title_norm'] = tracks_df.apply(lambda r: normalize_title(r['title_raw'], r['artist_raw']), axis=1)
tracks_df['artist_norm'] = tracks_df['artist_raw'].apply(normalize_artist)

# Merge sales with tracks
merged = sales_df.merge(tracks_df, on='track_id', how='left', suffixes=('_sale', '_track'))

# Create grouping key: title_norm + artist_norm (if artist_norm empty, use title only)
merged['group_key'] = merged.apply(lambda r: (r['title_norm'] + '||' + r['artist_norm']) if r['artist_norm'] else (r['title_norm'] + '||'), axis=1)

# Aggregate revenue by group
agg = merged.groupby('group_key').agg(
    total_revenue_usd=('revenue_usd', 'sum'),
    track_ids=('track_id', lambda x: sorted(set(x.tolist()))),
    count_tracks=('track_id', lambda x: len(set(x.tolist())))
).reset_index()

# Get top group
agg_sorted = agg.sort_values('total_revenue_usd', ascending=False).reset_index(drop=True)
if agg_sorted.shape[0] == 0:
    result = {"error": "No data after aggregation"}
else:
    top = agg_sorted.loc[0]
    key = top['group_key']
    total = float(top['total_revenue_usd'])
    track_ids = top['track_ids']
    # Find representative title and artist from tracks in this group: choose most common raw title/artist
    subset = merged[merged['group_key'] == key]
    # pick most frequent non-empty title_raw
    title_counts = subset['title_raw'].value_counts()
    rep_title = title_counts.idxmax() if not title_counts.empty else ''
    artist_counts = subset['artist_raw'].value_counts()
    rep_artist = artist_counts.idxmax() if not artist_counts.empty else ''

    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(total, 2),
        'track_ids': track_ids,
        'num_track_ids': len(track_ids)
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6eTCEOL6hs0fbxjmLYCydlti': 'file_storage/call_6eTCEOL6hs0fbxjmLYCydlti.json', 'var_call_5eGlZXLVm09aaTZvmhws2SNS': 'file_storage/call_5eGlZXLVm09aaTZvmhws2SNS.json'}

exec(code, env_args)
