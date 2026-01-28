code = """import json
import pandas as pd

# Load data
tracks_file = locals()['var_functions.query_db:2']
sales_file = locals()['var_functions.query_db:6']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Clean data
def clean_text(text):
    if not text or text == 'None' or text == '':
        return ''
    return str(text).strip().lower()

tracks_df['clean_title'] = tracks_df['title'].apply(clean_text)
tracks_df['clean_artist'] = tracks_df['artist'].apply(clean_text)

# Remove tracks with no meaningful title
tracks_df = tracks_df[tracks_df['clean_title'] != '']

# Calculate revenue per track
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
track_revenue = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()

# Join tracks with revenue
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
track_revenue['track_id'] = track_revenue['track_id'].astype(str)
tracks_with_rev = tracks_df.merge(track_revenue, on='track_id', how='inner')

# Sort by revenue to see top tracks
top_tracks = tracks_with_rev.sort_values('revenue_usd', ascending=False).head(20)

result = []
for _, track in top_tracks.iterrows():
    result.append({
        'track_id': track['track_id'],
        'title': track['title'],
        'artist': track['artist'],
        'revenue': round(float(track['revenue_usd']), 2)
    })

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'tracks_rows': 19375, 'sales_rows': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_sample': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}], 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}]}, 'var_functions.execute_python:20': {'top_track_title': 'None', 'top_track_artist': 'Anathema', 'total_revenue': 61376.18, 'match_key': ''}}

exec(code, env_args)
