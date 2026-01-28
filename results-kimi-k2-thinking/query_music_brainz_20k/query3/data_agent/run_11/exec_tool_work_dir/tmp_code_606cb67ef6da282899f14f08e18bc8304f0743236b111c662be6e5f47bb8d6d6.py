code = """import json
import pandas as pd
import re

# Load data
sales_key = 'var_functions.query_db:0'
tracks_key = 'var_functions.query_db:2'

with open(locals()[sales_key], 'r') as f:
    sales_data = json.load(f)
with open(locals()[tracks_key], 'r') as f:
    tracks_data = json.load(f)

# DataFrames
sales_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

# Clean types
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['track_id'] = sales_df['track_id'].astype(int)
tracks_df['track_id'] = tracks_df['track_id'].astype(int)

# Revenue by track
track_revenue = sales_df.groupby('track_id')['revenue_usd'].sum()
tracks_df['revenue'] = tracks_df['track_id'].map(track_revenue).fillna(0)

# Helper functions
def normalize_artist(artist):
    if pd.isna(artist) or str(artist) in ['None', '[unknown]', '[no artist]', '', ' ', '  ']:
        return None
    return str(artist).strip().lower()

def parse_song_title(title):
    if pd.isna(title) or str(title) in ['None', '', ' ']:
        return None
    
    title_str = str(title).strip()
    patterns = [
        r'\(live[^)]*\)', r'\(acoustic[^)]*\)', r'\(instrumental[^)]*\)',
        r'\(remix[^)]*\)', r'\(album version\)', r'\(edit[^)]*\)',
        r'\d{4}-\d{2}-\d{2}.*', r'\d{4}.*', r'- \d{4}.*'
    ]
    
    cleaned = title_str
    for pattern in patterns:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
    
    if ' - ' in cleaned:
        parts = cleaned.split(' - ', 1)
        if len(parts) == 2:
            cleaned = parts[1]
    
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    cleaned = re.sub(r'[-:]$', '', cleaned).strip()
    
    return cleaned.lower() if cleaned else None

# Normalize
tracks_df['artist_norm'] = tracks_df['artist'].apply(normalize_artist)
tracks_df['song_parsed'] = tracks_df['title'].apply(parse_song_title)

# Valid tracks
valid_tracks = tracks_df[
    tracks_df['artist_norm'].notna() & 
    tracks_df['song_parsed'].notna() &
    (tracks_df['artist_norm'] != '') & 
    (tracks_df['song_parsed'] != '')
]

# Group by song
song_revenue = valid_tracks.groupby(['artist_norm', 'song_parsed']).agg({
    'track_id': list,
    'revenue': 'sum',
    'title': lambda x: list(x.unique())[:5]
}).reset_index()

song_revenue['track_count'] = song_revenue['track_id'].apply(len)
song_revenue = song_revenue.sort_values('revenue', ascending=False)

# Top result
top_result = song_revenue.iloc[0]

stats = {
    'top_song_revenue': float(top_result['revenue']),
    'top_song_artist': top_result['artist_norm'],
    'top_song_title': top_result['song_parsed'],
    'top_song_track_count': int(top_result['track_count']),
    'top_song_track_ids': [int(x) for x in top_result['track_id']],
    'top_song_original_titles': top_result['title'][:3],
    'total_revenue_all_tracks': float(tracks_df['revenue'].sum()),
    'unique_songs_identified': len(song_revenue)
}

print('__RESULT__:')
print(json.dumps(stats))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'sales_count': 58049, 'tracks_count': 19375, 'first_few_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'first_few_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}]}, 'var_functions.execute_python:8': {'sales_shape': [58049, 6], 'tracks_shape': [19375, 9], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'first_tracks': [{'track_id': 1, 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': 2, 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': 3, 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': 4, 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': 5, 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': 6, 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': 7, 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': 8, 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': 9, 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': 10, 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'sample_sales': [{'sale_id': '1', 'track_id': 1, 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': 408.0}, {'sale_id': '2', 'track_id': 1, 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': 137.59}, {'sale_id': '3', 'track_id': 1, 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': 371.57}, {'sale_id': '4', 'track_id': 1, 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': 269.49}, {'sale_id': '5', 'track_id': 2, 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': 184.74}, {'sale_id': '6', 'track_id': 2, 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': 270.79}, {'sale_id': '7', 'track_id': 2, 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': 186.98}, {'sale_id': '8', 'track_id': 2, 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': 217.41}, {'sale_id': '9', 'track_id': 2, 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': 399.35}, {'sale_id': '10', 'track_id': 3, 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': 418.71}]}, 'var_functions.execute_python:10': {'top_20_revenue': {'14719': 2522.82, '5124': 2503.19, '1344': 2500.72, '6725': 2489.81, '10377': 2466.71, '5050': 2466.31, '6667': 2452.7, '7245': 2436.9700000000003, '11641': 2428.2200000000003, '964': 2425.61, '12984': 2401.71, '6208': 2385.0299999999997, '666': 2382.74, '12620': 2377.59, '19232': 2368.75, '17757': 2365.59, '3462': 2359.23, '9639': 2351.68, '18760': 2349.33, '2516': 2346.18}, 'top_tracks': [{'track_id': 666, 'title': 'Emblem G - G of the Planets - Original Soundtrack', 'artist': 'Hoyt S. Curtin', 'album': 'None'}, {'track_id': 964, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'album': 'None'}, {'track_id': 1344, 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams'}, {'track_id': 2516, 'title': '006-Osm', 'artist': 'Ourson', 'album': 'Eth (2007)'}, {'track_id': 3462, 'title': 'Word (15 second) - Electronica', 'artist': 'Thomas Foyer', 'album': 'None'}, {'track_id': 5050, 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'album': 'Munich City Nights, Volume 11'}, {'track_id': 5124, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)'}, {'track_id': 6208, 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'album': 'Helloween, Part z: The Rise of Satan'}, {'track_id': 6667, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'album': 'None'}, {'track_id': 6725, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)'}, {'track_id': 7245, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'album': 'Indul a boksz'}, {'track_id': 9639, 'title': 'Traces of Paganea', 'artist': 'Furious', 'album': 'Peace and Love'}, {'track_id': 10377, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None'}, {'track_id': 11641, 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'album': 'Share Your Love'}, {'track_id': 12620, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'album': 'None'}, {'track_id': 12984, 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'album': 'None'}, {'track_id': 14719, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?"}, {'track_id': 17757, 'title': '008-FanFanFanatic', 'artist': 'Rheingold', 'album': 'R. (2005)'}, {'track_id': 18760, 'title': 'Patience - Distant Relatives', 'artist': 'Nas & Damian Marley', 'album': 'None'}, {'track_id': 19232, 'title': 'Misfortunes - From Horizon to Horizon: Singles 1983-92', 'artist': 'And Also The Trees', 'album': 'None'}]}, 'var_functions.execute_python:12': {'artist_value_counts': {'None': 4057, 'Johann Sebastian Bach': 92, 'Wolfgang Amadeus Mozart': 58, '[unknown]': 57, ' ': 28, 'Ludwig van Beethoven': 26, 'U2': 22, 'Elvis Presley': 20, 'Frédéric Chopin': 20, 'Metallica': 20, 'Louis Armstrong': 18, 'Georg Friedrich Händel': 18, 'Antonio Vivaldi': 16, 'unk.': 16, 'Bob Dylan': 16, 'Richard Wagner': 16, 'Henry Purcell': 15, 'unknown': 15, '  ': 15, '[no artist]': 15}, 'year_value_counts': {'None': 7708, '2006': 344, '2007': 334, '2005': 327, '2008': 315, '2010': 305, '2004': 303, '2009': 265, '2003': 263, '2000': 249, '2002': 246, '2011': 235, '2001': 221, '2012': 218, '1999': 211, '1998': 201, "'06": 189, '06': 182, "'05": 175, '08': 169}, 'sample_titles': ["Daniel Balavoine - L'enfant aux yeux d'Italie", '007', 'Action PAINTING! - Mustard Gas', 'Your Grace', "Well You Needn't", 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'Bruce Maginnis - Sttreet Hype', 'Luce Dufault - Ballade à donner', "Just Like Tom Thumb's Blues (live)", 'Στα καμένα', 'None', 'El Vaquero Chido (The Cool Cowboy)', '002-Particle/Wave', '001-Deja Vu', '019-Feeling Good', 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'Marlene Dietrich - Wo ist der Mann?', '00-1', 'Gimme Dat (remix)', "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))"], 'null_counts': {'track_id': 0, 'source_id': 0, 'source_track_id': 0, 'title': 0, 'artist': 0, 'album': 0, 'year': 0, 'length': 0, 'language': 0}, 'empty_string_counts': {'track_id': 0, 'source_id': 0, 'source_track_id': 0, 'title': 0, 'artist': 0, 'album': 0, 'year': 0, 'length': 0, 'language': 0}, 'none_string_counts': {'track_id': 0, 'source_id': 0, 'source_track_id': 115, 'title': 67, 'artist': 4057, 'album': 3810, 'year': 7708, 'length': 1052, 'language': 4481}, 'unknown_artist_count': 4142, 'total_tracks': 19375}, 'var_functions.execute_python:14': {'top_single_track': {'track_id': 14719, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'revenue': 2522.82}, 'similar_tracks_count': 1, 'similar_tracks': [{'track_id': 14719, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'total_revenue': 2522.82}], 'top_duplicates': [{'title_norm': 'groovey', 'artist_norm': 'rich matteson', 'track_id': [8829, 16496, 17312], 'total_revenue': 4128.59, 'album_norm': ['groovey'], 'track_count': 3}, {'title_norm': 'the fire still burns', 'artist_norm': 'russ ballard', 'track_id': [1154, 12644], 'total_revenue': 3807.3999999999996, 'album_norm': ['the fire still burns'], 'track_count': 2}, {'title_norm': 'vostok', 'artist_norm': 'craig padilla', 'track_id': [4643, 13843, 18940], 'total_revenue': 3767.95, 'album_norm': ['vostok', 'vosttok'], 'track_count': 3}, {'title_norm': 'all my friends say (album version)', 'artist_norm': 'luke bryan', 'track_id': [2133, 12601], 'total_revenue': 3241.21, 'album_norm': ['all my friends say'], 'track_count': 2}, {'title_norm': 'beautiful (instrumental)', 'artist_norm': 'damian marley', 'track_id': [3282, 11133, 16595], 'total_revenue': 3228.62, 'album_norm': ['', 'beautiful'], 'track_count': 3}, {'title_norm': 'private soul security', 'artist_norm': 'down below', 'track_id': [2614, 8279], 'total_revenue': 3218.63, 'album_norm': ['private soul security', 'pirvate soul security'], 'track_count': 2}, {'title_norm': 'bring back the love (spaced out dub)', 'artist_norm': 'laura harris', 'track_id': [52, 5348, 15142], 'total_revenue': 3171.7, 'album_norm': ['bring back the love'], 'track_count': 3}, {'title_norm': 'chi to rome (broke one edit)', 'artist_norm': 'lazy ants & rob threezy', 'track_id': [11481, 12261], 'total_revenue': 3091.7700000000004, 'album_norm': ['chi to rome'], 'track_count': 2}, {'title_norm': 'bad hearts', 'artist_norm': 'tights', 'track_id': [9183, 12827], 'total_revenue': 3052.75, 'album_norm': ['bad hearts'], 'track_count': 2}, {'title_norm': 'skin', 'artist_norm': 'westworld', 'track_id': [2095, 8689], 'total_revenue': 3008.01, 'album_norm': ['skin'], 'track_count': 2}]}}

exec(code, env_args)
