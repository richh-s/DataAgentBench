code = """import json
import pandas as pd
import re
import os

# Load data using locals()
tracks_file_path = locals()['var_functions.query_db:14']
sales_file_path = locals()['var_functions.query_db:20']

# Load tracks data
if isinstance(tracks_file_path, str) and os.path.exists(tracks_file_path):
    with open(tracks_file_path, 'r') as f:
        tracks_data = json.load(f)
else:
    tracks_data = tracks_file_path

# Load sales data  
if isinstance(sales_file_path, str) and os.path.exists(sales_file_path):
    with open(sales_file_path, 'r') as f:
        sales_data = json.load(f)
else:
    sales_data = sales_file_path

print(f"Loaded {len(tracks_data)} tracks and {len(sales_data)} sales records")

# Data cleaning functions
def clean_text(text):
    if pd.isna(text) or text is None:
        return ''
    return str(text).lower().strip()

def extract_year(year):
    if pd.isna(year) or year is None:
        return None
    try:
        s = str(year)
        match = re.search(r'(\\d{4})', s)
        if match:
            return int(match.group(1))
        if len(s.strip()) == 2 and s.strip().isdigit():
            y = int(s.strip())
            return 2000 + y if y <= 25 else 1900 + y
        return None
    except:
        return None

# Process DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Clean tracks data
tracks_df['title_clean'] = tracks_df['title'].apply(clean_text)
tracks_df['artist_clean'] = tracks_df['artist'].apply(clean_text)
tracks_df['album_clean'] = tracks_df['album'].apply(clean_text)
tracks_df['year_clean'] = tracks_df['year'].apply(extract_year)

# Extract artist from title when artist is missing/unknown
mask_no_artist = (tracks_df['artist_clean'] == '') | (tracks_df['artist_clean'] == 'none') | (tracks_df['artist_clean'] == '[unknown]')

def extract_artist_from_title(title):
    if pd.notna(title) and ' - ' in str(title):
        parts = str(title).split(' - ', 1)
        if len(parts) == 2:
            return clean_text(parts[0])
    return ''

tracks_df.loc[mask_no_artist, 'artist_clean'] = tracks_df.loc[mask_no_artist, 'title'].apply(extract_artist_from_title)

# Clean sales data
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'])
sales_df['units_sold'] = pd.to_numeric(sales_df['units_sold'])

result = {
    'tracks_loaded': len(tracks_df),
    'sales_loaded': len(sales_df),
    'sample_tracks': tracks_df[['track_id', 'title', 'artist', 'title_clean', 'artist_clean']].head(3).to_dict('records'),
    'sample_sales': sales_df.head(3).to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'var_functions.query_db:8': [{'track_count': '19375'}], 'var_functions.query_db:10': [{'title': 'All Is Forgiven', 'album': 'All Is Forgiven', 'artist': 'Siren', 'year': 'None', 'count': '2'}, {'title': 'Asa Di War - Part 1', 'album': 'Asa Di War', 'artist': 'Bhai Ravinder Singh Ji', 'year': '1997', 'count': '2'}, {'title': 'Avenida', 'album': 'Avenida', 'artist': 'Jukkis Uotila', 'year': '1987', 'count': '2'}, {'title': 'Beautiful (instrumental)', 'album': 'Beautiful', 'artist': 'Damian Marley', 'year': '2006', 'count': '2'}, {'title': 'Bende Can', 'album': 'Bende Can', 'artist': 'Yurdal Tokcan', 'year': 'None', 'count': '2'}], 'var_functions.query_db:12': [{'sale_count': '58049'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
