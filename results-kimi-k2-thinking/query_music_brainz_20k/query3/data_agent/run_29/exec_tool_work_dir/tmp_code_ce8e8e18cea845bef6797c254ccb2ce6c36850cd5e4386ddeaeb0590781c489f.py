code = """import json

# Load sales data (already aggregated by track_id)
sales_results = locals().get('var_functions.query_db:12', '')
if isinstance(sales_results, str) and sales_results.endswith('.json'):
    with open(sales_results, 'r') as f:
        sales_data = json.load(f)
else:
    sales_data = sales_results

# Load tracks data
tracks_results = locals().get('var_functions.query_db:13', '')
if isinstance(tracks_results, str) and tracks_results.endswith('.json'):
    with open(tracks_results, 'r') as f:
        tracks_data = json.load(f)
else:
    tracks_data = tracks_results

# Create a dictionary mapping track_id to track info
tracks_dict = {track['track_id']: track for track in tracks_data}

# Get the top revenue track
top_revenue_track = sales_data[0]
top_track_id = top_revenue_track['track_id']
top_track_info = tracks_dict.get(top_track_id, {})

# Check for potential duplicates of the top track
top_title = top_track_info.get('title', '').lower()
top_artist = top_track_info.get('artist', '').lower()
top_album = top_track_info.get('album', '').lower()
top_year = top_track_info.get('year', '')

# Look for tracks that might be duplicates
candidates = []
for track in tracks_data:
    title = track.get('title', '').lower()
    artist = track.get('artist', '').lower()
    album = track.get('album', '').lower()
    year = track.get('year', '')
    
    # Check if this might be the same song
    if (top_title in title or title in top_title) and track['track_id'] != top_track_id:
        candidates.append(track)
    elif top_artist and top_artist != 'none' and top_artist in artist and track['track_id'] != top_track_id:
        candidates.append(track)

# Get revenue for candidates
candidate_revenues = []
for track in candidates:
    track_id = track['track_id']
    for sale in sales_data:
        if sale['track_id'] == track_id:
            candidate_revenues.append({
                'track_id': track_id,
                'title': track.get('title'),
                'artist': track.get('artist'),
                'revenue': float(sale['total_revenue'])
            })

result = {
    'top_track_id': top_track_id,
    'top_track_title': top_track_info.get('title'),
    'top_track_artist': top_track_info.get('artist'),
    'top_track_album': top_track_info.get('album'),
    'top_track_year': top_track_info.get('year'),
    'top_revenue': float(top_revenue_track['total_revenue']),
    'candidate_duplicates': candidate_revenues[:10],  # Show first 10
    'candidate_count': len(candidate_revenues)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:1': ['sales'], 'var_functions.query_db:4': [{'track_id': '1', 'source_id': '2', 'source_track_id': 'MBox7368722-HH', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75', 'length': '219', 'language': 'French'}, {'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '3', 'source_id': '2', 'source_track_id': 'MBox38440522-HH', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95', 'length': '129', 'language': 'English'}, {'track_id': '4', 'source_id': '5', 'source_track_id': '4489993', 'title': 'Your Grace', 'artist': 'Kathy Troccoli', 'album': 'Comfort', 'year': '2005', 'length': 'unk.', 'language': 'English'}, {'track_id': '5', 'source_id': '5', 'source_track_id': '10339621', 'title': "Well You Needn't", 'artist': 'Ernie Stadler Jazz Quintet', 'album': 'First Down', 'year': '2010', 'length': '321266', 'language': 'English'}, {'track_id': '6', 'source_id': '3', 'source_track_id': '49425110MB-01', 'title': 'Try (acoustic) - 2008-02-15: Le Grand Rex, Paris, France', 'artist': 'Neil Young', 'album': 'None', 'year': 'None', 'length': 'None', 'language': 'English'}, {'track_id': '7', 'source_id': '2', 'source_track_id': 'MBox28675636-HH', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05', 'length': '177', 'language': 'English'}, {'track_id': '8', 'source_id': '2', 'source_track_id': 'MBox9589118-HH', 'title': 'Luce Dufault - Ballade à donner', 'artist': 'None', 'album': 'Luce Dufault', 'year': '96', 'length': '242', 'language': 'French'}, {'track_id': '9', 'source_id': '5', 'source_track_id': '10992441', 'title': "Just Like Tom Thumb's Blues (live)", 'artist': 'Wendy Saddington', 'album': 'Blues Women Anthology, Volume 7', 'year': '2007', 'length': '462000', 'language': 'English'}, {'track_id': '10', 'source_id': '5', 'source_track_id': '15761001', 'title': 'Στα καμένα', 'artist': 'Λαυρέντης Μαχαιρίίτσας', 'album': 'Συλλογή Δίφωνο, 22: Μουσικοί βιότοποι', 'year': '1997', 'length': '195000', 'language': 'Greek'}], 'var_functions.query_db:5': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}, {'sale_id': '6', 'track_id': '2', 'country': 'USA', 'store': 'iTunes', 'units_sold': '236', 'revenue_usd': '270.79'}, {'sale_id': '7', 'track_id': '2', 'country': 'Germany', 'store': 'Amazon Music', 'units_sold': '170', 'revenue_usd': '186.98'}, {'sale_id': '8', 'track_id': '2', 'country': 'Canada', 'store': 'Amazon Music', 'units_sold': '190', 'revenue_usd': '217.41'}, {'sale_id': '9', 'track_id': '2', 'country': 'USA', 'store': 'Apple Music', 'units_sold': '320', 'revenue_usd': '399.35'}, {'sale_id': '10', 'track_id': '3', 'country': 'UK', 'store': 'Amazon Music', 'units_sold': '329', 'revenue_usd': '418.71'}], 'var_functions.query_db:10': [{'total_sales': '58049'}], 'var_functions.query_db:11': [{'total_tracks': '19375'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.execute_python:16': {'sales_count': 19375, 'tracks_count': 19375, 'top_revenue_track': {'track_id': '14719', 'total_revenue': '2522.82'}}, 'var_functions.query_db:19': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:20': [{'track_id': '7962', 'title': 'Chalk Circle - Scrambled', 'artist': 'None', 'album': 'Reflection', 'year': '11'}, {'track_id': '12395', 'title': 'The Devil Made Me Do That - Bridge Over Troubled Water', 'artist': 'Buck Owens and His Buckaroos', 'album': 'None', 'year': "'04"}, {'track_id': '13311', 'title': 'The Devil Made Me Do That (Bridge Over T roubled Water)', 'artist': 'Buck Owens and His Buckaroos', 'album': 'Bridge Over Troubled Water', 'year': '2004'}, {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, {'track_id': '14984', 'title': 'Scrambled - Reflection', 'artist': 'Circle', 'album': 'None', 'year': "'11"}, {'track_id': '15065', 'title': 'The Hope Conspiracy - Bled Across the Wire', 'artist': 'None', 'album': 'Cold Blue', 'year': '00'}, {'track_id': '16131', 'title': 'Salena Jones - Bridge Over Troubled Water', 'artist': 'None', 'album': 'Ballad with Luv', 'year': '10'}, {'track_id': '17003', 'title': 'Bridge Over Troubled Water - Ballad with Luv', 'artist': 'Salena Jon es', 'album': 'None', 'year': "'10"}], 'var_functions.query_db:22': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:24': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}], 'var_functions.query_db:25': [{'track_id': '7962', 'title': 'Chalk Circle - Scrambled', 'artist': 'None', 'album': 'Reflection', 'year': '11'}, {'track_id': '12395', 'title': 'The Devil Made Me Do That - Bridge Over Troubled Water', 'artist': 'Buck Owens and His Buckaroos', 'album': 'None', 'year': "'04"}, {'track_id': '13311', 'title': 'The Devil Made Me Do That (Bridge Over T roubled Water)', 'artist': 'Buck Owens and His Buckaroos', 'album': 'Bridge Over Troubled Water', 'year': '2004'}, {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, {'track_id': '14984', 'title': 'Scrambled - Reflection', 'artist': 'Circle', 'album': 'None', 'year': "'11"}, {'track_id': '15065', 'title': 'The Hope Conspiracy - Bled Across the Wire', 'artist': 'None', 'album': 'Cold Blue', 'year': '00'}, {'track_id': '16131', 'title': 'Salena Jones - Bridge Over Troubled Water', 'artist': 'None', 'album': 'Ballad with Luv', 'year': '10'}, {'track_id': '17003', 'title': 'Bridge Over Troubled Water - Ballad with Luv', 'artist': 'Salena Jon es', 'album': 'None', 'year': "'10"}], 'var_functions.execute_python:28': {'message': 'Data loaded successfully', 'sales_count': 19375, 'tracks_count': 19375, 'sample_sales': [{'track_id': '14719', 'total_revenue': '2522.82'}, {'track_id': '5124', 'total_revenue': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue': '2500.72'}], 'sample_tracks': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}]}}

exec(code, env_args)
