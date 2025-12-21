code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-16438138636169770779'], 'r') as f:
    revenue_data = json.load(f)
with open(locals()['var_function-call-17040196689853941222'], 'r') as f:
    track_data = json.load(f)

df_revenue = pd.DataFrame(revenue_data)
df_tracks = pd.DataFrame(track_data)
df_revenue['track_id'] = df_revenue['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_revenue['total_revenue'] = pd.to_numeric(df_revenue['total_revenue'])

df = pd.merge(df_revenue, df_tracks, on='track_id', how='inner')

def clean_track(row):
    title = str(row['title'])
    artist = str(row['artist'])
    
    if artist == 'None' or artist == '[unknown]':
        artist = ''
    if title == 'None':
        title = ''

    # Handle "Artist - Title"
    if not artist and ' - ' in title:
        parts = title.split(' - ', 1)
        if not re.match(r'^\d+$', parts[0]):
             artist = parts[0]
             title = parts[1]

    # Remove leading numbering
    title = re.sub(r'^\d+[\s-]*', '', title)
    
    # Remove parens/brackets
    title = re.sub(r'\s*\(.*?\)', '', title)
    title = re.sub(r'\s*\[.*?\]', '', title)
    
    # Remove text after " - " (often subtitles, mix names, etc.)
    if ' - ' in title:
        title = title.split(' - ')[0]
    
    # Remove text after " | "
    if ' | ' in title:
        title = title.split(' | ')[0]

    # Remove "#..."
    title = re.sub(r'#\d+', '', title)

    # Normalize
    title = title.lower().strip()
    artist = artist.lower().strip()
    
    return pd.Series([title, artist])

df[['clean_title', 'clean_artist']] = df.apply(clean_track, axis=1)
df_clean = df[df['clean_title'] != ''].copy()

grouped = df_clean.groupby(['clean_title', 'clean_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-16438138636169770779': 'file_storage/function-call-16438138636169770779.json', 'var_function-call-17040196689853941222': 'file_storage/function-call-17040196689853941222.json', 'var_function-call-2203332676551410598': [{'norm_title': '', 'norm_artist': '', 'total_revenue': 14647.52}, {'norm_title': '003-', 'norm_artist': '', 'total_revenue': 6841.18}, {'norm_title': '005-', 'norm_artist': '', 'total_revenue': 5222.0}, {'norm_title': '009-', 'norm_artist': '', 'total_revenue': 5045.7}, {'norm_title': '004-', 'norm_artist': '', 'total_revenue': 4868.47}, {'norm_title': '010-', 'norm_artist': '', 'total_revenue': 4734.36}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'norm_title': '002-', 'norm_artist': '', 'total_revenue': 4119.89}, {'norm_title': '006-', 'norm_artist': '', 'total_revenue': 3946.78}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': '001-', 'norm_artist': '', 'total_revenue': 3742.44}, {'norm_title': '012-', 'norm_artist': '', 'total_revenue': 3635.13}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'total_revenue': 3228.62}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63}, {'norm_title': 'unknown', 'norm_artist': '', 'total_revenue': 3218.35}, {'norm_title': '020-', 'norm_artist': '', 'total_revenue': 3202.16}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'total_revenue': 3171.7}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}], 'var_function-call-8257422295327477108': [{'norm_title': '', 'norm_artist': '', 'total_revenue': 14647.52, 'original_titles': ['None'], 'original_artists': ['None']}, {'norm_title': '003-', 'norm_artist': '', 'total_revenue': 6841.18, 'original_titles': ['003-', '003- '], 'original_artists': ['None', ' ']}, {'norm_title': '005-', 'norm_artist': '', 'total_revenue': 5222.0, 'original_titles': ['005-', '005- ', '005-    '], 'original_artists': ['None', ' ']}, {'norm_title': '009-', 'norm_artist': '', 'total_revenue': 5045.7, 'original_titles': ['009-  ', '009-   ', '009- '], 'original_artists': [' ', 'None']}, {'norm_title': '004-', 'norm_artist': '', 'total_revenue': 4868.47, 'original_titles': ['004- ', '004-'], 'original_artists': [' ', 'None']}, {'norm_title': '010-', 'norm_artist': '', 'total_revenue': 4734.36, 'original_titles': ['010-'], 'original_artists': ['None', ' ']}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59, 'original_titles': ['Groovey'], 'original_artists': ['Rich Matteson']}, {'norm_title': '002-', 'norm_artist': '', 'total_revenue': 4119.89, 'original_titles': ['002-'], 'original_artists': [' ', 'None']}, {'norm_title': '006-', 'norm_artist': '', 'total_revenue': 3946.78, 'original_titles': ['006- ', '006-'], 'original_artists': [' ', 'None']}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4, 'original_titles': ['The Fire Still Burns'], 'original_artists': ['Russ Ballard']}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95, 'original_titles': ['Vostok'], 'original_artists': ['Craig Padilla']}, {'norm_title': '001-', 'norm_artist': '', 'total_revenue': 3742.44, 'original_titles': ['001-'], 'original_artists': ['None']}, {'norm_title': '012-', 'norm_artist': '', 'total_revenue': 3635.13, 'original_titles': ['012-'], 'original_artists': [' ', 'None']}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21, 'original_titles': ['All My Friends Say (album version)'], 'original_artists': ['Luke Bryan']}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'total_revenue': 3228.62, 'original_titles': ['Beautiful (instrumental)'], 'original_artists': ['Damian Marley']}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63, 'original_titles': ['Private Soul Security'], 'original_artists': ['Down Below']}, {'norm_title': 'unknown', 'norm_artist': '', 'total_revenue': 3218.35, 'original_titles': ['unknown'], 'original_artists': ['None']}, {'norm_title': '020-', 'norm_artist': '', 'total_revenue': 3202.16, 'original_titles': ['020-', '020- '], 'original_artists': ['None', ' ', '[unknown]']}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'total_revenue': 3171.7, 'original_titles': ['Bring Back the Love (Spaced Out dub)'], 'original_artists': ['Laura Harris']}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77, 'original_titles': ['Chi to Rome (Broke One edit)'], 'original_artists': ['Lazy Ants & Rob Threezy']}], 'var_function-call-5877707530030629813': [{'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'total_revenue': 3228.62}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'total_revenue': 3171.7}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'total_revenue': 3052.75}, {'norm_title': 'skin', 'norm_artist': 'westworld', 'total_revenue': 3008.01}], 'var_function-call-8155288403483350143': [{'clean_title': 'emerge', 'clean_artist': 'fischerspooner', 'total_revenue': 6665.27}, {'clean_title': 'zo gaat het leven aan je voor', 'clean_artist': 'syb van der ploeg', 'total_revenue': 6636.1}, {'clean_title': 'vagga', 'clean_artist': 'ske', 'total_revenue': 6611.56}, {'clean_title': 'lovers', 'clean_artist': 'fausto papetti', 'total_revenue': 6259.3}, {'clean_title': 'ne veruj', 'clean_artist': 'vrisak generacije', 'total_revenue': 6125.34}, {'clean_title': 'chile', 'clean_artist': 'neil biggin', 'total_revenue': 6008.71}, {'clean_title': 'travel', 'clean_artist': 'guts pie earshot', 'total_revenue': 5825.26}, {'clean_title': 'lookin boy', 'clean_artist': 'hotstylz', 'total_revenue': 5712.89}, {'clean_title': 'groovey', 'clean_artist': 'rich matteson', 'total_revenue': 5668.5}, {'clean_title': 'ghetto supastar', 'clean_artist': 'pras', 'total_revenue': 5514.57}], 'var_function-call-743926260662242085': [{'clean_title': 'emerge', 'clean_artist': 'fischerspooner', 'total_revenue': 6665.2699999999995, 'tracks': [{'track_id': '7575', 'title': 'Emerge (Dave Clarke remix)', 'artist': 'Fischerspooner', 'total_revenue': 850.86}, {'track_id': '10606', 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'total_revenue': 672.1200000000001}, {'track_id': '4895', 'title': 'Fischerspooner - Emerge (Dexter remix)', 'artist': 'None', 'total_revenue': 1610.46}, {'track_id': '6988', 'title': 'Emerge (Dexter remix) (#1)', 'artist': 'Fischerspooner', 'total_revenue': 1762.8000000000002}, {'track_id': '17167', 'title': '027-Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'total_revenue': 1769.03}]}, {'clean_title': 'zo gaat het leven aan je voor', 'clean_artist': 'syb van der ploeg', 'total_revenue': 6636.1, 'tracks': [{'track_id': '3024', 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'total_revenue': 1754.6800000000003}, {'track_id': '12854', 'title': '006-Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'total_revenue': 1379.6699999999998}, {'track_id': '13225', 'title': 'Syb van der Ploeg - Zo gaat het leven aan je voor', 'artist': 'None', 'total_revenue': 1477.38}, {'track_id': '3435', 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'total_revenue': 2024.37}]}, {'clean_title': 'vagga', 'clean_artist': 'ske', 'total_revenue': 6611.56, 'tracks': [{'track_id': '6188', 'title': 'Ske - Vagga', 'artist': 'None', 'total_revenue': 1459.5600000000002}, {'track_id': '17878', 'title': '011-Vagga', 'artist': 'Ske', 'total_revenue': 1630.18}, {'track_id': '14686', 'title': 'Vagga (Feelings Are Great)', 'artist': 'Ske', 'total_revenue': 2163.69}, {'track_id': '12735', 'title': 'Vagga', 'artist': 'Ske', 'total_revenue': 1358.13}]}, {'clean_title': 'lovers', 'clean_artist': 'fausto papetti', 'total_revenue': 6259.3, 'tracks': [{'track_id': '2621', 'title': 'Lovers', 'artist': 'Fausto Papetti', 'total_revenue': 777.86}, {'track_id': '3412', 'title': 'Fausto Papetti - Lovers', 'artist': 'None', 'total_revenue': 2250.04}, {'track_id': '17070', 'title': '001-Lovers', 'artist': 'Fausto Papetti', 'total_revenue': 1742.64}, {'track_id': '13097', 'title': 'Lovers (27ª raccolta)', 'artist': 'Fausto Papetti', 'total_revenue': 1488.76}]}, {'clean_title': 'ne veruj', 'clean_artist': 'vrisak generacije', 'total_revenue': 6125.339999999998, 'tracks': [{'track_id': '4445', 'title': 'Ne veruj (Beer Drinkers Revenge)', 'artist': 'Vrisak generacije', 'total_revenue': 1675.0499999999995}, {'track_id': '8315', 'title': '005-Ne veruj', 'artist': 'Vrisak generacije', 'total_revenue': 1432.08}, {'track_id': '5568', 'title': 'Vrisak generacije - Ne veruj', 'artist': 'None', 'total_revenue': 1458.2199999999998}, {'track_id': '11570', 'title': 'Ne veruj', 'artist': 'Vrisak generacije', 'total_revenue': 1559.9899999999998}]}]}

exec(code, env_args)
