code = """import json, pandas as pd
from pathlib import Path

# Load full results
tracks_path = Path(var_call_RZhHOEd0CDHnslZTravcDMej)
sales_path = Path(var_call_DaSsjpZTGyCSfcfaIqey6htQ)
tracks = json.loads(tracks_path.read_text())
sales = json.loads(sales_path.read_text())

tracks_df = pd.DataFrame(tracks)
sales_df = pd.DataFrame(sales)

# Convert numeric columns
tracks_df['track_id'] = tracks_df['track_id'].astype(int)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Basic blocking key based on normalized title and artist (casefold, keep alnum)
import re

def norm(s):
    if s is None:
        return ''
    s = str(s)
    s = s.casefold()
    s = re.sub(r"[^0-9a-z]+", "", s)
    return s

tracks_df['title_norm'] = tracks_df['title'].apply(norm)
tracks_df['artist_norm'] = tracks_df['artist'].apply(norm)

# Entity key: title+artist; if artist missing, just title
tracks_df['entity_key'] = tracks_df.apply(
    lambda r: r['title_norm'] if (not r['artist_norm']) else r['title_norm'] + '|' + r['artist_norm'], axis=1
)

# Map each track_id to canonical entity_key
track_to_entity = tracks_df.set_index('track_id')['entity_key']

sales_df['entity_key'] = sales_df['track_id'].map(track_to_entity)

# Aggregate revenue per entity_key
agg = sales_df.groupby('entity_key', dropna=False)['revenue_usd'].sum().reset_index()

# Exclude empty entity_key if any
agg_nonempty = agg[agg['entity_key'].notna() & (agg['entity_key'] != '')]

# Find best entity
best = agg_nonempty.sort_values('revenue_usd', ascending=False).iloc[0]

best_key = best['entity_key']

# Decode key back to a representative song (pick most frequent or first)
if '|' in best_key:
    t_norm, a_norm = best_key.split('|', 1)
else:
    t_norm, a_norm = best_key, ''

cand = tracks_df[tracks_df['entity_key'] == best_key]

# Choose representative with longest album name as heuristic
rep = cand.sort_values(['album'], ascending=[True]).iloc[0]

result = {
    'title': rep['title'],
    'artist': rep['artist'],
    'album': rep['album'],
    'total_revenue_usd': round(float(best['revenue_usd']), 2)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RZhHOEd0CDHnslZTravcDMej': 'file_storage/call_RZhHOEd0CDHnslZTravcDMej.json', 'var_call_DaSsjpZTGyCSfcfaIqey6htQ': 'file_storage/call_DaSsjpZTGyCSfcfaIqey6htQ.json'}

exec(code, env_args)
