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

def normalize_text(s):
    if not isinstance(s, str): return ""
    s = s.lower().strip()
    # Remove leading track numbers
    s = re.sub(r'^\d+[\.\-\s_]+', '', s)
    # Remove punctuation, keep alphanum and spaces. 
    # Using [^\w\s] might strip too little if we want to match "O.M.G." with "OMG"
    # But let's stick to removing punctuation.
    s = re.sub(r'[^\w\s]', ' ', s, flags=re.UNICODE)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def get_key(row):
    t = normalize_text(row['title'])
    a = normalize_text(row['artist'])
    
    # Filter junk
    if t in ["", "none", "unknown", "untitled"] or re.match(r'^track \d+$', t):
        return None
    
    if not a:
        # If artist missing, maybe check raw title again? 
        # But for now let's just use title.
        pass
    else:
         if a in ["none", "unknown"]:
             a = ""
    
    return (t, a)

df['norm_key'] = df.apply(get_key, axis=1)

# Remove None keys
df_valid = df.dropna(subset=['norm_key'])

grouped = df_valid.groupby('norm_key').agg({
    'total_revenue': 'sum',
    'track_id': 'count',
    'title': lambda x: list(x)[:1],
    'artist': lambda x: list(x)[:1]
}).reset_index()

grouped = grouped.sort_values('total_revenue', ascending=False).head(10)

