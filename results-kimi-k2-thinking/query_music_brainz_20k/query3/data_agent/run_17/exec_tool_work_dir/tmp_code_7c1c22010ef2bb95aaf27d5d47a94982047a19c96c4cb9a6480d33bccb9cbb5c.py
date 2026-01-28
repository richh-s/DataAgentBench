code = """import json
import re
from collections import defaultdict

with open(locals()['var_functions.query_db:8'], 'r') as f:
    tracks = json.load(f)

with open(locals()['var_functions.query_db:9'], 'r') as f:
    sales = json.load(f)

# Filter out problematic tracks first
valid_tracks = []
for track in tracks:
    title = track.get('title', '')
    if not title or title == 'None' or title.strip() == '':
        continue
    # Skip tracks with numeric-only titles (likely data artifacts)
    if re.match(r'^\d+$', title.strip()):
        continue
    # Skip titles that are just numbered prefixes
    if re.match(r'^\d{3}-\s*$', title):
        continue
    valid_tracks.append(track)

print(f"Total tracks: {len(tracks)}, Valid tracks: {len(valid_tracks)}")

# Extract artist from title for tracks with "Artist - Title" format
track_mapping = {}
for track in valid_tracks:
    tid = track['track_id']
    title = track.get('title', '')
    artist = track.get('artist', '')
    
    # Handle "Artist - Title" format
    if ' - ' in title:
        if not artist or artist.lower() in ['none', 'unknown', '[unknown]', '']:
            parts = title.split(' - ', 1)
            artist = parts[0].strip()
            title = parts[1].strip()
    
    # Normalize
    title = title.strip().lower()
    artist = artist.strip().lower() if artist and artist.lower() not in ['none', 'unknown', '[unknown]'] else 'unknown'
    
    track_mapping[tid] = {'title': title, 'artist': artist, 'original': track}

# Group by title and artist
revenue_by_song = defaultdict(float)
song_tracks = defaultdict(list)

for sale in sales:
    tid = sale['track_id']
    if tid in track_mapping:
        song = track_mapping[tid]
        key = f"{song['title']}||{song['artist']}"
        revenue_by_song[key] += float(sale['revenue_usd'])
        song_tracks[key].append(tid)

# Find top song
top_key, top_revenue = max(revenue_by_song.items(), key=lambda x: x[1])
top_track_ids = song_tracks[top_key]

print("__RESULT__:")
print(json.dumps({
    'top_song_key': top_key,
    'total_revenue': top_revenue,
    'track_ids_with_same_key': len(top_track_ids),
    'sample_track': track_mapping[top_track_ids[0]] if top_track_ids else None
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:3': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.execute_python:7': 'Got sample data', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:14': 'Loaded 19375 tracks and 58049 sales records', 'var_functions.execute_python:16': 'Tracks: 19375, Sales: 58049', 'var_functions.execute_python:18': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375}, 'var_functions.execute_python:20': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}, {'track_id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005'}, {'track_id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05'}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96'}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007'}, {'track_id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997'}, {'track_id': '11', 'title': 'None', 'artist': 'Anathema', 'album': 'Alternative 4', 'year': '1998'}, {'track_id': '12', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal', 'album': 'Mexico', 'year': 'None'}, {'track_id': '13', 'title': '002-Particle/Wave', 'artist': 'Lunchbox', 'album': 'Evolver (2002)', 'year': 'None'}, {'track_id': '14', 'title': '001-Deja Vu', 'artist': 'Blanket', 'album': 'Nice (2000)', 'year': 'None'}, {'track_id': '15', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters', 'album': 'Andy Bey and the Bey Sisters (2000)', 'year': 'None'}, {'track_id': '16', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch', 'album': 'The Classical Album, Volume 1', 'year': '1996'}, {'track_id': '17', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None', 'album': 'Die frühen Aufnahmen', 'year': 'None'}, {'track_id': '18', 'title': '00-1', 'artist': 'None', 'album': ' (2010)', 'year': 'None'}, {'track_id': '19', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye', 'album': 'RYEot powRR', 'year': '2011'}, {'track_id': '20', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini', 'album': 'Forbidden Broadway 2001: A Spoof Odyssey (2001 original off-Broadway cast)', 'year': '2901'}], 'var_functions.execute_python:26': 'Tracks: 19375, Sales: 58049', 'var_functions.execute_python:30': [{'key': '||unknown', 'revenue': 14647.520000000002, 'track_count': 17, 'title': 'None', 'artist': 'None'}, {'key': '003-||unknown', 'revenue': 6841.1799999999985, 'track_count': 6, 'title': '003-', 'artist': 'None'}, {'key': 'groovey||rich matteson', 'revenue': 5417.34, 'track_count': 4, 'title': 'Rich Matteson - Groovey', 'artist': 'None'}, {'key': '005-||unknown', 'revenue': 5221.999999999999, 'track_count': 7, 'title': '005-', 'artist': 'None'}, {'key': '009-||unknown', 'revenue': 5045.7, 'track_count': 4, 'title': '009-  ', 'artist': ' '}, {'key': '004-||unknown', 'revenue': 4868.470000000001, 'track_count': 5, 'title': '004- ', 'artist': ' '}, {'key': '010-||unknown', 'revenue': 4734.360000000001, 'track_count': 5, 'title': '010-', 'artist': 'None'}, {'key': '002-||unknown', 'revenue': 4119.89, 'track_count': 3, 'title': '002-', 'artist': 'None'}, {'key': 'all my friends say (album version)||luke bryan', 'revenue': 4110.549999999999, 'track_count': 3, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}, {'key': 'kapitel 01||kerstin gier', 'revenue': 4091.1200000000003, 'track_count': 2, 'title': 'Kerstin Gier - Kapitel 01', 'artist': 'None'}]}

exec(code, env_args)
