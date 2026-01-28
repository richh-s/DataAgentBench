code = """import json
import pandas as pd
import re
import numpy as np
from collections import defaultdict
from difflib import SequenceMatcher

# Load data
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

# Calculate revenue per track
track_revenues = df_sales.groupby('track_id')['revenue_usd'].sum()

# Add revenue to tracks
df_tracks['revenue'] = df_tracks['track_id'].map(track_revenues).fillna(0)

# Filter out tracks with no revenue and clean up data
df_tracks = df_tracks[df_tracks['revenue'] > 0]

# Clean titles and artists
def clean_title_advanced(title):
    if pd.isna(title) or str(title).strip() in ['None', '', 'n.a.', '[untitled]']:
        return None
    
    title = str(title).strip()
    
    # Extract title from "Artist - Title" format
    if ' - ' in title:
        parts = title.split(' - ')
        if len(parts) >= 2:
            # Take the last part as title, but check if first part looks like artist
            if len(parts[0]) < 100 and (len(parts[0].split()) <= 5 or any(indicator in parts[0].lower() for indicator in ['feat', 'ft', 'vs', 'and', 'or', '&'])):
                title = parts[-1]
    
    # Remove track numbers from beginning
    title = re.sub(r'^\s*\d{1,3}[-\s\.\)]*\s*', '', title)
    title = re.sub(r'^\s*\d{2,3}[a-zA-Z]?[-\s\.\)]*\s*', '', title)
    
    # Remove dates and locations
    title = re.sub(r'\(\s*\d{4}[^)]*\)', '', title)  # (YYYY...)
    title = re.sub(r'\d{4}[-/]\d{2}[-/]\d{2}.*', '', title)  # YYYY-MM-DD
    title = re.sub(r'\d{1,2}:\d{2}.*', '', title)  # HH:MM times
    
    # Remove live/acoustic markers but keep main title
    title = re.sub(r'\s*\(\s*live\s*(?:\d{4})?\s*\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*-\s*live\s*(?:\d{4})?', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\([^)]*acoustic[^)]*\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\([^)]*remix[^)]*\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\([^)]*edit[^)]*\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\([^)]*version[^)]*\)', '', title, flags=re.IGNORECASE)
    
    # Clean up whitespace
    title = re.sub(r'\s+', ' ', title).strip()
    
    # Return None if title is too short or just numbers/symbols
    if len(title) < 3 or re.match(r'^[_\-"\'\d\s]+$', title):
        return None
    
    return title

def clean_artist_advanced(artist):
    if pd.isna(artist) or str(artist).strip() in ['None', '[unknown]', '   ', '', 'n.a.', '-']:
        return 'Unknown'
    return str(artist).strip()

df_tracks['clean_title'] = df_tracks['title'].apply(clean_title_advanced)
df_tracks['clean_artist'] = df_tracks['artist'].apply(clean_artist_advanced)

# Filter out tracks we couldn't clean
df_tracks_clean = df_tracks[df_tracks['clean_title'].notna()].copy()

# Create normalized identifiers
df_tracks_clean['title_norm'] = df_tracks_clean['clean_title'].str.lower().str.replace(r'[^a-z0-9\s]', '', regex=True)
df_tracks_clean['artist_norm'] = df_tracks_clean['clean_artist'].str.lower().str.replace(r'[^a-z0-9\s]', '', regex=True)

# Split into words and sort for better matching
def get_sorted_words(text):
    words = text.split()
    words.sort()
    return ' '.join(words)

df_tracks_clean['title_sorted'] = df_tracks_clean['title_norm'].apply(get_sorted_words)

# Group by sorted title and artist
title_groups = df_tracks_clean.groupby(['title_sorted', 'artist_norm'])

# Calculate total revenue for each group
song_revenues = []
for (title_key, artist_key), group in title_groups:
    total_revenue = group['revenue'].sum()
    track_count = len(group)
    example_track = group.iloc[0]
    
    song_revenues.append({
        'title_key': title_key,
        'artist_key': artist_key,
        'total_revenue': total_revenue,
        'track_count': track_count,
        'example_title': example_track['clean_title'],
        'example_artist': example_track['clean_artist'],
        'all_titles': group['title'].tolist()[:5],  # Keep some original titles
        'track_ids': group['track_id'].tolist()
    })

# Sort by total revenue
df_songs = pd.DataFrame(song_revenues)
df_songs = df_songs.sort_values('total_revenue', ascending=False)

# Get the top song
top_song = df_songs.iloc[0]

print('__RESULT__:')
print(json.dumps({
    'top_song_title': top_song['example_title'],
    'top_song_artist': top_song['example_artist'],
    'total_revenue': float(top_song['total_revenue']),
    'track_variations': int(top_song['track_count']),
    'all_variations': top_song['all_titles'],
    'sample_track_ids': top_song['track_ids'][:5]
}, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:4': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'sales_rows': 58049, 'tracks_rows': 10, 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sample_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375, 'unique_track_ids_in_tracks': 19375, 'sales_revenue_stats': {'mean': 284.72739151406574, 'max': 641.82, 'min': 0.99, 'total': 16528140.350000001}}, 'var_functions.execute_python:18': {'first_20_tracks': [{'id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None'}, {'id': '2', 'title': '007', 'artist': '[unknown]'}, {'id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None'}, {'id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli'}, {'id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet'}, {'id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young'}, {'id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None'}, {'id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None'}, {'id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington'}, {'id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας'}, {'id': '11', 'title': 'None', 'artist': 'Anathema'}, {'id': '12', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal'}, {'id': '13', 'title': '002-Particle/Wave', 'artist': 'Lunchbox'}, {'id': '14', 'title': '001-Deja Vu', 'artist': 'Blanket'}, {'id': '15', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters'}, {'id': '16', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch'}, {'id': '17', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None'}, {'id': '18', 'title': '00-1', 'artist': 'None'}, {'id': '19', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye'}, {'id': '20', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini'}]}, 'var_functions.execute_python:22': {'tracks_after_cleaning': 19308, 'sample_normalized': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'clean_title': "L'enfant aux yeux d'Italie", 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'lenfantauxyeuxditalie', 'artist_key': 'unknown'}, {'track_id': '2', 'title': '007', 'clean_title': '007', 'artist': '[unknown]', 'clean_artist': 'Unknown', 'title_key': '007', 'artist_key': 'unknown'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'clean_title': 'Mustard Gas', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'mustardgas', 'artist_key': 'unknown'}, {'track_id': '4', 'title': 'Your Grace', 'clean_title': 'Your Grace', 'artist': 'Kathy Troccoli', 'clean_artist': 'Kathy Troccoli', 'title_key': 'yourgrace', 'artist_key': 'kathytroccoli'}, {'track_id': '5', 'title': "Well You Needn't", 'clean_title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'clean_artist': 'Ernie Stadler Jazz Quintet', 'title_key': 'wellyouneednt', 'artist_key': 'erniestadlerjazzquintet'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'clean_title': 'Try (acoustic)', 'artist': 'Neil Young', 'clean_artist': 'Neil Young', 'title_key': 'tryacoustic', 'artist_key': 'neilyoung'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'clean_title': 'Sttreet Hype', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'sttreethype', 'artist_key': 'unknown'}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'clean_title': 'Ballade à donner', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'balladedonner', 'artist_key': 'unknown'}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'clean_title': "Just Like Tom Thumb's Blues", 'artist': 'Wendy Saddington', 'clean_artist': 'Wendy Saddington', 'title_key': 'justliketomthumbsblues', 'artist_key': 'wendysaddington'}, {'track_id': '10', 'title': 'Στα καμένα', 'clean_title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'clean_artist': 'Λαυρέντης Μαχαιρίίτσας', 'title_key': '', 'artist_key': ''}], 'unique_title_keys': 16881, 'unique_combinations': 18500}, 'var_functions.execute_python:24': {'top_song_title': 'None', 'top_song_artist': 'None', 'total_revenue': 14647.519999999997, 'track_count': 17, 'track_ids_sample': ['2126', '2153', '3422', '4421', '5048'], 'revenue_by_track': [{'track_id': '2126', 'revenue': 1102.6899999999998}, {'track_id': '2153', 'revenue': 1246.92}, {'track_id': '3422', 'revenue': 492.4}, {'track_id': '4421', 'revenue': 3.14}, {'track_id': '5048', 'revenue': 1630.66}, {'track_id': '7036', 'revenue': 745.94}, {'track_id': '7146', 'revenue': 45.93}, {'track_id': '7481', 'revenue': 786.56}, {'track_id': '9478', 'revenue': 455.7}, {'track_id': '9788', 'revenue': 1791.84}]}, 'var_functions.execute_python:26': {'top_song_normalized_title': '[untitled]', 'total_revenue': 23134.27, 'track_variations': 25, 'example_variations': [{'original_title': 'David Weber - [untitled]', 'artist': 'None', 'revenue': 1236.1000000000001}, {'original_title': '[untitled]', 'artist': 'WB Loops', 'revenue': 849.13}, {'original_title': 'Amino People - [untitled]', 'artist': 'None', 'revenue': 915.63}, {'original_title': 'Howard Blake - [untitled]', 'artist': 'None', 'revenue': 708.72}, {'original_title': '[untitled]', 'artist': '神聖かまってちゃん', 'revenue': 710.3100000000001}]}, 'var_functions.execute_python:28': [], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': [{'track_id': '14719', 'revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö'}, {'track_id': '5124', 'revenue': 2503.19, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels'}, {'track_id': '1344', 'revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen'}, {'track_id': '6725', 'revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers'}, {'track_id': '10377', 'revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas'}, {'track_id': '5050', 'revenue': 2466.31, 'title': "Chilliwack - Who's Winning", 'artist': 'None'}, {'track_id': '6667', 'revenue': 2452.7, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven'}, {'track_id': '7245', 'revenue': 2436.97, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick'}, {'track_id': '11641', 'revenue': 2428.22, 'title': 'So in Love With You', 'artist': 'Kenny Rogers'}, {'track_id': '964', 'revenue': 2425.61, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge'}]}

exec(code, env_args)
