code = """import pandas as pd
import json
import unicodedata
import re

# Load data from storage-provided file paths
tracks = pd.read_json(var_call_y2KkmNMhc13Lswag58bRrq43)
sales = pd.read_json(var_call_QPobvzbfUoMTh79jiXCfDKoR)

# Ensure track_id is string for consistent merging
tracks['track_id'] = tracks['track_id'].astype(str)
sales['track_id'] = sales['track_id'].astype(str)

# Convert revenue to numeric
sales['revenue_usd'] = pd.to_numeric(sales['revenue_usd'], errors='coerce').fillna(0.0)

# Aggregate revenue by track_id
rev_by_track = sales.groupby('track_id', dropna=False)['revenue_usd'].sum().reset_index()
rev_by_track.rename(columns={'revenue_usd': 'total_revenue_usd'}, inplace=True)

# Merge with tracks
tracks_rev = pd.merge(tracks, rev_by_track, on='track_id', how='left')
tracks_rev['total_revenue_usd'] = tracks_rev['total_revenue_usd'].fillna(0.0)

# Normalization function
REMOVE_TERMS = ['live', 'remix', 'acoustic', 'version', 'edit', 'remastered', 'feat', 'featuring', 'with']

def normalize_text(s):
    if pd.isna(s):
        return ''
    s = str(s)
    s = unicodedata.normalize('NFKD', s)
    s = s.lower()
    # remove content in parentheses/brackets
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # remove punctuation
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    # remove common terms
    for term in REMOVE_TERMS:
        s = re.sub(r"\b" + re.escape(term) + r"\b", "", s)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Create normalized keys
tracks_rev['title_norm'] = tracks_rev['title'].apply(normalize_text)
tracks_rev['artist_norm'] = tracks_rev['artist'].apply(normalize_text)
tracks_rev['album_norm'] = tracks_rev['album'].apply(normalize_text)
tracks_rev['year_norm'] = tracks_rev['year'].fillna('').astype(str).apply(lambda x: re.sub(r"[^0-9]", "", x))

# Build a grouping key: prefer title+artist; if artist missing, fallback to title+album+year
def make_key(row):
    if row['artist_norm']:
        return row['title_norm'] + ' ### ' + row['artist_norm']
    else:
        return row['title_norm'] + ' ### ' + row['album_norm'] + ' ### ' + row['year_norm']

tracks_rev['group_key'] = tracks_rev.apply(make_key, axis=1)

# Group by group_key and sum revenue
grouped = tracks_rev.groupby('group_key').agg({
    'total_revenue_usd': 'sum',
    'track_id': lambda ids: list(ids),
    'title': lambda s: list(s),
    'artist': lambda s: list(s)
}).reset_index()

# Find the top group by revenue
top = grouped.sort_values('total_revenue_usd', ascending=False).iloc[0]

# Choose a representative title and artist: pick the title/artist from the track with max individual revenue within the group
candidate_ids = top['track_id']
subset = tracks_rev[tracks_rev['track_id'].isin(candidate_ids)]
rep_row = subset.sort_values('total_revenue_usd', ascending=False).iloc[0]

result = {
    'title': rep_row['title'] if not pd.isna(rep_row['title']) else None,
    'artist': rep_row['artist'] if not pd.isna(rep_row['artist']) else None,
    'total_revenue_usd': float(round(top['total_revenue_usd'], 2)),
    'contributing_track_ids': candidate_ids,
    'num_contributing_records': len(candidate_ids)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ICmYI2eTECtIaz5t0521ZbS2': ['tracks'], 'var_call_MQpdN9rP38Taqw3zizmhuUkr': ['sales'], 'var_call_y2KkmNMhc13Lswag58bRrq43': 'file_storage/call_y2KkmNMhc13Lswag58bRrq43.json', 'var_call_QPobvzbfUoMTh79jiXCfDKoR': 'file_storage/call_QPobvzbfUoMTh79jiXCfDKoR.json'}

exec(code, env_args)
