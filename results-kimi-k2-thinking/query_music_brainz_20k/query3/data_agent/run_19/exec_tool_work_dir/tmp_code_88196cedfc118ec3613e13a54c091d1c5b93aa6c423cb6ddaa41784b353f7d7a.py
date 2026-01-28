code = """import json
import pandas as pd

# Load data to verify the top entity
tracks_file_path = locals()['var_functions.query_db:14']
sales_file_path = locals()['var_functions.query_db:20']

with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

# Recreate the entity resolution
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])

def clean_text(text):
    if pd.isna(text) or text is None:
        return ''
    return str(text).lower().strip()

tracks_df['title_clean'] = tracks_df['title'].apply(clean_text)
tracks_df['artist_clean'] = tracks_df['artist'].apply(clean_text)
tracks_df['album_clean'] = tracks_df['album'].apply(clean_text)

# Extract artist from title when missing
mask_no_artist = (tracks_df['artist_clean'] == '') | (tracks_df['artist_clean'] == 'none') | (tracks_df['artist_clean'] == '[unknown]')
def extract_artist_from_title(title):
    if pd.notna(title) and ' - ' in str(title):
        parts = str(title).split(' - ', 1)
        if len(parts) == 2:
            return clean_text(parts[0])
    return ''
tracks_df.loc[mask_no_artist, 'artist_clean'] = tracks_df.loc[mask_no_artist, 'title'].apply(extract_artist_from_title)

# Group by title and artist to find the top entity
entity_revenue = sales_df.copy()
# Merge to get track info
sales_with_tracks = entity_revenue.merge(
    tracks_df[['track_id', 'title_clean', 'artist_clean']], 
    on='track_id', 
    how='left'
)

# Calculate revenue by entity (title_clean + artist_clean)
entity_totals = sales_with_tracks.groupby(['title_clean', 'artist_clean'])['revenue_usd'].sum().sort_values(ascending=False)

# Get top entity
top_entity_key = entity_totals.index[0]
top_revenue = entity_totals.iloc[0]

# Find all track_ids for this entity
entity_tracks = tracks_df[
    (tracks_df['title_clean'] == top_entity_key[0]) & 
    (tracks_df['artist_clean'] == top_entity_key[1])
]

result = {
    'top_entity': {
        'title': top_entity_key[0],
        'artist': top_entity_key[1],
        'total_revenue': round(top_revenue, 2)
    },
    'track_ids': entity_tracks['track_id'].tolist(),
    'track_details': entity_tracks[['track_id', 'title', 'artist', 'album']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'var_functions.query_db:8': [{'track_count': '19375'}], 'var_functions.query_db:10': [{'title': 'All Is Forgiven', 'album': 'All Is Forgiven', 'artist': 'Siren', 'year': 'None', 'count': '2'}, {'title': 'Asa Di War - Part 1', 'album': 'Asa Di War', 'artist': 'Bhai Ravinder Singh Ji', 'year': '1997', 'count': '2'}, {'title': 'Avenida', 'album': 'Avenida', 'artist': 'Jukkis Uotila', 'year': '1987', 'count': '2'}, {'title': 'Beautiful (instrumental)', 'album': 'Beautiful', 'artist': 'Damian Marley', 'year': '2006', 'count': '2'}, {'title': 'Bende Can', 'album': 'Bende Can', 'artist': 'Yurdal Tokcan', 'year': 'None', 'count': '2'}], 'var_functions.query_db:12': [{'sale_count': '58049'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'tracks_loaded': 19375, 'sales_loaded': 58049, 'sample_tracks': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'title_clean': "daniel balavoine - l'enfant aux yeux d'italie", 'artist_clean': 'daniel balavoine'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'title_clean': '007', 'artist_clean': ''}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'title_clean': 'action painting! - mustard gas', 'artist_clean': 'action painting!'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': 349, 'revenue_usd': 408.0}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': 122, 'revenue_usd': 137.59}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': 373, 'revenue_usd': 371.57}]}, 'var_functions.execute_python:30': {'top_track_title': 'chi to rome (broke one edit)', 'top_track_artist': 'lazy ants & rob threezy', 'top_track_album': 'chi to rome', 'top_track_year': 2011.0, 'total_revenue_usd': 3091.77, 'num_track_ids': 2}, 'var_functions.execute_python:32': {'top_5_tracks_by_track_id': {'14719': {'revenue': 2522.82, 'info': {'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}}, '5124': {'revenue': 2503.19, 'info': {'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}}, '1344': {'revenue': 2500.72, 'info': {'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}}, '6725': {'revenue': 2489.81, 'info': {'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}}, '10377': {'revenue': 2466.71, 'info': {'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}}}}}

exec(code, env_args)
