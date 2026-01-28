code = """import json
import pandas as pd
import re
from collections import defaultdict

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

# Clean sales data
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')
sales_df['track_id'] = sales_df['track_id'].astype(str)

# Get top 100 highest revenue track_ids
track_revenue = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
top_track_ids = track_revenue.nlargest(100, 'revenue_usd')['track_id'].tolist()

# Get track details for these top tracks
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
top_tracks = tracks_df[tracks_df['track_id'].isin(top_track_ids)].copy()

# Clean track data
def clean_text(text):
    if not text or text == 'None' or text == '':
        return ''
    return str(text).strip()

top_tracks['clean_title'] = top_tracks['title'].apply(clean_text)
top_tracks['clean_artist'] = top_tracks['artist'].apply(clean_text)

# Join with revenue
top_tracks_with_rev = top_tracks.merge(track_revenue, on='track_id', how='inner')
top_tracks_with_rev = top_tracks_with_rev.sort_values('revenue_usd', ascending=False)

print("Top 30 highest revenue tracks before entity resolution:")
for idx, row in top_tracks_with_rev.head(30).iterrows():
    print(f"${row['revenue_usd']:>8.2f} | ID: {row['track_id']:>6} | {row['clean_title'][:50]:<50} | {row['clean_artist'][:25]:<25}")

# Let's try to find duplicates manually among these top tracks
candidates = top_tracks_with_rev.head(50)
print(f"\n\nAnalyzing {len(candidates)} top tracks for potential duplicates...")

# Create a simple grouping based on title similarity and artist similarity
def is_similar(text1, text2):
    if not text1 or not text2:
        return False
    # Exact match
    if text1.lower() == text2.lower():
        return True
    # One contains the other (for cases like "Song" vs "Song (Live)")
    if len(text1) > 5 and len(text2) > 5:
        if text1.lower() in text2.lower() or text2.lower() in text1.lower():
            return True
    return False

# Group by potential duplicates
groups = defaultdict(list)
used = set()

for idx1, row1 in candidates.iterrows():
    if row1['track_id'] in used:
        continue
    
    groups[row1['track_id']].append(row1)
    used.add(row1['track_id'])
    
    for idx2, row2 in candidates.iterrows():
        if row2['track_id'] in used:
            continue
            
        # Check if titles are similar and artists match
        if is_similar(row1['clean_title'], row2['clean_title']) and row1['clean_artist'] == row2['clean_artist']:
            groups[row1['track_id']].append(row2)
            used.add(row2['track_id'])

# Calculate total revenue for each group
group_results = []
for base_id, group_tracks in groups.items():
    if len(group_tracks) > 1:  # Only groups with duplicates
        total_revenue = sum(t['revenue_usd'] for t in group_tracks)
        total_units = sum(t.get('units_sold', 0) for t in group_tracks)
        titles = [t['clean_title'] for t in group_tracks]
        artist = group_tracks[0]['clean_artist']
        
        group_results.append({
            'base_track_id': base_id,
            'total_revenue': total_revenue,
            'track_count': len(group_tracks),
            'artist': artist,
            'titles': titles
        })

# Sort by total revenue
group_results.sort(key=lambda x: x['total_revenue'], reverse=True)

print(f"\n\nFound {len(group_results)} groups of duplicates:")
for i, group in enumerate(group_results[:10]):
    print(f"\nGroup {i+1}: ${group['total_revenue']:.2f} total ({group['track_count']} tracks)")
    print(f"  Artist: {group['artist']}")
    for title in group['titles']:
        print(f"    - {title[:60]}")

# Also check if there are any single-track results that are just very high
single_tracks = [t for t in tracks_with_rev]

result = {
    'groups_found': len(group_results),
    'top_group': group_results[0] if group_results else None
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'tracks_rows': 19375, 'sales_rows': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_sample': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}], 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}]}, 'var_functions.execute_python:20': {'top_track_title': 'None', 'top_track_artist': 'Anathema', 'total_revenue': 61376.18, 'match_key': ''}, 'var_functions.execute_python:22': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'revenue': 2522.82}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'revenue': 2503.19}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'revenue': 2500.72}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'revenue': 2489.81}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'revenue': 2466.71}, {'track_id': '5050', 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'revenue': 2466.31}, {'track_id': '6667', 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'revenue': 2452.7}, {'track_id': '7245', 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'revenue': 2436.97}, {'track_id': '11641', 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'revenue': 2428.22}, {'track_id': '964', 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'revenue': 2425.61}, {'track_id': '12984', 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'revenue': 2401.71}, {'track_id': '6208', 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'revenue': 2385.03}, {'track_id': '666', 'title': 'Emblem G - G of the Planets - Original Soundtrack', 'artist': 'Hoyt S. Curtin', 'revenue': 2382.74}, {'track_id': '12620', 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'revenue': 2377.59}, {'track_id': '19232', 'title': 'Misfortunes - From Horizon to Horizon: Singles 1983-92', 'artist': 'And Also The Trees', 'revenue': 2368.75}, {'track_id': '17757', 'title': '008-FanFanFanatic', 'artist': 'Rheingold', 'revenue': 2365.59}, {'track_id': '3462', 'title': 'Word (15 second) - Electronica', 'artist': 'Thomas Foyer', 'revenue': 2359.23}, {'track_id': '9639', 'title': 'Traces of Paganea', 'artist': 'Furious', 'revenue': 2351.68}, {'track_id': '18760', 'title': 'Patience - Distant Relatives', 'artist': 'Nas & Damian Marley', 'revenue': 2349.33}, {'track_id': '2516', 'title': '006-Osm', 'artist': 'Ourson', 'revenue': 2346.18}], 'var_functions.execute_python:24': [{'title': 'Vuelo (Frisvold & Lindbæk mix) (Remix You, Remix Me)', 'artist': 'Skatebård', 'revenue_usd': 4499.6, 'units_sold': 3863194594446895486256193167275264470, 'match_key': 'vuelo frisvold lindbk mix|skatebrd'}, {'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue_usd': 4132.27, 'units_sold': 187187316334468346448415454456, 'match_key': 'zo gaat het leven aan je voor hillich fjoer heilig'}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 4128.59, 'units_sold': 421413293279398362147411102353219264, 'match_key': 'groovey|rich matteson'}, {'title': 'Thousand Finger Man - Salsoul 30th', 'artist': 'Candido', 'revenue_usd': 3934.83, 'units_sold': 46844785284460374345254288347, 'match_key': 'thousand finger man salsoul 30th|candido'}, {'title': 'Fret One (Grow Old) - Inside Your Wave', 'artist': 'Ugly Winner', 'revenue_usd': 3844.09, 'units_sold': 487331153460308398176363402231, 'match_key': 'fret one grow old inside your wave|ugly winner'}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue_usd': 3807.4, 'units_sold': 27541930232243220369325489438, 'match_key': 'the fire still burns|russ ballard'}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'revenue_usd': 3767.95, 'units_sold': 986727303241430428340417422283297328, 'match_key': 'vostok|craig padilla'}, {'title': 'Someone So Young (Nice Dreams)', 'artist': 'Coke Weed', 'revenue_usd': 3694.38, 'units_sold': 25613619644241535948538448767, 'match_key': 'someone so young nice dreams|coke weed'}, {'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'revenue_usd': 3563.36, 'units_sold': 2733694254804884984933118, 'match_key': 'world down under helloween part 2 the rise of sata'}, {'title': 'Chile (Re-Loaded)', 'artist': 'Neil Biggin', 'revenue_usd': 3529.25, 'units_sold': 4253243558735122336046439399, 'match_key': 'chile reloaded|neil biggin'}], 'var_functions.execute_python:26': {'title': '003-  ', 'artist': 'n.a.', 'total_revenue_usd': 8394.15, 'total_units_sold': 7408, 'unique_track_ids': 9}, 'var_functions.execute_python:28': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'revenue_usd': 2522.82}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'revenue_usd': 2503.19}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'revenue_usd': 2500.72}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'revenue_usd': 2489.81}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'revenue_usd': 2466.71}, {'track_id': '7245', 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'revenue_usd': 2436.97}, {'track_id': '11641', 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'revenue_usd': 2428.22}, {'track_id': '964', 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'revenue_usd': 2425.61}, {'track_id': '12984', 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'revenue_usd': 2401.71}, {'track_id': '6208', 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'revenue_usd': 2385.03}]}

exec(code, env_args)
