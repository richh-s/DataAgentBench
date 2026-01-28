code = """import json
import pandas as pd

# Read the full tracks data from the JSON file
tracks_file_path = locals()['var_functions.query_db:6']
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

# Read the full sales data from the JSON file  
sales_file_path = locals()['var_functions.query_db:8']
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

# Convert to DataFrames for analysis
tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Clean up the data - convert revenue to numeric and check data
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')
tracks_df['year'] = tracks_df['year'].astype(str)

# Perform entity resolution by grouping similar tracks
# Create a standardized key for grouping
tracks_df['std_title'] = tracks_df['title'].str.lower().str.strip()
tracks_df['std_artist'] = tracks_df['artist'].str.lower().str.strip()
tracks_df['std_album'] = tracks_df['album'].str.lower().str.strip()
tracks_df['std_year'] = tracks_df['year'].str.extract(r'(\d{4}|\d{2})')[0]

# Clean up None/NaN values
tracks_df = tracks_df.fillna('')

# Create a grouping key based on title and artist primarily
# This is a simplified entity resolution approach
tracks_df['entity_key'] = tracks_df['std_title'] + '|' + tracks_df['std_artist']

# Merge sales with tracks
sales_with_track = sales_df.merge(tracks_df[['track_id', 'title', 'artist', 'entity_key']], 
                                 on='track_id', how='left')

# Group by entity key to combine sales for the same song
grouped_sales = sales_with_track.groupby('entity_key').agg({
    'revenue_usd': 'sum',
    'title': lambda x: x.iloc[0],  # Keep first title
    'artist': lambda x: x.iloc[0]   # Keep first artist
}).reset_index()

# Find the song with maximum revenue
max_revenue_row = grouped_sales.loc[grouped_sales['revenue_usd'].idxmax()]

# Also get top 10 for context
top_10 = grouped_sales.nlargest(10, 'revenue_usd')

result = {
    'song_title': max_revenue_row['title'],
    'artist': max_revenue_row['artist'],
    'total_revenue_usd': float(max_revenue_row['revenue_usd']),
    'top_10_preview': top_10.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
