code = """import json
import pandas as pd
import re
from collections import defaultdict

# Reload all data
tracks_file = locals()['var_functions.query_db:8']
sales_file = locals()['var_functions.query_db:16']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)
with open(sales_file, 'r') as f:
    sales_data = json.load(f)

df_tracks = pd.DataFrame(tracks_data)
df_sales = pd.DataFrame(sales_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(int)
df_sales['revenue_usd'] = df_sales['revenue_usd'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(int)

# Create a dictionary to map track_ids to their entity information
track_entities = {}

# Clean tracks data
for _, track in df_tracks.iterrows():
    track_id = track['track_id']
    
    # Clean artist
    artist = track['artist']
    if pd.isna(artist) or str(artist).strip().lower() in ['none', '[unknown]', '']:
        artist = None
    else:
        artist = str(artist).strip()
    
    # Clean title
    title = track['title']
    if pd.isna(title) or str(title).strip().lower() == 'none':
        title = None
    else:
        title = str(title).strip()
    
    # Try to extract artist from title
    extracted_artist = None
    if title and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            extracted_artist = parts[0].strip()
            if not artist:
                artist = extracted_artist
            title = parts[1].strip()
    
    # Clean album
    album = track['album']
    if pd.isna(album) or str(album).strip().lower() == 'none':
        album = None
    else:
        album = str(album).strip()
    
    # Normalize year
    year = track['year']
    year_clean = None
    if not pd.isna(year) and str(year).strip().lower() != 'none':
        year_str = str(year).strip()
        if year_str.startswith("'"):
            year_str = year_str[1:]
        year_match = re.search(r'\d{4}', year_str)
        if year_match:
            try:
                year_int = int(year_match.group())
                if 1900 <= year_int <= 2023:
                    year_clean = year_int
            except:
                pass
    
    track_entities[track_id] = {
        'artist': artist,
        'title': title,
        'album': album,
        'year': year_clean,
        'raw_artist': track['artist'],
        'raw_title': track['title']
    }

# Build entity groups based on artist/title similarity
entity_groups = defaultdict(list)
group_counter = 0

# Strategy: Group by exact matches on artist and title first
artist_title_map = defaultdict(list)

for track_id, info in track_entities.items():
    if info['artist'] and info['title']:
        # Create a key from cleaned artist and title
        artist_key = re.sub(r'[^a-zA-Z0-9]', '', info['artist'].lower())[:30]
        title_key = re.sub(r'[^a-zA-Z0-9]', '', info['title'].lower())[:40]
        key = f"{artist_key}|{title_key}"
        artist_title_map[key].append(track_id)
    else:
        # Keep unknowns separate
        entity_groups[f"unknown_{group_counter}"] = [track_id]
        group_counter += 1

# Add the grouped tracks to entity_groups
for key, track_ids in artist_title_map.items():
    group_id = f"group_{group_counter}"
    entity_groups[group_id] = track_ids
    group_counter += 1

# Calculate revenue for each entity group
entity_revenues = []
for group_id, track_ids in entity_groups.items():
    group_sales = df_sales[df_sales['track_id'].isin(track_ids)]
    if not group_sales.empty:
        total_revenue = group_sales['revenue_usd'].sum()
        total_units = group_sales['units_sold'].astype(int).sum()
        
        # Get representative track info
        first_track_id = track_ids[0]
        track_info = track_entities[first_track_id]
        
        entity_revenues.append({
            'group_id': group_id,
            'track_ids': track_ids,
            'revenue': total_revenue,
            'units_sold': total_units,
            'artist': track_info['artist'],
            'title': track_info['title'],
            'album': track_info['album'],
            'year': track_info['year'],
            'track_count': len(track_ids)
        })

# Find top entity
top_entity = max(entity_revenues, key=lambda x: x['revenue'])

# Prepare result
result = {
    'song_title': str(top_entity['title']) if top_entity['title'] else 'Unknown Title',
    'artist': str(top_entity['artist']) if top_entity['artist'] else 'Unknown Artist',
    'total_revenue_usd': round(float(top_entity['revenue']), 2),
    'total_units_sold': int(top_entity['units_sold']),
    'track_variants_found': int(top_entity['track_count'])
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:2': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:5': [{'track_count': '19375'}], 'var_functions.query_db:7': [{'sales_count': '58049'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'song_title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'total_revenue_usd': 418.71}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'tracks_count': 19375, 'sales_count': 58049, 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}, 'var_functions.execute_python:20': {'status': 'ready', 'tracks_with_keys': 19375}, 'var_functions.execute_python:22': {'song_title': 'Из далеких из краев', 'artist': 'Песняры', 'total_revenue_usd': 11630.39, 'total_units_sold': 10210}, 'var_functions.execute_python:24': {'top_tracks_by_id': [{'track_id': 14719, 'revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö'}, {'track_id': 5124, 'revenue': 2503.19, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels'}, {'track_id': 1344, 'revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen'}, {'track_id': 6725, 'revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers'}, {'track_id': 10377, 'revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas'}], 'total_top_revenue': 2522.82}}

exec(code, env_args)