print("__RESULT__:")
print(grouped.to_json(orient='records'))"""

env_args = {'var_function-call-14958088041472959322': 'file_storage/function-call-14958088041472959322.json', 'var_function-call-14958088041472958953': 'file_storage/function-call-14958088041472958953.json', 'var_function-call-1650018392869466056': [{'entity_key': ['', ''], 'total_revenue': 254383.89}, {'entity_key': ['none', ''], 'total_revenue': 17150.55}, {'entity_key': ['003', ''], 'total_revenue': 8582.15}, {'entity_key': ['004', ''], 'total_revenue': 7271.32}, {'entity_key': ['005', ''], 'total_revenue': 6155.29}, {'entity_key': ['009', ''], 'total_revenue': 5045.7}, {'entity_key': ['002', ''], 'total_revenue': 5013.44}, {'entity_key': ['001', ''], 'total_revenue': 4927.17}, {'entity_key': ['ki meil pahanu', ''], 'total_revenue': 4916.11}, {'entity_key': ['010', ''], 'total_revenue': 4734.36}], 'var_function-call-5138246457515100991': [{'track_id': '14719', 'total_revenue': 2522.82, 'title': 'Systemisch bled', 'artist': 'Stüngö', 'album': "Um wos gehts'n?", 'year': '2009'}, {'track_id': '5124', 'total_revenue': 2503.19, 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'album': 'Autumn of Their Years (unknown)', 'year': 'None'}, {'track_id': '1344', 'total_revenue': 2500.72, 'title': 'Life CycUles', 'artist': 'Chosen', 'album': 'Space Jams', 'year': '2011'}, {'track_id': '6725', 'total_revenue': 2489.81, 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'album': 'In Motion (1979)', 'year': 'None'}, {'track_id': '10377', 'total_revenue': 2466.71, 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'album': 'None', 'year': "'12"}, {'track_id': '5050', 'total_revenue': 2466.31, 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'album': 'Munich City Nights, Volume 11', 'year': '90'}, {'track_id': '6667', 'total_revenue': 2452.7, 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'album': 'None', 'year': "'04"}, {'track_id': '7245', 'total_revenue': 2436.97, 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'album': 'Indul a boksz', 'year': '1996'}, {'track_id': '11641', 'total_revenue': 2428.22, 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'album': 'Share Your Love', 'year': '1981'}, {'track_id': '964', 'total_revenue': 2425.61, 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'album': 'None', 'year': 'None'}, {'track_id': '12984', 'total_revenue': 2401.71, 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'album': 'None', 'year': "'97"}, {'track_id': '6208', 'total_revenue': 2385.03, 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'album': 'Helloween, Part z: The Rise of Satan', 'year': '2010'}, {'track_id': '666', 'total_revenue': 2382.74, 'title': 'Emblem G - G of the Planets - Original Soundtrack', 'artist': 'Hoyt S. Curtin', 'album': 'None', 'year': 'None'}, {'track_id': '12620', 'total_revenue': 2377.59, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'album': 'None', 'year': "'08"}, {'track_id': '19232', 'total_revenue': 2368.75, 'title': 'Misfortunes - From Horizon to Horizon: Singles 1983-92', 'artist': 'And Also The Trees', 'album': 'None', 'year': "'93"}, {'track_id': '17757', 'total_revenue': 2365.59, 'title': '008-FanFanFanatic', 'artist': 'Rheingold', 'album': 'R. (2005)', 'year': 'None'}, {'track_id': '3462', 'total_revenue': 2359.23, 'title': 'Word (15 second) - Electronica', 'artist': 'Thomas Foyer', 'album': 'None', 'year': 'None'}, {'track_id': '9639', 'total_revenue': 2351.68, 'title': 'Traces of Paganea', 'artist': 'Furious', 'album': 'Peace and Love', 'year': 'None'}, {'track_id': '18760', 'total_revenue': 2349.33, 'title': 'Patience - Distant Relatives', 'artist': 'Nas & Damian Marley', 'album': 'None', 'year': "'10"}, {'track_id': '2516', 'total_revenue': 2346.18, 'title': '006-Osm', 'artist': 'Ourson', 'album': 'Eth (2007)', 'year': 'None'}], 'var_function-call-6053834500192605748': [{'norm_key': ['none', ''], 'total_revenue': 17150.55, 'track_id': 19, 'title': ['None', 'None', 'None'], 'artist': ['None', 'None', 'None']}, {'norm_key': ['unknown', ''], 'total_revenue': 4739.46, 'track_id': 7, 'title': ['unknown', '[unknown] - 棄樟', 'unknown'], 'artist': ['None', 'None', 'None']}, {'norm_key': ['tv', ''], 'total_revenue': 4527.58, 'track_id': 4, 'title': ['キーボード・イントロダクション (TVアニメ「けいおん!」オフィシャル バンドやろーよ!! (バンドスコア付))', 'キーボード・イントロダクション - TVアニメ「けいおん!」オフィシャル バンドやろーよ!! (バンドスコア付)', 'たよりりになる先輩? (TVニメ 『ひだまりスケッチ×☆☆☆』 オリジナルサウンドトラック 『ひだまり・でいず・ないと』)'], 'artist': ['放課後ティータイム', '放課後ティータイム', '菊谷知樹']}, {'norm_key': ['groovey', 'rich matteson'], 'total_revenue': 4379.75, 'track_id': 4, 'title': ['Groovey', 'Groovey', 'Groovey'], 'artist': ['Rich Matteson', 'Rich Matteson', 'Rich Matteson']}, {'norm_key': ['all my friends say album version', 'luke bryan'], 'total_revenue': 4311.59, 'track_id': 3, 'title': ['All My Friends Say (album version)', 'All My Friends Say (album version)', '002-All My Friends Say (album version)'], 'artist': ['Luke Bryan', 'Luke Bryan', 'Luke Bryan']}, {'norm_key': ['1', ''], 'total_revenue': 4201.84, 'track_id': 3, 'title': ['1', '00-1', '00-1'], 'artist': ['大江千里', '[unknown]', 'None']}, {'norm_key': ['zo gaat het leven aan je voor hillich fjoer heilig vuur', 'syb van der ploeg'], 'total_revenue': 4132.27, 'track_id': 2, 'title': ['Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)'], 'artist': ['Syb van der Ploeg', 'Syb van der Ploeg']}, {'norm_key': ['the fire still burns', 'russ ballard'], 'total_revenue': 4102.45, 'track_id': 3, 'title': ['The Fire Still Burns', 'The Fire Still Burns', '008-The Fire Still Burns'], 'artist': ['Russ Ballard', 'Russ Ballard', 'Russ Ballard']}, {'norm_key': ['untitled', ''], 'total_revenue': 4032.21, 'track_id': 5, 'title': ['[untitled]', '011-[untitled]', '[untitled]'], 'artist': ['Шумы России', 'None', '神聖かまってちゃん']}, {'norm_key': ['thousand finger man salsoul 30th', 'candido'], 'total_revenue': 3934.83, 'track_id': 2, 'title': ['Thousand Finger Man - Salsoul 30th', 'Thousand Finger Man (Salsoul 30th)'], 'artist': ['Candido', 'Candido']}]}

exec(code, env_args)
