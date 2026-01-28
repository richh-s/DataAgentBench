code = """import json
import pandas as pd

# Read the full tracks data
with open(var_functions.query_db:14, 'r') as f:
    tracks = json.load(f)

# Create DataFrame
tracks_df = pd.DataFrame(tracks)

# Standardize and clean tracks
# Clean up title, artist, album fields
tracks_df['title_clean'] = tracks_df['title'].fillna('').str.lower().str.strip()
tracks_df['artist_clean'] = tracks_df['artist'].fillna('').str.lower().str.strip()
tracks_df['album_clean'] = tracks_df['album'].fillna('').str.lower().str.strip()

# Clean year field - extract 4-digit years
def extract_year(year):
    if pd.isna(year) or year is None:
        return None
    try:
        # Convert to string
        s = str(year)
        # Look for 4 consecutive digits
        import re
        match = re.search(r'(\d{4})', s)
        if match:
            return int(match.group(1))
        # If only 2 digits at start, assume 1900s or 2000s
        if len(s.strip()) == 2 and s.strip().isdigit():
            y = int(s.strip())
            if y >= 0 and y <= 25:
                return 2000 + y
            elif y >= 26 and y <= 99:
                return 1900 + y
        return None
    except:
        return None

tracks_df['year_clean'] = tracks_df['year'].apply(extract_year)

# Load sales data completely
with open(var_functions.query_db:6, 'r') as f:
    sales_preview = json.load(f)

# Get all sales (the preview showed it's not the full result)
# Need to query again to get full sales data
print('__RESULT__:')
print('Data loaded, need to query full sales data')"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}], 'var_functions.query_db:8': [{'track_count': '19375'}], 'var_functions.query_db:10': [{'title': 'All Is Forgiven', 'album': 'All Is Forgiven', 'artist': 'Siren', 'year': 'None', 'count': '2'}, {'title': 'Asa Di War - Part 1', 'album': 'Asa Di War', 'artist': 'Bhai Ravinder Singh Ji', 'year': '1997', 'count': '2'}, {'title': 'Avenida', 'album': 'Avenida', 'artist': 'Jukkis Uotila', 'year': '1987', 'count': '2'}, {'title': 'Beautiful (instrumental)', 'album': 'Beautiful', 'artist': 'Damian Marley', 'year': '2006', 'count': '2'}, {'title': 'Bende Can', 'album': 'Bende Can', 'artist': 'Yurdal Tokcan', 'year': 'None', 'count': '2'}], 'var_functions.query_db:12': [{'sale_count': '58049'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
