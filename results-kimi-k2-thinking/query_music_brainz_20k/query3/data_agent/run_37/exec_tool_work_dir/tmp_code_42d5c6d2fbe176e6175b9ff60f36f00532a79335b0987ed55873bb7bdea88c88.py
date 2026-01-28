code = """import json
import pandas as pd

# Read tracks data
with open(locals()['var_functions.query_db:5'], 'r') as f:
    tracks_data = json.load(f)

# Create DataFrame
tracks_df = pd.DataFrame(tracks_data)

# Normalize strings for matching - remove extra spaces, convert to lower
tracks_df['title_norm'] = tracks_df['title'].str.lower().str.strip()
tracks_df['artist_norm'] = tracks_df['artist'].str.lower().str.strip()
tracks_df['album_norm'] = tracks_df['album'].str.lower().str.strip()

# Find the target track
target_track = tracks_df[tracks_df['track_id'] == '14719'].iloc[0]

# Find potential duplicates based on title/artist/album
duplicates = tracks_df[
    (tracks_df['title_norm'] == target_track['title_norm']) &
    (tracks_df['artist_norm'] == target_track['artist_norm']) &
    (tracks_df['album_norm'] == target_track['album_norm'])
]

# Check for similar title matches too
similar_title = tracks_df[tracks_df['title_norm'].str.contains('systemisch', na=False)]

print('__RESULT__:')
print(json.dumps({
    'exact_duplicates': len(duplicates),
    'duplicate_track_ids': duplicates['track_id'].tolist(),
    'similar_title_matches': len(similar_title),
    'similar_titles': similar_title[['track_id', 'title', 'artist', 'album']].to_dict('records')
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'max_track_id': '17096', 'total_revenue': 999.8799999999999, 'track_info': {'title': 'Vinger Alleen (feat. Adriaan Brand) - Die Heuwels Fantasties', 'artist': 'Heuwels Fantasties', 'album': 'None', 'year': "'09"}}, 'var_functions.execute_python:12': {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'total_revenue': 2522.82}, 'var_functions.execute_python:14': [{'track_id': '14719', 'total_revenue': 2522.82}, {'track_id': '5124', 'total_revenue': 2503.19}, {'track_id': '1344', 'total_revenue': 2500.72}, {'track_id': '6725', 'total_revenue': 2489.81}, {'track_id': '10377', 'total_revenue': 2466.71}, {'track_id': '5050', 'total_revenue': 2466.31}, {'track_id': '6667', 'total_revenue': 2452.7}, {'track_id': '7245', 'total_revenue': 2436.97}, {'track_id': '11641', 'total_revenue': 2428.22}, {'track_id': '964', 'total_revenue': 2425.61}], 'var_functions.execute_python:16': [{'track_id': '17096', 'total_revenue': '999.8799999999999'}, {'track_id': '13202', 'total_revenue': '999.75'}, {'track_id': '909', 'total_revenue': '999.73'}], 'var_functions.execute_python:18': {'track_id': '14719', 'total_revenue': 2522.82, 'all_max_revenues': [{'track_id': '14719', 'total_revenue': 2522.82}]}, 'var_functions.execute_python:20': {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}}

exec(code, env_args)
