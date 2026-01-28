code = """import json
import pandas as pd
import re
import unicodedata

# Load data from storage files
tracks_path = var_call_FF4CgLpqWt3RzUHB6pSZuOHX
sales_path = var_call_VUH72T21U2oiAI8dWdyO9QPh
with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Normalize types
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
# Ensure columns exist
for col in ['title','artist','album','year']:
    if col not in tracks_df.columns:
        tracks_df[col] = ''

sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Normalization function
def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    # Unicode normalize
    s = unicodedata.normalize('NFKD', s)
    # Remove content in parentheses/brackets
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"\[[^]]*\]", "", s)
    # Lowercase
    s = s.lower()
    # Remove common live/remix/acoustic tags
    s = re.sub(r"\b(live|remix|acoustic|explicit|edit|version|feat\.|featuring|ft\.|instrumental)\b", "", s)
    # Remove punctuation
    s = re.sub(r"[^0-9a-z\s]", " ", s)
    # Collapse spaces
    s = re.sub(r"\s+", " ", s).strip()
    return s

tracks_df['norm_title'] = tracks_df['title'].fillna('').apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].fillna('').apply(normalize_text)
tracks_df['norm_album'] = tracks_df['album'].fillna('').apply(normalize_text)
tracks_df['norm_year'] = tracks_df['year'].fillna('').astype(str).apply(lambda x: re.sub(r"[^0-9]", "", x))

# Tokenize
tracks_df['title_tokens'] = tracks_df['norm_title'].apply(lambda x: set(x.split()))
tracks_df['artist_tokens'] = tracks_df['norm_artist'].apply(lambda x: set(x.split()))
tracks_df['album_tokens'] = tracks_df['norm_album'].apply(lambda x: set(x.split()))

# Jaccard similarity
def jaccard(a, b):
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter/union if union else 0.0

# Union-find for clustering
n = len(tracks_df)
parent = list(range(n))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a,b):
    ra = find(a); rb = find(b)
    if ra != rb:
        parent[rb] = ra

# Compare pairs
rows = tracks_df.reset_index()
for i in range(n):
    for j in range(i+1, n):
        ti = rows.loc[i]
        tj = rows.loc[j]
        title_sim = jaccard(ti['title_tokens'], tj['title_tokens'])
        artist_sim = jaccard(ti['artist_tokens'], tj['artist_tokens'])
        album_sim = jaccard(ti['album_tokens'], tj['album_tokens'])
        year_match = (ti['norm_year'] and tj['norm_year'] and ti['norm_year']==tj['norm_year'])
        # Heuristic scoring
        score = 0.7*title_sim + 0.2*artist_sim + 0.1*album_sim
        # Boost if year matches
        if year_match:
            score += 0.1
        # If titles are very similar or identical, or score high, union
        if title_sim >= 0.9 or score >= 0.75:
            union(i,j)
        else:
            # allow matches when title contains other and artist matches reasonably
            if (ti['norm_title'] and tj['norm_title']) and (ti['norm_title'] in tj['norm_title'] or tj['norm_title'] in ti['norm_title']):
                if artist_sim >= 0.5:
                    union(i,j)

# Build clusters
clusters = {}
for idx in range(n):
    root = find(idx)
    clusters.setdefault(root, []).append(rows.loc[idx]['track_id'])

# Map track_id to cluster id (use smallest track_id in cluster as cluster id)
cluster_map = {}
cluster_info = {}
for root, tid_list in clusters.items():
    cid = min(tid_list)
    for tid in tid_list:
        cluster_map[int(tid)] = cid
    # choose representative title/artist
    subset = tracks_df[tracks_df['track_id'].isin(tid_list)]
    # pick most common non-empty title
    titles = subset['title'].replace(['','None','None '], pd.NA).dropna()
    if len(titles)>0:
        rep_title = titles.mode().iloc[0]
    else:
        rep_title = subset['title'].iloc[0]
    artists = subset['artist'].replace(['','None','None '], pd.NA).dropna()
    if len(artists)>0:
        rep_artist = artists.mode().iloc[0]
    else:
        rep_artist = subset['artist'].iloc[0]
    cluster_info[cid] = {'track_ids': tid_list, 'title': rep_title, 'artist': rep_artist}

# Aggregate sales per cluster
sales_df['cluster_id'] = sales_df['track_id'].map(cluster_map)
# Some sales may reference tracks not in tracks_db; drop those
sales_with_cluster = sales_df.dropna(subset=['cluster_id']).copy()
sales_with_cluster['cluster_id'] = sales_with_cluster['cluster_id'].astype(int)
revenue_by_cluster = sales_with_cluster.groupby('cluster_id')['revenue_usd'].sum().reset_index()

if revenue_by_cluster.empty:
    result = {'error': 'No sales matched to tracks'}
else:
    # find top cluster
    top = revenue_by_cluster.sort_values('revenue_usd', ascending=False).iloc[0]
    cid = int(top['cluster_id'])
    total_revenue = float(top['revenue_usd'])
    info = cluster_info.get(cid, {})
    result = {
        'representative_track_id': cid,
        'title': info.get('title',''),
        'artist': info.get('artist',''),
        'constituent_track_ids': sorted(info.get('track_ids',[])),
        'total_revenue_usd': round(total_revenue, 2)
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FF4CgLpqWt3RzUHB6pSZuOHX': 'file_storage/call_FF4CgLpqWt3RzUHB6pSZuOHX.json', 'var_call_VUH72T21U2oiAI8dWdyO9QPh': 'file_storage/call_VUH72T21U2oiAI8dWdyO9QPh.json'}

exec(code, env_args)
