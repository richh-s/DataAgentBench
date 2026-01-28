code = """import json
import pandas as pd
import re

# Load inputs from storage variables
# var_call_gCRTSRV2gEM56hPkO5nwhlCp may be a file path (string) because result was large
tracks_var = var_call_gCRTSRV2gEM56hPkO5nwhlCp
sales_var = var_call_pQmdbFxKCu3mo89IzpliWuxI

if isinstance(tracks_var, str) and tracks_var.endswith('.json'):
    with open(tracks_var, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_var

sales = sales_var

# Create DataFrames
tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure track_id consistent type
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)

# Convert revenue to float
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)

# Merge sales totals with track metadata
merged = sales_df.merge(tracks_df, on='track_id', how='left')

# Define normalization for title and artist for entity resolution

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.lower()
    # remove content inside parentheses or brackets
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # remove common descriptors
    s = re.sub(r"\\b(live|remix|acoustic|version|edit|radio|mono|stereo|instrumental)\\b", "", s)
    # remove featuring markers
    s = re.sub(r"\\b(feat\\.?|ft\\.?|featuring)\\b", "", s)
    # remove punctuation
    s = re.sub(r"[^0-9a-z ]+", " ", s)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s)
    s = s.strip()
    return s

# Apply normalization to title and artist
merged['title_norm'] = merged['title'].fillna('').apply(normalize_text)
merged['artist_norm'] = merged['artist'].fillna('').apply(normalize_text)

# Create composite key
merged['song_key'] = (merged['title_norm'] + ' - ' + merged['artist_norm']).apply(lambda x: x.strip())

# Aggregate revenue by song_key
agg = merged.groupby('song_key').agg(
    total_revenue_usd=('total_revenue_usd', 'sum'),
    occurrences=('track_id', 'nunique')
).reset_index()

# Find top song_key by revenue
agg_sorted = agg.sort_values('total_revenue_usd', ascending=False)
if agg_sorted.empty:
    result = {
        'title': None,
        'artist': None,
        'total_revenue_usd': None,
        'contributing_track_ids': []
    }
else:
    top = agg_sorted.iloc[0]
    top_key = top['song_key']
    top_revenue = float(top['total_revenue_usd'])
    # Find representative title and artist: choose the most common exact pair among contributing rows
    contrib = merged[merged['song_key'] == top_key]
    # pick the mode of title and artist (most frequent non-empty)
    rep_title = contrib['title'].dropna().mode()
    rep_artist = contrib['artist'].dropna().mode()
    rep_title = rep_title.iloc[0] if not rep_title.empty else ''
    rep_artist = rep_artist.iloc[0] if not rep_artist.empty else ''
    contributing_track_ids = sorted(contrib['track_id'].unique(), key=lambda x: int(x))
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(top_revenue, 2),
        'contributing_track_ids': contributing_track_ids,
        'num_contributing_track_ids': len(contributing_track_ids)
    }

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gCRTSRV2gEM56hPkO5nwhlCp': 'file_storage/call_gCRTSRV2gEM56hPkO5nwhlCp.json', 'var_call_pQmdbFxKCu3mo89IzpliWuxI': [{'track_id': '14719', 'total_revenue_usd': '2522.82'}, {'track_id': '5124', 'total_revenue_usd': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue_usd': '2500.72'}, {'track_id': '6725', 'total_revenue_usd': '2489.81'}, {'track_id': '10377', 'total_revenue_usd': '2466.71'}, {'track_id': '5050', 'total_revenue_usd': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue_usd': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue_usd': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue_usd': '2428.2200000000003'}, {'track_id': '964', 'total_revenue_usd': '2425.61'}, {'track_id': '12984', 'total_revenue_usd': '2401.71'}, {'track_id': '6208', 'total_revenue_usd': '2385.0299999999997'}, {'track_id': '666', 'total_revenue_usd': '2382.74'}, {'track_id': '12620', 'total_revenue_usd': '2377.59'}, {'track_id': '19232', 'total_revenue_usd': '2368.7499999999995'}, {'track_id': '17757', 'total_revenue_usd': '2365.59'}, {'track_id': '3462', 'total_revenue_usd': '2359.23'}, {'track_id': '9639', 'total_revenue_usd': '2351.68'}, {'track_id': '18760', 'total_revenue_usd': '2349.33'}, {'track_id': '2516', 'total_revenue_usd': '2346.18'}]}

exec(code, env_args)
