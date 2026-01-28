code = """import json, pandas as pd, re

# Read the query results from storage
sales_path = var_functions.query_db:22
tracks_path = var_functions.query_db:23

# Load the JSON data from files
with open(sales_path, 'r') as f:
    sales_revenue = json.load(f)

with open(tracks_path, 'r') as f:
    tracks_info = json.load(f)

# Create DataFrames
revenue_df = pd.DataFrame(sales_revenue)
tracks_df = pd.DataFrame(tracks_info)

# Convert numeric columns
revenue_df['total_revenue'] = pd.to_numeric(revenue_df['total_revenue'])

# Normalize track info for grouping
def normalize(text):
    if pd.isna(text) or text is None:
        return ''
    # Remove non-alphanumeric and convert to lower case
    return re.sub(r'[^a-zA-Z0-9]', '', str(text).lower())

tracks_df['norm_title'] = tracks_df['title'].apply(normalize)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize)

# Create a grouping key (song identity)
tracks_df['song_key'] = tracks_df['norm_title'] + '_' + tracks_df['norm_artist']

# Map track_id to song_key
song_key_map = dict(zip(tracks_df['track_id'], tracks_df['song_key']))

# Add song_key to revenue data
revenue_df['song_key'] = revenue_df['track_id'].map(song_key_map)

# Sum revenue by song_key
song_revenue = revenue_df.groupby('song_key')['total_revenue'].sum().reset_index()
song_revenue = song_revenue.sort_values('total_revenue', ascending=False)

# Get the top earning song
top_song = song_revenue.iloc[0]
top_key = top_song['song_key']

# Find all tracks with this key to get representative info
representative_tracks = tracks_df[tracks_df['song_key'] == top_key]

# Use the first track as representative
rep_track = representative_tracks.iloc[0]

result = {
    'song_title': rep_track['title'],
    'artist': rep_track['artist'],
    'album': rep_track['album'],
    'year': rep_track['year'],
    'total_revenue_usd': round(float(top_song['total_revenue']), 2)
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, default=str))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'test': 123}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json'}

exec(code, env_args)
