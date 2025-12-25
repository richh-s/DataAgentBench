code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-9337511221425881705'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6125831079873594295'], 'r') as f:
    tracks_data = json.load(f)

sales_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

sales_df['revenue_usd'] = pd.to_numeric(sales_df['total_revenue'], errors='coerce').fillna(0.0)
sales_df['track_id'] = sales_df['track_id'].astype(str)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

merged_df = pd.merge(sales_df, tracks_df, on='track_id', how='left')

def clean_str(s):
    if not isinstance(s, str):
        return ""
    s = s.lower()
    # Remove track numbers like "001-", "01 ", "01-"
    # Pattern: start of string, 2 or 3 digits, followed by separator
    s = re.sub(r'^\d{2,3}[-\s]+', '', s)
    # Remove things in brackets/parentheses
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'\[.*?\]', '', s)
    # Remove punctuation
    s = re.sub(r'[^\w\s]', '', s)
    # Remove extra spaces
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def resolve_artist_title(row):
    title = str(row['title'])
    artist = str(row['artist'])
    
    # Check for None strings
    if title.lower() in ['none', 'unknown', '']:
        title = ""
    if artist.lower() in ['none', 'unknown', '[unknown]', '']:
        artist = ""
    
    # If artist is empty, check if title contains " - "
    if artist == "" and " - " in title:
        parts = title.split(" - ", 1)
        if len(parts) == 2:
            artist = parts[0].strip()
            title = parts[1].strip()

    clean_t = clean_str(title)
    clean_a = clean_str(artist)
    
    if clean_a.startswith("the "):
        clean_a = clean_a[4:]
        
    return pd.Series([clean_t, clean_a])

merged_df[['clean_title', 'clean_artist']] = merged_df.apply(resolve_artist_title, axis=1)

# Remove entries with empty title
merged_df = merged_df[merged_df['clean_title'] != ""]

# Create grouping keys
# Remove spaces for comparison? "endlesslove"
merged_df['key_title'] = merged_df['clean_title'].str.replace(' ', '')
merged_df['key_artist'] = merged_df['clean_artist'].str.replace(' ', '')

grouped = merged_df.groupby(['key_title', 'key_artist'])['revenue_usd'].sum().reset_index()
top_songs = grouped.sort_values('revenue_usd', ascending=False).head(10)

