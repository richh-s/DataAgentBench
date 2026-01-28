code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load all data
tracks_file_path = locals()['var_functions.query_db:5']
sales_file_path = locals()['var_functions.query_db:8']

with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)
with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)

tracks_df = pd.DataFrame(tracks_data)
sales_df = pd.DataFrame(sales_data)

# Clean and normalize data
tracks_df['track_id'] = tracks_df['track_id'].astype(str)
sales_df['track_id'] = sales_df['track_id'].astype(str)
sales_df['revenue_usd'] = pd.to_numeric(sales_df['revenue_usd'], errors='coerce')

# Normalize string fields for entity resolution
def normalize_string(s):
    if pd.isna(s) or s is None or s == 'None' or s == '[unknown]':
        return ''
    return str(s).strip().lower()

tracks_df['norm_title'] = tracks_df['title'].apply(normalize_string)
tracks_df['norm_artist'] = tracks_df['artist'].apply(normalize_string)
tracks_df['norm_album'] = tracks_df['album'].apply(normalize_string)
tracks_df['norm_year'] = tracks_df['year'].apply(normalize_string)

# Extract year digits
def extract_year(s):
    if not s:
        return ''
    year_match = re.search(r'\d{2,4}', s)
    if year_match:
        year = year_match.group()
        return year[-4:] if len(year) >= 4 else ('19' + year if year.startswith('0') or year.startswith('9') else '20' + year)
    return s

tracks_df['clean_year'] = tracks_df['norm_year'].apply(extract_year)

# Remove common noise words
def clean_title(s):
    patterns = [
        r'\s*-\s*(live|acoustic|demo|remix|album version|radio edit|explicit)',
        r'\s*\([^)]*\)$',  # Parentheses at end
        r'^\d{3}-',  # Number prefix
        r'^0+',  # Leading zeros
    ]
    result = s
    for pattern in patterns:
        result = re.sub(pattern, '', result)
    return result.strip()

tracks_df['base_title'] = tracks_df['norm_title'].apply(clean_title)

# Group tracks by key attributes (artist, base_title, album)
track_groups = defaultdict(list)
for _, row in tracks_df.iterrows():
    key = (row['norm_artist'], row['base_title'], row['norm_album'], row['clean_year'])
    track_groups[key].append(row['track_id'])

# Merge sales data for grouped tracks
merged_sales = []
for key, track_ids in track_groups.items():
    total_revenue = sales_df[sales_df['track_id'].isin(track_ids)]['revenue_usd'].sum()
    if total_revenue > 0:
        merged_sales.append({
            'artist': key[0],
            'title': key[1],
            'album': key[2],
            'year': key[3],
            'track_ids': track_ids,
            'revenue_usd': total_revenue,
            'track_count': len(track_ids)
        })

# Sort by revenue
merged_sales = sorted(merged_sales, key=lambda x: x['revenue_usd'], reverse=True)

top_10 = merged_sales[:10]

