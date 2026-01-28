code = """import json
import pandas as pd
import re
import unicodedata

# Load data from storage-provided file paths
with open(var_call_h5xIywaIgLYcalDZbgbuUAVN, 'r', encoding='utf-8') as f:
    tracks_list = json.load(f)
with open(var_call_ZMyhlPldCrwGICSgQ8DiATd3, 'r', encoding='utf-8') as f:
    sales_list = json.load(f)

tracks = pd.DataFrame(tracks_list)
sales = pd.DataFrame(sales_list)

# Clean types
tracks['track_id'] = tracks['track_id'].astype(str)
sales['track_id'] = sales['track_id'].astype(str)

# Convert revenue_usd to float
sales['revenue_usd'] = pd.to_numeric(sales['revenue_usd'], errors='coerce').fillna(0.0)

# Normalization function for text
import math

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() in ('none', 'nan', "nan"):
        return ''
    # Unicode normalize
    s = unicodedata.normalize('NFKD', s)
    # Remove parenthetical/bracketed content
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # Remove punctuation except spaces
    s = re.sub(r"[^\w\s]", " ", s)
    # Remove common words like live, remix, acoustic, version, remaster, edit, feat, ft
    s = re.sub(r"\b(live|remix|acoustic|version|remaster|edit|feat|ft|instrumental)\b", "", s, flags=re.IGNORECASE)
    # Collapse whitespace and lowercase
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s

# Create normalized fields
tracks['norm_title'] = tracks['title'].apply(normalize_text)
tracks['norm_artist'] = tracks['artist'].apply(normalize_text)
tracks['norm_album'] = tracks['album'].apply(normalize_text)
tracks['norm_year'] = tracks['year'].fillna('').astype(str).apply(lambda x: re.sub('[^0-9]', '', x))

# Build entity key: prefer title+artist, fallback to title only
def make_entity_key(row):
    if row['norm_title']:
        if row['norm_artist']:
            return row['norm_title'] + ' ||| ' + row['norm_artist']
        else:
            return row['norm_title']
    else:
        # fallback to album+year
        key = (row['norm_album'] or '') + ' ||| ' + (row['norm_year'] or '')
        return key

tracks['entity_key'] = tracks.apply(make_entity_key, axis=1)

# Map track_id to entity_key
track_to_entity = tracks.set_index('track_id')['entity_key'].to_dict()

# Attach entity_key to sales
sales['entity_key'] = sales['track_id'].map(track_to_entity).fillna('')

# Aggregate revenue by entity_key
rev_by_entity = sales.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()
rev_by_entity = rev_by_entity.sort_values('revenue_usd', ascending=False)

# Get top entity
top = rev_by_entity.iloc[0]
top_key = top['entity_key']
top_revenue = float(top['revenue_usd'])

# Gather representative metadata for the top entity
group_tracks = tracks[tracks['entity_key'] == top_key]
# Choose the title/artist/album that appears most frequently and is non-empty
def most_common_nonempty(series):
    vals = series.fillna('').astype(str)
    vals = vals[vals.str.lower() != 'none']
    vals = vals[vals.str.strip() != '']
    if vals.empty:
        return ''
    return vals.value_counts().idxmax()

rep_title = most_common_nonempty(group_tracks['title'])
rep_artist = most_common_nonempty(group_tracks['artist'])
rep_album = most_common_nonempty(group_tracks['album'])
rep_year = most_common_nonempty(group_tracks['year'])

# Also gather contributing track_ids and per-track revenues
contrib = sales[sales['entity_key'] == top_key].groupby('track_id')['revenue_usd'].sum().reset_index()
contrib = contrib.sort_values('revenue_usd', ascending=False)
contrib_list = contrib.to_dict(orient='records')

result = {
    'representative_title': rep_title,
    'representative_artist': rep_artist,
    'representative_album': rep_album,
    'representative_year': rep_year,
    'entity_key': top_key,
    'total_revenue_usd': round(top_revenue, 2),
    'contributing_tracks': contrib_list,
    'num_distinct_track_records': int(group_tracks.shape[0])
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_h5xIywaIgLYcalDZbgbuUAVN': 'file_storage/call_h5xIywaIgLYcalDZbgbuUAVN.json', 'var_call_ZMyhlPldCrwGICSgQ8DiATd3': 'file_storage/call_ZMyhlPldCrwGICSgQ8DiATd3.json'}

exec(code, env_args)
