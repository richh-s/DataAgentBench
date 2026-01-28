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

for col in ['title','artist','album','year']:
    if col not in tracks_df.columns:
        tracks_df[col] = ''

tracks_df['norm_title'] = tracks_df['title'].fillna('').apply(normalize_text)
tracks_df['norm_artist'] = tracks_df['artist'].fillna('').apply(normalize_text)
tracks_df['norm_album'] = tracks_df['album'].fillna('').apply(normalize_text)
tracks_df['norm_year'] = tracks_df['year'].fillna('').astype(str).apply(lambda x: re.sub(r"[^0-9]", "", x))

# Create grouping key: prefer normalized title; if empty, use artist+album+year
tracks_df['group_key'] = tracks_df['norm_title']
mask_empty = tracks_df['group_key']=='')
tracks_df.loc[mask_empty, 'group_key'] = (tracks_df.loc[mask_empty, 'norm_artist'] + '|' + 
                                         tracks_df.loc[mask_empty, 'norm_album'] + '|' + 
                                         tracks_df.loc[mask_empty, 'norm_year'])

# For small variations, also collapse keys by removing stopwords and short tokens
stopwords = set(['the','a','an','and','of','in','to','with','for','feat','ft'])
def simplify_key(k):
    toks = [t for t in k.split() if len(t)>2 and t not in stopwords]
    return ' '.join(toks)

tracks_df['simple_key'] = tracks_df['group_key'].apply(simplify_key)

# Final cluster id: use simple_key; if simple_key empty, fallback to group_key
def final_key(row):
    return row['simple_key'] if row['simple_key']!='' else row['group_key']

tracks_df['cluster_key'] = tracks_df.apply(final_key, axis=1)

# Build cluster map: assign cluster id as min track_id per cluster
cluster_groups = tracks_df.groupby('cluster_key')['track_id'].apply(list).to_dict()
cluster_map = {}
cluster_info = {}
for key, tid_list in cluster_groups.items():
    tid_list_int = [int(x) for x in tid_list]
    cid = min(tid_list_int)
    for tid in tid_list_int:
        cluster_map[tid] = cid
    subset = tracks_df[tracks_df['track_id'].isin(tid_list_int)]
    titles = subset['title'].replace(['','None','None '], pd.NA).dropna()
    rep_title = titles.mode().iloc[0] if len(titles)>0 else subset['title'].iloc[0]
    artists = subset['artist'].replace(['','None','None '], pd.NA).dropna()
    rep_artist = artists.mode().iloc[0] if len(artists)>0 else subset['artist'].iloc[0]
    cluster_info[cid] = {'track_ids': sorted(tid_list_int), 'title': rep_title, 'artist': rep_artist}

# Map sales to clusters and aggregate
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
