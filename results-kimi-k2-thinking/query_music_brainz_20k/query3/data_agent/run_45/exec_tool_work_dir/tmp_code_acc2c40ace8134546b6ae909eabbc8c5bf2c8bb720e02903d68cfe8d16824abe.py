code = """import json
import pandas as pd
import re

# Load data from files
sales_file = "var_functions.query_db:22"
tracks_file = "var_functions.query_db:23"

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

# Create DataFrames
revenue_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

# Convert revenue to numeric
revenue_df['total_revenue'] = pd.to_numeric(revenue_df['total_revenue'])

# Show basic info
print("Sales records:", len(revenue_df))
print("Tracks records:", len(tracks_df))
print("\nTop 10 revenue by track_id:")
print(revenue_df.head(10))

# Normalize strings for entity resolution
def normalize(text):
    if pd.isna(text) or text is None:
        return ''
    # Convert to lowercase and keep only alphanumeric characters
    return re.sub(r'[^a-z0-9]', '', str(text).lower())

# Apply normalization
tracks_df['norm_title'] = tracks_df['title'].apply(normalize)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize)

# Create song identity key
tracks_df['song_key'] = tracks_df['norm_title'] + '_' + tracks_df['norm_artist']

# Map track_id to song_key
song_key_map = dict(zip(tracks_df['track_id'], tracks_df['song_key']))

# Add song_key to revenue data
revenue_df['song_key'] = revenue_df['track_id'].map(song_key_map)

# Calculate total revenue per song (grouping by song_key)
song_revenue = revenue_df.groupby('song_key')['total_revenue'].sum().reset_index()
song_revenue = song_revenue.sort_values('total_revenue', ascending=False)

# Get the top song
top_song = song_revenue.iloc[0]
top_key = top_song['song_key']
top_revenue = float(top_song['total_revenue'])

# Get representative track info for this song
representative_tracks = tracks_df[tracks_df['song_key'] == top_key]

if len(representative_tracks) > 0:
    # Use the best representative (non-null values)
    rep_track = representative_tracks.iloc[0]
    
    # Prepare result
    result = {
        'song_title': str(rep_track['title']) if pd.notna(rep_track['title']) else 'Unknown',
        'artist': str(rep_track['artist']) if pd.notna(rep_track['artist']) else 'Unknown', 
        'album': str(rep_track['album']) if pd.notna(rep_track['album']) else 'Unknown',
        'year': str(rep_track['year']) if pd.notna(rep_track['year']) else 'Unknown',
        'total_revenue_usd': round(top_revenue, 2)
    }
else:
    result = {'error': 'No representative track found'}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, default=str))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'test': 123}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json'}

exec(code, env_args)
