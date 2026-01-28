code = """import json
import pandas as pd
import re

# Read the data
sales_file_path = var_functions.query_db:4
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

tracks_file_path = var_functions.query_db:5
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

sdf = pd.DataFrame(sales_data)
tdf = pd.DataFrame(tracks_data)

# Convert revenue to numeric
sdf[['revenue_usd']] = sdf[['revenue_usd']].astype(float)

# Total revenue per track
track_revenue = sdf.groupby('track_id')['revenue_usd'].sum().reset_index().sort_values('revenue_usd', ascending=False)

# Merge track info
tracks_for_merge = tdf[['track_id', 'title', 'artist', 'album', 'year']].copy()
merged = pd.merge(track_revenue, tracks_for_merge, on='track_id', how='inner')

# Normalize for entity resolution
def normalize_string(s):
    if pd.isna(s) or s is None or str(s) == 'None':
        return ''
    return str(s).lower().strip()

def normalize_year(s):
    if pd.isna(s) or s is None or str(s) == 'None':
        return None
    s = str(s)
    import re
    match = re.search(r'\d{4}', s)
    if match:
        return match.group(0)
    match = re.search(r"(\d{2})", s)
    if match:
        year = int(match.group(1))
        return f"19{year:02d}" if year >= 40 else f"20{year:02d}"
    return None

tdf['norm_title'] = tdf['title'].apply(normalize_string)
tdf['norm_artist'] = tdf['artist'].apply(normalize_string)
tdf['norm_album'] = tdf['album'].apply(normalize_string)
tdf['norm_year'] = tdf['year'].apply(normalize_year)

# Group
tdf['group_key'] = tdf['norm_title'] + ':' + tdf['norm_artist'] + ':' + tdf['norm_album'] + ':' + tdf['norm_year'].astype(str)

# Calculate revenue per group
track_groups = tdf[['track_id', 'group_key']].copy()
revenue_with_groups = pd.merge(track_revenue, track_groups, on='track_id', how='inner')
group_revenue = revenue_with_groups.groupby('group_key')['revenue_usd'].sum().reset_index().sort_values('revenue_usd', ascending=False)

result = {'sales_records': int(len(sdf)), 'tracks_records': int(len(tdf)), 'top_revenue': float(group_revenue.iloc[0]['revenue_usd']) if len(group_revenue) > 0 else 0}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
