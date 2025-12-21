code = """import json
import pandas as pd
import re

sales_file_path = locals()['var_function-call-17703763520691558553']
tracks_file_path = locals()['var_function-call-17703763520691559746']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

def normalize_text(s):
    if not isinstance(s, str):
        return ""
    s = s.lower().strip()
    s = re.sub(r'[^\w\s]', '', s) 
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def extract_artist_title(row):
    title = row.get('title')
    artist = row.get('artist')
    if title is None: title = ""
    if artist is None: artist = ""
    if title == "None": title = ""
    if artist == "None": artist = ""
    
    if not artist or artist.lower() in ['[unknown]', 'unk', 'various artists']:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist_cand = parts[0]
            title_cand = parts[1]
            return artist_cand, title_cand
    return artist, title

cleaned_data = []
for _, row in df_tracks.iterrows():
    raw_artist, raw_title = extract_artist_title(row)
    norm_artist = normalize_text(raw_artist)
    norm_title = normalize_text(raw_title)
    
    if not norm_artist and not norm_title:
        merge_key = f"UNKNOWN_{row['track_id']}"
    else:
        merge_key = f"{norm_artist}|{norm_title}"
    
    cleaned_data.append({
        'track_id': row['track_id'],
        'original_title': row['title'],
        'original_artist': row['artist'],
        'norm_artist': norm_artist,
        'norm_title': norm_title,
        'merge_key': merge_key
    })

df_clean = pd.DataFrame(cleaned_data)
df_merged = pd.merge(df_clean, df_sales, on='track_id', how='inner')

# Group
df_grouped = df_merged.groupby('merge_key').agg({
    'revenue_usd': 'sum',
    'original_title': 'first', 
    'original_artist': 'first',
    'norm_artist': 'first',
    'norm_title': 'first'
}).reset_index()

# Sort
df_sorted = df_grouped.sort_values('revenue_usd', ascending=False)

# Filter out empty artists
df_filtered = df_sorted[df_sorted['norm_artist'] != ""]

top_songs = df_filtered.head(10).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_songs))"""

env_args = {'var_function-call-17703763520691558553': 'file_storage/function-call-17703763520691558553.json', 'var_function-call-17703763520691559746': 'file_storage/function-call-17703763520691559746.json', 'var_function-call-17375738143367374828': [{'merge_key': '|', 'revenue_usd': 206433.9, 'original_title': 'Στα καμένα', 'original_artist': 'Λαυρέντης Μαχαιρίίτσας'}, {'merge_key': '|none', 'revenue_usd': 17150.55, 'original_title': 'None', 'original_artist': '幡谷尚史'}, {'merge_key': '|004', 'revenue_usd': 7271.32, 'original_title': '004-/', 'original_artist': 'None'}, {'merge_key': '|003', 'revenue_usd': 7090.13, 'original_title': '003-', 'original_artist': 'None'}, {'merge_key': '|001', 'revenue_usd': 6283.24, 'original_title': '00-1', 'original_artist': 'None'}, {'merge_key': '|005', 'revenue_usd': 6155.29, 'original_title': '005', 'original_artist': 'None'}, {'merge_key': 'richmatteson|groovey', 'revenue_usd': 5417.34, 'original_title': 'Rich Matteson - Groovey', 'original_artist': 'None'}, {'merge_key': '|009', 'revenue_usd': 5045.7, 'original_title': '009-  ', 'original_artist': ' '}, {'merge_key': '|002', 'revenue_usd': 5013.4400000000005, 'original_title': '002-', 'original_artist': 'None'}, {'merge_key': '|010', 'revenue_usd': 4734.360000000001, 'original_title': '010-', 'original_artist': 'None'}], 'var_function-call-18226785664855278143': [{'merge_key': '|004', 'revenue_usd': 7271.32, 'original_title': '004-/', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '004'}, {'merge_key': '|003', 'revenue_usd': 7090.13, 'original_title': '003-', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '003'}, {'merge_key': '|005', 'revenue_usd': 6155.29, 'original_title': '005', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '005'}, {'merge_key': 'rich matteson|groovey', 'revenue_usd': 5417.34, 'original_title': 'Rich Matteson - Groovey', 'original_artist': 'None', 'norm_artist': 'rich matteson', 'norm_title': 'groovey'}, {'merge_key': '|009', 'revenue_usd': 5045.7, 'original_title': '009-  ', 'original_artist': ' ', 'norm_artist': '', 'norm_title': '009'}, {'merge_key': '|002', 'revenue_usd': 5013.4400000000005, 'original_title': '002-', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '002'}, {'merge_key': '|010', 'revenue_usd': 4734.360000000001, 'original_title': '010-', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '010'}, {'merge_key': '|001', 'revenue_usd': 4681.75, 'original_title': '00-1', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '001'}, {'merge_key': '|012', 'revenue_usd': 4641.08, 'original_title': '012-', 'original_artist': 'None', 'norm_artist': '', 'norm_title': '012'}, {'merge_key': 'syb van der ploeg|zo gaat het leven aan je voor hillich fjoer heilig vuur', 'revenue_usd': 4132.27, 'original_title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'original_artist': 'Syb van der Ploeg', 'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor hillich fjoer heilig vuur'}], 'var_function-call-17561599202807340368': [{'track_id': '14719', 'total_revenue': '2522.82', 'revenue_usd': 2522.82}, {'track_id': '5124', 'total_revenue': '2503.1899999999996', 'revenue_usd': 2503.19}, {'track_id': '1344', 'total_revenue': '2500.72', 'revenue_usd': 2500.72}, {'track_id': '6725', 'total_revenue': '2489.81', 'revenue_usd': 2489.81}, {'track_id': '10377', 'total_revenue': '2466.71', 'revenue_usd': 2466.71}, {'track_id': '5050', 'total_revenue': '2466.3100000000004', 'revenue_usd': 2466.3100000000004}, {'track_id': '6667', 'total_revenue': '2452.7000000000003', 'revenue_usd': 2452.7000000000003}, {'track_id': '7245', 'total_revenue': '2436.9700000000003', 'revenue_usd': 2436.9700000000003}, {'track_id': '11641', 'total_revenue': '2428.2200000000003', 'revenue_usd': 2428.2200000000003}, {'track_id': '964', 'total_revenue': '2425.61', 'revenue_usd': 2425.61}], 'var_function-call-13577778132664272131': {'|004': {'revenue': 7271.32, 'titles': ['004-/', '004-"" (, , , )', '004- ', '004-'], 'artists': ['None', ' ', '    ""'], 'track_count': 8}, '|003': {'revenue': 7090.129999999999, 'titles': ['003-', '003-,  ', '003- '], 'artists': ['None', ' '], 'track_count': 7}, '|005': {'revenue': 6155.29, 'titles': ['005', '005-', '005- ', '005-    '], 'artists': ['None', ' '], 'track_count': 8}, 'rich matteson|groovey': {'revenue': 5417.34, 'titles': ['Rich Matteson - Groovey', 'Groovey'], 'artists': ['None', 'Rich Matteson'], 'track_count': 4}, '|009': {'revenue': 5045.7, 'titles': ['009-  ', '009-   ', '009-', '009- '], 'artists': [' ', 'None'], 'track_count': 4}}}

exec(code, env_args)
