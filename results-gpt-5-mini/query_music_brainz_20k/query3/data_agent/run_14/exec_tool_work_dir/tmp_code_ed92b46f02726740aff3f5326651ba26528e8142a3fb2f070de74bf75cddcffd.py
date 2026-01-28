code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_DFWB6NjZoKICRqEJ50q5d5Ba, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_gkcuTbrQPQxUN5BnGUzFfIjU, 'r', encoding='utf-8') as f:
    sales = json.load(f)

# Create DataFrames
df_tracks = pd.DataFrame(tracks)
df_sales = pd.DataFrame(sales)

# Normalize types
if 'track_id' in df_tracks.columns:
    df_tracks['track_id'] = df_tracks['track_id'].astype(str)
if 'track_id' in df_sales.columns:
    df_sales['track_id'] = df_sales['track_id'].astype(str)

# Convert revenue to float
if 'revenue_usd' in df_sales.columns:
    df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)

# Normalization function
_non_alnum_re = re.compile(r"[^0-9a-z ]+")
_multi_space_re = re.compile(r"\s+")
_parentheses_re = re.compile(r"\(.*?\)")

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ('none', 'nan', 'null', '', '[unknown]'):
        return ''
    # remove parenthetical content
    s = _parentheses_re.sub('', s)
    s = s.lower()
    # replace non-alphanumeric with space
    s = _non_alnum_re.sub(' ', s)
    s = _multi_space_re.sub(' ', s)
    s = s.strip()
    return s

# Build resolution key: prefer title+artist when possible
df_tracks['title_norm'] = df_tracks['title'].apply(normalize_text)
df_tracks['artist_norm'] = df_tracks['artist'].apply(normalize_text)
df_tracks['album_norm'] = df_tracks['album'].apply(normalize_text)

def build_key(row):
    t = row['title_norm']
    a = row['artist_norm']
    if a:
        return t + '||' + a
    else:
        return t

df_tracks['entity_key'] = df_tracks.apply(build_key, axis=1)

# Map track_id -> entity_key
trackid_to_key = df_tracks.set_index('track_id')['entity_key'].to_dict()

# Attach entity keys to sales
# For any sales track_id not in tracks, use its raw track_id as key
df_sales['entity_key'] = df_sales['track_id'].map(trackid_to_key).fillna(df_sales['track_id'].astype(str))

# Aggregate revenue by entity_key
agg = df_sales.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()
# Find max revenue
max_rev = agg['revenue_usd'].max()
max_rows = agg[agg['revenue_usd'] == max_rev]

results = []
for _, row in max_rows.iterrows():
    key = row['entity_key']
    total = float(row['revenue_usd'])
    # find all track_ids that map to this key
    track_ids = [tid for tid, k in trackid_to_key.items() if k == key]
    # pick representative metadata from df_tracks for these track_ids
    rep = df_tracks[df_tracks['track_id'].isin(track_ids)]
    if not rep.empty:
        # choose the most common non-empty title and artist
        title = rep['title'].replace('None', '').replace('', pd.NA).dropna().mode()
        artist = rep['artist'].replace('None', '').replace('', pd.NA).dropna().mode()
        title = title.iloc[0] if not title.empty else ''
        artist = artist.iloc[0] if not artist.empty else ''
    else:
        # no matching tracks (rare)
        title = ''
        artist = ''
    results.append({
        'entity_key': key,
        'representative_title': title,
        'representative_artist': artist,
        'track_ids': track_ids,
        'total_revenue_usd': total
    })

# If multiple ties, include all
output = {
    'max_total_revenue_usd': float(max_rev),
    'winners': results
}

import json as _json
print("__RESULT__:")
print(_json.dumps(output))"""

env_args = {'var_call_DFWB6NjZoKICRqEJ50q5d5Ba': 'file_storage/call_DFWB6NjZoKICRqEJ50q5d5Ba.json', 'var_call_gkcuTbrQPQxUN5BnGUzFfIjU': 'file_storage/call_gkcuTbrQPQxUN5BnGUzFfIjU.json'}

exec(code, env_args)
