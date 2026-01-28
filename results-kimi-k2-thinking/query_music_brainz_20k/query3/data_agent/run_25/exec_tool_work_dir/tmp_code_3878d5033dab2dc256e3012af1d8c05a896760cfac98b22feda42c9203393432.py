code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load data from files
tracks_path = locals()['var_functions.query_db:2']
sales_path = locals()['var_functions.query_db:6']

with open(tracks_path, 'r') as f:
    tracks_raw = json.load(f)

with open(sales_path, 'r') as f:
    sales_raw = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_raw)
sales_df = pd.DataFrame(sales_raw)

# Clean sales data
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')
sales_df['units_sold'] = pd.to_numeric(sales_df['units_sold'], errors='coerce')
sales_df = sales_df.dropna(subset=['revenue_usd'])
sales_df['track_id'] = sales_df['track_id'].astype(str)

# Calculate revenue per track
track_revenue = sales_df.groupby('track_id').agg({'revenue_usd': 'sum', 'units_sold': 'sum'}).reset_index()

# Clean track data
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

def clean_text(text):
    if pd.isna(text) or str(text) in ['None', 'nan', '']:
        return ''
    return str(text).strip()

tracks_df['clean_title'] = tracks_df['title'].apply(clean_text)
tracks_df['clean_artist'] = tracks_df['artist'].apply(clean_text)
tracks_df['clean_album'] = tracks_df['album'].apply(clean_text)

# Normalize for matching
def normalize(text):
    if not text:
        return ''
    # Lowercase and remove non-alphanumeric
    text = text.lower()
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

# Remove version indicators
def remove_versions(text):
    if not text:
        return ''
    patterns = [r'\(live[^)]*\)', r'\(acoustic[^)]*\)', r'\(remix[^)]*\)', r'\(version[^)]*\)']
    for pattern in patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    return text.strip()

tracks_df['base_title'] = tracks_df['clean_title'].apply(remove_versions)
tracks_df['norm_title'] = tracks_df['base_title'].apply(normalize)
tracks_df['norm_artist'] = tracks_df['clean_artist'].apply(normalize)
tracks_df['norm_album'] = tracks_df['clean_album'].apply(normalize)

# Filter for meaningful tracks
valid_tracks = tracks_df[
    (tracks_df['norm_title'] != '') & 
    (tracks_df['norm_title'] != 'none') &
    (tracks_df['norm_artist'] != '') & 
    (tracks_df['norm_artist'] != 'none') &
    (tracks_df['norm_artist'] != 'unknown') &
    (tracks_df['norm_artist'] != '[unknown]')
].copy()

# Add revenue
def get_revenue(track_id):
    rev = track_revenue[track_revenue['track_id'] == track_id]['revenue_usd']
    return rev.iloc[0] if not rev.empty else 0

valid_tracks['revenue'] = valid_tracks['track_id'].apply(get_revenue)
valid_tracks = valid_tracks[valid_tracks['revenue'] > 0]

# Create match key: title + artist
valid_tracks['match_key'] = valid_tracks.apply(
    lambda row: row['norm_title'] + '|' + row['norm_artist'] if len(row['norm_title']) >= 5 and len(row['norm_artist']) >= 3 else None,
    axis=1
)
valid_tracks = valid_tracks.dropna(subset=['match_key'])

# Group by match key
groups = defaultdict(lambda: {'revenue': 0, 'titles': set(), 'artists': set(), 'track_ids': []})

for _, row in valid_tracks.iterrows():
    key = row['match_key']
    groups[key]['revenue'] += float(row['revenue'])
    groups[key]['titles'].add(row['clean_title'])
    groups[key]['artists'].add(row['clean_artist'])
    groups[key]['track_ids'].append(row['track_id'])

# Find top song
best_key = max(groups.keys(), key=lambda k: groups[k]['revenue'])
best = groups[best_key]

best_title = list(best['titles'])[0]
best_artist = list(best['artists'])[0]

# Calculate total units sold for this song group
group_track_ids = best['track_ids']
total_units = sales_df[sales_df['track_id'].isin(group_track_ids)]['units_sold'].sum()

