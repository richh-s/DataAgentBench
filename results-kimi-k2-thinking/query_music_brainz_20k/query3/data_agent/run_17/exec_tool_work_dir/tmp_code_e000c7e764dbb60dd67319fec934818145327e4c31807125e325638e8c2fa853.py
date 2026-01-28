code = """import json
import re
from collections import defaultdict

# Load all data
with open(locals()['var_functions.query_db:8'], 'r') as f:
    tracks = json.load(f)

with open(locals()['var_functions.query_db:9'], 'r') as f:
    sales = json.load(f)

print(f"Total tracks: {len(tracks)}, Total sales: {len(sales)}")

# Step 1: Clean and normalize track data
def clean_track_data(track):
    """Extract and clean title/artist from a track record"""
    title = track.get('title', '').strip()
    artist = track.get('artist', '').strip()
    
    # Handle "Artist - Title" format when artist field is empty/generic
    if ' - ' in title and (not artist or artist.lower() in ['none', 'unknown', '[unknown]', '', 'various', 'various artists']):
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            artist = parts[0].strip()
            title = parts[1].strip()
    
    # Clean up artist
    if not artist or artist.lower() in ['none', 'unknown', '[unknown]', '', 'various', 'various artists']:
        artist = 'Unknown'
    else:
        artist = artist.strip()
    
    # Clean up title
    title = title.strip()
    
    # Remove numeric prefixes like "006-", "007-", "001-"
    title = re.sub(r'^(?:\d{3}-|0{2}\d-|\d+-)\s*', '', title)
    
    # Remove whitespace-only titles
    if not title or title.isspace():
        return None
    
    # Filter out obvious data artifacts
    if re.match(r'^(\d+\s*)+$', title):  # Only numbers
        return None
    if title == 'None':
        return None
    if len(title) < 2 and title.isdigit():  # Single digit
        return None
    
    return {'title': title, 'artist': artist, 'track_id': track['track_id']}

# Clean all tracks
cleaned_tracks = []
for track in tracks:
    cleaned = clean_track_data(track)
    if cleaned:
        cleaned_tracks.append(cleaned)

print(f"Cleaned tracks: {len(cleaned_tracks)}")

# Step 2: Group tracks by normalized title and artist
song_groups = defaultdict(list)
for track in cleaned_tracks:
    # Normalize for comparison (lowercase, but keep original for display)
    normalized_key = f"{track['title'].lower()}||{track['artist'].lower()}"
    song_groups[normalized_key].append(track)

print(f"Unique songs after grouping: {len(song_groups)}")

# Step 3: Calculate revenue per song
# Build track_id to song_key mapping
track_to_song_key = {}
for key, tracks in song_groups.items():
    for track in tracks:
        track_to_song_key[track['track_id']] = key

# Sum revenue for each song
song_revenues = defaultdict(float)
for sale in sales:
    tid = sale['track_id']
    if tid in track_to_song_key:
        key = track_to_song_key[tid]
        song_revenues[key] += float(sale['revenue_usd'])

# Step 4: Find top songs (excluding Unknown artists)
print("\nTop 10 songs (excluding Unknown artists):")
sorted_songs = sorted(song_revenues.items(), key=lambda x: x[1], reverse=True)

valid_top_songs = []
for key, revenue in sorted_songs:
    title, artist = key.split('||')
    if artist != 'unknown' and title.strip():
        valid_top_songs.append({
            'title': title,
            'artist': artist,
            'revenue': round(revenue, 2),
            'variants': len(song_groups[key])
        })
        if len(valid_top_songs) >= 10:
            break

for i, song in enumerate(valid_top_songs, 1):
    print(f"{i}. '{song['title']}' by {song['artist']} - ${song['revenue']} (from {song['variants']} track variants)")

# Get the highest revenue song
if valid_top_songs:
    top_song = valid_top_songs[0]
    result = {
        'song_title': top_song['title'],
        'artist': top_song['artist'],
        'total_revenue_usd': top_song['revenue']
    }
else:
    result = {'error': 'No valid songs found'}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:3': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.execute_python:7': 'Got sample data', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:14': 'Loaded 19375 tracks and 58049 sales records', 'var_functions.execute_python:16': 'Tracks: 19375, Sales: 58049', 'var_functions.execute_python:18': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375}, 'var_functions.execute_python:20': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}, {'track_id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005'}, {'track_id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05'}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96'}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007'}, {'track_id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997'}, {'track_id': '11', 'title': 'None', 'artist': 'Anathema', 'album': 'Alternative 4', 'year': '1998'}, {'track_id': '12', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal', 'album': 'Mexico', 'year': 'None'}, {'track_id': '13', 'title': '002-Particle/Wave', 'artist': 'Lunchbox', 'album': 'Evolver (2002)', 'year': 'None'}, {'track_id': '14', 'title': '001-Deja Vu', 'artist': 'Blanket', 'album': 'Nice (2000)', 'year': 'None'}, {'track_id': '15', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters', 'album': 'Andy Bey and the Bey Sisters (2000)', 'year': 'None'}, {'track_id': '16', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch', 'album': 'The Classical Album, Volume 1', 'year': '1996'}, {'track_id': '17', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None', 'album': 'Die frühen Aufnahmen', 'year': 'None'}, {'track_id': '18', 'title': '00-1', 'artist': 'None', 'album': ' (2010)', 'year': 'None'}, {'track_id': '19', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye', 'album': 'RYEot powRR', 'year': '2011'}, {'track_id': '20', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini', 'album': 'Forbidden Broadway 2001: A Spoof Odyssey (2001 original off-Broadway cast)', 'year': '2901'}], 'var_functions.execute_python:26': 'Tracks: 19375, Sales: 58049', 'var_functions.execute_python:30': [{'key': '||unknown', 'revenue': 14647.520000000002, 'track_count': 17, 'title': 'None', 'artist': 'None'}, {'key': '003-||unknown', 'revenue': 6841.1799999999985, 'track_count': 6, 'title': '003-', 'artist': 'None'}, {'key': 'groovey||rich matteson', 'revenue': 5417.34, 'track_count': 4, 'title': 'Rich Matteson - Groovey', 'artist': 'None'}, {'key': '005-||unknown', 'revenue': 5221.999999999999, 'track_count': 7, 'title': '005-', 'artist': 'None'}, {'key': '009-||unknown', 'revenue': 5045.7, 'track_count': 4, 'title': '009-  ', 'artist': ' '}, {'key': '004-||unknown', 'revenue': 4868.470000000001, 'track_count': 5, 'title': '004- ', 'artist': ' '}, {'key': '010-||unknown', 'revenue': 4734.360000000001, 'track_count': 5, 'title': '010-', 'artist': 'None'}, {'key': '002-||unknown', 'revenue': 4119.89, 'track_count': 3, 'title': '002-', 'artist': 'None'}, {'key': 'all my friends say (album version)||luke bryan', 'revenue': 4110.549999999999, 'track_count': 3, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}, {'key': 'kapitel 01||kerstin gier', 'revenue': 4091.1200000000003, 'track_count': 2, 'title': 'Kerstin Gier - Kapitel 01', 'artist': 'None'}], 'var_functions.execute_python:32': {'top_song_key': 'groovey||rich matteson', 'total_revenue': 5417.34, 'track_ids_with_same_key': 15, 'sample_track': {'title': 'groovey', 'artist': 'rich matteson', 'original': {'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'album': 'Groovey', 'year': '09'}}}, 'var_functions.execute_python:34': {'found_track_ids': 5, 'revenue': 5668.5, 'sample_tracks': [{'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey'}, {'title': '006-Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey (2009)'}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey'}]}, 'var_functions.execute_python:38': {'top_song': {'title': '', 'artist': 'unknown', 'total_revenue_usd': 59061.99, 'track_variants_count': 65}, 'top_10': [{'rank': 1, 'canonical_title': '', 'canonical_artist': 'unknown', 'total_revenue_usd': 59061.99, 'unique_track_ids': 65, 'sample_original_title': '011- ', 'sample_original_artist': '   '}, {'rank': 2, 'canonical_title': 'none', 'canonical_artist': 'unknown', 'total_revenue_usd': 14647.52, 'unique_track_ids': 17, 'sample_original_title': 'None', 'sample_original_artist': 'None'}, {'rank': 3, 'canonical_title': 'groovey', 'canonical_artist': 'rich matteson', 'total_revenue_usd': 5668.5, 'unique_track_ids': 5, 'sample_original_title': 'Rich Matteson - Groovey', 'sample_original_artist': 'None'}, {'rank': 4, 'canonical_title': 'all my friends say (album version)', 'canonical_artist': 'luke bryan', 'total_revenue_usd': 5180.93, 'unique_track_ids': 4, 'sample_original_title': 'All My Friends Say (album version)', 'sample_original_artist': 'Luke Bryan'}, {'rank': 5, 'canonical_title': 'ghetto supastar (that is what you are)', 'canonical_artist': 'pras', 'total_revenue_usd': 4933.98, 'unique_track_ids': 4, 'sample_original_title': 'Ghetto Supastar (That Is What You Are)', 'sample_original_artist': 'Pras'}, {'rank': 6, 'canonical_title': 'the power of love (rob searle club mix)', 'canonical_artist': 'frankie goes to hollywood', 'total_revenue_usd': 4909.04, 'unique_track_ids': 5, 'sample_original_title': 'The Power of Love (Rob Searle club mix)', 'sample_original_artist': 'Frankie Goes to Hollywood'}, {'rank': 7, 'canonical_title': 'zo gaat het leven aan je voor', 'canonical_artist': 'syb van der ploeg', 'total_revenue_usd': 4881.42, 'unique_track_ids': 3, 'sample_original_title': 'Zo gaat het leven aan je voor', 'sample_original_artist': 'Syb van der Ploeg'}, {'rank': 8, 'canonical_title': 'lovers', 'canonical_artist': 'fausto papetti', 'total_revenue_usd': 4770.54, 'unique_track_ids': 3, 'sample_original_title': 'Lovers', 'sample_original_artist': 'Fausto Papetti'}, {'rank': 9, 'canonical_title': 'happy together', 'canonical_artist': 'the turtles', 'total_revenue_usd': 4747.05, 'unique_track_ids': 3, 'sample_original_title': '001-Happy Together', 'sample_original_artist': 'The Turtles'}, {'rank': 10, 'canonical_title': 'jah love (vip remix)', 'canonical_artist': 'lemon d', 'total_revenue_usd': 4645.11, 'unique_track_ids': 3, 'sample_original_title': 'Lemon D - Jah Love (VIP Remix)', 'sample_original_artist': 'None'}]}}

exec(code, env_args)
