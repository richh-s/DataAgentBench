code = """import json
import pandas as pd
import re

# Load the full sales data by track_id
sales_file_path = locals()['var_functions.query_db:11']
with open(sales_file_path, 'r') as f:
    sales_by_track = json.load(f)

# Load the full tracks data
tracks_file_path = locals()['var_functions.query_db:8']
with open(tracks_file_path, 'r') as f:
    tracks = json.load(f)

# Convert to DataFrames
df_sales = pd.DataFrame(sales_by_track)
df_tracks = pd.DataFrame(tracks)

# Ensure revenue is numeric
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Get the track_id with the highest revenue
top_track_id = df_sales.loc[df_sales['total_revenue'].idxmax(), 'track_id']

# Find all tracks that might be duplicates by looking at the metadata
top_track_meta = df_tracks[df_tracks['track_id'] == top_track_id]

if not top_track_meta.empty:
    top_title = str(top_track_meta.iloc[0]['title'])
    top_artist = str(top_track_meta.iloc[0]['artist'])
    top_album = str(top_track_meta.iloc[0]['album'])
    
    # Look for similar tracks
    search_title = top_title.split('-')[0].split('(')[0].strip().lower() if top_title else ''
    search_artist = top_artist.lower() if top_artist and top_artist != 'None' and top_artist != '[unknown]' else ''
    
    similar_tracks = df_tracks[
        (df_tracks['title'].str.lower().str.contains(search_title, na=False)) |
        (df_tracks['artist'].str.lower().str.contains(search_artist, na=False))
    ]
    
    similar_track_ids = similar_tracks['track_id'].astype(str).tolist()
    
    # Sum revenue for all similar tracks
    total_revenue = df_sales[df_sales['track_id'].isin(similar_track_ids)]['total_revenue'].sum()
    
    # Get the most common clean metadata
    clean_title = similar_tracks['title'].mode().iloc[0] if not similar_tracks.empty else 'Unknown Title'
    clean_artist = similar_tracks['artist'].mode().iloc[0] if not similar_tracks.empty else 'Unknown Artist'
    clean_album = similar_tracks['album'].mode().iloc[0] if not similar_tracks.empty else 'Unknown Album'
    
    result = {
        'title': clean_title,
        'artist': clean_artist,
        'album': clean_album,
        'total_revenue': round(float(total_revenue), 2)
    }
else:
    # If no metadata found, just return the raw track_id info
    top_revenue = df_sales.loc[df_sales['total_revenue'].idxmax(), 'total_revenue']
    result = {
        'title': f'Track ID {top_track_id}',
        'artist': 'Unknown',
        'album': 'Unknown',
        'total_revenue': round(float(top_revenue), 2)
    }

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:4': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}, {'track_id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005'}, {'track_id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05'}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96'}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007'}, {'track_id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997'}], 'var_functions.query_db:7': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:16': {'title': 'Unknown Title', 'artist': 'Unknown Artist', 'album': '(Unknown)', 'total_revenue': 77183.57}}

exec(code, env_args)
