code = """import json
import pandas as pd

# Load data
tracks_file_path = locals()['var_functions.query_db:14']
sales_file_path = locals()['var_functions.query_db:20']

with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

# Clean track data - this time more strict on entity resolution
def normalize_title(title):
    if pd.isna(title):
        return ''
    import re
    # Convert to lowercase and strip
    t = str(title).lower().strip()
    # Remove common suffixes/prefixes that might differ between versions
    t = re.sub(r'\(album version\)', '', t)
    t = re.sub(r'\(live\)', '', t)
    t = re.sub(r'\(acoustic\)', '', t)
    t = re.sub(r'\(remix\)', '', t)
    t = re.sub(r'\(edit\)', '', t)
    # Remove extra whitespace
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def normalize_artist(artist):
    if pd.isna(artist):
        return ''
    import re
    a = str(artist).lower().strip()
    # Remove common artist name variations
    a = re.sub(r'\band\b', '', a)
    a = re.sub(r'\bthe\b', '', a)
    a = re.sub(r'\(.*\)', '', a)  # Remove parentheses content
    a = re.sub(r'\s+', ' ', a).strip()
    return a

# Create normalized versions
tracks_df['title_norm'] = tracks_df['title'].apply(normalize_title)
tracks_df['artist_norm'] = tracks_df['artist'].apply(normalize_artist)

# Merge with sales
sales_with_tracks = sales_df.merge(
    tracks_df[['track_id', 'title_norm', 'artist_norm', 'title', 'artist', 'album']], 
    on='track_id', 
    how='left'
)

# Filter for substantial tracks only
def is_substantial_track(title, artist):
    if pd.isna(title):
        return False
    
    title_str = str(title).strip()
    title_lower = title_str.lower()
    
    # Exclude placeholder titles
    if title_lower in ['', 'none', 'null', 'n/a', 'track', 'song', 'untitled', 'unknown']:
        return False
    
    # Exclude if title is just numbers/symbols
    import re
    if re.match(r'^\d+[-\s]*$', title_str):
        return False
    if re.match(r'^\d{3,}-\s*$', title_str):
        return False
    if re.match(r'^\d+-\s+\w*$', title_str):
        return False
    
    # Must have meaningful words (at least 3 letters)
    words = re.findall(r'[a-zA-Z]{3,}', title_str)
    if len(words) == 0:
        return False
    
    return True

# Filter substantial tracks
substantial_sales = sales_with_tracks[sales_with_tracks.apply(
    lambda row: is_substantial_track(row['title'], row['artist']), axis=1
)]

# Group by normalized title and artist to catch variations
top_tracks = substantial_sales.groupby(['title_norm', 'artist_norm'])['revenue_usd'].sum().sort_values(ascending=False)

# Get the absolute top track
top_entity = top_tracks.index[0]
top_revenue = top_tracks.iloc[0]

# Find all matching tracks for this entity
matching_tracks = substantial_sales[
    (substantial_sales['title_norm'] == top_entity[0]) & 
    (substantial_sales['artist_norm'] == top_entity[1])
]

# Get actual title/artist from first match
actual_title = matching_tracks['title'].iloc[0]
actual_artist = matching_tracks['artist'].iloc[0]

result = {
    'song_title': actual_title,
    'artist_name': actual_artist,
    'total_revenue_usd': round(top_revenue, 2),
    'number_of_tracks_combined': matching_tracks['track_id'].nunique(),
    'total_units_sold': int(matching_tracks['units_sold'].sum())
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'var_functions.query_db:8': [{'track_count': '19375'}], 'var_functions.query_db:10': [{'title': 'All Is Forgiven', 'album': 'All Is Forgiven', 'artist': 'Siren', 'year': 'None', 'count': '2'}, {'title': 'Asa Di War - Part 1', 'album': 'Asa Di War', 'artist': 'Bhai Ravinder Singh Ji', 'year': '1997', 'count': '2'}, {'title': 'Avenida', 'album': 'Avenida', 'artist': 'Jukkis Uotila', 'year': '1987', 'count': '2'}, {'title': 'Beautiful (instrumental)', 'album': 'Beautiful', 'artist': 'Damian Marley', 'year': '2006', 'count': '2'}, {'title': 'Bende Can', 'album': 'Bende Can', 'artist': 'Yurdal Tokcan', 'year': 'None', 'count': '2'}], 'var_functions.query_db:12': [{'sale_count': '58049'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'tracks_loaded': 19375, 'sales_loaded': 58049, 'sample_tracks': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'title_clean': "daniel balavoine - l'enfant aux yeux d'italie", 'artist_clean': 'daniel balavoine'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'title_clean': '007', 'artist_clean': ''}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'title_clean': 'action painting! - mustard gas', 'artist_clean': 'action painting!'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': 349, 'revenue_usd': 408.0}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': 122, 'revenue_usd': 137.59}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': 373, 'revenue_usd': 371.57}]}, 'var_functions.execute_python:30': {'top_track_title': 'chi to rome (broke one edit)', 'top_track_artist': 'lazy ants & rob threezy', 'top_track_album': 'chi to rome', 'top_track_year': 2011.0, 'total_revenue_usd': 3091.77, 'num_track_ids': 2}, 'var_functions.execute_python:32': {'top_5_tracks_by_track_id': {'14719': {'revenue': 2522.82, 'info': {'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}}, '5124': {'revenue': 2503.19, 'info': {'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}}, '1344': {'revenue': 2500.72, 'info': {'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}}, '6725': {'revenue': 2489.81, 'info': {'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}}, '10377': {'revenue': 2466.71, 'info': {'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}}}}, 'var_functions.execute_python:34': {'top_entity': {'title': 'none', 'artist': '', 'total_revenue': 14647.52}, 'track_ids': ['2126', '2153', '3422', '4421', '5048', '7036', '7146', '7481', '9478', '9788', '10617', '12019', '12196', '14462', '15469', '16886', '18790'], 'track_details': [{'track_id': '2126', 'title': 'None', 'artist': 'None', 'album': 'Drop Dead Gorgeous'}, {'track_id': '2153', 'title': 'None', 'artist': 'None', 'album': "Live in '05"}, {'track_id': '3422', 'title': 'None', 'artist': 'None', 'album': 'Untitled 2 / Bad Brother'}, {'track_id': '4421', 'title': 'None', 'artist': 'None', 'album': 'None'}, {'track_id': '5048', 'title': 'None', 'artist': 'None', 'album': '20032010'}, {'track_id': '7036', 'title': 'None', 'artist': 'None', 'album': 'Iridescence: Sequencer Sketches, Volume 2'}, {'track_id': '7146', 'title': 'None', 'artist': 'None', 'album': 'Soundtrack'}, {'track_id': '7481', 'title': 'None', 'artist': 'None', 'album': 'This Is My First Album'}, {'track_id': '9478', 'title': 'None', 'artist': 'None', 'album': 'Bakom Kulisserna'}, {'track_id': '9788', 'title': 'None', 'artist': 'None', 'album': 'The Metal Years: Gothic Doom'}, {'track_id': '10617', 'title': 'None', 'artist': 'None', 'album': 'None'}, {'track_id': '12019', 'title': 'None', 'artist': 'None', 'album': 'None'}, {'track_id': '12196', 'title': 'None', 'artist': 'None', 'album': 'Mijn Restaurant!'}, {'track_id': '14462', 'title': 'None', 'artist': 'None', 'album': 'Journey to Persia'}, {'track_id': '15469', 'title': 'None', 'artist': 'None', 'album': 'Live - Blow the House Down'}, {'track_id': '16886', 'title': 'None', 'artist': 'None', 'album': 'East Volume Lotus - Mixed by Ping'}, {'track_id': '18790', 'title': 'None', 'artist': 'None', 'album': 'Ultimo Trem'}]}, 'var_functions.execute_python:38': [{'rank': 1, 'title': '003-', 'artist': 'None', 'album': ' (1980)', 'revenue': 6841.18}, {'rank': 2, 'title': '005-', 'artist': 'None', 'album': '  (unknown)', 'revenue': 5222.0}, {'rank': 3, 'title': '009-  ', 'artist': ' ', 'album': '  (1995)', 'revenue': 5045.7}, {'rank': 4, 'title': '004- ', 'artist': ' ', 'album': ' , 22:   (1997)', 'revenue': 4868.47}, {'rank': 5, 'title': '010-', 'artist': 'None', 'album': ' (2004)', 'revenue': 4734.36}], 'var_functions.execute_python:40': [{'rank': 1, 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey', 'revenue_usd': 4128.59}, {'rank': 2, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'album': 'The Fire Still Burns', 'revenue_usd': 3807.4}, {'rank': 3, 'title': 'Vostok', 'artist': 'Craig Padilla', 'album': 'Vostok', 'revenue_usd': 3767.95}, {'rank': 4, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'album': 'All My Friends Say', 'revenue_usd': 3241.21}, {'rank': 5, 'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'album': 'None', 'revenue_usd': 3228.62}, {'rank': 6, 'title': 'Private Soul Security', 'artist': 'Down Below', 'album': 'Private Soul Security', 'revenue_usd': 3218.63}, {'rank': 7, 'title': 'unknown', 'artist': 'None', 'album': 'モンゴルのホーミー～ガンボルド、ヤヴガーン', 'revenue_usd': 3218.35}, {'rank': 8, 'title': 'Bring Back the Love (Spaced Out dub)', 'artist': 'Laura Harris', 'album': 'Bring Back the Love', 'revenue_usd': 3171.7}, {'rank': 9, 'title': 'Chi to Rome (Broke One edit)', 'artist': 'Lazy Ants & Rob Threezy', 'album': 'Chi to Rome', 'revenue_usd': 3091.77}, {'rank': 10, 'title': 'Bad Hearts', 'artist': 'Tights', 'album': 'Bad Hearts', 'revenue_usd': 3052.75}]}

exec(code, env_args)
