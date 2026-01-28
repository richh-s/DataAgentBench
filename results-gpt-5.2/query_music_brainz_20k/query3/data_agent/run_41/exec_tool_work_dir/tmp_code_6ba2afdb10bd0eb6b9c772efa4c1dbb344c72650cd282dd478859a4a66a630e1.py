code = """import json, pandas as pd

# Load sales totals
sales_src = var_call_6omYMJrDez0wdwyJ5DmwRzdi
if isinstance(sales_src, str):
    with open(sales_src, 'r', encoding='utf-8') as f:
        sales = json.load(f)
else:
    sales = sales_src

tracks_src = var_call_8rL6LMwTG2QZAvxDfB95YU9T
if isinstance(tracks_src, str):
    with open(tracks_src, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
else:
    tracks = tracks_src

sales_df = pd.DataFrame(sales)
tracks_df = pd.DataFrame(tracks)

# types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['total_revenue_usd'] = sales_df['total_revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Basic entity resolution: canonical key based on normalized title+artist+album
import re

def norm(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() in ['none', 'null', 'nan']:
        return ''
    s = s.lower().strip()
    s = re.sub(r'\s+', ' ', s)
    # remove common decorations
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'\[.*?\]', '', s)
    s = re.sub(r'\s+-\s+.*$', '', s)  # remove trailing after dash
    s = re.sub(r"[^a-z0-9 ]+", '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

tracks_df['n_title'] = tracks_df['title'].map(norm)
tracks_df['n_artist'] = tracks_df['artist'].map(norm)
tracks_df['n_album'] = tracks_df['album'].map(norm)

# Build entity key
tracks_df['entity_key'] = tracks_df['n_title'] + '|' + tracks_df['n_artist'] + '|' + tracks_df['n_album']

# attach sales totals
df = sales_df.merge(tracks_df[['track_id','title','artist','album','year','entity_key']], on='track_id', how='left')

# group by entity
entity_rev = df.groupby('entity_key', dropna=False)['total_revenue_usd'].sum().reset_index()
entity_rev = entity_rev.sort_values('total_revenue_usd', ascending=False)

top_key = entity_rev.iloc[0]['entity_key']
top_rev = float(entity_rev.iloc[0]['total_revenue_usd'])

# pick a representative track row (max revenue track_id within entity)
rep = df[df['entity_key']==top_key].sort_values('total_revenue_usd', ascending=False).iloc[0]

answer = {
    'title': None if pd.isna(rep['title']) else str(rep['title']),
    'artist': None if pd.isna(rep['artist']) else str(rep['artist']),
    'album': None if pd.isna(rep['album']) else str(rep['album']),
    'total_revenue_usd': round(top_rev, 2)
}

print('__RESULT__:')
print(json.dumps(answer, ensure_ascii=False))"""

env_args = {'var_call_6omYMJrDez0wdwyJ5DmwRzdi': 'file_storage/call_6omYMJrDez0wdwyJ5DmwRzdi.json', 'var_call_8rL6LMwTG2QZAvxDfB95YU9T': 'file_storage/call_8rL6LMwTG2QZAvxDfB95YU9T.json'}

exec(code, env_args)
