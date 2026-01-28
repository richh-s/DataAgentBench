code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load complete data
tracks_var = locals()['var_functions.query_db:12']
if isinstance(tracks_var, str) and tracks_var.endswith('.json'):
    with open(tracks_var, 'r') as f:
        tracks_data = json.load(f)
else:
    tracks_data = tracks_var

sales_var = locals()['var_functions.query_db:6']
if isinstance(sales_var, str) and sales_var.endswith('.json'):
    with open(sales_var, 'r') as f:
        sales_data = json.load(f)
else:
    sales_data = sales_var

# Create DataFrames
df_tracks = pd.DataFrame(tracks_data)
df_sales = pd.DataFrame(sales_data)

# Clean data types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Define placeholder patterns to exclude
placeholder_patterns = [
    r'^\s*none\s*$',
    r'^\s*\[untitled\]\s*$',
    r'^\s*\d+\s*$',  # Just numbers
    r'^\s*$',  # Empty
    r'^\s*[-_]+\s*$',  # Just dashes/underscores
    r'^\s*00\d+[-\s]*\w*$',  # Patterns like 001-something
]

# Filter out placeholder titles
mask = pd.Series(True, index=df_tracks.index)
for pattern in placeholder_patterns:
    mask = mask & ~df_tracks['title'].str.fullmatch(pattern, case=False, na=True)

df_tracks_valid = df_tracks[mask].copy()

# Better normalization that preserves meaningful titles
def normalize_title_complete(title):
    if pd.isna(title) or title == 'None':
        return ''
    # Remove leading track numbers
    title = re.sub(r'^\d+[-\s]*', '', str(title))
    # Remove dates in various formats
    title = re.sub(r'\d{4}[-/]\d{2}[-/]\d{2}.*', '', title)  # YYYY-MM-DD
    title = re.sub(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}.*', '', title)  # Other date formats
    # Remove common suffixes but keep main title
    title = re.sub(r'\s*\([^)]*\d{4}[^)]*\)\s*$', '', title)  # Remove (YYYY...)
    title = re.sub(r'\s*-\s*live\s*[^-]*$', '', title, flags=re.IGNORECASE)  # Remove - live
    title = re.sub(r'\s*-\s*acoustic\s*[^-]*$', '', title, flags=re.IGNORECASE)  # Remove - acoustic
    title = re.sub(r'\s*\(live[^)]*\)\s*$', '', title, flags=re.IGNORECASE)  # Remove (live...)
    title = re.sub(r'\s*\(acoustic[^)]*\)\s*$', '', title, flags=re.IGNORECASE)  # Remove (acoustic...)
    return title.strip()

# Create more sophisticated song matching
df_tracks_valid['norm_title'] = df_tracks_valid['title'].apply(normalize_title_complete)
df_tracks_valid['norm_artist'] = df_tracks_valid['artist'].fillna('Unknown').str.lower().str.strip()

# Remove common words that might interfere with matching
common_words = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']
def create_matching_key(title, artist):
    if pd.isna(title):
        return ''
    # Remove artist name from title if present
    title_lower = title.lower()
    artist_lower = str(artist).lower() if artist else ''
    
    # Create word-based key
    words = re.findall(r'\b\w+\b', title_lower)
    # Remove common words
    key_words = [w for w in words if w not in common_words and len(w) > 2]
    return ' '.join(key_words[:8])  # Use first 8 significant words

df_tracks_valid['match_key'] = df_tracks_valid.apply(
    lambda row: create_matching_key(row['norm_title'], row['norm_artist']), axis=1
)

# Filter out empty match keys
df_tracks_valid = df_tracks_valid[df_tracks_valid['match_key'].str.len() > 0]

# Calculate revenue per track
track_revenue = df_sales.groupby('track_id')['revenue_usd'].sum().to_dict()

# Group by match key and sum revenues
song_revenue = defaultdict(float)
song_details = defaultdict(list)

for _, track in df_tracks_valid.iterrows():
    track_id = track['track_id']
    if track_id in track_revenue:
        revenue = track_revenue[track_id]
        match_key = track['match_key']
        song_revenue[match_key] += revenue
        song_details[match_key].append({
            'title': track['title'],
            'artist': track['artist'],
            'track_id': track_id,
            'revenue': revenue
        })

# Sort by total revenue
sorted_songs = sorted(song_revenue.items(), key=lambda x: x[1], reverse=True)

# Get top 10 to verify
top_10 = sorted_songs[:10]
results = []
for key, revenue in top_10:
    examples = song_details[key][:3]
    results.append({
        'match_key': key,
        'total_revenue': float(revenue),
        'track_count': len(song_details[key]),
        'examples': [
            {
                'title': ex['title'],
                'artist': ex['artist'],
                'revenue': float(ex['revenue'])
            } for ex in examples
        ]
    })

