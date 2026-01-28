code = """import json
import pandas as pd
import re

# Load all data
sales_file = locals()['var_functions.query_db:0']
tracks_file = locals()['var_functions.query_db:10']

with open(sales_file, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

sales_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

# Convert revenue to float
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

# Merge to see which tracks have sales
merged_df = sales_df.merge(tracks_df, on='track_id', how='left')

# Check for tracks with missing/empty titles
empty_title_tracks = merged_df[
    (merged_df['title'].isna()) | 
    (merged_df['title'] == 'None') | 
    (merged_df['title'] == '') | 
    (merged_df['title'].str.strip() == '')
]

# Filter out invalid tracks for entity resolution
valid_tracks = merged_df[
    ~(merged_df['title'].isna()) & 
    (merged_df['title'] != 'None') & 
    (merged_df['title'] != '') & 
    (merged_df['title'].str.strip() != '')
]

# Clean for entity resolution
def clean_for_matching(text):
    if not text or text == 'None' or pd.isna(text):
        return ''
    text = str(text).lower().strip()
    text = re.sub(r'^(\d+[-_:\.])+\s*', '', text)
    text = re.sub(r'^[a-z0-9]{3,}[-_]', '', text)
    # Remove artist prefix like "Artist - " or "Artist -"
    text = re.sub(r'^[^-]+-\s*', '', text)
    return text.strip()

valid_tracks['clean_title'] = valid_tracks['title'].apply(clean_for_matching)
valid_tracks['clean_artist'] = valid_tracks['artist'].apply(lambda x: '' if pd.isna(x) or x == 'None' else str(x).lower().strip())
valid_tracks['clean_album'] = valid_tracks['album'].apply(lambda x: '' if pd.isna(x) or x == 'None' else str(x).lower().strip())

# Create entity key - if title is empty after cleaning, use original title
valid_tracks['entity_key'] = valid_tracks.apply(
    lambda row: f"{row['clean_title']}|{row['clean_artist']}|{row['clean_album']}",
    axis=1
)

# Group by entities
track_entities = valid_tracks.groupby(['entity_key']).agg({
    'revenue_usd': 'sum',
    'track_id': 'nunique',
    'title': 'first',
    'artist': 'first',
    'album': 'first'
}).reset_index()
track_entities = track_entities.sort_values('revenue_usd', ascending=False)

top_entity = track_entities.iloc[0]

# Also get top individual tracks
top_individual_tracks = valid_tracks.groupby(['track_id', 'title', 'artist', 'album']).agg({
    'revenue_usd': 'sum'
}).reset_index().sort_values('revenue_usd', ascending=False)

print('__RESULT__:')
print(json.dumps({
    'top_entity': {
        'title': top_entity['title'],
        'artist': top_entity['artist'],
        'album': top_entity['album'],
        'revenue': float(top_entity['revenue_usd']),
        'track_variants': int(top_entity['track_id'])
    },
    'top_individual_track': {
        'track_id': str(top_individual_tracks.iloc[0]['track_id']),
        'title': top_individual_tracks.iloc[0]['title'],
        'artist': top_individual_tracks.iloc[0]['artist'],
        'album': top_individual_tracks.iloc[0]['album'],
        'revenue': float(top_individual_tracks.iloc[0]['revenue_usd'])
    },
    'total_valid_tracks_with_sales': len(valid_tracks['track_id'].unique()),
    'total_tracks_in_database': len(tracks_df)
}, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}, {'track_id': '11', 'source_id': '5', 'source_track_id': '855829', 'title': 'None', 'artist': 'Anathema', 'album': 'Alternative 4', 'year': '1998', 'length': '188400', 'language': 'English'}, {'track_id': '12', 'source_id': '5', 'source_track_id': '8987422', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal', 'album': 'Mexico', 'year': 'None', 'length': '129000', 'language': 'English'}, {'track_id': '13', 'source_id': '4', 'source_track_id': '182555-A056', 'title': '002-Particle/Wave', 'artist': 'Lunchbox', 'album': 'Evolver (2002)', 'year': 'None', 'length': '6m 21sec', 'language': 'Eng.'}, {'track_id': '14', 'source_id': '4', 'source_track_id': '51445-A041', 'title': '001-Deja Vu', 'artist': 'Blanket', 'album': 'Nice (2000)', 'year': 'None', 'length': '3m 36sec', 'language': 'ng.'}, {'track_id': '15', 'source_id': '4', 'source_track_id': '231700-A015', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters', 'album': 'Andy Bey and the Bey Sisters (2000)', 'year': 'None', 'length': '2m 55sec', 'language': 'Eng.'}, {'track_id': '16', 'source_id': '1', 'source_track_id': 'WoM186470', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch', 'album': 'The Classical Album, Volume 1', 'year': '1996', 'length': '04:04', 'language': 'None'}, {'track_id': '17', 'source_id': '2', 'source_track_id': 'MBox374174-HH', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None', 'album': 'Die frühen Aufnahmen', 'year': 'None', 'length': '188', 'language': '[Multiple languages]'}, {'track_id': '18', 'source_id': '4', 'source_track_id': '131573-A04', 'title': '00-1', 'artist': 'None', 'album': ' (2010)', 'year': 'None', 'length': '3m 52sec', 'language': 'Jap.'}, {'track_id': '19', 'source_id': '5', 'source_track_id': '12319476', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye', 'album': 'RYEot powRR', 'year': '2011', 'length': '263497', 'language': 'English'}, {'track_id': '20', 'source_id': '1', 'source_track_id': 'WoM109609', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini', 'album': 'Forbidden Broadway 2001: A Spoof Odyssey (2001 original off-Broadway cast)', 'year': '2901', 'length': '03:39', 'language': 'None'}], 'var_functions.execute_python:8': {'sales_count': 58049, 'tracks_count': 20, 'first_sale': {'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, 'first_track': {'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'top_track_id': '14719', 'top_revenue': 2522.82, 'track_details': {'track_id': '14719', 'source_id': '5', 'source_track_id': '11323763', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009', 'length': '223000', 'language': 'German'}, 'total_tracks_in_sales': 19375}, 'var_functions.execute_python:14': {'top_track_title': '', 'top_track_artist': '', 'top_track_album': '(2002)', 'top_revenue': 4290.95, 'track_variants': 13}, 'var_functions.execute_python:16': {'top_5_tracks_by_track_id': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'revenue_usd': 2522.82}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'revenue_usd': 2503.19}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'revenue_usd': 2500.72}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'revenue_usd': 2489.81}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'revenue_usd': 2466.71}], 'top_5_entities': [{'entities': 6153, 'revenue': 4128.59, 'track_variants': 3}, {'entities': 15141, 'revenue': 3807.4, 'track_variants': 2}, {'entities': 15861, 'revenue': 3803.5, 'track_variants': 2}, {'entities': 17841, 'revenue': 3779.05, 'track_variants': 2}, {'entities': 16161, 'revenue': 3703.98, 'track_variants': 2}]}, 'var_functions.execute_python:20': {'top_entity_revenue': 4290.95, 'top_entity_title': '', 'top_entity_artist': '', 'top_entity_album': '(2002)', 'track_variants_count': 3, 'top_individual_tracks': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'revenue_usd': 2522.82}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'revenue_usd': 2503.19}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'revenue_usd': 2500.72}]}}

exec(code, env_args)
