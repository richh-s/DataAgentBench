code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load full data
tracks_result = locals()['var_functions.query_db:12']
sales_result = locals()['var_functions.query_db:13']

if isinstance(tracks_result, str) and '.json' in tracks_result:
    with open(tracks_result, 'r') as f:
        tracks_data = json.load(f)
else:
    tracks_data = tracks_result

if isinstance(sales_result, str) and '.json' in sales_result:
    with open(sales_result, 'r') as f:
        sales_data = json.load(f)
else:
    sales_data = sales_result

# Convert to DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Convert numeric types
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Calculate total revenue per track
total_revenue_by_track = sales_df.groupby('track_id')['revenue_usd'].sum()

# Find the track with maximum revenue
top_track_id = total_revenue_by_track.idxmax()
max_revenue = total_revenue_by_track.max()

# Get details of top track
top_track = tracks_df[tracks_df['track_id'] == top_track_id].iloc[0]

# Look for potential duplicates
# Define fuzzy matching criteria
def is_similar(text1, text2, threshold=0.8):
    if pd.isna(text1) or pd.isna(text2):
        return False
    text1, text2 = str(text1).lower().strip(), str(text2).lower().strip()
    if text1 == text2:
        return True
    
    # Check if one is substring of another
    if len(text1) > 3 and len(text2) > 3:
        if text1 in text2 or text2 in text1:
            return True
    
    return False

# Find tracks with similar title or artist
title_keywords = ['systemisch', 'bled']
artist_variations = ['stüngö', 'stungö', 'stungo', 'stüngo', 'stung']

candidate_tracks = []
for idx, row in tracks_df.iterrows():
    title = str(row['title']).lower()
    artist = str(row['artist']).lower()
    
    title_match = any(keyword in title for keyword in title_keywords)
    artist_match = any(var in artist for var in artist_variations)
    
    if title_match or artist_match:
        candidate_tracks.append(row['track_id'])

