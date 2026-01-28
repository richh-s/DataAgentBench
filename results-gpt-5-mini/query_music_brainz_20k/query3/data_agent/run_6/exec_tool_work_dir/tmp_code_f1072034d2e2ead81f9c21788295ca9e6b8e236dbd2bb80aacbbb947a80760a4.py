code = """import json
import pandas as pd
import unicodedata
from difflib import SequenceMatcher

# Load data from provided storage file paths
tracks_path = var_call_pbno0vllvG9W6yX5kYZnPMj7
sales_path = var_call_WQCI5VPUk7hLG83cBtbIV0eB

with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Ensure correct dtypes
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce').fillna(0.0)
sales_df['track_id'] = sales_df['track_id'].astype(str)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

# Normalize function
import re

def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = s.strip()
    if s.lower() in ('none', 'nan', "nan", ''):
        return ''
    # remove parenthetical/bracketed content
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\[.*?\]", "", s)
    # if contains ' - ' and left looks like artist and right like title, try to keep right
    if ' - ' in s:
        parts = [p.strip() for p in s.split(' - ', 1)]
        # Heuristic: if left contains letters and no spaces? We'll prefer right side as title
        if len(parts[0].split()) <= 3:
            s = parts[1]
    # remove punctuation
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r"[^0-9a-zA-Z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    s = s.lower().strip()
    return s

tracks_df['norm_title'] = tracks_df['title'].apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)
tracks_df['orig_title'] = tracks_df['title'].fillna('').astype(str)
tracks_df['orig_artist'] = tracks_df['artist'].fillna('').astype(str)

# Build clusters of tracks by normalized title+artist similarity
unique_records = tracks_df[['track_id', 'norm_title', 'norm_artist', 'orig_title', 'orig_artist']].to_dict(orient='records')
clusters = []  # list of lists of track_ids
cluster_reps = []

for rec in unique_records:
    tid = rec['track_id']
    nt = rec['norm_title']
    na = rec['norm_artist']
    if nt == '':
        # fallback to using orig title raw
        nt = rec['orig_title'].lower()
    placed = False
    for ci, rep in enumerate(cluster_reps):
        # compute similarity between this record and rep
        rep_nt = rep['norm_title']
        rep_na = rep['norm_artist']
        title_sim = SequenceMatcher(None, nt, rep_nt).ratio() if nt and rep_nt else 0.0
        artist_sim = SequenceMatcher(None, na, rep_na).ratio() if na and rep_na else 0.0
        score = 0.75 * title_sim + 0.25 * artist_sim
        if score >= 0.90:
            clusters[ci].append(rec)
            placed = True
            break
    if not placed:
        clusters.append([rec])
        cluster_reps.append({'norm_title': nt, 'norm_artist': na})

# For each cluster, determine representative title and artist (most common orig)
cluster_summaries = []
for cluster in clusters:
    # collect track_ids
    tids = [c['track_id'] for c in cluster]
    titles = [c['orig_title'] for c in cluster if c['orig_title']]
    artists = [c['orig_artist'] for c in cluster if c['orig_artist']]
    # choose representative as most common non-empty title/artist, or first
    rep_title = titles[0] if titles else ''
    rep_artist = artists[0] if artists else ''
    if titles:
        rep_title = max(set(titles), key=titles.count)
    if artists:
        rep_artist = max(set(artists), key=artists.count)
    cluster_summaries.append({'track_ids': tids, 'rep_title': rep_title, 'rep_artist': rep_artist})

# Map track_id to cluster id
track_to_cluster = {}
for i, cs in enumerate(cluster_summaries):
    for t in cs['track_ids']:
        track_to_cluster[str(t)] = i

# Add cluster id to sales by joining via track_id
sales_df['cluster_id'] = sales_df['track_id'].map(track_to_cluster)
# Some sales may reference tracks not present in tracks_df; treat cluster as None
sales_df['cluster_id'] = sales_df['cluster_id'].fillna(-1).astype(int)

# Aggregate revenue by cluster
agg = sales_df.groupby('cluster_id', dropna=False)['revenue_usd'].sum().reset_index()
# merge representative info
agg['rep_title'] = agg['cluster_id'].map(lambda x: cluster_summaries[x]['rep_title'] if x >=0 and x < len(cluster_summaries) else '')
agg['rep_artist'] = agg['cluster_id'].map(lambda x: cluster_summaries[x]['rep_artist'] if x >=0 and x < len(cluster_summaries) else '')

# Find max revenue cluster (exclude cluster_id -1 if present unless it's max)
max_row = agg.loc[agg['revenue_usd'].idxmax()]
max_title = max_row['rep_title'] if pd.notna(max_row['rep_title']) and max_row['rep_title']!='' else 'Unknown Title'
max_artist = max_row['rep_artist'] if pd.notna(max_row['rep_artist']) and max_row['rep_artist']!='' else 'Unknown Artist'
max_revenue = float(max_row['revenue_usd'])
# Round to 2 decimals
max_revenue_rounded = round(max_revenue, 2)

final_text = f"{max_title} by {max_artist} generated ${max_revenue_rounded} total revenue across all stores and countries."

# Prepare JSON-serializable output
out = {
    'title': max_title,
    'artist': max_artist,
    'total_revenue_usd': max_revenue_rounded,
    'message': final_text
}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_5748BnJF4cSKibjMEy6OEUqa': ['tracks'], 'var_call_HpVP6a6szkJm8nSPsFcQLNPg': ['sales'], 'var_call_pbno0vllvG9W6yX5kYZnPMj7': 'file_storage/call_pbno0vllvG9W6yX5kYZnPMj7.json', 'var_call_WQCI5VPUk7hLG83cBtbIV0eB': 'file_storage/call_WQCI5VPUk7hLG83cBtbIV0eB.json'}

exec(code, env_args)