result = {
    'song_title': best_title,
    'artist': best_artist,
    'total_revenue_usd': round(best['revenue'], 2),
    'unique_variants': len(best['titles']),
    'total_units_sold': int(total_units),
    'representative_track_id': group_track_ids[0]
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'tracks_rows': 19375, 'sales_rows': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_sample': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}], 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}]}, 'var_functions.execute_python:20': {'top_track_title': 'None', 'top_track_artist': 'Anathema', 'total_revenue': 61376.18, 'match_key': ''}, 'var_functions.execute_python:22': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'revenue': 2522.82}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'revenue': 2503.19}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'revenue': 2500.72}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'revenue': 2489.81}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'revenue': 2466.71}, {'track_id': '5050', 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'revenue': 2466.31}, {'track_id': '6667', 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'revenue': 2452.7}, {'track_id': '7245', 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'revenue': 2436.97}, {'track_id': '11641', 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'revenue': 2428.22}, {'track_id': '964', 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'revenue': 2425.61}, {'track_id': '12984', 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'revenue': 2401.71}, {'track_id': '6208', 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'revenue': 2385.03}, {'track_id': '666', 'title': 'Emblem G - G of the Planets - Original Soundtrack', 'artist': 'Hoyt S. Curtin', 'revenue': 2382.74}, {'track_id': '12620', 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'revenue': 2377.59}, {'track_id': '19232', 'title': 'Misfortunes - From Horizon to Horizon: Singles 1983-92', 'artist': 'And Also The Trees', 'revenue': 2368.75}, {'track_id': '17757', 'title': '008-FanFanFanatic', 'artist': 'Rheingold', 'revenue': 2365.59}, {'track_id': '3462', 'title': 'Word (15 second) - Electronica', 'artist': 'Thomas Foyer', 'revenue': 2359.23}, {'track_id': '9639', 'title': 'Traces of Paganea', 'artist': 'Furious', 'revenue': 2351.68}, {'track_id': '18760', 'title': 'Patience - Distant Relatives', 'artist': 'Nas & Damian Marley', 'revenue': 2349.33}, {'track_id': '2516', 'title': '006-Osm', 'artist': 'Ourson', 'revenue': 2346.18}], 'var_functions.execute_python:24': [{'title': 'Vuelo (Frisvold & Lindbæk mix) (Remix You, Remix Me)', 'artist': 'Skatebård', 'revenue_usd': 4499.6, 'units_sold': 3863194594446895486256193167275264470, 'match_key': 'vuelo frisvold lindbk mix|skatebrd'}, {'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue_usd': 4132.27, 'units_sold': 187187316334468346448415454456, 'match_key': 'zo gaat het leven aan je voor hillich fjoer heilig'}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 4128.59, 'units_sold': 421413293279398362147411102353219264, 'match_key': 'groovey|rich matteson'}, {'title': 'Thousand Finger Man - Salsoul 30th', 'artist': 'Candido', 'revenue_usd': 3934.83, 'units_sold': 46844785284460374345254288347, 'match_key': 'thousand finger man salsoul 30th|candido'}, {'title': 'Fret One (Grow Old) - Inside Your Wave', 'artist': 'Ugly Winner', 'revenue_usd': 3844.09, 'units_sold': 487331153460308398176363402231, 'match_key': 'fret one grow old inside your wave|ugly winner'}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue_usd': 3807.4, 'units_sold': 27541930232243220369325489438, 'match_key': 'the fire still burns|russ ballard'}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'revenue_usd': 3767.95, 'units_sold': 986727303241430428340417422283297328, 'match_key': 'vostok|craig padilla'}, {'title': 'Someone So Young (Nice Dreams)', 'artist': 'Coke Weed', 'revenue_usd': 3694.38, 'units_sold': 25613619644241535948538448767, 'match_key': 'someone so young nice dreams|coke weed'}, {'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'revenue_usd': 3563.36, 'units_sold': 2733694254804884984933118, 'match_key': 'world down under helloween part 2 the rise of sata'}, {'title': 'Chile (Re-Loaded)', 'artist': 'Neil Biggin', 'revenue_usd': 3529.25, 'units_sold': 4253243558735122336046439399, 'match_key': 'chile reloaded|neil biggin'}], 'var_functions.execute_python:26': {'title': '003-  ', 'artist': 'n.a.', 'total_revenue_usd': 8394.15, 'total_units_sold': 7408, 'unique_track_ids': 9}, 'var_functions.execute_python:28': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'revenue_usd': 2522.82}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'revenue_usd': 2503.19}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'revenue_usd': 2500.72}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'revenue_usd': 2489.81}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'revenue_usd': 2466.71}, {'track_id': '7245', 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'revenue_usd': 2436.97}, {'track_id': '11641', 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'revenue_usd': 2428.22}, {'track_id': '964', 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'revenue_usd': 2425.61}, {'track_id': '12984', 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'revenue_usd': 2401.71}, {'track_id': '6208', 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'revenue_usd': 2385.03}], 'var_functions.execute_python:32': {'song_title': '[unknown] - バロス （キクラデス諸島ナクソス島のカップル・ダンス）', 'artist': '', 'total_revenue_usd': 4739.46, 'track_variants': 3}}

exec(code, env_args)
