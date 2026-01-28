code = """import json, os, pandas as pd

# Helper to load JSON from stored result (either file path or list)

def load_json(res):
    if isinstance(res, str) and os.path.exists(res):
        with open(res, 'r') as f:
            return json.load(f)
    return res if isinstance(res, list) else []

# Access stored results
sales_path = locals()['var_functions.query_db:8']
tracks_path = locals()['var_functions.query_db:9']
sales_list = load_json(sales_path)
tracks_list = load_json(tracks_path)

# Create DataFrames
sales_df = pd.DataFrame(sales_list)
tracks_df = pd.DataFrame(tracks_list)

# Ensure necessary columns exist
if sales_df.empty or tracks_df.empty:
    answer = {'error': 'Data missing', 'title': 'N/A', 'artist': 'N/A', 'total_revenue_usd': 0}
else:
    # If columns named differently in sales, rename to track_id and revenue
    if 'sale_track_id' in sales_df.columns:
        sales_df = sales_df.rename(columns={'sale_track_id': 'track_id', 'total_revenue': 'revenue_usd'})
    # Normalize revenue column name to revenue_usd if needed
    if 'revenue_usd' not in sales_df.columns:
        sales_df.rename(columns={'total_revenue': 'revenue_usd'}, inplace=True)
    # Ensure numeric revenue
    sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')
    # Ensure track_id is string
    sales_df['track_id'] = sales_df['track_id'].astype(str)
    tracks_df['track_id'] = tracks_df['track_id'].astype(str)
    # Clean title and artist: strip, lowercase, replace missing with empty string
    for col in ['title', 'artist']:
        tracks_df[col] = tracks_df[col].fillna('').astype(str).str.strip().str.lower()
    # Merge sales with tracks to attach metadata
    merged = sales_df.merge(tracks_df[['track_id', 'title', 'artist']], on='track_id', how='left')
    # Filter out rows where title or artist is empty (skip rows without metadata)
    merged = merged[(merged['title'] != '') & (merged['artist'] != '')]
    # Group by title and artist to sum revenue across duplicate tracks
    song_revenue = merged.groupby(['title', 'artist'], as_index=False)['revenue_usd'].sum()
    # Find the song with highest total revenue
    top_idx = song_revenue['revenue_usd'].idxmax()
    top_song = song_revenue.loc[top_idx]
    answer = {
        'title': top_song['title'].strip().title(),
        'artist': top_song['artist'].strip().title(),
        'total_revenue_usd': round(top_song['revenue_usd'], 2)
    }

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.query_db:2': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}, {'track_id': '11', 'source_id': '5', 'source_track_id': '855829', 'title': 'None', 'artist': 'Anathema', 'album': 'Alternative 4', 'year': '1998', 'length': '188400', 'language': 'English'}, {'track_id': '12', 'source_id': '5', 'source_track_id': '8987422', 'title': 'El Vaquero Chido (The Cool Cowboy)', 'artist': 'Byron Brizuela & Enrique Carbajal', 'album': 'Mexico', 'year': 'None', 'length': '129000', 'language': 'English'}, {'track_id': '13', 'source_id': '4', 'source_track_id': '182555-A056', 'title': '002-Particle/Wave', 'artist': 'Lunchbox', 'album': 'Evolver (2002)', 'year': 'None', 'length': '6m 21sec', 'language': 'Eng.'}, {'track_id': '14', 'source_id': '4', 'source_track_id': '51445-A041', 'title': '001-Deja Vu', 'artist': 'Blanket', 'album': 'Nice (2000)', 'year': 'None', 'length': '3m 36sec', 'language': 'ng.'}, {'track_id': '15', 'source_id': '4', 'source_track_id': '231700-A015', 'title': '019-Feeling Good', 'artist': 'Andy Bey and the Bey Sisters', 'album': 'Andy Bey and the Bey Sisters (2000)', 'year': 'None', 'length': '2m 55sec', 'language': 'Eng.'}, {'track_id': '16', 'source_id': '1', 'source_track_id': 'WoM186470', 'title': 'Scottish Fantasy: Adagio cantabile (The Classical Album, Volume 1)', 'artist': 'Max Bruch', 'album': 'The Classical Album, Volume 1', 'year': '1996', 'length': '04:04', 'language': 'None'}, {'track_id': '17', 'source_id': '2', 'source_track_id': 'MBox374174-HH', 'title': 'Marlene Dietrich - Wo ist der Mann?', 'artist': 'None', 'album': 'Die frühen Aufnahmen', 'year': 'None', 'length': '188', 'language': '[Multiple languages]'}, {'track_id': '18', 'source_id': '4', 'source_track_id': '131573-A04', 'title': '00-1', 'artist': 'None', 'album': ' (2010)', 'year': 'None', 'length': '3m 52sec', 'language': 'Jap.'}, {'track_id': '19', 'source_id': '5', 'source_track_id': '12319476', 'title': 'Gimme Dat (remix)', 'artist': 'Rye Rye', 'album': 'RYEot powRR', 'year': '2011', 'length': '263497', 'language': 'English'}, {'track_id': '20', 'source_id': '1', 'source_track_id': 'WoM109609', 'title': "AmnerisIntro:EveryStoryIsaLoveStory/HeatherHeadley/It'sCheesy:EasyasLife(ForbiddenBroadway2001:ASpoofOdyssey(2001originaloffBroadwaycast))", 'artist': 'Gerard Alessandrini', 'album': 'Forbidden Broadway 2001: A Spoof Odyssey (2001 original off-Broadway cast)', 'year': '2901', 'length': '03:39', 'language': 'None'}], 'var_functions.list_db:5': ['sales'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:24': [{'cid': '0', 'name': 'sale_id', 'type': 'INTEGER', 'notnull': 'True', 'dflt_value': 'None', 'pk': 'True'}, {'cid': '1', 'name': 'track_id', 'type': 'INTEGER', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'country', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'store', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'units_sold', 'type': 'INTEGER', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'revenue_usd', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_functions.execute_python:26': {'title': 'None', 'artist': 'None', 'total_revenue_usd': 14647.52}, 'var_functions.query_db:28': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}, {'track_id': '6725', 'total_revenue': '2489.81'}, {'track_id': '10377', 'total_revenue': '2466.71'}]}

exec(code, env_args)