# Get details
result_list = []
for idx, row in top_songs.iterrows():
    # Find a representative
    mask = (merged_df['key_title'] == row['key_title']) & (merged_df['key_artist'] == row['key_artist'])
    rep = merged_df[mask].iloc[0]
    result_list.append({
        "rank": idx,
        "key_title": row['key_title'],
        "key_artist": row['key_artist'],
        "revenue": row['revenue_usd'],
        "example_title": rep['title'],
        "example_artist": rep['artist']
    })

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-9337511221425881705': 'file_storage/function-call-9337511221425881705.json', 'var_function-call-6125831079873594295': 'file_storage/function-call-6125831079873594295.json', 'var_function-call-18017158687461219526': {'clean_title': 'none', 'clean_artist': '', 'original_title': 'None', 'original_artist': 'None', 'total_revenue': 14647.52, 'top_5': [{'key_title': 'none', 'key_artist': '', 'revenue_usd': 14647.52}, {'key_title': '003', 'key_artist': '', 'revenue_usd': 8582.15}, {'key_title': '001', 'key_artist': '', 'revenue_usd': 7467.97}, {'key_title': '004', 'key_artist': '', 'revenue_usd': 7271.32}, {'key_title': '005', 'key_artist': '', 'revenue_usd': 6155.29}, {'key_title': 'groovey', 'key_artist': 'richmatteson', 'revenue_usd': 5417.34}, {'key_title': 'zogaathetlevenaanjevoor', 'key_artist': 'sybvanderploeg', 'revenue_usd': 5256.43}, {'key_title': '009', 'key_artist': '', 'revenue_usd': 5045.7}, {'key_title': '002', 'key_artist': '', 'revenue_usd': 5013.4400000000005}, {'key_title': 'vagga', 'key_artist': 'ske', 'revenue_usd': 4981.380000000001}]}, 'var_function-call-1009324656712476888': [{'track_id': '2', 'source_id': '4', 'source_track_id': '139137-A047', 'title': '007', 'artist': '[unknown]', 'album': 'Cantigas de roda (unknown)', 'year': 'None', 'length': '1m 58sec', 'language': 'Por.'}, {'track_id': '13', 'source_id': '4', 'source_track_id': '182555-A056', 'title': '002-Particle/Wave', 'artist': 'Lunchbox', 'album': 'Evolver (2002)', 'year': 'None', 'length': '6m 21sec', 'language': 'Eng.'}, {'track_id': '14', 'source_id': '4', 'source_track_id': '51445-A041', 'title': '001-Deja Vu', 'artist': 'Blanket', 'album': 'Nice (2000)', 'year': 'None', 'length': '3m 36sec', 'language': 'ng.'}, {'track_id': '18', 'source_id': '4', 'source_track_id': '131573-A04', 'title': '00-1', 'artist': 'None', 'album': ' (2010)', 'year': 'None', 'length': '3m 52sec', 'language': 'Jap.'}, {'track_id': '41', 'source_id': '4', 'source_track_id': '222683-A055', 'title': "007-A Tout A L'Heure", 'artist': 'Bibio', 'album': 'Ministry of Sound: Chillout Sessions XVI (2013)', 'year': 'None', 'length': '4m 0sec', 'language': 'Eng.'}, {'track_id': '80', 'source_id': '4', 'source_track_id': '61084-A067', 'title': "005-Candy / All I Do Is Dream of You / Spring Is Here / 720 in the Books / It Happened in Monterey / What Can I Say After I Say I'm Sorry", 'artist': 'Ella Fitzgerald', 'album': '30 by Ella (1999)', 'year': 'None', 'length': '6m 42sec', 'language': 'Eng.'}, {'track_id': '84', 'source_id': '4', 'source_track_id': '97860-A037', 'title': '001-Berimbou', 'artist': 'Astrud Gilberto', 'album': 'Look to the Rainbow (2008)', 'year': 'None', 'length': '2m 23sec', 'language': ' Eng.'}, {'track_id': '88', 'source_id': '4', 'source_track_id': '18751-A065', 'title': '005-Al verte las flores lloran', 'artist': 'Camaron de la Isla', 'album': 'Una leyenda flamenca (1992)', 'year': 'None', 'length': '2m 42sec', 'language': 'Spa.'}, {'track_id': '89', 'source_id': '4', 'source_track_id': '122115-A032', 'title': '006-My Pretty Pecker', 'artist': 'Dr. Dre Del', 'album': "Dr Dre Del's Mic of Defiance (1999)", 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}, {'track_id': '91', 'source_id': '4', 'source_track_id': '21846-A018', 'title': '006-Murder & Mayhem', 'artist': 'Noelle Hampton', 'album': 'Under  These Skies (unknown)', 'year': 'None', 'length': '6m 26sec', 'language': 'E.'}, {'track_id': '93', 'source_id': '4', 'source_track_id': '34732-A08', 'title': '005-Put Me Back Together', 'artist': 'Drive Like You Stole It', 'album': 'Frequency (unknown)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}, {'track_id': '102', 'source_id': '4', 'source_track_id': 'None', 'title': '005-Piranhes', 'artist': 'Rattler', 'album': 'Demo 2012 (unknown)', 'year': 'None', 'length': '5m 12sec', 'language': 'Eng.'}, {'track_id': '107', 'source_id': '4', 'source_track_id': '79094-A031', 'title': '003-Jayne', 'artist': 'Stereophonics', 'album': 'The Sunday Times: The State of Independence - V2 (2007)', 'year': 'None', 'length': '3m 37sec', 'language': 'Eng.'}, {'track_id': '110', 'source_id': '4', 'source_track_id': '17735-A045', 'title': '001-Nation of Sorrow', 'artist': 'Battle Zone', 'album': 'Arson Around With Matches (unknown)', 'year': 'None', 'length': 'unknown', 'language': 'Eng.'}, {'track_id': '114', 'source_id': '4', 'source_track_id': '140342-A048', 'title': '007-When Love Comes to Town', 'artist': 'U2 & B.B. King', 'album': '1987-11-24: Tarrant County Convention Center, Fort Worth, TX, USA (unknown)', 'year': 'None', 'length': 'unknown', 'language': 'Enkg.'}, {'track_id': '120', 'source_id': '4', 'source_track_id': '95960-A037', 'title': '001-Stronger Woman', 'artist': 'Jewel', 'album': 'Perfectly Clear (2008)', 'year': 'None', 'length': '4m 2sec', 'language': 'Eng.'}, {'track_id': '121', 'source_id': '4', 'source_track_id': '179846-A029', 'title': '006-Turning', 'artist': 'Glass America', 'album': 'Fathom (unknown)', 'year': 'None', 'length': '3m 21sec', 'language': 'Eng.'}, {'track_id': '134', 'source_id': '4', 'source_track_id': '197258-A00', 'title': '006-The Jailer', 'artist': 'Erin McKeown', 'album': 'Paste mPlayer #77 (2013)', 'year': 'None', 'length': '2m 49sec', 'language': 'Eng.'}, {'track_id': '137', 'source_id': '4', 'source_track_id': '151449-A063', 'title': '001-Sunlight', 'artist': 'The One AM Radio', 'album': 'Heaven Is Attached by a Slender Thhread (2011)', 'year': 'None', 'length': '3m 40sec', 'language': 'Eng.'}, {'track_id': '138', 'source_id': '4', 'source_track_id': '101777-A055', 'title': '005-Where the Wild Things Are', 'artist': 'Chenard Walcker', 'album': 'Middle (2004)', 'year': 'None', 'length': '2m 42sec', 'language': 'Eng.'}]}

exec(code, env_args)
