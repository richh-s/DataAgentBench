code = """import json
import re
from collections import defaultdict

# Get the file paths from storage
tracks_file = locals()['var_functions.query_db:8']
sales_file = locals()['var_functions.query_db:12']

# Read the data
with open(tracks_file, 'r') as f:
    tracks = json.load(f)

with open(sales_file, 'r') as f:
    sales = json.load(f)

# Create a revenue dictionary by track_id
revenue_by_track_id = {}
for sale in sales:
    track_id = sale['track_id']
    revenue = float(sale['revenue_usd'])
    revenue_by_track_id[track_id] = revenue_by_track_id.get(track_id, 0) + revenue

# Normalize title and artist names
def normalize_title(title):
    if not title or title == 'None':
        return ''
    # Remove common suffixes, convert to lowercase, strip
    title = title.lower()
    # Remove things like (live), (acoustic), etc. at the end
    title = re.sub(r'\s*\([^)]*\)$', '', title)
    # Remove things like - live: ... or - acoustic... at the end
    title = re.sub(r'\s*-\s*(live|acoustic|remix|radio edit|single version|album version|explicit).*', '', title)
    # Clean up extra whitespace
    title = re.sub(r'\s+', ' ', title)
    return title.strip()

def normalize_artist(artist):
    if not artist or artist in ['None', '[unknown]', '   ', 'none', '']:
        return ''
    # Standardize common unknown artist variations
    artist = artist.lower().strip()
    if artist in ['none', '[unknown]', 'unkown', 'unknown', 'none']:
        return ''
    # Clean up extra whitespace
    artist = re.sub(r'\s+', ' ', artist)
    return artist.strip()

# Group tracks by normalized title + artist, but also handle cases where this might be too generic
track_groups = defaultdict(list)
for track in tracks:
    norm_title = normalize_title(track['title'])
    norm_artist = normalize_artist(track['artist'])
    
    # If title is empty or too generic, use track_id as key
    if not norm_title or len(norm_title) < 2:
        key = (track['track_id'], '')
    elif norm_title and norm_artist:
        key = (norm_title, norm_artist)
    elif norm_title:
        key = (norm_title, '')
    elif norm_artist:
        key = ('', norm_artist)
    else:
        key = (track['track_id'], '')
    
    track_groups[key].append(track)

# Calculate revenue for each group
revenue_by_song = {}
best_song = None
best_revenue = 0
best_tracks = []

for (norm_title, norm_artist), track_list in track_groups.items():
    total_revenue = 0
    track_ids_with_revenue = []
    
    for track in track_list:
        track_id = track['track_id']
        if track_id in revenue_by_track_id:
            total_revenue += revenue_by_track_id[track_id]
            track_ids_with_revenue.append(track_id)
    
    if total_revenue > best_revenue:
        best_revenue = total_revenue
        best_song = (norm_title, norm_artist, len(track_list), len(track_ids_with_revenue))
        best_tracks = track_list

# Get the best track info (prefer the one with actual title/artist if available)
best_track = None
if best_tracks:
    # Prefer tracks with non-empty title and artist first, then by revenue contribution
    def track_score(track):
        score = 0
        if track['title'] and track['title'] != 'None':
            score += 2
        if track['artist'] and track['artist'] not in ['None', '[unknown]']:
            score += 2
        track_id = track['track_id']
        if track_id in revenue_by_track_id:
            score += float(revenue_by_track_id[track_id]) / 1000.0
        return score
    
    best_track = max(best_tracks, key=track_score)

result = {
    'normalized_title': best_song[0] if best_song else '',
    'normalized_artist': best_song[1] if best_song else '',
    'total_tracks_in_group': best_song[2] if best_song else 0,
    'tracks_with_sales': best_song[3] if best_song else 0,
    'total_revenue': best_revenue,
    'best_track_example': {
        'track_id': best_track['track_id'] if best_track else None,
        'title': best_track['title'] if best_track else None,
        'artist': best_track['artist'] if best_track else None,
        'album': best_track['album'] if best_track else None
    }
}

print("__RESULT__:")
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}, {'track_id': '11', 'source_id': '5', 'source_track_id': '855829', 'title': 'None', 'artist': 'Anathema', 'album': 'Alternative 4', 'year': '1998', 'length': '188400', 'language': 'English'}, {'track_id': '12', 'source_id': '5', 'source_track_id': '8987422', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal', 'album': 'Mexico', 'year': 'None', 'length': '129000', 'language': 'English'}, {'track_id': '13', 'source_id': '4', 'source_track_id': '182555-A056', 'title': '002-Particle/Wave', 'artist': 'Lunchbox', 'album': 'Evolver (2002)', 'year': 'None', 'length': '6m 21sec', 'language': 'Eng.'}, {'track_id': '14', 'source_id': '4', 'source_track_id': '51445-A041', 'title': '001-Deja Vu', 'artist': 'Blanket', 'album': 'Nice (2000)', 'year': 'None', 'length': '3m 36sec', 'language': 'ng.'}, {'track_id': '15', 'source_id': '4', 'source_track_id': '231700-A015', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters', 'album': 'Andy Bey and the Bey Sisters (2000)', 'year': 'None', 'length': '2m 55sec', 'language': 'Eng.'}, {'track_id': '16', 'source_id': '1', 'source_track_id': 'WoM186470', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch', 'album': 'The Classical Album, Volume 1', 'year': '1996', 'length': '04:04', 'language': 'None'}, {'track_id': '17', 'source_id': '2', 'source_track_id': 'MBox374174-HH', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None', 'album': 'Die frühen Aufnahmen', 'year': 'None', 'length': '188', 'language': '[Multiple languages]'}, {'track_id': '18', 'source_id': '4', 'source_track_id': '131573-A04', 'title': '00-1', 'artist': 'None', 'album': ' (2010)', 'year': 'None', 'length': '3m 52sec', 'language': 'Jap.'}, {'track_id': '19', 'source_id': '5', 'source_track_id': '12319476', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye', 'album': 'RYEot powRR', 'year': '2011', 'length': '263497', 'language': 'English'}, {'track_id': '20', 'source_id': '1', 'source_track_id': 'WoM109609', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini', 'album': 'Forbidden Broadway 2001: A Spoof Odyssey (2001 original off-Broadway cast)', 'year': '2901', 'length': '03:39', 'language': 'None'}], 'var_functions.query_db:9': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}, {'sale_id': '11', 'track_id': '3', 'country': 'UK', 'store': 'Spotify', 'units_sold': '14', 'revenue_usd': '15.14'}, {'sale_id': '12', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '53', 'revenue_usd': '56.3'}, {'sale_id': '13', 'track_id': '3', 'country': 'Germany', 'store': 'Google Play', 'units_sold': '444', 'revenue_usd': '550.54'}, {'sale_id': '14', 'track_id': '3', 'country': 'USA', 'store': 'Amazon Music', 'units_sold': '35', 'revenue_usd': '36.56'}, {'sale_id': '15', 'track_id': '4', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '2', 'revenue_usd': '2.09'}, {'sale_id': '16', 'track_id': '4', 'country': 'UK', 'store': 'Spotify', 'units_sold': '191', 'revenue_usd': '214.86'}, {'sale_id': '17', 'track_id': '4', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '202', 'revenue_usd': '202.72'}, {'sale_id': '18', 'track_id': '4', 'country': 'France', 'store': 'Google Play', 'units_sold': '296', 'revenue_usd': '317.14'}, {'sale_id': '19', 'track_id': '5', 'country': 'UK', 'store': 'iTunes', 'units_sold': '280', 'revenue_usd': '300.8'}, {'sale_id': '20', 'track_id': '5', 'country': 'France', 'store': 'iTunes', 'units_sold': '380', 'revenue_usd': '409.98'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'tracks_count': 19375, 'sales_count': 58049}, 'var_functions.execute_python:18': {'max_track_id': '14719', 'total_revenue': 2522.82, 'track_info': {'track_id': '14719', 'source_id': '5', 'source_track_id': '11323763', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009', 'length': '223000', 'language': 'German'}}, 'var_functions.execute_python:20': {'normalized_title': '003-', 'normalized_artist': '', 'total_revenue': 8333.2, 'track_ids_count': 8, 'best_track_info': {'track_id': '5576', 'source_id': '4', 'source_track_id': '132343-A048', 'title': '003-', 'artist': ' ', 'album': ' (2003)', 'year': 'None', 'length': '3m 8sec', 'language': 'Rus.'}}, 'var_functions.execute_python:22': [{'track_id': '14719', 'revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?"}, {'track_id': '5124', 'revenue': 2503.1899999999996, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)'}, {'track_id': '1344', 'revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams'}, {'track_id': '6725', 'revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)'}, {'track_id': '10377', 'revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None'}, {'track_id': '5050', 'revenue': 2466.3100000000004, 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'album': 'Munich City Nights, Volume 11'}, {'track_id': '6667', 'revenue': 2452.7000000000003, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'album': 'None'}, {'track_id': '7245', 'revenue': 2436.9700000000003, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'album': 'Indul a boksz'}, {'track_id': '11641', 'revenue': 2428.2200000000003, 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'album': 'Share Your Love'}, {'track_id': '964', 'revenue': 2425.61, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'album': 'None'}]}

exec(code, env_args)
