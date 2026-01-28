code = """import json
import pandas as pd

# Load complete data
tracks_var = locals()['var_functions.query_db:12']
if isinstance(tracks_var, str) and tracks_var.endswith('.json'):
    with open(tracks_var, 'r') as f:
        tracks_data = json.load(f)
else:
    tracks_data = tracks_var

sales_var = locals()['var_functions.query_db:6']
if isinstance(sales_var, str) and sales_var.endswith('.json'):
    with open(sales_var, 'r') as f:
        sales_data = json.load(f)
else:
    sales_data = sales_var

# Create DataFrames
df_tracks = pd.DataFrame(tracks_data)
df_sales = pd.DataFrame(sales_data)

# Clean data types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['revenue_usd'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Entity resolution: Aggregate revenue by track_id first, then join with tracks
track_revenue = df_sales.groupby('track_id')['revenue_usd'].sum().reset_index()
track_revenue = track_revenue.sort_values('revenue_usd', ascending=False)

# Merge with tracks to get song details
df_tracks_clean = df_tracks[['track_id', 'title', 'artist']].copy()
df_tracks_clean['title_artist'] = df_tracks_clean['title'].fillna('') + ' - ' + df_tracks_clean['artist'].fillna('')

# Merge revenue with tracks
revenue_with_details = pd.merge(track_revenue, df_tracks_clean, on='track_id', how='left')
revenue_with_details = revenue_with_details.sort_values('revenue_usd', ascending=False)

# For entity resolution, group by normalized title and artist
def normalize_text(text):
    if pd.isna(text) or text == 'None':
        return ''
    return str(text).lower().strip()

df_tracks_clean['norm_title'] = df_tracks_clean['title'].apply(normalize_text)
df_tracks_clean['norm_artist'] = df_tracks_clean['artist'].apply(normalize_text)

# Group tracks by normalized title and artist
track_groups = df_tracks_clean.groupby(['norm_title', 'norm_artist'])['track_id'].apply(list).reset_index()

# Calculate total revenue for each group
def get_group_revenue(track_ids):
    return df_sales[df_sales['track_id'].isin(track_ids)]['revenue_usd'].sum()

track_groups['total_revenue'] = track_groups['track_id'].apply(get_group_revenue)
track_groups = track_groups.sort_values('total_revenue', ascending=False)

# Get the top song
top_song = track_groups.iloc[0]
top_track_ids = top_song['track_id']
top_revenue = top_song['total_revenue']

# Get actual song details for these tracks
top_song_details = df_tracks_clean[df_tracks_clean['track_id'].isin(top_track_ids)]

print('__RESULT__:')
print(json.dumps({
    'top_song_title': top_song_details.iloc[0]['title'],
    'top_song_artist': top_song_details.iloc[0]['artist'],
    'total_revenue': float(top_revenue),
    'track_count': len(top_track_ids),
    'track_ids_sample': top_track_ids[:5],
    'revenue_by_track': [
        {
            'track_id': tid,
            'revenue': float(df_sales[df_sales['track_id'] == tid]['revenue_usd'].sum())
        } for tid in top_track_ids[:10]
    ]
}))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:4': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'sales_rows': 58049, 'tracks_rows': 10, 'sales_columns': ['sale_id', 'track_id', 'country', 'store', 'units_sold', 'revenue_usd'], 'tracks_columns': ['track_id', 'source_id', 'source_track_id', 'title', 'artist', 'album', 'year', 'length', 'language'], 'sample_tracks': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'tracks_count': 19375, 'sales_count': 58049, 'unique_track_ids_in_sales': 19375, 'unique_track_ids_in_tracks': 19375, 'sales_revenue_stats': {'mean': 284.72739151406574, 'max': 641.82, 'min': 0.99, 'total': 16528140.350000001}}, 'var_functions.execute_python:18': {'first_20_tracks': [{'id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None'}, {'id': '2', 'title': '007', 'artist': '[unknown]'}, {'id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None'}, {'id': '4', 'title': 'Your Grace', 'artist': 'Kathy Troccoli'}, {'id': '5', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet'}, {'id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young'}, {'id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None'}, {'id': '8', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None'}, {'id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington'}, {'id': '10', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας'}, {'id': '11', 'title': 'None', 'artist': 'Anathema'}, {'id': '12', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal'}, {'id': '13', 'title': '002-Particle/Wave', 'artist': 'Lunchbox'}, {'id': '14', 'title': '001-Deja Vu', 'artist': 'Blanket'}, {'id': '15', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters'}, {'id': '16', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch'}, {'id': '17', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None'}, {'id': '18', 'title': '00-1', 'artist': 'None'}, {'id': '19', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye'}, {'id': '20', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini'}]}, 'var_functions.execute_python:22': {'tracks_after_cleaning': 19308, 'sample_normalized': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'clean_title': "L'enfant aux yeux d'Italie", 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'lenfantauxyeuxditalie', 'artist_key': 'unknown'}, {'track_id': '2', 'title': '007', 'clean_title': '007', 'artist': '[unknown]', 'clean_artist': 'Unknown', 'title_key': '007', 'artist_key': 'unknown'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'clean_title': 'Mustard Gas', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'mustardgas', 'artist_key': 'unknown'}, {'track_id': '4', 'title': 'Your Grace', 'clean_title': 'Your Grace', 'artist': 'Kathy Troccoli', 'clean_artist': 'Kathy Troccoli', 'title_key': 'yourgrace', 'artist_key': 'kathytroccoli'}, {'track_id': '5', 'title': "Well You Needn't", 'clean_title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'clean_artist': 'Ernie Stadler Jazz Quintet', 'title_key': 'wellyouneednt', 'artist_key': 'erniestadlerjazzquintet'}, {'track_id': '6', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'clean_title': 'Try (acoustic)', 'artist': 'Neil Young', 'clean_artist': 'Neil Young', 'title_key': 'tryacoustic', 'artist_key': 'neilyoung'}, {'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'clean_title': 'Sttreet Hype', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'sttreethype', 'artist_key': 'unknown'}, {'track_id': '8', 'title': 'Luce Dufault - Ballade à donner', 'clean_title': 'Ballade à donner', 'artist': 'None', 'clean_artist': 'Unknown', 'title_key': 'balladedonner', 'artist_key': 'unknown'}, {'track_id': '9', 'title': "Just Like Tom Thumb's Blues (live)", 'clean_title': "Just Like Tom Thumb's Blues", 'artist': 'Wendy Saddington', 'clean_artist': 'Wendy Saddington', 'title_key': 'justliketomthumbsblues', 'artist_key': 'wendysaddington'}, {'track_id': '10', 'title': 'Στα καμένα', 'clean_title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'clean_artist': 'Λαυρέντης Μαχαιρίίτσας', 'title_key': '', 'artist_key': ''}], 'unique_title_keys': 16881, 'unique_combinations': 18500}}

exec(code, env_args)
