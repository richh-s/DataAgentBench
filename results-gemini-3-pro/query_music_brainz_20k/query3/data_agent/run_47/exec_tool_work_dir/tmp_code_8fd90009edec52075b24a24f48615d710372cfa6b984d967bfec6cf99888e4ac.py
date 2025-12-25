code = """import json
import pandas as pd

# Load previous results (the full list is not available, so I have to reload and process)
# Actually I have the files.

with open(locals()['var_function-call-18145844648055813096'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-16557127791975595763'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_tracks['norm_title'] = df_tracks['title'].apply(lambda x: str(x).lower().strip() if x else "")
df_tracks['norm_artist'] = df_tracks['artist'].apply(lambda x: str(x).lower().strip() if x else "")

merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Check variations for Groovey
groovey_mask = merged['norm_title'].str.contains('groovey') | merged['norm_artist'].str.contains('matteson')
groovey_entries = merged[groovey_mask]

# Check variations for Fire Still Burns
fire_mask = merged['norm_title'].str.contains('fire still burns') | merged['norm_artist'].str.contains('ballard')
fire_entries = merged[fire_mask]

print("__RESULT__:")
print(json.dumps({
    "groovey_entries": groovey_entries[['title', 'artist', 'revenue_usd']].to_dict(orient='records'),
    "fire_entries": fire_entries[['title', 'artist', 'revenue_usd']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-18145844648055813096': 'file_storage/function-call-18145844648055813096.json', 'var_function-call-16557127791975595763': 'file_storage/function-call-16557127791975595763.json', 'var_function-call-4354660084992028470': [{'norm_title': 'none', 'norm_artist': 'none', 'revenue_usd': 14647.52}, {'norm_title': '010-', 'norm_artist': 'none', 'revenue_usd': 4163.48}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue_usd': 4128.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'revenue_usd': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'revenue_usd': 3767.95}, {'norm_title': '001-', 'norm_artist': 'none', 'revenue_usd': 3742.44}, {'norm_title': '003-', 'norm_artist': 'none', 'revenue_usd': 3446.78}, {'norm_title': '003-', 'norm_artist': '', 'revenue_usd': 3394.4}, {'norm_title': '005-', 'norm_artist': 'none', 'revenue_usd': 3347.89}, {'norm_title': '002-', 'norm_artist': 'none', 'revenue_usd': 3343.61}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'revenue_usd': 3241.21}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'revenue_usd': 3228.62}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'revenue_usd': 3218.63}, {'norm_title': 'unknown', 'norm_artist': 'none', 'revenue_usd': 3218.35}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'revenue_usd': 3171.7}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'revenue_usd': 3091.77}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'revenue_usd': 3052.75}, {'norm_title': 'al stewart - year of the cat', 'norm_artist': 'none', 'revenue_usd': 3049.93}, {'norm_title': 'skin', 'norm_artist': 'westworld', 'revenue_usd': 3008.01}, {'norm_title': 'christmas in my heart', 'norm_artist': 'candi staton', 'revenue_usd': 2969.33}], 'var_function-call-16644640437275407882': [{'norm_title': 'none', 'norm_artist': 'none', 'revenue_usd': 14647.52, 'album': ['Mijn Restaurant!', 'Journey to Persia', 'Drop Dead Gorgeous', "Live in '05", 'Bakom Kulisserna', 'Untitled 2 / Bad Brother', 'Soundtrack', '20032010', 'None', 'Ultimo Trem', 'This Is My First Album', 'Iridescence: Sequencer Sketches, Volume 2', 'Live - Blow the House Down', 'East Volume Lotus - Mixed by Ping', 'The Metal Years: Gothic Doom'], 'title': ['None'], 'artist': ['None']}, {'norm_title': '010-', 'norm_artist': 'none', 'revenue_usd': 4163.48, 'album': ['MOON (unknown)', ' (2004)', ' VOL  (1997)', 'CD (1997)'], 'title': ['010-'], 'artist': ['None']}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue_usd': 4128.59, 'album': ['Groovey'], 'title': ['Groovey'], 'artist': ['Rich Matteson']}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'revenue_usd': 3807.4, 'album': ['The Fire Still Burns'], 'title': ['The Fire Still Burns'], 'artist': ['Russ Ballard']}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'revenue_usd': 3767.95, 'album': ['Vostok', 'Vosttok'], 'title': ['Vostok'], 'artist': ['Craig Padilla']}, {'norm_title': '001-', 'norm_artist': 'none', 'revenue_usd': 3742.44, 'album': [' ! (2004)', '  (2007)', 'WAKU WAKU (1983)', ' (1997)'], 'title': ['001-'], 'artist': ['None']}, {'norm_title': '003-', 'norm_artist': 'none', 'revenue_usd': 3446.78, 'album': [' (1988)', '    (2002)', ' (1980)', 'Grace and Charm (2005)'], 'title': ['003-'], 'artist': ['None']}, {'norm_title': '003-', 'norm_artist': '', 'revenue_usd': 3394.4, 'album': [' (2003)', '  (1996)'], 'title': ['003-', '003- '], 'artist': [' ']}, {'norm_title': '005-', 'norm_artist': 'none', 'revenue_usd': 3347.89, 'album': ['  (unknown)', '+ SINGLES  (2007)', ' (1996)'], 'title': ['005-'], 'artist': ['None']}, {'norm_title': '002-', 'norm_artist': 'none', 'revenue_usd': 3343.61, 'album': [' BOX (2011)', ' 3 / (2000)'], 'title': ['002-'], 'artist': ['None']}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'revenue_usd': 3241.21, 'album': ['All My Friends Say'], 'title': ['All My Friends Say (album version)'], 'artist': ['Luke Bryan']}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'revenue_usd': 3228.62, 'album': ['Beautiful', 'None'], 'title': ['Beautiful (instrumental)'], 'artist': ['Damian Marley']}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'revenue_usd': 3218.63, 'album': ['Private Soul Security', 'Pirvate Soul Security'], 'title': ['Private Soul Security'], 'artist': ['Down Below']}, {'norm_title': 'unknown', 'norm_artist': 'none', 'revenue_usd': 3218.35, 'album': ['モンゴルのホーミー～ガンボルド、ヤヴガーン', 'Magician & Gershwin & Kern', '1999-06-28: Glasgow, UK', 'Faith, Hope & Love', 'Symphony in D minor / Symphonic Variations (Vienna Philharmonic Orchestra feat. conductor: Carlos Maria Giulini)'], 'title': ['unknown'], 'artist': ['None']}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'revenue_usd': 3171.7, 'album': ['Bring Back the Love'], 'title': ['Bring Back the Love (Spaced Out dub)'], 'artist': ['Laura Harris']}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'revenue_usd': 3091.77, 'album': ['Chi to Rome'], 'title': ['Chi to Rome (Broke One edit)'], 'artist': ['Lazy Ants & Rob Threezy']}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'revenue_usd': 3052.75, 'album': ['Bad Hearts'], 'title': ['Bad Hearts'], 'artist': ['Tights']}, {'norm_title': 'al stewart - year of the cat', 'norm_artist': 'none', 'revenue_usd': 3049.93, 'album': ['Mel low Rock Classics', 'Missing You'], 'title': ['Al Stewart - Year of the Cat'], 'artist': ['None']}, {'norm_title': 'skin', 'norm_artist': 'westworld', 'revenue_usd': 3008.01, 'album': ['Skin'], 'title': ['Skin'], 'artist': ['Westworld']}, {'norm_title': 'christmas in my heart', 'norm_artist': 'candi staton', 'revenue_usd': 2969.33, 'album': ['Christmas In My Heart'], 'title': ['Christmas In My Heart'], 'artist': ['Candi Staton']}]}

exec(code, env_args)
