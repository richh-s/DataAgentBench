code = """import json
import re
from collections import defaultdict
from difflib import SequenceMatcher

# Load data files
tracks_path = locals().get('var_functions.query_db:38')
sales_path = locals().get('var_functions.query_db:12')

# Read tracks data
if isinstance(tracks_path, str):
    with open(tracks_path, 'r', encoding='utf-8') as f:
        tracks_data = json.load(f)
else:
    tracks_data = tracks_path

# Read sales data
if isinstance(sales_path, str):
    with open(sales_path, 'r', encoding='utf-8') as f:
        sales_data = json.load(f)
else:
    sales_data = sales_path

# Normalize text function
def normalize_text(text):
    if not text or text == 'None' or text == '[unknown]' or str(text).strip() == '':
        return ''
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = ' '.join(text.split())
    return text.strip()

# Normalize year function
def normalize_year(year):
    if not year or year == 'None' or str(year).strip() == '':
        return ''
    year_str = str(year)
    match = re.search(r'\d{4}', year_str)
    if match:
        return match.group()
    match = re.search(r'\d{2}', year_str)
    if match:
        year_num = int(match.group())
        if year_num <= 24:
            return f'20{year_num:02d}'
        else:
            return f'19{year_num:02d}'
    return ''

# Prepare normalized tracks
tracks_norm = []
for track in tracks_data:
    tracks_norm.append({
        'track_id': str(track['track_id']),
        'title': track.get('title', ''),
        'artist': track.get('artist', ''),
        'album': track.get('album', ''),
        'year': track.get('year', ''),
        'norm_title': normalize_text(track.get('title', '')),
        'norm_artist': normalize_text(track.get('artist', '')),
        'norm_album': normalize_text(track.get('album', '')),
        'norm_year': normalize_year(track.get('year', ''))
    })

# Aggregate revenue
track_revenue = defaultdict(float)
for sale in sales_data:
    track_id = str(sale['track_id'])
    track_revenue[track_id] += float(sale['revenue_usd'])

# Add revenue to tracks
for track in tracks_norm:
    track['revenue'] = track_revenue.get(track['track_id'], 0)

# Sort by revenue
tracks_norm.sort(key=lambda x: x['revenue'], reverse=True)

# Entity resolution function
def is_duplicate(t1, t2):
    if t1['norm_title'] and t2['norm_title']:
        title_sim = SequenceMatcher(None, t1['norm_title'], t2['norm_title']).ratio()
        
        if title_sim >= 0.9:
            if t1['norm_artist'] and t2['norm_artist']:
                artist_sim = SequenceMatcher(None, t1['norm_artist'], t2['norm_artist']).ratio()
                if artist_sim >= 0.7:
                    return True
            elif not t1['norm_artist'] or not t2['norm_artist']:
                return True
        elif title_sim >= 0.8 and t1['norm_artist'] and t2['norm_artist']:
            artist_sim = SequenceMatcher(None, t1['norm_artist'], t2['norm_artist']).ratio()
            if artist_sim >= 0.9:
                return True
    return False

# Group similar tracks
processed = set()
song_groups = []

for i, track in enumerate(tracks_norm):
    if track['track_id'] in processed or track['revenue'] == 0:
        continue
    
    group = [track]
    processed.add(track['track_id'])
    
    for j in range(i+1, len(tracks_norm)):
        other = tracks_norm[j]
        if other['track_id'] in processed or other['revenue'] == 0:
            continue
        
        if is_duplicate(track, other):
            group.append(other)
            processed.add(other['track_id'])
    
    song_groups.append(group)

# Calculate group revenues and find top song
top_song = None
top_revenue = 0

for group in song_groups:
    total_revenue = sum(t['revenue'] for t in group)
    group.sort(key=lambda x: x['revenue'], reverse=True)
    main = group[0]
    
    if total_revenue > top_revenue:
        top_revenue = total_revenue
        top_song = {
            'song_title': main['title'],
            'artist': main['artist'],
            'album': main['album'],
            'year': main['year'],
            'total_revenue': round(total_revenue, 2),
            'duplicate_count': len(group)
        }

print('__RESULT__:')
print(json.dumps(top_song, default=str))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:22': {'top_revenue_tracks': [{'track_id': '14719', 'revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, {'track_id': '5124', 'revenue': 2503.1899999999996, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}, {'track_id': '1344', 'revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}, {'track_id': '6725', 'revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}, {'track_id': '10377', 'revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}, {'track_id': '5050', 'revenue': 2466.3100000000004, 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'album': 'Munich City Nights, Volume 11', 'year': '90'}, {'track_id': '6667', 'revenue': 2452.7000000000003, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'album': 'None', 'year': "'04"}, {'track_id': '7245', 'revenue': 2436.9700000000003, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'album': 'Indul a boksz', 'year': '1996'}, {'track_id': '11641', 'revenue': 2428.2200000000003, 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'album': 'Share Your Love', 'year': '1981'}, {'track_id': '964', 'revenue': 2425.61, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'album': 'None', 'year': 'None'}], 'total_tracks_analyzed': 19375, 'total_sales_analyzed': 58049, 'track_with_highest_revenue_id': '14719', 'highest_revenue_amount': 2522.82}, 'var_functions.execute_python:26': {'tracks_count': 19375, 'sales_count': 58049, 'sample_track': {'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, 'sample_sale': {'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'status': 'data_loaded', 'tracks_count': 19375, 'sales_count': 58049, 'first_few_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}], 'first_few_tracks': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}]}, 'var_functions.execute_python:34': {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009', 'total_revenue': 2522.82}, 'var_functions.execute_python:36': {'top_track': {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009', 'revenue': 2522.82}, 'sampling_result': 'Top track: Systemisch bled by Stüngö, revenue: $2522.82'}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
