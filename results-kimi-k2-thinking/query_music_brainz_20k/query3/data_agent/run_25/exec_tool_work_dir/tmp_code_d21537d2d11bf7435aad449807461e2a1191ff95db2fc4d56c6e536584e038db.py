code = """import json
import pandas as pd
import re

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

# Clean text function
def clean_text(text):
    if not text or text == 'None' or text == '':
        return ''
    return str(text).strip()

# Normalize function
def normalize_text(text):
    if not text:
        return ''
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and special chars (keep alphanumeric and spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Collapse multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Apply cleaning
tracks_df['clean_title'] = tracks_df['title'].apply(clean_text)
tracks_df['norm_title'] = tracks_df['title'].apply(normalize_text)
tracks_df['clean_artist'] = tracks_df['artist'].apply(clean_text)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)
tracks_df['clean_album'] = tracks_df['album'].apply(clean_text)

# Remove common live/acoustic/remix indicators for better matching
def remove_versions(text):
    if not text:
        return ''
    patterns = [
        r'\(live[^)]*\)', r'\(acoustic[^)]*\)', r'\(remix[^)]*\)', 
        r'\(version[^)]*\)', r'- live[^\|]*', r'- acoustic[^\|]*', 
        r'- remix[^\|]*', r'- version[^\|]*'
    ]
    for pattern in patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    return text.strip()

tracks_df['base_title'] = tracks_df['clean_title'].apply(remove_versions)

# Create match key: base_title + artist (if artist is meaningful)
def create_match_key(row):
    title = normalize_text(row['base_title'])
    artist = row['norm_artist']
    
    # Skip if no meaningful title
    if not title or len(title) < 3:
        return None
    
    # Use artist if it's meaningful
    if artist and artist not in ['', 'none', 'unknown', '[unknown]'] and len(artist) > 2:
        return f"{title}|{artist}"
    
    # Otherwise use album if available
    album = normalize_text(row['clean_album'])
    if album and album not in ['', 'none']:
        return f"{title}|{album}"
    
    # Otherwise just use title (for instrumentals, etc.)
    return title

tracks_df['match_key'] = tracks_df.apply(create_match_key, axis=1)

# Filter out tracks that couldn't be matched
matched_tracks = tracks_df[tracks_df['match_key'].notna()].copy()

# Calculate total revenue per track_id
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['track_id'] = sales_df['track_id'].astype(str)

track_revenue = sales_df.groupby('track_id').agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum'
}).reset_index()

# Join tracks with revenue
matched_tracks['track_id'] = matched_tracks['track_id'].astype(str)
tracks_with_rev = matched_tracks.merge(track_revenue, on='track_id', how='inner')

print(f"Total matched tracks with sales: {len(tracks_with_rev)}")
print(f"Unique match keys: {tracks_with_rev['match_key'].nunique()}")

# Group by match key and sum revenue
grouped = tracks_with_rev.groupby('match_key').agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum',
    'title': 'first',  # Take first title as representative
    'artist': 'first'  # Take first artist as representative
}).reset_index()

# Sort by revenue
grouped = grouped.sort_values('revenue_usd', ascending=False)

# Get top 10
top_10 = grouped.head(10)

result = []
for _, track in top_10.iterrows():
    result.append({
        'title': track['title'],
        'artist': track['artist'],
        'revenue_usd': round(float(track['revenue_usd']), 2),
        'units_sold': int(track['units_sold']),
        'match_key': track['match_key'][:50]  # Truncate for display
    })

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'tracks_rows': 19375, 'sales_rows': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_sample': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}], 'sales_sample': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}]}, 'var_functions.execute_python:20': {'top_track_title': 'None', 'top_track_artist': 'Anathema', 'total_revenue': 61376.18, 'match_key': ''}, 'var_functions.execute_python:22': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'revenue': 2522.82}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'revenue': 2503.19}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'revenue': 2500.72}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'revenue': 2489.81}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'revenue': 2466.71}, {'track_id': '5050', 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'revenue': 2466.31}, {'track_id': '6667', 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'revenue': 2452.7}, {'track_id': '7245', 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'revenue': 2436.97}, {'track_id': '11641', 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'revenue': 2428.22}, {'track_id': '964', 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'revenue': 2425.61}, {'track_id': '12984', 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'revenue': 2401.71}, {'track_id': '6208', 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'revenue': 2385.03}, {'track_id': '666', 'title': 'Emblem G - G of the Planets - Original Soundtrack', 'artist': 'Hoyt S. Curtin', 'revenue': 2382.74}, {'track_id': '12620', 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'revenue': 2377.59}, {'track_id': '19232', 'title': 'Misfortunes - From Horizon to Horizon: Singles 1983-92', 'artist': 'And Also The Trees', 'revenue': 2368.75}, {'track_id': '17757', 'title': '008-FanFanFanatic', 'artist': 'Rheingold', 'revenue': 2365.59}, {'track_id': '3462', 'title': 'Word (15 second) - Electronica', 'artist': 'Thomas Foyer', 'revenue': 2359.23}, {'track_id': '9639', 'title': 'Traces of Paganea', 'artist': 'Furious', 'revenue': 2351.68}, {'track_id': '18760', 'title': 'Patience - Distant Relatives', 'artist': 'Nas & Damian Marley', 'revenue': 2349.33}, {'track_id': '2516', 'title': '006-Osm', 'artist': 'Ourson', 'revenue': 2346.18}]}

exec(code, env_args)
