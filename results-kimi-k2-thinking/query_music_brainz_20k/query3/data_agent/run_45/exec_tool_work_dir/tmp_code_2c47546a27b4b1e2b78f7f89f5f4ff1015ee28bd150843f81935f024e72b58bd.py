code = """import json, pandas as pd, re, os

# Load data from files
sales_path = var_functions.query_db:22
tracks_path = var_functions.query_db:23

with open(sales_path) as sf:
    sales_data = json.load(sf)
with open(tracks_path) as tf:
    tracks_data = json.load(tf)

# Create DataFrames
sdf = pd.DataFrame(sales_data)
tdf = pd.DataFrame(tracks_data)

# Clean data
sdf['total_revenue'] = sdf['total_revenue'].astype(float)

# Simple normalization for entity resolution
def clean(txt):
    return re.sub(r'[^a-z0-9]', '', str(txt).lower())

tdf['merge_key'] = clean(tdf['title']) + '_' + clean(tdf['artist'])

# Group by key
key_map = tdf[['track_id', 'merge_key']].set_index('track_id')

# Add keys to sales
sdf['merge_key'] = sdf['track_id'].map(key_map['merge_key'])

# Sum revenue by key
key_revenue = sdf.groupby('merge_key')['total_revenue'].sum()

# Find top key
top_key = key_revenue.idxmax()
top_revenue = key_revenue.max()

# Get representative track details
tracks_for_key = tdf[tdf['merge_key'] == top_key]
rep_track = tracks_for_key.iloc[0]

result = {
    'title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'year': rep_track['year'],
    'total_revenue': round(float(top_revenue), 2)
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'test': 123}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json'}

exec(code, env_args)
