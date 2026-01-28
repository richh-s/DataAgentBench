code = """import json
import pandas as pd
import re
import unicodedata

# Load data from storage files
tracks_path = var_call_hkJ77bG7biqKdHJh1ixzrgci
sales_path = var_call_BSDmerZPa9ANnvWl0BQOfEYY

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize types
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)

# Convert revenue to float, coerce errors to 0
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0)

# Sum revenue per track_id
revenue_by_track = sales_df.groupby('track_id', as_index=False)['revenue_usd'].sum()
revenue_by_track.rename(columns={'revenue_usd': 'total_revenue_usd'}, inplace=True)

# Merge with tracks
merged = pd.merge(tracks_df, revenue_by_track, on='track_id', how='left')
merged['total_revenue_usd'] = merged['total_revenue_usd'].fillna(0.0)

# Normalization function for entity resolution
REMOVE_WORDS = set(['live','remix','acoustic','version','feat','featuring','ft','remastered','original','edit','live)', 'live:'])

def normalize_text(s):
    if s is None:
        return ''
    if isinstance(s, float) and pd.isna(s):
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() == 'none' or s == '':
        return ''
    # Unicode normalize
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', 'ignore').decode('ascii')
    s = s.lower()
    # Remove content in parentheses
    s = re.sub(r"\(.*?\)", "", s)
    # Remove content after '/' which often are extraneous
    s = s.split('/')[0]
    # Replace dashes that may separate artist and title
    s = s.replace(' - ', ' ')  # replace common separator
    s = s.replace('-', ' ')
    # Remove common descriptors
    tokens = re.split(r"\s+", s)
    tokens = [t for t in tokens if t not in REMOVE_WORDS]
    s = ' '.join(tokens)
    # Remove punctuation
    s = re.sub(r"[^0-9a-z ]", ' ', s)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# Create normalized title and artist
merged['norm_title'] = merged['title'].apply(normalize_text)
merged['norm_artist'] = merged['artist'].apply(normalize_text)

# If artist is empty, rely on title only; create grouping key
def make_key(row):
    if row['norm_artist']:
        return row['norm_title'] + ' ||| ' + row['norm_artist']
    else:
        return row['norm_title']

merged['group_key'] = merged.apply(make_key, axis=1)

# Group by group_key and sum revenue
grouped = merged.groupby('group_key', as_index=False).agg({
    'total_revenue_usd': 'sum',
    'track_id': lambda x: list(x),
    'title': lambda x: list(x),
    'artist': lambda x: list(x),
    'norm_title': 'first',
    'norm_artist': 'first'
})

# Find top group
top_idx = grouped['total_revenue_usd'].idxmax()
if pd.isna(top_idx):
    result = {
        'title': None,
        'artist': None,
        'total_revenue_usd': 0.0,
        'member_track_ids': []
    }
else:
    top_row = grouped.loc[top_idx]
    # Choose a representative title/artist: pick the one from the member with highest individual revenue
    member_ids = top_row['track_id']
    # Filter merged for these ids and get the track_id with max revenue
    members = merged[merged['track_id'].isin(member_ids)].copy()
    rep = members.sort_values('total_revenue_usd', ascending=False).iloc[0]
    rep_title = rep['title'] if rep['title'] not in (None, 'None') else ''
    rep_artist = rep['artist'] if rep['artist'] not in (None, 'None') else ''
    result = {
        'title': rep_title,
        'artist': rep_artist,
        'total_revenue_usd': round(float(top_row['total_revenue_usd']), 2),
        'member_track_ids': [int(x) for x in member_ids]
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CIXTBcO2saIjAAMFLVAvpDX8': ['tracks'], 'var_call_OaBt3DzcjPno219VmwWn7j02': ['sales'], 'var_call_hkJ77bG7biqKdHJh1ixzrgci': 'file_storage/call_hkJ77bG7biqKdHJh1ixzrgci.json', 'var_call_BSDmerZPa9ANnvWl0BQOfEYY': 'file_storage/call_BSDmerZPa9ANnvWl0BQOfEYY.json'}

exec(code, env_args)
