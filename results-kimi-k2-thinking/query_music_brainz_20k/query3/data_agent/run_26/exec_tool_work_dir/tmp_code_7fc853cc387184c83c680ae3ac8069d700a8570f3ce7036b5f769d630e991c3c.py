code = """import json
import pandas as pd
import re

# Load all data
tracks_file_path = locals()['var_functions.query_db:5']
sales_file_path = locals()['var_functions.query_db:8']

with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Properly convert data types
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')

# Calculate revenue per track_id (no entity resolution yet)
track_revenue = sales_df.groupby('track_id')['revenue_usd'].sum().reset_index()
track_revenue = track_revenue.sort_values('revenue_usd', ascending=False)

# Get top 50 tracks by revenue
top_50_tracks = track_revenue.head(50).to_dict('records')
top_50_ids = [t['track_id'] for t in top_50_tracks]

# Get track info for top 50
top_tracks_info = tracks_df[tracks_df['track_id'].isin(top_50_ids)].copy()

# Normalize metadata for entity resolution
def normalize_string(s):
    if pd.isna(s) or s is None or str(s) == 'None' or str(s) == '[unknown]' or str(s).strip() == '':
        return ''
    return str(s).strip().lower()

def clean_title(s):
    if pd.isna(s) or not s:
        return ''
    s = str(s)
    # Remove prefixes like numbers, codes
    s = re.sub(r'^\d{3,4}-\s*', '', s)
    s = re.sub(r'^0+', '', s)
    # Remove suffixes in parentheses/brackets at end
    s = re.sub(r'\s*\([^)]*\)$', '', s)
    s = re.sub(r'\s*-\s*(live|acoustic|demo|remix|radio edit|album version|feat[^)]*)\s*$', '', s)
    return s.strip().lower()

def extract_year(s):
    if pd.isna(s) or not s:
        return ''
    s = str(s)
    # Extract 4-digit year
    match = re.search(r'\d{4}', s)
    if match:
        return match.group()
    # Handle 2-digit years
    match = re.search(r'\d{2}', s)
    if match:
        year = match.group()
        if year.startswith(('0', '1', '2', '3')):
            return '20' + year
        else:
            return '19' + year
    return ''

top_tracks_info['norm_artist'] = top_tracks_info['artist'].apply(normalize_string)
top_tracks_info['base_title'] = top_tracks_info['title'].apply(clean_title)
top_tracks_info['norm_album'] = top_tracks_info['album'].apply(normalize_string)
top_tracks_info['clean_year'] = top_tracks_info['year'].apply(extract_year)

# Create entity groups from top tracks
entity_groups = {}
used_track_ids = set()

for i, track1 in top_tracks_info.iterrows():
    if track1['track_id'] in used_track_ids:
        continue
    
    group_key = (track1['norm_artist'], track1['base_title'], track1['norm_album'], track1['clean_year'])
    
    # Skip empty groups
    if group_key == ('', '', '', ''):
        used_track_ids.add(track1['track_id'])
        entity_groups[track1['track_id']] = {
            'track_ids': [track1['track_id']],
            'revenue': 0
        }
        continue
    
    # Find matching tracks
    matching_ids = [track1['track_id']]
    
    for j, track2 in top_tracks_info.iterrows():
        if i == j or track2['track_id'] in used_track_ids:
            continue
            
        # Check if same entity (loose matching)
        same_artist = track1['norm_artist'] and track2['norm_artist'] and track1['norm_artist'] == track2['norm_artist']
        same_title = track1['base_title'] and track2['base_title'] and track1['base_title'] == track2['base_title']
        same_album = track1['norm_album'] and track2['norm_album'] and track1['norm_album'] == track2['norm_album']
        
        # If artist and title match, it's likely the same track
        if same_artist and same_title:
            matching_ids.append(track2['track_id'])
            used_track_ids.add(track2['track_id'])
    
    used_track_ids.add(track1['track_id'])
    
    # Calculate total revenue for the group
    total_revenue = sales_df[sales_df['track_id'].isin(matching_ids)]['revenue_usd'].sum()
    
    entity_groups[track1['track_id']] = {
        'track_ids': matching_ids,
        'artist': track1['artist'],
        'title': track1['title'],
        'album': track1['album'],
        'year': track1['year'],
        'revenue': total_revenue
    }

# Sort by revenue
sorted_entities = sorted(entity_groups.values(), key=lambda x: x['revenue'], reverse=True)

print("__RESULT__:") 
print(json.dumps(sorted_entities[:10], default=str))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'tracks_count': 19375, 'sales_count': 58049, 'sample_tracks': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}]}, 'var_functions.execute_python:14': {'top_revenue_tracks': [{'track_id': '3286', 'revenue_usd': '99.98285.25500.21446.99'}, {'track_id': '6756', 'revenue_usd': '99.98117.85419.33212.17428.32'}, {'track_id': '13552', 'revenue_usd': '99.96159.23'}, {'track_id': '4551', 'revenue_usd': '99.89208.7770.92'}, {'track_id': '15755', 'revenue_usd': '99.87208.83120.06393.9'}, {'track_id': '10022', 'revenue_usd': '99.85'}, {'track_id': '15502', 'revenue_usd': '99.84436.174.75476.44'}, {'track_id': '1373', 'revenue_usd': '99.84361.87362.77301.09552.87'}, {'track_id': '16249', 'revenue_usd': '99.83472.81322.78484.78'}, {'track_id': '10110', 'revenue_usd': '99.78199.13450.92123.15'}, {'track_id': '7300', 'revenue_usd': '99.76179.7'}, {'track_id': '10053', 'revenue_usd': '99.73118.18109.72384.47'}, {'track_id': '7929', 'revenue_usd': '99.69'}, {'track_id': '1331', 'revenue_usd': '99.63241.97384.56344.6860.48'}, {'track_id': '467', 'revenue_usd': '99.54342.43242.88402.78525.16'}, {'track_id': '3376', 'revenue_usd': '99.4827.24'}, {'track_id': '15652', 'revenue_usd': '99.47'}, {'track_id': '16972', 'revenue_usd': '99.45281.6132.5712.13'}, {'track_id': '16484', 'revenue_usd': '99.45190.62328.14316.45481.3'}, {'track_id': '8757', 'revenue_usd': '99.45148.2322.69507.17'}], 'top_tracks': [{'track_id': '467', 'title': 'St Louis Blues March (Swing Greats)', 'artist': 'Colin Busby Big Swing Band', 'album': 'Swing Greats', 'year': '1999'}, {'track_id': '1331', 'title': 'The Great and the Good - The Code Is Red... Long Live the Code', 'artist': 'Napalm Death', 'album': 'None', 'year': "'05"}, {'track_id': '1373', 'title': '006-Haste Suraj Ki', 'artist': 'Nadeem-Shravan', 'album': 'Dil Ka Rishta (2005)', 'year': 'None'}, {'track_id': '3286', 'title': 'Jungle Beat', 'artist': 'George Bruns', 'album': 'The Jungle Book', 'year': '1990'}, {'track_id': '3376', 'title': '1001 Doses (Até Você Voltar) (Taito Não Engole Fichas)', 'artist': 'Carbona', 'album': 'Taito Não Engole Fichas', 'year': '2003'}, {'track_id': '4551', 'title': 'Calling of Setnacht: Twofold Triunity (Thaumiel)', 'artist': 'Ofermod', 'album': 'Thaumiel', 'year': '2012'}, {'track_id': '6756', 'title': 'Stab (narrationn)', 'artist': 'Daniel C. Holter & Chris Weerts', 'album': 'Gearbox', 'year': 'None'}, {'track_id': '7300', 'title': 'The Lonesome One - The Trio: Live From Chicago', 'artist': 'Oscar Peterson Trio', 'album': 'None', 'year': "'97"}, {'track_id': '7929', 'title': 'Ham-dyt (Шаманское дерево) (Shizo I.D.)', 'artist': 'Gen-DOS', 'album': 'Shizo IZ.D.', 'year': '2006'}, {'track_id': '8757', 'title': 'Serena - Segnali di umana prseenza', 'artist': 'Nino Buonocore', 'album': 'None', 'year': "'13"}, {'track_id': '10022', 'title': 'One Shots: Snare: One Shots Snares 78-02 (Sony Sound Series: Loops & Samples: On the Jazz Tip)', 'artist': '[unknown]', 'album': 'Sony Sound Series: Loops & Samples: On the Jazz Tip', 'year': 'None'}, {'track_id': '10053', 'title': 'Csak a piknik (Gyere át!)', 'artist': 'Emil.RuleZ!', 'album': 'Gyere át!', 'year': '2012'}, {'track_id': '10110', 'title': 'Soul Corruption (Live! Alone in America)', 'artist': 'GrahamParker', 'album': 'Live! Alone in America', 'year': '1989'}, {'track_id': '13552', 'title': 'Think (Something to Believe In)', 'artist': 'Aretha Franklin', 'album': 'Something to Believe In', 'year': '2002'}, {'track_id': '15502', 'title': "Let's Start Over Again - Safari", 'artist': 'Flat DuoJets', 'album': 'None', 'year': "'93"}, {'track_id': '15652', 'title': 'Ensemble Gilles Binchois - Dominus vobiscum - oremus', 'artist': 'None', 'album': 'Le Manuscrit du Puy / / Les Premières Polyphonies Françaises', 'year': '01'}, {'track_id': '15755', 'title': 'Fire Horse (remix) - Просто любить', 'artist': 'Авраам Руссо', 'album': 'None', 'year': "'03"}, {'track_id': '16249', 'title': '0A4-House of the Rising Sun', 'artist': 'Joan Baez', 'album': 'Joan Baez (1970)', 'year': 'None'}, {'track_id': '16484', 'title': '006-One Step Closer', 'artist': 'Oceans Divide', 'album': 'Oceans Divide EP (2011)', 'year': 'None'}, {'track_id': '16972', 'title': 'Agent Caine - Medicine Man', 'artist': 'None', 'album': 'Chillout Fourever', 'year': '97'}]}, 'var_functions.execute_python:16': {'sales_dtypes': "{'sale_id': dtype('O'), 'track_id': dtype('O'), 'country': dtype('O'), 'store': dtype('O'), 'units_sold': dtype('O'), 'revenue_usd': dtype('O')}", 'revenue_sample': ['408.0', '137.59', '371.57', '269.49', '184.74'], 'revenue_type_sample': ['str', 'str', 'str', 'str', 'str']}, 'var_functions.execute_python:18': {'top_track_id': '14719', 'top_revenue': 2522.82, 'top_track': {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, 'track_type': "<class 'str'>"}, 'var_functions.execute_python:20': [{'artist': '', 'title': '', 'album': '(2002)', 'year': '', 'track_ids': ['10208', '12562', '19081'], 'revenue_usd': 4290.95, 'track_count': 3}, {'artist': 'hellsongs', 'title': '[introduction]', 'album': '2010-08-23: nachtmix, bayerischer rundfunk, munich, germany', 'year': '2010', 'track_ids': ['974', '7647', '8488'], 'revenue_usd': 4180.26, 'track_count': 3}, {'artist': '', 'title': '', 'album': '(unknown)', 'year': '', 'track_ids': ['1355', '5644', '17188', '17584', '18731'], 'revenue_usd': 4151.38, 'track_count': 5}, {'artist': 'russ ballard', 'title': 'the fire still burns', 'album': 'the fire still burns', 'year': '', 'track_ids': ['1154', '12644'], 'revenue_usd': 3807.4000000000005, 'track_count': 2}, {'artist': 'syb van der ploeg', 'title': 'zo gaat het leven aan je voor', 'album': 'hillich fjoer | heilig vuur', 'year': '2008', 'track_ids': ['3024', '3435'], 'revenue_usd': 3779.05, 'track_count': 2}, {'artist': '', 'title': '', 'album': '(1996)', 'year': '', 'track_ids': ['11703', '14373'], 'revenue_usd': 3619.73, 'track_count': 2}, {'artist': 'swervedriver', 'title': 'for seeking heat', 'album': 'mezcal head', 'year': '2008', 'track_ids': ['4366', '8854'], 'revenue_usd': 3495.75, 'track_count': 2}, {'artist': 'skabucks', 'title': "don't fucking care", 'album': "superhero's finest", 'year': '', 'track_ids': ['6301', '18586'], 'revenue_usd': 3487.6900000000005, 'track_count': 2}, {'artist': 'earl zinger', 'title': 'intro', 'album': 'put your phazers on stun throw your health food skyward', 'year': '2002', 'track_ids': ['6516', '9801'], 'revenue_usd': 3399.37, 'track_count': 2}, {'artist': '服部隆之', 'title': 'lifework', 'album': 'hero -original sound track', 'year': '', 'track_ids': ['6830', '11162'], 'revenue_usd': 3391.42, 'track_count': 2}]}

exec(code, env_args)
