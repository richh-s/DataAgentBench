code = """import json
import pandas as pd
import re
import unicodedata

# Load data
tracks_path = var_call_FF4CgLpqWt3RzUHB6pSZuOHX
sales_path = var_call_VUH72T21U2oiAI8dWdyO9QPh
with open(tracks_path, 'r', encoding='utf-8') as f:
    tracks = json.load(f)
with open(sales_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Normalization
def normalize_text(s):
    if s is None:
        return ''
    s = str(s)
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"\[[^]]*\]", "", s)
    s = s.lower()
    s = re.sub(r"\b(live|remix|acoustic|explicit|edit|version|feat\.|featuring|ft\.|instrumental)\b", "", s)
    s = re.sub(r"[^0-9a-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

tracks_df['norm_title'] = tracks_df['title'].fillna('').apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].fillna('').apply(normalize_text)
tracks_df['norm_year'] = tracks_df['year'].fillna('').astype(str).apply(lambda x: re.sub(r"[^0-9]", "", x))

# Build unique normalized title buckets
title_groups = {}
for _, row in tracks_df.iterrows():
    nt = row['norm_title'] if row['norm_title']!='' else '__empty__'
    title_groups.setdefault(nt, []).append(int(row['track_id']))

unique_titles = list(title_groups.keys())
U = len(unique_titles)

# Token sets for titles and artists representative
def tokens(s):
    return set(s.split()) if s else set()

title_tokens = {t: tokens(t if t!='__empty__' else '') for t in unique_titles}
# Representative artist token set: choose most common artist among group
rep_artist_tokens = {}
for t in unique_titles:
    tids = title_groups[t]
    artists = tracks_df[tracks_df['track_id'].isin(tids)]['norm_artist'].replace('', pd.NA).dropna()
    if len(artists)>0:
        rep = artists.mode().iloc[0]
    else:
        rep = ''
    rep_artist_tokens[t] = tokens(rep)

# Jaccard
def jaccard(a,b):
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter/union if union else 0.0

# Union-find on unique title indices
parent = list(range(U))
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]
        x=parent[x]
    return x
def union(a,b):
    ra=find(a); rb=find(b)
    if ra!=rb:
        parent[rb]=ra

# Compare unique titles (much smaller)
for i in range(U):
    ti = unique_titles[i]
    for j in range(i+1, U):
        tj = unique_titles[j]
        t_sim = jaccard(title_tokens[ti], title_tokens[tj])
        a_sim = jaccard(rep_artist_tokens[ti], rep_artist_tokens[tj])
        # Heuristic: if titles identical or one contains the other
        if ti==tj or (ti in tj and len(ti)>3) or (tj in ti and len(tj)>3):
            union(i,j)
            continue
        # else if title jaccard high and artist similar
        if t_sim>=0.7 and a_sim>=0.3:
            union(i,j)
        elif t_sim>=0.85:
            union(i,j)

# Build clusters mapping to representative cluster id (min track id)
clusters = {}
for idx, t in enumerate(unique_titles):
    root = find(idx)
    clusters.setdefault(root, []).extend(title_groups[t])

cluster_map = {}
cluster_info = {}
for root, tid_list in clusters.items():
    cid = min(tid_list)
    for tid in tid_list:
        cluster_map[tid]=cid
    subset = tracks_df[tracks_df['track_id'].isin(tid_list)]
    titles = subset['title'].replace(['','None','None '], pd.NA).dropna()
    rep_title = titles.mode().iloc[0] if len(titles)>0 else subset['title'].iloc[0]
    artists = subset['artist'].replace(['','None','None '], pd.NA).dropna()
    rep_artist = artists.mode().iloc[0] if len(artists)>0 else subset['artist'].iloc[0]
    cluster_info[cid] = {'track_ids': sorted(tid_list), 'title': rep_title, 'artist': rep_artist}

# Map sales to clusters
sales_df['cluster_id'] = sales_df['track_id'].map(cluster_map)
sales_with_cluster = sales_df.dropna(subset=['cluster_id']).copy()
if sales_with_cluster.empty:
    result = {'error':'No sales matched to clusters'}
else:
    sales_with_cluster['cluster_id'] = sales_with_cluster['cluster_id'].astype(int)
    revenue_by_cluster = sales_with_cluster.groupby('cluster_id')['revenue_usd'].sum().reset_index()
    top = revenue_by_cluster.sort_values('revenue_usd', ascending=False).iloc[0]
    cid = int(top['cluster_id'])
    total_revenue = float(top['revenue_usd'])
    info = cluster_info.get(cid, {})
    result = {
        'representative_track_id': cid,
        'title': info.get('title',''),
        'artist': info.get('artist',''),
        'constituent_track_ids': info.get('track_ids',[]),
        'total_revenue_usd': round(total_revenue,2)
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FF4CgLpqWt3RzUHB6pSZuOHX': 'file_storage/call_FF4CgLpqWt3RzUHB6pSZuOHX.json', 'var_call_VUH72T21U2oiAI8dWdyO9QPh': 'file_storage/call_VUH72T21U2oiAI8dWdyO9QPh.json'}

exec(code, env_args)
