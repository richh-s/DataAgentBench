code = """import json
import pandas as pd
import re

# Load sales data
sales_path = var_functions.query_db:52
with open(sales_path, 'r') as f:
    sales_raw = json.load(f)

# Load tracks data  
tracks_path = var_functions.query_db:53
with open(tracks_path, 'r') as f:
    tracks_raw = json.load(f)

print('Sales records:', len(sales_raw))
print('Tracks records:', len(tracks_raw))

# Create DataFrames
sales_df = pd.DataFrame(sales_raw)
tracks_df = pd.DataFrame(tracks_raw)

# Convert revenue to numeric
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Normalize function
def normalize(text):
    if pd.isna(text) or text is None or str(text) == 'None':
        return ''
    # Lowercase and keep only letters/numbers
    return re.sub(r'[^a-z0-9]', '', str(text).lower())

# Apply normalization to tracks
tracks_df['norm_title'] = tracks_df['title'].apply(normalize)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize)

# Create song identifier key
tracks_df['song_key'] = tracks_df['norm_title'] + '_' + tracks_df['norm_artist']

# Map track_id to song_key
song_key_map = dict(zip(tracks_df['track_id'], tracks_df['song_key']))

# Add song_key to sales data
sales_df['song_key'] = sales_df['track_id'].map(song_key_map)

# Calculate total revenue per song (grouping by song_key)
song_revenue = sales_df.groupby('song_key')['revenue_usd'].sum().reset_index()
song_revenue = song_revenue.sort_values('revenue_usd', ascending=False)

# Get top song
top_song = song_revenue.iloc[0]
top_key = top_song['song_key']
top_revenue = float(top_song['revenue_usd'])

# Get representative track info
rep_tracks = tracks_df[tracks_df['song_key'] == top_key]
rep_track = rep_tracks.iloc[0]

result = {
    'song_title': str(rep_track['title']) if pd.notna(rep_track['title']) else 'Unknown',
    'artist': str(rep_track['artist']) if pd.notna(rep_track['artist']) else 'Unknown',
    'album': str(rep_track['album']) if pd.notna(rep_track['album']) else 'Unknown', 
    'year': str(rep_track['year']) if pd.notna(rep_track['year']) else 'Unknown',
    'total_revenue_usd': round(top_revenue, 2)
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, default=str))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'test': 123}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.query_db:34': [{'track_id': '14719', 'total_revenue': '2522.82'}], 'var_functions.query_db:35': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}, {'track_id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005'}, {'track_id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010'}], 'var_functions.query_db:38': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003'}, {'track_id': '964', 'total_revenue': '2425.61'}], 'var_functions.query_db:39': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:42': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003'}, {'track_id': '964', 'total_revenue': '2425.61'}, {'track_id': '12984', 'total_revenue': '2401.71'}, {'track_id': '6208', 'total_revenue': '2385.0299999999997'}, {'track_id': '666', 'total_revenue': '2382.74'}, {'track_id': '12620', 'total_revenue': '2377.59'}, {'track_id': '19232', 'total_revenue': '2368.7499999999995'}, {'track_id': '17757', 'total_revenue': '2365.59'}, {'track_id': '3462', 'total_revenue': '2359.23'}, {'track_id': '9639', 'total_revenue': '2351.68'}, {'track_id': '18760', 'total_revenue': '2349.33'}, {'track_id': '2516', 'total_revenue': '2346.18'}, {'track_id': '6326', 'total_revenue': '2331.91'}, {'track_id': '5836', 'total_revenue': '2321.31'}, {'track_id': '9988', 'total_revenue': '2317.41'}, {'track_id': '18508', 'total_revenue': '2308.44'}, {'track_id': '10760', 'total_revenue': '2293.1099999999997'}, {'track_id': '9002', 'total_revenue': '2288.23'}, {'track_id': '14169', 'total_revenue': '2281.23'}, {'track_id': '9649', 'total_revenue': '2276.7200000000003'}, {'track_id': '10856', 'total_revenue': '2275.85'}, {'track_id': '7422', 'total_revenue': '2275.04'}, {'track_id': '8705', 'total_revenue': '2273.46'}, {'track_id': '5933', 'total_revenue': '2271.62'}, {'track_id': '5809', 'total_revenue': '2269.24'}, {'track_id': '16084', 'total_revenue': '2259.8599999999997'}, {'track_id': '9652', 'total_revenue': '2251.2200000000003'}, {'track_id': '3412', 'total_revenue': '2250.04'}, {'track_id': '15664', 'total_revenue': '2249.3900000000003'}, {'track_id': '12207', 'total_revenue': '2248.7200000000003'}, {'track_id': '5467', 'total_revenue': '2246.94'}, {'track_id': '13102', 'total_revenue': '2244.51'}, {'track_id': '4145', 'total_revenue': '2243.27'}, {'track_id': '13132', 'total_revenue': '2238.21'}, {'track_id': '13211', 'total_revenue': '2233.62'}, {'track_id': '2244', 'total_revenue': '2230.04'}, {'track_id': '18846', 'total_revenue': '2227.95'}, {'track_id': '2029', 'total_revenue': '2226.42'}, {'track_id': '3488', 'total_revenue': '2222.25'}, {'track_id': '17669', 'total_revenue': '2212.4700000000003'}, {'track_id': '12969', 'total_revenue': '2211.97'}, {'track_id': '12551', 'total_revenue': '2210.78'}], 'var_functions.query_db:48': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003'}, {'track_id': '964', 'total_revenue': '2425.61'}, {'track_id': '12984', 'total_revenue': '2401.71'}, {'track_id': '6208', 'total_revenue': '2385.0299999999997'}, {'track_id': '666', 'total_revenue': '2382.74'}, {'track_id': '12620', 'total_revenue': '2377.59'}, {'track_id': '19232', 'total_revenue': '2368.7499999999995'}, {'track_id': '17757', 'total_revenue': '2365.59'}, {'track_id': '3462', 'total_revenue': '2359.23'}, {'track_id': '9639', 'total_revenue': '2351.68'}, {'track_id': '18760', 'total_revenue': '2349.33'}, {'track_id': '2516', 'total_revenue': '2346.18'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:53': 'file_storage/functions.query_db:53.json'}

exec(code, env_args)
