code = """import json
import pandas as pd
import re

# Read data
with open(var_functions.query_db:4, 'r') as f:
    sales_data = json.load(f)
with open(var_functions.query_db:5, 'r') as f:
    tracks_data = json.load(f)

sdf = pd.DataFrame(sales_data)
tdf = pd.DataFrame(tracks_data)

sdf['revenue_usd'] = sdf['revenue_usd'].astype(float)

# Calculate total revenue per track_id
track_revenue = sdf.groupby('track_id')['revenue_usd'].sum().reset_index()
track_revenue = track_revenue.sort_values('revenue_usd', ascending=False)

# Normalize strings
def norm_str(s):
    if pd.isna(s) or s is None or str(s) == 'None':
        return ''
    return str(s).lower().strip()

def norm_year(s):
    if pd.isna(s) or s is None or str(s) == 'None':
        return 'unknown'
    s = str(s)
    m = re.search(r'(\d{4})', s)
    if m:
        return m.group(1)
    m = re.search(r'(\d{2})', s)
    if m:
        y = int(m.group(1))
        return f"19{y:02d}" if y >= 40 else f"20{y:02d}"
    return 'unknown'

tdf['n_title'] = tdf['title'].apply(norm_str)
tdf['n_artist'] = tdf['artist'].apply(norm_str)
tdf['n_album'] = tdf['album'].apply(norm_str)
tdf['n_year'] = tdf['year'].apply(norm_year)

# Create grouping key
tdf['gkey'] = tdf['n_title'] + '|' + tdf['n_artist'] + '|' + tdf['n_album'] + '|' + tdf['n_year']

# Join and aggregate by group
merged = pd.merge(track_revenue, tdf[['track_id', 'gkey']], on='track_id', how='inner')
group_revenue = merged.groupby('gkey')['revenue_usd'].sum().reset_index()
group_revenue = group_revenue.sort_values('revenue_usd', ascending=False)

# Get top group
top_gkey = group_revenue.iloc[0]['gkey']
top_revenue = float(group_revenue.iloc[0]['revenue_usd'])

# Get tracks in top group
top_tracks = tdf[tdf['gkey'] == top_gkey]

# Pick best representative
def pick_best(tracks, col):
    vals = [v for v in tracks[col] if v is not None and str(v) != 'None' and str(v).strip()]
    if not vals:
        return None
    return max(vals, key=lambda x: len(str(x)))

best = {
    'title': pick_best(top_tracks, 'title'),
    'artist': pick_best(top_tracks, 'artist'),
    'album': pick_best(top_tracks, 'album'),
    'year': pick_best(top_tracks, 'year')
}

result = {
    'song_title': best['title'],
    'artist': best['artist'],
    'album': best['album'],
    'year': best['year'],
    'total_revenue_usd': top_revenue
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'test': 123}}

exec(code, env_args)
