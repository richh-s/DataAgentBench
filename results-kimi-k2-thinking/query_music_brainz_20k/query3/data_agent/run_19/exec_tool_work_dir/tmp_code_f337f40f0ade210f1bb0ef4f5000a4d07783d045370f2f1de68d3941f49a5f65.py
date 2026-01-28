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

# Clean track data
def clean_text(text):
    if pd.isna(text) or text is None:
        return ''
    return str(text).lower().strip()

tracks_df['title_clean'] = tracks_df['title'].apply(clean_text)
tracks_df['artist_clean'] = tracks_df['artist'].apply(clean_text)

# Extract artist from title when missing
mask_no_artist = (tracks_df['artist_clean'] == '') | (tracks_df['artist_clean'] == 'none') | (tracks_df['artist_clean'] == '[unknown]')
def extract_artist_from_title(title):
    if pd.notna(title) and ' - ' in str(title):
        parts = str(title).split(' - ', 1)
        if len(parts) == 2:
            return clean_text(parts[0])
    return ''
tracks_df.loc[mask_no_artist, 'artist_clean'] = tracks_df.loc[mask_no_artist, 'title'].apply(extract_artist_from_title)

# Merge sales and track info
sales_with_tracks = sales_df.merge(
    tracks_df[['track_id', 'title_clean', 'artist_clean', 'title', 'artist', 'album']], 
    on='track_id', 
    how='left'
)

# Filter for legitimate tracks only (exclude numeric/placeholder titles)
def is_legit_title(title):
    if pd.isna(title):
        return False
    title_str = str(title).strip()
    title_lower = title_str.lower()
    
    # Exclude obviously placeholder titles
    if title_lower in ['', 'none', 'null', 'n/a', 'track', 'song', 'untitled']:
        return False
    
    # Exclude titles that are just numbers and dashes
    import re
    if re.match(r'^\d+[-\s]*$', title_str):
        return False
    if re.match(r'^\d{3,}-\s*$', title_str):
        return False
    if re.match(r'^\d{3}-\s+\d*$', title_str):
        return False
        
    # Must have some actual words (at least 3 characters that aren't numbers/special chars)
    words = re.findall(r'[a-zA-Z]{3,}', title_str)
    if len(words) == 0:
        return False
    
    return True

legitimate_sales = sales_with_tracks[sales_with_tracks['title'].apply(is_legit_title)]
legitimate_sales = legitimate_sales.dropna(subset=['title_clean', 'artist_clean'])

# Calculate revenue by entity
top_entities = legitimate_sales.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().sort_values(ascending=False)

# Get top 10 with full details
top_tracks = []
for i, ((title, artist), revenue) in enumerate(top_entities.head(10).items(), 1):
    entity_tracks = legitimate_sales[
        (legitimate_sales['title_clean'] == title) & (legitimate_sales['artist_clean'] == artist)
    ]
    
    if not entity_tracks.empty:
        best_track = entity_tracks.iloc[0]
        top_tracks.append({
            'rank': i,
            'title': best_track['title'],
            'artist': best_track['artist'],
            'album': best_track['album'],
            'revenue_usd': round(revenue, 2)
        })

