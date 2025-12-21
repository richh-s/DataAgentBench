code = """import json
import pandas as pd
import re

# Load sales data
with open(locals()['var_function-call-13586711412280274277'], 'r') as f:
    sales_data = json.load(f)
df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Load tracks data
with open(locals()['var_function-call-15404616828467795232'], 'r') as f:
    tracks_data = json.load(f)
df_tracks = pd.DataFrame(tracks_data)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_row(row):
    title = str(row['title'])
    artist = str(row['artist'])
    
    # Normalize nulls
    if artist in ['None', 'nan', '[unknown]', '']:
        artist = None
        
    # 1. Handle "Artist - Title" in title if artist is missing
    if artist is None and ' - ' in title:
        parts = title.split(' - ', 1)
        artist = parts[0].strip()
        title = parts[1].strip()
        
    # 2. Remove numeric prefixes from title (e.g. "011-", "01 ")
    # Matches "001-", "12-", "05 " at start
    title = re.sub(r'^\d{2,3}[- ]\s*', '', title)
    
    # 3. Clean Artist if still None
    if artist is None:
        artist = "unknown"
        
    # 4. Remove Artist from Title if present at start
    # Normalize for comparison
    norm_title = title.lower()
    norm_artist = artist.lower()
    
    if norm_title.startswith(norm_artist):
        # Remove artist from title
        # Check for separator
        remaining = title[len(artist):]
        if remaining.startswith(' - '):
            title = remaining[3:]
        elif remaining.startswith(' '):
            title = remaining[1:]
            
    # 5. Remove parentheses and brackets content from title
    # e.g. "Song (Live)" -> "Song"
    title = re.sub(r'\s*\(.*?\)', '', title)
    title = re.sub(r'\s*\[.*?\]', '', title)
    
    # 6. Remove trailing " - .*" (Album or other info)
    # Be careful not to kill "Song - Part 2" if it's significant, 
    # but generally "Song - Album" is common.
    # Let's try splitting by " - " and taking the first part.
    if ' - ' in title:
        title = title.split(' - ')[0]
        
    # Final strip
    title = title.strip().lower()
    artist = artist.strip().lower()
    
    # Remove "the " from artist
    if artist.startswith("the "):
        artist = artist[4:]
        
    return pd.Series([artist, title])

df[['clean_artist', 'clean_title']] = df.apply(clean_row, axis=1)

# Group
grouped = df.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values(by='total_revenue', ascending=False)

top_5 = grouped.head(5)
print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-13586711412280274277': 'file_storage/function-call-13586711412280274277.json', 'var_function-call-15404616828467795232': 'file_storage/function-call-15404616828467795232.json', 'var_function-call-17951451854293294471': [{'track_id': '14719', 'total_revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?"}, {'track_id': '5124', 'total_revenue': 2503.19, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)'}, {'track_id': '1344', 'total_revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams'}, {'track_id': '6725', 'total_revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)'}, {'track_id': '10377', 'total_revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None'}, {'track_id': '5050', 'total_revenue': 2466.31, 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'album': 'Munich City Nights, Volume 11'}, {'track_id': '6667', 'total_revenue': 2452.7, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'album': 'None'}, {'track_id': '7245', 'total_revenue': 2436.97, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'album': 'Indul a boksz'}, {'track_id': '11641', 'total_revenue': 2428.22, 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'album': 'Share Your Love'}, {'track_id': '964', 'total_revenue': 2425.61, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'album': 'None'}, {'track_id': '12984', 'total_revenue': 2401.71, 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'album': 'None'}, {'track_id': '6208', 'total_revenue': 2385.03, 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'album': 'Helloween, Part z: The Rise of Satan'}, {'track_id': '666', 'total_revenue': 2382.74, 'title': 'Emblem G - G of the Planets - Original Soundtrack', 'artist': 'Hoyt S. Curtin', 'album': 'None'}, {'track_id': '12620', 'total_revenue': 2377.59, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'album': 'None'}, {'track_id': '19232', 'total_revenue': 2368.75, 'title': 'Misfortunes - From Horizon to Horizon: Singles 1983-92', 'artist': 'And Also The Trees', 'album': 'None'}, {'track_id': '17757', 'total_revenue': 2365.59, 'title': '008-FanFanFanatic', 'artist': 'Rheingold', 'album': 'R. (2005)'}, {'track_id': '3462', 'total_revenue': 2359.23, 'title': 'Word (15 second) - Electronica', 'artist': 'Thomas Foyer', 'album': 'None'}, {'track_id': '9639', 'total_revenue': 2351.68, 'title': 'Traces of Paganea', 'artist': 'Furious', 'album': 'Peace and Love'}, {'track_id': '18760', 'total_revenue': 2349.33, 'title': 'Patience - Distant Relatives', 'artist': 'Nas & Damian Marley', 'album': 'None'}, {'track_id': '2516', 'total_revenue': 2346.18, 'title': '006-Osm', 'artist': 'Ourson', 'album': 'Eth (2007)'}, {'track_id': '6326', 'total_revenue': 2331.91, 'title': 'Clara Ponty - The Paths to Wisdom', 'artist': 'None', 'album': 'Mirror of Truth'}, {'track_id': '5836', 'total_revenue': 2321.31, 'title': '002-Karma', 'artist': 'The Waterboys', 'album': 'Glastonbury Song (1993)'}, {'track_id': '9988', 'total_revenue': 2317.41, 'title': 'U Got It Bad (Pure… R&B)', 'artist': 'Usher', 'album': 'Pure… R&B'}, {'track_id': '18508', 'total_revenue': 2308.44, 'title': 'Arizona Telegram - The Arista Albums', 'artist': 'Alpha Band', 'album': 'None'}, {'track_id': '10760', 'total_revenue': 2293.11, 'title': 'Eichenschild - Armer Sünder', 'artist': 'None', 'album': 'Das Ende vom Lied'}, {'track_id': '9002', 'total_revenue': 2288.23, 'title': 'Gong - New Age Transformation Try: No More Sages', 'artist': 'None', 'album': 'The Best of Gong'}, {'track_id': '14169', 'total_revenue': 2281.23, 'title': 'Three Live Wires: Theme', 'artist': 'Bob Wallis', 'album': 'The Avengers & Other Top Sixties TV Themes'}, {'track_id': '9649', 'total_revenue': 2276.72, 'title': '004-I Forgot That Love Existed', 'artist': 'Van Morrison', 'album': 'Poetic Champions Compose (1998)'}, {'track_id': '10856', 'total_revenue': 2275.85, 'title': 'The Amenta - Mictlan', 'artist': 'None', 'album': 'Mictlan'}, {'track_id': '7422', 'total_revenue': 2275.04, 'title': 'Mr. Vain (High on Dance)', 'artist': 'Culture Beat', 'album': 'High on Dance'}]}

exec(code, env_args)
