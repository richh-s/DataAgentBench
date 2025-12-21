code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-14958088041472959322'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-14958088041472958953'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize_title(t):
    if not isinstance(t, str): return ""
    t = t.lower().strip()
    # Remove leading track numbers e.g. "01-", "01 ", "1.", "001-"
    t = re.sub(r'^\d+[\.\-\s_]+', '', t)
    # Remove content in brackets? Maybe just remove the brackets
    # t = re.sub(r'[\(\[].*?[\)\]]', '', t) # Let's NOT do this yet, too risky
    # Remove special chars but keep spaces
    t = re.sub(r'[^a-z0-9\s]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def normalize_artist(a):
    if not isinstance(a, str): return ""
    a = a.lower().strip()
    if a in ['none', 'unknown', '[unknown]']: return ""
    # Remove special chars
    a = re.sub(r'[^a-z0-9\s]', '', a)
    a = re.sub(r'\s+', ' ', a).strip()
    return a

def get_key(row):
    t = normalize_title(row['title'])
    a = normalize_artist(row['artist'])
    if not a:
        # If artist is missing, rely on title.
        # Check if title has a " - " split?
        # But we already stripped special chars in normalize_title...
        # Let's go back to raw title for splitting check
        raw_t = row['title'] if isinstance(row['title'], str) else ""
        if " - " in raw_t:
             parts = raw_t.split(" - ", 1)
             # Heuristic: assume Artist - Title if artist is missing?
             # Or just use the whole title as the key if artist is missing.
             # Using whole title is safer to avoid splitting wrong.
             pass
    return (t, a)

df['norm_key'] = df.apply(get_key, axis=1)

# Filter out empty keys
df_valid = df[df['norm_key'] != ("", "")]

grouped = df_valid.groupby('norm_key').agg({
    'total_revenue': 'sum',
    'track_id': 'count',
    'title': lambda x: list(x)[:3], # sample titles
    'artist': lambda x: list(x)[:3] # sample artists
}).reset_index()

grouped = grouped.sort_values('total_revenue', ascending=False).head(10)

print("__RESULT__:")
print(grouped.to_json(orient='records'))"""

env_args = {'var_function-call-14958088041472959322': 'file_storage/function-call-14958088041472959322.json', 'var_function-call-14958088041472958953': 'file_storage/function-call-14958088041472958953.json', 'var_function-call-1650018392869466056': [{'entity_key': ['', ''], 'total_revenue': 254383.89}, {'entity_key': ['none', ''], 'total_revenue': 17150.55}, {'entity_key': ['003', ''], 'total_revenue': 8582.15}, {'entity_key': ['004', ''], 'total_revenue': 7271.32}, {'entity_key': ['005', ''], 'total_revenue': 6155.29}, {'entity_key': ['009', ''], 'total_revenue': 5045.7}, {'entity_key': ['002', ''], 'total_revenue': 5013.44}, {'entity_key': ['001', ''], 'total_revenue': 4927.17}, {'entity_key': ['ki meil pahanu', ''], 'total_revenue': 4916.11}, {'entity_key': ['010', ''], 'total_revenue': 4734.36}], 'var_function-call-5138246457515100991': [{'track_id': '14719', 'total_revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, {'track_id': '5124', 'total_revenue': 2503.19, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}, {'track_id': '1344', 'total_revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}, {'track_id': '6725', 'total_revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}, {'track_id': '10377', 'total_revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}, {'track_id': '5050', 'total_revenue': 2466.31, 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'album': 'Munich City Nights, Volume 11', 'year': '90'}, {'track_id': '6667', 'total_revenue': 2452.7, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'album': 'None', 'year': "'04"}, {'track_id': '7245', 'total_revenue': 2436.97, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'album': 'Indul a boksz', 'year': '1996'}, {'track_id': '11641', 'total_revenue': 2428.22, 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'album': 'Share Your Love', 'year': '1981'}, {'track_id': '964', 'total_revenue': 2425.61, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'album': 'None', 'year': 'None'}, {'track_id': '12984', 'total_revenue': 2401.71, 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'album': 'None', 'year': "'97"}, {'track_id': '6208', 'total_revenue': 2385.03, 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'album': 'Helloween, Part z: The Rise of Satan', 'year': '2010'}, {'track_id': '666', 'total_revenue': 2382.74, 'title': 'Emblem G - G of the Planets - Original Soundtrack', 'artist': 'Hoyt S. Curtin', 'album': 'None', 'year': 'None'}, {'track_id': '12620', 'total_revenue': 2377.59, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'album': 'None', 'year': "'08"}, {'track_id': '19232', 'total_revenue': 2368.75, 'title': 'Misfortunes - From Horizon to Horizon: Singles 1983-92', 'artist': 'And Also The Trees', 'album': 'None', 'year': "'93"}, {'track_id': '17757', 'total_revenue': 2365.59, 'title': '008-FanFanFanatic', 'artist': 'Rheingold', 'album': 'R. (2005)', 'year': 'None'}, {'track_id': '3462', 'total_revenue': 2359.23, 'title': 'Word (15 second) - Electronica', 'artist': 'Thomas Foyer', 'album': 'None', 'year': 'None'}, {'track_id': '9639', 'total_revenue': 2351.68, 'title': 'Traces of Paganea', 'artist': 'Furious', 'album': 'Peace and Love', 'year': 'None'}, {'track_id': '18760', 'total_revenue': 2349.33, 'title': 'Patience - Distant Relatives', 'artist': 'Nas & Damian Marley', 'album': 'None', 'year': "'10"}, {'track_id': '2516', 'total_revenue': 2346.18, 'title': '006-Osm', 'artist': 'Ourson', 'album': 'Eth (2007)', 'year': 'None'}]}

exec(code, env_args)
