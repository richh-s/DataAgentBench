code = """import json
import pandas as pd
import numpy as np

# Load full sales data
sales_file = locals()['var_functions.query_db:5']
if isinstance(sales_file, str) and sales_file.endswith('.json'):
    with open(sales_file, 'r') as f:
        sales = json.load(f)
else:
    sales = sales_file

# Load full tracks data
tracks_file = locals()['var_functions.query_db:12']
if isinstance(tracks_file, str) and tracks_file.endswith('.json'):
    with open(tracks_file, 'r') as f:
        tracks = json.load(f)
else:
    tracks = tracks_file

df_sales = pd.DataFrame(sales)
df_tracks = pd.DataFrame(tracks)

# Convert data types 
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'], errors='coerce')
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

def clean_value(x):
    if pd.isna(x) or x is None or str(x) == 'None' or str(x).strip() == '':
        return ''
    return str(x).lower().strip()

for col in ['title', 'artist']:
    df_tracks[f'{col}_clean'] = df_tracks[col].apply(clean_value)

valid_tracks = df_tracks[
    (df_tracks['title_clean'] != '') & 
    (df_tracks['artist_clean'] != '') & 
    (df_tracks['title_clean'] != 'none') & 
    (df_tracks['artist_clean'] != 'none') &
    (df_tracks['title_clean'] != '011- ') & 
    (df_tracks['title_clean'] != '00-1') &
    (df_tracks['title_clean'] != '007') &
    (~df_tracks['artist_clean'].isin(['[unknown]', 'none']))
].copy()

valid_track_ids = valid_tracks['track_id'].unique()
df_valid_sales = df_sales[df_sales['track_id'].isin(valid_track_ids)]

df_merged = df_valid_sales.merge(valid_tracks[['track_id', 'title', 'artist', 'title_clean']], 
                          on='track_id', how='left')

# Group by title clean and sum revenues
title_revenue = df_merged.groupby('title_clean')['revenue_usd'].sum().sort_values(ascending=False)

# Get top titles
top_titles = title_revenue.head(20)

result_list = []
for title_clean, revenue in top_titles.items():
    # Get all variants of this title
    title_tracks = valid_tracks[valid_tracks['title_clean'] == title_clean]
    artists = title_tracks['artist'].unique()
    
    result_list.append({
        'title_clean': title_clean,
        'revenue': float(revenue),
        'artist_variants': len(artists),
        'track_variants': len(title_tracks),
        'artists': list(artists)[:5]  # First 5 artists to see diversity
    })

print("__RESULT__:")
print(json.dumps(result_list[:10], indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'tracks_shape': [100, 9], 'sales_shape': [58049, 6], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_tracks': 19375, 'total_sales': 58049, 'total_revenue': 16528140.350000001, 'distinct_tracks_with_sales': 19375}, 'var_functions.execute_python:18': {'top_track_title': 'None', 'top_track_artist': 'None', 'total_revenue': 14647.52, 'track_variants_count': 17}, 'var_functions.execute_python:20': {'top_track_title': 'Groovey', 'top_track_artist': 'Rich Matteson', 'total_revenue': 4128.59, 'track_variants_count': 3}}

exec(code, env_args)
