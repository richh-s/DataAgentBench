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

for col in ['title', 'artist', 'album', 'year']:
    df_tracks[f'{col}_clean'] = df_tracks[col].apply(clean_value)

# Define placeholder values to exclude
placeholder_titles = {
    '', 'none', '[untitled]', 'unknown', 'n.a.', '[silence]', 'unk.', 
    '011- ', '00-1', '007', '001-deja vu', '002-particle/wave', 
    '00-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
}
placeholder_titles.update(str(i) for i in range(100))

# Filter out placeholder tracks
valid_tracks = df_tracks[~df_tracks['title_clean'].isin(placeholder_titles)].copy()

# Also exclude tracks with 1-3 character titles that are just numbers or punctuation
def is_placeholder(title):
    if not title:
        return True
    t = str(title).lower().strip()
    if len(t) <= 3:
        if t.isdigit() or all(c in '0123456789.-_ ' for c in t):
            return True
    return False

valid_tracks = valid_tracks[~valid_tracks['title'].apply(is_placeholder)]
valid_track_ids = valid_tracks['track_id'].unique()
df_valid_sales = df_sales[df_sales['track_id'].isin(valid_track_ids)]

# Merge sales with tracks
df_merged = df_valid_sales.merge(valid_tracks[['track_id', 'title', 'artist', 'title_clean', 'artist_clean']], 
                          on='track_id', how='left')

# Group by title and artist (entity resolution)
song_revenue = df_merged.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().sort_values(ascending=False)

# Get top 10 songs with actual titles
top_songs = []
for (title_clean, artist_clean), revenue in song_revenue.head(50).items():
    if title_clean and artist_clean and title_clean not in ['none', 'unknown', '']:
        # Get representative details
        song_tracks = valid_tracks[
            (valid_tracks['title_clean'] == title_clean) & 
            (valid_tracks['artist_clean'] == artist_clean)
        ]
        if len(song_tracks) > 0:
            rep_title = song_tracks['title'].mode().iloc[0] if not song_tracks['title'].mode().empty else song_tracks['title'].iloc[0]
            rep_artist = song_tracks['artist'].mode().iloc[0] if not song_tracks['artist'].mode().empty else song_tracks['artist'].iloc[0]
            
            top_songs.append({
                'title': rep_title,
                'artist': rep_artist,
                'revenue': float(revenue),
                'track_variants': len(song_tracks),
                'title_clean': title_clean
            })

# Sort by revenue and get top
if top_songs:
    top = sorted(top_songs, key=lambda x: x['revenue'], reverse=True)[0]
    
    print("__RESULT__:")
    print(json.dumps(top))
else:
    print("__RESULT__:")
    print(json.dumps({'error': 'No valid songs found'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'tracks_shape': [100, 9], 'sales_shape': [58049, 6], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_tracks': 19375, 'total_sales': 58049, 'total_revenue': 16528140.350000001, 'distinct_tracks_with_sales': 19375}, 'var_functions.execute_python:18': {'top_track_title': 'None', 'top_track_artist': 'None', 'total_revenue': 14647.52, 'track_variants_count': 17}, 'var_functions.execute_python:20': {'top_track_title': 'Groovey', 'top_track_artist': 'Rich Matteson', 'total_revenue': 4128.59, 'track_variants_count': 3}, 'var_functions.execute_python:22': [{'title_clean': '[untitled]', 'revenue': 15127.48, 'artist_variants': 14, 'track_variants': 14, 'artists': ['WB Loops', '神聖かまってちゃん', 'The Residents', 'L.S.U.', 'Ester Kočičková a Lubomír Nohavica']}, {'title_clean': 'unknown', 'revenue': 11303.73, 'artist_variants': 11, 'track_variants': 11, 'artists': ['Eric Johnson', 'Octx', 'Alex Wilson', 'Sharon Redd', 'Charles Walker']}, {'title_clean': 'n.a.', 'revenue': 10388.44, 'artist_variants': 10, 'track_variants': 10, 'artists': ['Banda Magnificos', 'ZBS Foundation', 'Sarah Vaughan', 'Marianne Nowottny', 'Ludwig van Beethoven']}, {'title_clean': '[silence]', 'revenue': 9672.74, 'artist_variants': 8, 'track_variants': 8, 'artists': ['Phono-Comb & Jad Fair', 'Tafs', 'BUMP OF CHICKEN', 'Cornelius', '大塚p愛']}, {'title_clean': 'unk.', 'revenue': 6207.7, 'artist_variants': 9, 'track_variants': 9, 'artists': ['Friend', 'Voicians', 'Source', 'Manic', 'Einstürzende Neubauten']}, {'title_clean': '1', 'revenue': 5229.19, 'artist_variants': 7, 'track_variants': 7, 'artists': ['165', '195', '4m 31sec', '大江千里', '3.867']}, {'title_clean': 'groovey', 'revenue': 4128.59, 'artist_variants': 1, 'track_variants': 3, 'artists': ['Rich Matteson']}, {'title_clean': '2', 'revenue': 3989.61, 'artist_variants': 5, 'track_variants': 5, 'artists': ['Johann Sebastian Bach', 'InnerWish', '3m 56sec', '3.8n83', '298']}, {'title_clean': 'the fire still burns', 'revenue': 3807.4, 'artist_variants': 1, 'track_variants': 2, 'artists': ['Russ Ballard']}, {'title_clean': 'vostok', 'revenue': 3767.95, 'artist_variants': 1, 'track_variants': 3, 'artists': ['Craig Padilla']}]}

exec(code, env_args)