print('__RESULT__:')
print(json.dumps(top_tracks, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'var_functions.query_db:8': [{'track_count': '19375'}], 'var_functions.query_db:10': [{'title': 'All Is Forgiven', 'album': 'All Is Forgiven', 'artist': 'Siren', 'year': 'None', 'count': '2'}, {'title': 'Asa Di War - Part 1', 'album': 'Asa Di War', 'artist': 'Bhai Ravinder Singh Ji', 'year': '1997', 'count': '2'}, {'title': 'Avenida', 'album': 'Avenida', 'artist': 'Jukkis Uotila', 'year': '1987', 'count': '2'}, {'title': 'Beautiful (instrumental)', 'album': 'Beautiful', 'artist': 'Damian Marley', 'year': '2006', 'count': '2'}, {'title': 'Bende Can', 'album': 'Bende Can', 'artist': 'Yurdal Tokcan', 'year': 'None', 'count': '2'}], 'var_functions.query_db:12': [{'sale_count': '58049'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'tracks_loaded': 19375, 'sales_loaded': 58049, 'sample_tracks': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'title_clean': "daniel balavoine - l'enfant aux yeux d'italie", 'artist_clean': 'daniel balavoine'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'title_clean': '007', 'artist_clean': ''}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'title_clean': 'action painting! - mustard gas', 'artist_clean': 'action painting!'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': 349, 'revenue_usd': 408.0}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': 122, 'revenue_usd': 137.59}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': 373, 'revenue_usd': 371.57}]}, 'var_functions.execute_python:30': {'top_track_title': 'chi to rome (broke one edit)', 'top_track_artist': 'lazy ants & rob threezy', 'top_track_album': 'chi to rome', 'top_track_year': 2011.0, 'total_revenue_usd': 3091.77, 'num_track_ids': 2}, 'var_functions.execute_python:32': {'top_5_tracks_by_track_id': {'14719': {'revenue': 2522.82, 'info': {'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}}, '5124': {'revenue': 2503.19, 'info': {'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}}, '1344': {'revenue': 2500.72, 'info': {'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}}, '6725': {'revenue': 2489.81, 'info': {'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}}, '10377': {'revenue': 2466.71, 'info': {'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}}}}, 'var_functions.execute_python:34': {'top_entity': {'title': 'none', 'artist': '', 'total_revenue': 14647.52}, 'track_ids': ['2126', '2153', '3422', '4421', '5048', '7036', '7146', '7481', '9478', '9788', '10617', '12019', '12196', '14462', '15469', '16886', '18790'], 'track_details': [{'track_id': '2126', 'title': 'None', 'artist': 'None', 'album': 'Drop Dead Gorgeous'}, {'track_id': '2153', 'title': 'None', 'artist': 'None', 'album': "Live in '05"}, {'track_id': '3422', 'title': 'None', 'artist': 'None', 'album': 'Untitled 2 / Bad Brother'}, {'track_id': '4421', 'title': 'None', 'artist': 'None', 'album': 'None'}, {'track_id': '5048', 'title': 'None', 'artist': 'None', 'album': '20032010'}, {'track_id': '7036', 'title': 'None', 'artist': 'None', 'album': 'Iridescence: Sequencer Sketches, Volume 2'}, {'track_id': '7146', 'title': 'None', 'artist': 'None', 'album': 'Soundtrack'}, {'track_id': '7481', 'title': 'None', 'artist': 'None', 'album': 'This Is My First Album'}, {'track_id': '9478', 'title': 'None', 'artist': 'None', 'album': 'Bakom Kulisserna'}, {'track_id': '9788', 'title': 'None', 'artist': 'None', 'album': 'The Metal Years: Gothic Doom'}, {'track_id': '10617', 'title': 'None', 'artist': 'None', 'album': 'None'}, {'track_id': '12019', 'title': 'None', 'artist': 'None', 'album': 'None'}, {'track_id': '12196', 'title': 'None', 'artist': 'None', 'album': 'Mijn Restaurant!'}, {'track_id': '14462', 'title': 'None', 'artist': 'None', 'album': 'Journey to Persia'}, {'track_id': '15469', 'title': 'None', 'artist': 'None', 'album': 'Live - Blow the House Down'}, {'track_id': '16886', 'title': 'None', 'artist': 'None', 'album': 'East Volume Lotus - Mixed by Ping'}, {'track_id': '18790', 'title': 'None', 'artist': 'None', 'album': 'Ultimo Trem'}]}, 'var_functions.execute_python:38': [{'rank': 1, 'title': '003-', 'artist': 'None', 'album': ' (1980)', 'revenue': 6841.18}, {'rank': 2, 'title': '005-', 'artist': 'None', 'album': '  (unknown)', 'revenue': 5222.0}, {'rank': 3, 'title': '009-  ', 'artist': ' ', 'album': '  (1995)', 'revenue': 5045.7}, {'rank': 4, 'title': '004- ', 'artist': ' ', 'album': ' , 22:   (1997)', 'revenue': 4868.47}, {'rank': 5, 'title': '010-', 'artist': 'None', 'album': ' (2004)', 'revenue': 4734.36}]}

exec(code, env_args)
