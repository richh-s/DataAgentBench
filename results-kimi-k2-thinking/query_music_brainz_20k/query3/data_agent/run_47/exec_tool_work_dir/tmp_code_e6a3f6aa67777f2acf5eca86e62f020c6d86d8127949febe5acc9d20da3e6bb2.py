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

# Remove rows where title or artist is None/empty after cleaning
def clean_value(x):
    if pd.isna(x) or x is None or str(x) == 'None' or str(x).strip() == '':
        return ''
    return str(x).lower().strip()

for col in ['title', 'artist']:
    df_tracks[f'{col}_clean'] = df_tracks[col].apply(clean_value)

# Filter out tracks with no title or artist
valid_tracks = df_tracks[
    (df_tracks['title_clean'] != '') & 
    (df_tracks['artist_clean'] != '') &
    (df_tracks['title_clean'] != 'none') & 
    (df_tracks['artist_clean'] != 'none') &
    (df_tracks['title_clean'] != '[unknown]')
].copy()

# Merge sales with tracks
valid_track_ids = valid_tracks['track_id'].unique()
df_valid_sales = df_sales[df_sales['track_id'].isin(valid_track_ids)]

# Merge to get track details
df_merged = df_valid_sales.merge(valid_tracks[['track_id', 'title', 'artist', 'title_clean', 'artist_clean']], 
                          on='track_id', how='left')

# Group by title and artist to identify songs
song_revenue = df_merged.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().sort_values(ascending=False)

# Get top 10
for i, ((title, artist), revenue) in enumerate(song_revenue.head(10).items()):
    print(f"{i+1}. Revenue: ${revenue:.2f} - {title} by {artist}")

# Get detailed info for top song
top_title, top_artist = song_revenue.index[0]
top_revenue = song_revenue.iloc[0]

matching_tracks = valid_tracks[
    (valid_tracks['title_clean'] == top_title) & 
    (valid_tracks['artist_clean'] == top_artist)
]

representative_title = matching_tracks['title'].mode().iloc[0] if not matching_tracks['title'].mode().empty else matching_tracks['title'].iloc[0]
representative_artist = matching_tracks['artist'].mode().iloc[0] if not matching_tracks['artist'].mode().empty else matching_tracks['artist'].iloc[0]

print("__RESULT__:")
result = {
    'top_track_title': representative_title,
    'top_track_artist': representative_artist,
    'total_revenue': float(top_revenue),
    'track_variants_count': len(matching_tracks)
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'tracks_shape': [100, 9], 'sales_shape': [58049, 6], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_tracks': 19375, 'total_sales': 58049, 'total_revenue': 16528140.350000001, 'distinct_tracks_with_sales': 19375}, 'var_functions.execute_python:18': {'top_track_title': 'None', 'top_track_artist': 'None', 'total_revenue': 14647.52, 'track_variants_count': 17}}

exec(code, env_args)