# Get revenue for candidate tracks
candidate_revenues = {tid: total_revenue_by_track.get(tid, 0) for tid in candidate_tracks}
sorted_candidates = sorted(candidate_revenues.items(), key=lambda x: x[1], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'top_track_id': int(top_track_id),
    'top_track_title': str(top_track['title']),
    'top_track_artist': str(top_track['artist']),
    'top_track_revenue': float(max_revenue),
    'candidate_tracks_found': len(candidate_tracks),
    'top_candidates': [(int(tid), float(rev)) for tid, rev in sorted_candidates[:10]]
}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'cid': '0', 'name': 'track_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'source_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'source_track_id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'title', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'artist', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'album', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'year', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'length', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'language', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:9': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:8': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.execute_python:10': {'status': 'data structures understood', 'tracks_fields': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_fields': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.execute_python:18': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375, 'unique_track_ids_in_tracks': 19375}, 'var_functions.execute_python:20': {'original_tracks': 19375, 'clean_tracks': 14630, 'removed_tracks': 4745}, 'var_functions.query_db:22': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003'}, {'track_id': '964', 'total_revenue': '2425.61'}], 'var_functions.query_db:24': [{'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}, {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.execute_python:26': {'tracks_with_revenue': 14630, 'total_revenue_all': 12487570.120000001, 'top_10_tracks_by_revenue': [{'track_id': 14719, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'revenue_usd': 2522.82}, {'track_id': 5124, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'revenue_usd': 2503.19}, {'track_id': 1344, 'title': 'Life CycUles', 'artist': 'Chosen', 'revenue_usd': 2500.72}, {'track_id': 6725, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'revenue_usd': 2489.81}, {'track_id': 10377, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'revenue_usd': 2466.71}, {'track_id': 6667, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'revenue_usd': 2452.7}, {'track_id': 7245, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'revenue_usd': 2436.9700000000003}, {'track_id': 11641, 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'revenue_usd': 2428.2200000000003}, {'track_id': 964, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'revenue_usd': 2425.61}, {'track_id': 12984, 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'revenue_usd': 2401.71}]}, 'var_functions.query_db:28': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}, {'track_id': '5050', 'total_revenue': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue': '2428.2200000000003'}, {'track_id': '964', 'total_revenue': '2425.61'}, {'track_id': '12984', 'total_revenue': '2401.71'}, {'track_id': '6208', 'total_revenue': '2385.0299999999997'}, {'track_id': '666', 'total_revenue': '2382.74'}, {'track_id': '12620', 'total_revenue': '2377.59'}, {'track_id': '19232', 'total_revenue': '2368.7499999999995'}, {'track_id': '17757', 'total_revenue': '2365.59'}, {'track_id': '3462', 'total_revenue': '2359.23'}, {'track_id': '9639', 'total_revenue': '2351.68'}, {'track_id': '18760', 'total_revenue': '2349.33'}, {'track_id': '2516', 'total_revenue': '2346.18'}, {'track_id': '6326', 'total_revenue': '2331.91'}, {'track_id': '5836', 'total_revenue': '2321.31'}, {'track_id': '9988', 'total_revenue': '2317.41'}, {'track_id': '18508', 'total_revenue': '2308.44'}, {'track_id': '10760', 'total_revenue': '2293.1099999999997'}, {'track_id': '9002', 'total_revenue': '2288.23'}, {'track_id': '14169', 'total_revenue': '2281.23'}, {'track_id': '9649', 'total_revenue': '2276.7200000000003'}, {'track_id': '10856', 'total_revenue': '2275.85'}, {'track_id': '7422', 'total_revenue': '2275.04'}, {'track_id': '8705', 'total_revenue': '2273.46'}, {'track_id': '5933', 'total_revenue': '2271.62'}, {'track_id': '5809', 'total_revenue': '2269.24'}, {'track_id': '16084', 'total_revenue': '2259.8599999999997'}, {'track_id': '9652', 'total_revenue': '2251.2200000000003'}, {'track_id': '3412', 'total_revenue': '2250.04'}, {'track_id': '15664', 'total_revenue': '2249.3900000000003'}, {'track_id': '12207', 'total_revenue': '2248.7200000000003'}, {'track_id': '5467', 'total_revenue': '2246.94'}, {'track_id': '13102', 'total_revenue': '2244.51'}, {'track_id': '4145', 'total_revenue': '2243.27'}, {'track_id': '13132', 'total_revenue': '2238.21'}, {'track_id': '13211', 'total_revenue': '2233.62'}, {'track_id': '2244', 'total_revenue': '2230.04'}, {'track_id': '18846', 'total_revenue': '2227.95'}, {'track_id': '2029', 'total_revenue': '2226.42'}, {'track_id': '3488', 'total_revenue': '2222.25'}, {'track_id': '17669', 'total_revenue': '2212.4700000000003'}, {'track_id': '12969', 'total_revenue': '2211.97'}, {'track_id': '12551', 'total_revenue': '2210.78'}], 'var_functions.query_db:30': [{'track_id': '7962', 'title': 'Chalk Circle - Scrambled', 'artist': 'None', 'album': 'Reflection', 'year': '11'}, {'track_id': '12395', 'title': 'The Devil Made Me Do That - Bridge Over Troubled Water', 'artist': 'Buck Owens and His Buckaroos', 'album': 'None', 'year': "'04"}, {'track_id': '13311', 'title': 'The Devil Made Me Do That (Bridge Over T roubled Water)', 'artist': 'Buck Owens and His Buckaroos', 'album': 'Bridge Over Troubled Water', 'year': '2004'}, {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, {'track_id': '14984', 'title': 'Scrambled - Reflection', 'artist': 'Circle', 'album': 'None', 'year': "'11"}, {'track_id': '15065', 'title': 'The Hope Conspiracy - Bled Across the Wire', 'artist': 'None', 'album': 'Cold Blue', 'year': '00'}, {'track_id': '16131', 'title': 'Salena Jones - Bridge Over Troubled Water', 'artist': 'None', 'album': 'Ballad with Luv', 'year': '10'}, {'track_id': '17003', 'title': 'Bridge Over Troubled Water - Ballad with Luv', 'artist': 'Salena Jon es', 'album': 'None', 'year': "'10"}], 'var_functions.query_db:32': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:34': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:36': [{'track_id': '7962', 'title': 'Chalk Circle - Scrambled', 'artist': 'None', 'album': 'Reflection', 'year': '11'}, {'track_id': '12395', 'title': 'The Devil Made Me Do That - Bridge Over Troubled Water', 'artist': 'Buck Owens and His Buckaroos', 'album': 'None', 'year': "'04"}, {'track_id': '13311', 'title': 'The Devil Made Me Do That (Bridge Over T roubled Water)', 'artist': 'Buck Owens and His Buckaroos', 'album': 'Bridge Over Troubled Water', 'year': '2004'}, {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, {'track_id': '14984', 'title': 'Scrambled - Reflection', 'artist': 'Circle', 'album': 'None', 'year': "'11"}, {'track_id': '15065', 'title': 'The Hope Conspiracy - Bled Across the Wire', 'artist': 'None', 'album': 'Cold Blue', 'year': '00'}, {'track_id': '16131', 'title': 'Salena Jones - Bridge Over Troubled Water', 'artist': 'None', 'album': 'Ballad with Luv', 'year': '10'}, {'track_id': '17003', 'title': 'Bridge Over Troubled Water - Ballad with Luv', 'artist': 'Salena Jon es', 'album': 'None', 'year': "'10"}], 'var_functions.query_db:38': [{'track_id': '7962', 'title': 'Chalk Circle - Scrambled', 'artist': 'None', 'album': 'Reflection', 'year': '11'}, {'track_id': '12395', 'title': 'The Devil Made Me Do That - Bridge Over Troubled Water', 'artist': 'Buck Owens and His Buckaroos', 'album': 'None', 'year': "'04"}, {'track_id': '13311', 'title': 'The Devil Made Me Do That (Bridge Over T roubled Water)', 'artist': 'Buck Owens and His Buckaroos', 'album': 'Bridge Over Troubled Water', 'year': '2004'}, {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, {'track_id': '14984', 'title': 'Scrambled - Reflection', 'artist': 'Circle', 'album': 'None', 'year': "'11"}, {'track_id': '15065', 'title': 'The Hope Conspiracy - Bled Across the Wire', 'artist': 'None', 'album': 'Cold Blue', 'year': '00'}, {'track_id': '16131', 'title': 'Salena Jones - Bridge Over Troubled Water', 'artist': 'None', 'album': 'Ballad with Luv', 'year': '10'}, {'track_id': '17003', 'title': 'Bridge Over Troubled Water - Ballad with Luv', 'artist': 'Salena Jon es', 'album': 'None', 'year': "'10"}]}

exec(code, env_args)