print("__RESULT__:")
print(json.dumps(top_10, default=str))"""

env_args = {'var_functions.list_db:0': ['tracks'], 'var_functions.list_db:2': ['sales'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}, {'sale_id': '4', 'track_id': '1', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '258', 'revenue_usd': '269.49'}, {'sale_id': '5', 'track_id': '2', 'country': 'Germany', 'store': 'Spotify', 'units_sold': '161', 'revenue_usd': '184.74'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'tracks_count': 19375, 'sales_count': 58049, 'sample_tracks': [{'track_id': '1', 'title': "Daniel Balavoine - L'enfant aux yeux d'Italie", 'artist': 'None', 'album': 'De vous à elle en passant par moi', 'year': '75'}, {'track_id': '2', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None'}, {'track_id': '3', 'title': 'Action PAINTING! - Mustard Gas', 'artist': 'None', 'album': 'There and Back Again Lane', 'year': '95'}], 'sample_sales': [{'sale_id': '1', 'track_id': '1', 'country': 'Canada', 'store': 'Google Play', 'units_sold': '349', 'revenue_usd': '408.0'}, {'sale_id': '2', 'track_id': '1', 'country': 'Canada', 'store': 'Apple Music', 'units_sold': '122', 'revenue_usd': '137.59'}, {'sale_id': '3', 'track_id': '1', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '373', 'revenue_usd': '371.57'}]}, 'var_functions.execute_python:14': {'top_revenue_tracks': [{'track_id': '3286', 'revenue_usd': '99.98285.25500.21446.99'}, {'track_id': '6756', 'revenue_usd': '99.98117.85419.33212.17428.32'}, {'track_id': '13552', 'revenue_usd': '99.96159.23'}, {'track_id': '4551', 'revenue_usd': '99.89208.7770.92'}, {'track_id': '15755', 'revenue_usd': '99.87208.83120.06393.9'}, {'track_id': '10022', 'revenue_usd': '99.85'}, {'track_id': '15502', 'revenue_usd': '99.84436.174.75476.44'}, {'track_id': '1373', 'revenue_usd': '99.84361.87362.77301.09552.87'}, {'track_id': '16249', 'revenue_usd': '99.83472.81322.78484.78'}, {'track_id': '10110', 'revenue_usd': '99.78199.13450.92123.15'}, {'track_id': '7300', 'revenue_usd': '99.76179.7'}, {'track_id': '10053', 'revenue_usd': '99.73118.18109.72384.47'}, {'track_id': '7929', 'revenue_usd': '99.69'}, {'track_id': '1331', 'revenue_usd': '99.63241.97384.56344.6860.48'}, {'track_id': '467', 'revenue_usd': '99.54342.43242.88402.78525.16'}, {'track_id': '3376', 'revenue_usd': '99.4827.24'}, {'track_id': '15652', 'revenue_usd': '99.47'}, {'track_id': '16972', 'revenue_usd': '99.45281.6132.5712.13'}, {'track_id': '16484', 'revenue_usd': '99.45190.62328.14316.45481.3'}, {'track_id': '8757', 'revenue_usd': '99.45148.2322.69507.17'}], 'top_tracks': [{'track_id': '467', 'title': 'St Louis Blues March (Swing Greats)', 'artist': 'Colin Busby Big Swing Band', 'album': 'Swing Greats', 'year': '1999'}, {'track_id': '1331', 'title': 'The Great and the Good - The Code Is Red... Long Live the Code', 'artist': 'Napalm Death', 'album': 'None', 'year': "'05"}, {'track_id': '1373', 'title': '006-Haste Suraj Ki', 'artist': 'Nadeem-Shravan', 'album': 'Dil Ka Rishta (2005)', 'year': 'None'}, {'track_id': '3286', 'title': 'Jungle Beat', 'artist': 'George Bruns', 'album': 'The Jungle Book', 'year': '1990'}, {'track_id': '3376', 'title': '1001 Doses (Até Você Voltar) (Taito Não Engole Fichas)', 'artist': 'Carbona', 'album': 'Taito Não Engole Fichas', 'year': '2003'}, {'track_id': '4551', 'title': 'Calling of Setnacht: Twofold Triunity (Thaumiel)', 'artist': 'Ofermod', 'album': 'Thaumiel', 'year': '2012'}, {'track_id': '6756', 'title': 'Stab (narrationn)', 'artist': 'Daniel C. Holter & Chris Weerts', 'album': 'Gearbox', 'year': 'None'}, {'track_id': '7300', 'title': 'The Lonesome One - The Trio: Live From Chicago', 'artist': 'Oscar Peterson Trio', 'album': 'None', 'year': "'97"}, {'track_id': '7929', 'title': 'Ham-dyt (Шаманское дерево) (Shizo I.D.)', 'artist': 'Gen-DOS', 'album': 'Shizo IZ.D.', 'year': '2006'}, {'track_id': '8757', 'title': 'Serena - Segnali di umana prseenza', 'artist': 'Nino Buonocore', 'album': 'None', 'year': "'13"}, {'track_id': '10022', 'title': 'One Shots: Snare: One Shots Snares 78-02 (Sony Sound Series: Loops & Samples: On the Jazz Tip)', 'artist': '[unknown]', 'album': 'Sony Sound Series: Loops & Samples: On the Jazz Tip', 'year': 'None'}, {'track_id': '10053', 'title': 'Csak a piknik (Gyere át!)', 'artist': 'Emil.RuleZ!', 'album': 'Gyere át!', 'year': '2012'}, {'track_id': '10110', 'title': 'Soul Corruption (Live! Alone in America)', 'artist': 'GrahamParker', 'album': 'Live! Alone in America', 'year': '1989'}, {'track_id': '13552', 'title': 'Think (Something to Believe In)', 'artist': 'Aretha Franklin', 'album': 'Something to Believe In', 'year': '2002'}, {'track_id': '15502', 'title': "Let's Start Over Again - Safari", 'artist': 'Flat DuoJets', 'album': 'None', 'year': "'93"}, {'track_id': '15652', 'title': 'Ensemble Gilles Binchois - Dominus vobiscum - oremus', 'artist': 'None', 'album': 'Le Manuscrit du Puy / / Les Premières Polyphonies Françaises', 'year': '01'}, {'track_id': '15755', 'title': 'Fire Horse (remix) - Просто любить', 'artist': 'Авраам Руссо', 'album': 'None', 'year': "'03"}, {'track_id': '16249', 'title': '0A4-House of the Rising Sun', 'artist': 'Joan Baez', 'album': 'Joan Baez (1970)', 'year': 'None'}, {'track_id': '16484', 'title': '006-One Step Closer', 'artist': 'Oceans Divide', 'album': 'Oceans Divide EP (2011)', 'year': 'None'}, {'track_id': '16972', 'title': 'Agent Caine - Medicine Man', 'artist': 'None', 'album': 'Chillout Fourever', 'year': '97'}]}, 'var_functions.execute_python:16': {'sales_dtypes': "{'sale_id': dtype('O'), 'track_id': dtype('O'), 'country': dtype('O'), 'store': dtype('O'), 'units_sold': dtype('O'), 'revenue_usd': dtype('O')}", 'revenue_sample': ['408.0', '137.59', '371.57', '269.49', '184.74'], 'revenue_type_sample': ['str', 'str', 'str', 'str', 'str']}, 'var_functions.execute_python:18': {'top_track_id': '14719', 'top_revenue': 2522.82, 'top_track': {'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, 'track_type': "<class 'str'>"}}

exec(code, env_args)
