code = """import json
import pandas as pd
import re

# Access the data files
tracks_file = locals()['var_functions.query_db:7']
sales_file = locals()['var_functions.query_db:8']

# Load full data
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Clean and normalize tracks data
def clean_text(text):
    if text is None or pd.isna(text) or text == 'None' or text == '[unknown]':
        return ''
    return str(text).strip().lower()

def normalize_year(year):
    if year is None or pd.isna(year) or year == 'None' or year == '':
        return ''
    
    year_str = str(year).strip()
    # Handle various year formats
    if year_str.startswith("'"):
        year_str = year_str[1:]  # Remove leading quote
    
    # Try to parse as number
    try:
        year_num = int(float(year_str))
        if year_num < 100:
            # Two-digit year, assume 1900s or 2000s
            if year_num < 30:
                year_num = 2000 + year_num
            else:
                year_num = 1900 + year_num
        return str(year_num)
    except:
        return ''

def extract_main_title(title):
    """Extract main title without artist prefix or parenthetical info"""
    if not title:
        return ''
    
    # Remove artist - title format (e.g., "Artist - Title")
    title = str(title)
    if ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            title = parts[1]  # Take the title part
    
    # Remove content in parentheses/brackets
    title = re.sub(r'\s*\([^)]*\)', '', title)
    title = re.sub(r'\s*\[[^\]]*\]', '', title)
    
    # Remove track numbers at start
    title = re.sub(r'^\d+\s*[-.]\s*', '', title)
    title = re.sub(r'^\d{3}\s*', '', title)  # Remove 3-digit codes like 007, 001
    
    return title.strip()

# Apply cleaning
tracks_df['clean_title'] = tracks_df['title'].apply(extract_main_title)
tracks_df['clean_artist'] = tracks_df['artist'].apply(clean_text)
tracks_df['clean_album'] = tracks_df['album'].apply(clean_text)
tracks_df['clean_year'] = tracks_df['year'].apply(normalize_year)

# Create a simplified title for matching (first 50 chars of cleaned title)
tracks_df['title_key'] = tracks_df['clean_title'].str[:50]

# Aggregate sales by track_id
sales_agg = sales_df.groupby('track_id').agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum'
}).reset_index()

# Merge tracks with sales
tracks_with_sales = tracks_df.merge(sales_agg, on='track_id', how='inner')

print('__RESULT__:')
print(json.dumps({
    'total_tracks_with_sales': len(tracks_with_sales),
    'total_revenue_all': float(tracks_with_sales['revenue_usd'].sum()),
    'sample_data': tracks_with_sales[['track_id', 'title', 'clean_title', 'clean_artist', 'revenue_usd']].head(10).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:3': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'tracks_shape': [19375, 9], 'sales_shape': [58049, 6], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}}

exec(code, env_args)
