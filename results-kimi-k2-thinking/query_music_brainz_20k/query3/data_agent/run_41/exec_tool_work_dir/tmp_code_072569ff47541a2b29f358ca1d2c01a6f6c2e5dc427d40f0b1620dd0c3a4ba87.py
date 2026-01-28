code = """import json
import pandas as pd

# Load data
sales_file = locals()['var_functions.query_db:11']
tracks_file = locals()['var_functions.query_db:8']

with open(sales_file, 'r') as f:
    sales_by_track = json.load(f)
with open(tracks_file, 'r') as f:
    tracks = json.load(f)

df_sales = pd.DataFrame(sales_by_track)
df_tracks = pd.DataFrame(tracks)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Find the top track
top_track = df_sales.loc[df_sales['total_revenue'].idxmax()]
top_track_id = top_track['track_id']

# Get the metadata for the top track
top_track_meta = df_tracks[df_tracks['track_id'] == top_track_id]

# Clean up the metadata for display
def clean_display(text):
    if pd.isna(text) or text is None or text == 'None':
        return 'Unknown'
    return str(text).strip()

if not top_track_meta.empty:
    title = clean_display(top_track_meta.iloc[0]['title'])
    artist = clean_display(top_track_meta.iloc[0]['artist'])
    album = clean_display(top_track_meta.iloc[0]['album'])
    revenue = round(float(top_track['total_revenue']), 2)
else:
    title = f'Track ID {top_track_id}'
    artist = 'Unknown'
    album = 'Unknown'
    revenue = round(float(top_track['total_revenue']), 2)

result = {
    'song_title': title,
    'artist': artist,
    'album': album,
    'total_revenue_usd': revenue
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:4': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}, {'track_id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005'}, {'track_id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05'}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96'}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007'}, {'track_id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997'}], 'var_functions.query_db:7': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'title': 'Unknown Title', 'artist': 'Unknown Artist', 'album': '(Unknown)', 'total_revenue': 77183.57}, 'var_functions.execute_python:18': {'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'total_revenue': 2522.82}, 'var_functions.execute_python:20': [{'track_id': '14719', 'total_revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?"}, {'track_id': '5124', 'total_revenue': 2503.19, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)'}, {'track_id': '1344', 'total_revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams'}, {'track_id': '6725', 'total_revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)'}, {'track_id': '10377', 'total_revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None'}, {'track_id': '5050', 'total_revenue': 2466.3100000000004, 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'album': 'Munich City Nights, Volume 11'}, {'track_id': '6667', 'total_revenue': 2452.7000000000003, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'album': 'None'}, {'track_id': '7245', 'total_revenue': 2436.9700000000003, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'album': 'Indul a boksz'}, {'track_id': '11641', 'total_revenue': 2428.2200000000003, 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'album': 'Share Your Love'}, {'track_id': '964', 'total_revenue': 2425.61, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'album': 'None'}, {'track_id': '12984', 'total_revenue': 2401.71, 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'album': 'None'}, {'track_id': '6208', 'total_revenue': 2385.03, 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'album': 'Helloween, Part z: The Rise of Satan'}, {'track_id': '666', 'total_revenue': 2382.74, 'title': 'Emblem G - G of the Planets - Original Soundtrack', 'artist': 'Hoyt S. Curtin', 'album': 'None'}, {'track_id': '12620', 'total_revenue': 2377.59, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'album': 'None'}, {'track_id': '19232', 'total_revenue': 2368.7499999999995, 'title': 'Misfortunes - From Horizon to Horizon: Singles 1983-92', 'artist': 'And Also The Trees', 'album': 'None'}, {'track_id': '17757', 'total_revenue': 2365.59, 'title': '008-FanFanFanatic', 'artist': 'Rheingold', 'album': 'R. (2005)'}, {'track_id': '3462', 'total_revenue': 2359.23, 'title': 'Word (15 second) - Electronica', 'artist': 'Thomas Foyer', 'album': 'None'}, {'track_id': '9639', 'total_revenue': 2351.68, 'title': 'Traces of Paganea', 'artist': 'Furious', 'album': 'Peace and Love'}, {'track_id': '18760', 'total_revenue': 2349.33, 'title': 'Patience - Distant Relatives', 'artist': 'Nas & Damian Marley', 'album': 'None'}, {'track_id': '2516', 'total_revenue': 2346.18, 'title': '006-Osm', 'artist': 'Ourson', 'album': 'Eth (2007)'}]}

exec(code, env_args)