print('__RESULT__:')
print(json.dumps(results, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:4': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'sales_rows': 58049, 'tracks_rows': 10, 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sample_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375, 'unique_track_ids_in_tracks': 19375, 'sales_revenue_stats': {'mean': 284.72739151406574, 'max': 641.82, 'min': 0.99, 'total': 16528140.350000001}}, 'var_functions.execute_python:18': {'first_20_tracks': [{'id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None'}, {'id': '2', 'title': '007', 'artist': '[unknown]'}, {'id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None'}, {'id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli'}, {'id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet'}, {'id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young'}, {'id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None'}, {'id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None'}, {'id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington'}, {'id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας'}, {'id': '11', 'title': 'None', 'artist': 'Anathema'}, {'id': '12', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal'}, {'id': '13', 'title': '002-Particle/Wave', 'artist': 'Lunchbox'}, {'id': '14', 'title': '001-Deja Vu', 'artist': 'Blanket'}, {'id': '15', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters'}, {'id': '16', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch'}, {'id': '17', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None'}, {'id': '18', 'title': '00-1', 'artist': 'None'}, {'id': '19', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye'}, {'id': '20', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini'}]}, 'var_functions.execute_python:22': {'tracks_after_cleaning': 19308, 'sample_normalized': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'clean_title': "L'enfant aux yeux d'Italie", 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'lenfantauxyeuxditalie', 'artist_key': 'unknown'}, {'track_id': '2', 'title': '007', 'clean_title': '007', 'artist': '[unknown]', 'clean_artist': 'Unknown', 'title_key': '007', 'artist_key': 'unknown'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'clean_title': 'Mustard Gas', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'mustardgas', 'artist_key': 'unknown'}, {'track_id': '4', 'title': 'Your Grace', 'clean_title': 'Your Grace', 'artist': 'Kathy Troccoli', 'clean_artist': 'Kathy Troccoli', 'title_key': 'yourgrace', 'artist_key': 'kathytroccoli'}, {'track_id': '5', 'title': "Well You Needn't", 'clean_title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'clean_artist': 'Ernie Stadler Jazz Quintet', 'title_key': 'wellyouneednt', 'artist_key': 'erniestadlerjazzquintet'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'clean_title': 'Try (acoustic)', 'artist': 'Neil Young', 'clean_artist': 'Neil Young', 'title_key': 'tryacoustic', 'artist_key': 'neilyoung'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'clean_title': 'Sttreet Hype', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'sttreethype', 'artist_key': 'unknown'}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'clean_title': 'Ballade à donner', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'balladedonner', 'artist_key': 'unknown'}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'clean_title': "Just Like Tom Thumb's Blues", 'artist': 'Wendy Saddington', 'clean_artist': 'Wendy Saddington', 'title_key': 'justliketomthumbsblues', 'artist_key': 'wendysaddington'}, {'track_id': '10', 'title': 'Στα καμένα', 'clean_title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'clean_artist': 'Λαυρέντης Μαχαιρίίτσας', 'title_key': '', 'artist_key': ''}], 'unique_title_keys': 16881, 'unique_combinations': 18500}, 'var_functions.execute_python:24': {'top_song_title': 'None', 'top_song_artist': 'None', 'total_revenue': 14647.519999999997, 'track_count': 17, 'track_ids_sample': ['2126', '2153', '3422', '4421', '5048'], 'revenue_by_track': [{'track_id': '2126', 'revenue': 1102.6899999999998}, {'track_id': '2153', 'revenue': 1246.92}, {'track_id': '3422', 'revenue': 492.4}, {'track_id': '4421', 'revenue': 3.14}, {'track_id': '5048', 'revenue': 1630.66}, {'track_id': '7036', 'revenue': 745.94}, {'track_id': '7146', 'revenue': 45.93}, {'track_id': '7481', 'revenue': 786.56}, {'track_id': '9478', 'revenue': 455.7}, {'track_id': '9788', 'revenue': 1791.84}]}, 'var_functions.execute_python:26': {'top_song_normalized_title': '[untitled]', 'total_revenue': 23134.27, 'track_variations': 25, 'example_variations': [{'original_title': 'David Weber - [untitled]', 'artist': 'None', 'revenue': 1236.1000000000001}, {'original_title': '[untitled]', 'artist': 'WB Loops', 'revenue': 849.13}, {'original_title': 'Amino People - [untitled]', 'artist': 'None', 'revenue': 915.63}, {'original_title': 'Howard Blake - [untitled]', 'artist': 'None', 'revenue': 708.72}, {'original_title': '[untitled]', 'artist': '神聖かまってちゃん', 'revenue': 710.3100000000001}]}}

exec(code, env_args)
