code = """import json
import pandas as pd
import re

# Read the full data
tracks_file_path = locals()['var_functions.query_db:6']
sales_file_path = locals()['var_functions.query_db:8']

with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# First, let's properly parse artist/title information
# Many entries have artist embedded in title as "Artist - Title" when artist is "None"
def extract_artist_title(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    
    if artist in ['None', '[unknown]', ''] and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            artist = parts[0]
            title = parts[1]
    
    return pd.Series({'clean_title': title, 'clean_artist': artist})

# Apply extraction
tracks_df[['clean_title', 'clean_artist']] = tracks_df.apply(extract_artist_title, axis=1)

# Create standardized keys for matching
tracks_df['std_title'] = tracks_df['clean_title'].str.lower().str.strip().str.replace(r'[^\w\s]', '', regex=True)
tracks_df['std_artist'] = tracks_df['clean_artist'].str.lower().str.strip().str.replace(r'[^\w\s]', '', regex=True)

# Clean up album info too
tracks_df['std_album'] = tracks_df['album'].astype(str).str.lower().str.strip()

# Extract year numbers (2 or 4 digit)
def extract_year(year_str):
    if pd.isna(year_str) or str(year_str) in ['None', '']:
        return None
    match = re.search(r'(\d{4}|\d{2})', str(year_str))
    return match.group(1) if match else None

tracks_df['year_num'] = tracks_df['year'].apply(extract_year)

# Now aggregate sales by track_id first
track_revenue = sales_df.groupby('track_id').agg({
    'revenue_usd': lambda x: pd.to_numeric(x, errors='coerce').sum(),
    'units_sold': lambda x: pd.to_numeric(x, errors='coerce').sum()
}).reset_index()

# Merge with tracks
tracks_with_revenue = track_revenue.merge(
    tracks_df[['track_id', 'clean_title', 'clean_artist', 'std_title', 'std_artist', 'std_album', 'year_num']], 
    on='track_id', 
    how='left'
)

# Fill NaN values
tracks_with_revenue = tracks_with_revenue.fillna('')

# Now perform entity resolution - group by standardized title and artist
# Also use album and year as secondary criteria

def create_entity_signature(row):
    title = row['std_title'] if row['std_title'] else ''
    artist = row['std_artist'] if row['std_artist'] else ''
    album = row['std_album'] if row['std_album'] not in ['none', ''] else ''
    year = row['year_num'] if row['year_num'] else ''
    
    # Primary key: title + artist
    primary_key = f"{title}|{artist}"
    
    # If title is very short/generic (like numbers), include album in key
    if len(title) < 5 and album:
        primary_key = f"{primary_key}|{album}"
    
    return primary_key

tracks_with_revenue['entity_key'] = tracks_with_revenue.apply(create_entity_signature, axis=1)

# Group by entity key and sum revenues
entity_revenue = tracks_with_revenue.groupby('entity_key').agg({
    'revenue_usd': 'sum',
    'units_sold': 'sum',
    'clean_title': lambda x: x.iloc[0] if not all(v == '' for v in x) else 'Unknown',
    'clean_artist': lambda x: x.iloc[0] if not all(v == '' for v in x) else 'Unknown',
    'std_album': lambda x: x.iloc[0] if not all(v in ['', 'none'] for v in x) else ''
}).reset_index()

# Filter out empty/unknown entities
entity_revenue = entity_revenue[
    (entity_revenue['clean_title'] != '') & 
    (entity_revenue['clean_title'] != 'Unknown') &
    (entity_revenue['entity_key'] != '|') &
    (entity_revenue['entity_key'] != 'none|')
]

# Find the top revenue song
top_song = entity_revenue.loc[entity_revenue['revenue_usd'].idxmax()]

# Get top 10 for context
top_10 = entity_revenue.nlargest(10, 'revenue_usd')

result = {
    'song_title': top_song['clean_title'],
    'artist': top_song['clean_artist'],
    'total_revenue_usd': float(top_song['revenue_usd']),
    'total_units_sold': int(top_song['units_sold']),
    'top_10_preview': top_10[['clean_title', 'clean_artist', 'revenue_usd']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'song_title': 'None', 'artist': 'None', 'total_revenue_usd': 14647.52, 'top_10_preview': [{'entity_key': 'none|none', 'revenue_usd': 14647.52, 'title': 'None', 'artist': 'None'}, {'entity_key': '010-|none', 'revenue_usd': 4163.48, 'title': '010-', 'artist': 'None'}, {'entity_key': 'groovey|rich matteson', 'revenue_usd': 4128.59, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'entity_key': 'the fire still burns|russ ballard', 'revenue_usd': 3807.4, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'entity_key': 'vostok|craig padilla', 'revenue_usd': 3767.95, 'title': 'Vostok', 'artist': 'Craig Padilla'}, {'entity_key': '001-|none', 'revenue_usd': 3742.44, 'title': '001-', 'artist': 'None'}, {'entity_key': '003-|none', 'revenue_usd': 3446.78, 'title': '003-', 'artist': 'None'}, {'entity_key': '003-|', 'revenue_usd': 3394.3999999999996, 'title': '003-', 'artist': ' '}, {'entity_key': '005-|none', 'revenue_usd': 3347.8900000000003, 'title': '005-', 'artist': 'None'}, {'entity_key': '002-|none', 'revenue_usd': 3343.61, 'title': '002-', 'artist': 'None'}]}}

exec(code, env_args)
