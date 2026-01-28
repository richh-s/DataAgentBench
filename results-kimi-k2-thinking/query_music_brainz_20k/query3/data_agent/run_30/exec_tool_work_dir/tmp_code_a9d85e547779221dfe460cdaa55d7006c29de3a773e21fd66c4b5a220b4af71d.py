code = """import json
import pandas as pd
import re

# Load full data
tracks_file = locals()['var_functions.query_db:7']
sales_file = locals()['var_functions.query_db:8']

with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

with open(sales_file, 'r') as f:
    sales_data = json.load(f)

# Create DataFrames
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Normalize functions
def normalize_text(text):
    if pd.isna(text) or text is None or str(text).strip() == '' or str(text) == 'None' or text == '[unknown]':
        return ''
    return str(text).strip().lower()

def normalize_year(year):
    if pd.isna(year) or year is None or str(year).strip() == '' or str(year) == 'None':
        return ''
    
    year_str = str(year).strip()
    
    # Handle formats like '75, '05, '11
    if year_str.startswith("'") and len(year_str) >= 3:
        year_str = year_str[1:]
    
    # Remove non-digit characters
    year_str = re.sub(r'[^0-9]', '', year_str)
    
    if not year_str:
        return ''
    
    try:
        year_num = int(year_str)
        
        # Convert 2-digit years to 4-digit
        if year_num < 100:
            if year_num < 30:
                year_num = 2000 + year_num  # 05 -> 2005
            else:
                year_num = 1900 + year_num  # 75 -> 1975
        
        return str(year_num)
    except:
        return ''

def extract_title_key(title):
    if pd.isna(title) or title is None or str(title).strip() == '' or str(title) == 'None':
        return ''
    
    title_str = str(title).strip()
    
    # Remove artist prefix (e.g., "Artist - Title")
    if ' - ' in title_str:
        parts = title_str.split(' - ', 1)
        if len(parts) == 2:
            title_str = parts[1]
    
    # Remove content in parentheses or brackets
    title_str = re.sub(r'\s*\([^)]*\)', '', title_str)
    title_str = re.sub(r'\s*\[[^\]]*\]', '', title_str)
    
    # Remove track numbers at start (e.g., "001- ", "007 ", "019-")
    title_str = re.sub(r'^\d{2,4}[-.\s]*', '', title_str)
    
    # Remove extra whitespace
    title_str = re.sub(r'\s+', ' ', title_str)
    
    return title_str.strip().lower()

# Apply normalization
tracks_df['norm_title'] = tracks_df['title'].apply(extract_title_key)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_text)
tracks_df['norm_album'] = tracks_df['album'].apply(normalize_text)
tracks_df['norm_year'] = tracks_df['year'].apply(normalize_year)

# Create matching key (first 60 chars of title + artist)
tracks_df['match_key'] = tracks_df['norm_title'].str[:60] + '|' + tracks_df['norm_artist'].str[:40]

# Aggregate sales revenue by track_id
sales_agg = sales_df.groupby('track_id').agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum'
}).reset_index()

# Convert revenue to numeric (it's stored as string in the data)
sales_agg['revenue_usd'] = pd.to_numeric(sales_agg['revenue_usd'], errors='coerce')
sales_agg['units_sold'] = pd.to_numeric(sales_agg['units_sold'], errors='coerce')

# Merge tracks with sales
tracks_with_sales = tracks_df.merge(sales_agg, on='track_id', how='inner')

# Group by match key to combine duplicates and sum revenues
track_revenue = tracks_with_sales.groupby('match_key').agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum',
    'norm_title': 'first',  # Take first occurrence
    'norm_artist': 'first',
    'track_id': lambda x: list(x)[:5]  # List of track_ids for verification
}).reset_index()

# Find track with maximum revenue
top_track = track_revenue.loc[track_revenue['revenue_usd'].idxmax()]

result = {
    'top_track_title': top_track['norm_title'],
    'top_track_artist': top_track['norm_artist'],
    'total_revenue_usd': float(top_track['revenue_usd']),
    'total_units_sold': float(top_track['units_sold']),
    'track_ids': top_track['track_id']
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:3': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'tracks_shape': [19375, 9], 'sales_shape': [58049, 6], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd']}}

exec(code, env_args)
