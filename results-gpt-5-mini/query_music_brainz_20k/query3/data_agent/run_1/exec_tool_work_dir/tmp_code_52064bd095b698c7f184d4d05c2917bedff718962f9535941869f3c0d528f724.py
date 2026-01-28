code = """import json
import pandas as pd
import re

# Load data from storage-provided JSON file paths
with open(var_call_X8S6xTQ6dOn4RL5Q6ptEJzFa, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(var_call_5RSuOqA5yx9xs0qGFly7Ltah, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure correct dtypes
if 'track_id' in tracks_df.columns:
    tracks_df['track_id'] = tracks_df['track_id'].astype(str)
if 'track_id' in sales_df.columns:
    sales_df['track_id'] = sales_df['track_id'].astype(str)

# Convert revenue to float
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0)

# Normalization helper
REMOVE_WORDS = [r'live', r'remix', r'acoustic', r'remaster', r'intro', r'outro', r'edit', r'version', r'featuring', r'feat', r'ft']

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ('none', '', 'nan', "nan"):
        return ''
    # remove content in parentheses
    s = re.sub(r"\([^)]*\)", " ", s)
    # replace common separators with space
    s = s.replace('-', ' ').replace('_', ' ').replace('/', ' ')
    # lowercase
    s = s.lower()
    # remove punctuation
    s = re.sub(r"[^a-z0-9& ]+", ' ', s)
    # remove unwanted words
    for w in REMOVE_WORDS:
        s = re.sub(r"\b" + w + r"\b", ' ', s)
    # replace & with and
    s = s.replace('&', ' and ')
    # collapse whitespace
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# Build normalized keys
tracks_df['norm_title'] = tracks_df['title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)
tracks_df['norm_album'] = tracks_df['album'].apply(normalize_text)

# Create grouping key: prefer title+artist; if artist missing use title+album
def make_key(row):
    if row['norm_title'] == '':
        return ''
    if row['norm_artist'] != '':
        return row['norm_title'] + '||' + row['norm_artist']
    elif row['norm_album'] != '':
        return row['norm_title'] + '||' + row['norm_album']
    else:
        return row['norm_title']

tracks_df['entity_key'] = tracks_df.apply(make_key, axis=1)

# For empty entity_key, fallback to track_id to avoid losing rows
tracks_df.loc[tracks_df['entity_key'] == '', 'entity_key'] = 'trackid||' + tracks_df.loc[tracks_df['entity_key'] == '', 'track_id']

# Group track_ids by entity_key
grouped = tracks_df.groupby('entity_key').agg({
    'track_id': lambda ids: list(ids),
    'title': lambda s: s.dropna().astype(str).tolist(),
    'artist': lambda s: s.dropna().astype(str).tolist()
}).reset_index()

# Build representative title and artist for each group: choose the most common non-empty, else longest
def choose_rep(vals):
    vals = [v for v in vals if str(v).strip().lower() not in ('', 'none', "nan")]
    if not vals:
        return ''
    # most common
    from collections import Counter
    c = Counter(vals)
    most_common = c.most_common()
    # pick the most frequent; break ties by longest length
    top_count = most_common[0][1]
    candidates = [v for v, cnt in most_common if cnt == top_count]
    candidates.sort(key=lambda x: (-len(str(x)), x))
    return candidates[0]

grouped['rep_title'] = grouped['title'].apply(choose_rep)
grouped['rep_artist'] = grouped['artist'].apply(choose_rep)

# Map track_id to entity_key
trackid_to_key = {}
for _, row in grouped.iterrows():
    for tid in row['track_id']:
        trackid_to_key[str(tid)] = row['entity_key']

# Map sales to entity_key
sales_df['entity_key'] = sales_df['track_id'].map(lambda x: trackid_to_key.get(str(x), 'unknown'))

# Sum revenue by entity_key
revenue_by_entity = sales_df.groupby('entity_key', dropna=False).agg({'revenue_usd': 'sum'}).reset_index()

# Join representative titles/artists
res = revenue_by_entity.merge(grouped[['entity_key','rep_title','rep_artist','track_id']], on='entity_key', how='left')

# Replace unknown entity names if missing
res['rep_title'] = res['rep_title'].fillna('')
res['rep_artist'] = res['rep_artist'].fillna('')
res['track_id'] = res['track_id'].apply(lambda x: x if isinstance(x, list) else [])

# Find max revenue
res['revenue_usd'] = res['revenue_usd'].astype(float)
max_row = res.loc[res['revenue_usd'].idxmax()]

result = {
    'title': max_row['rep_title'] if max_row['rep_title'] != '' else None,
    'artist': max_row['rep_artist'] if max_row['rep_artist'] != '' else None,
    'track_ids': max_row['track_id'],
    'total_revenue_usd': round(float(max_row['revenue_usd']), 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_X8S6xTQ6dOn4RL5Q6ptEJzFa': 'file_storage/call_X8S6xTQ6dOn4RL5Q6ptEJzFa.json', 'var_call_5RSuOqA5yx9xs0qGFly7Ltah': 'file_storage/call_5RSuOqA5yx9xs0qGFly7Ltah.json'}

exec(code, env_args)
