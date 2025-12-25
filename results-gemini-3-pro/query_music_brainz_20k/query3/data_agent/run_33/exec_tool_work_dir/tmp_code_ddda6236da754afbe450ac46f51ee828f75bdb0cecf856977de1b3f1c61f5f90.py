code = """import json
import pandas as pd

# Load previous results directly from variables to save time? 
# No, dataframes are not persisted across calls unless I put them in a file or they are in the 'results'.
# I have to reload.

with open(locals()['var_function-call-3835480464136415484'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6188791716186405650'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Same cleaning logic
import re
import unicodedata

def normalize_text(text):
    if not text:
        return ""
    text = str(text).lower()
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'[^\w\s]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_track_info(row):
    title = row['title']
    artist = row['artist']
    invalid = ['none', 'unknown', '[unknown]', '', 'null']
    if str(artist).lower().strip() in invalid:
        if title and '-' in title:
            p = title.split('-', 1)
            if len(p[0].strip()) < 50:
                artist = p[0].strip()
                title = p[1].strip()
    
    nt = normalize_text(title)
    na = normalize_text(artist)
    if na in invalid or na == "": na = "unknown"
    return pd.Series([nt, na])

df_tracks[['clean_title', 'clean_artist']] = df_tracks.apply(clean_track_info, axis=1)
df_tracks['match_key'] = df_tracks['clean_artist'] + "|||" + df_tracks['clean_title']

merged = df_sales.merge(df_tracks, on='track_id', how='left')
grouped = merged.groupby('match_key')['total_revenue'].sum().reset_index()

# Check specific artists
artists_to_check = ['rich matteson', 'luke bryan', 'syb van der ploeg', 'damian marley', 'kerstin gier']
rows = []
for art in artists_to_check:
    # Filter keys containing the artist name
    matches = grouped[grouped['match_key'].str.contains(art, na=False)]
    for idx, row in matches.iterrows():
        rows.append(row.to_dict())

print("__RESULT__:")
print(json.dumps(rows))"""

env_args = {'var_function-call-3835480464136415484': 'file_storage/function-call-3835480464136415484.json', 'var_function-call-6188791716186405650': 'file_storage/function-call-6188791716186405650.json', 'var_function-call-8554056373783831330': {'top_song_key': 'unknown|', 'revenue': 207955.01, 'sample_title': '妥協', 'sample_artist': '蔡依林', 'top_5': [{'match_key': 'unknown|', 'total_revenue': 207955.01}, {'match_key': 'unknown|none', 'total_revenue': 17150.55}, {'match_key': '004|', 'total_revenue': 7249.700000000001}, {'match_key': '003|', 'total_revenue': 7090.13}, {'match_key': 'richmatteson|groovey', 'total_revenue': 5417.34}]}, 'var_function-call-16098740597880241896': [{'key': 'unknown|||none', 'revenue': 14647.52, 'title': 'None', 'artist': 'None'}, {'key': '004|||', 'revenue': 7249.700000000001, 'title': '004- ', 'artist': ' '}, {'key': '003|||', 'revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'key': 'rich matteson|||groovey', 'revenue': 5417.34, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'key': '005|||', 'revenue': 5222.0, 'title': '005-', 'artist': 'None'}, {'key': '009|||', 'revenue': 5045.7, 'title': '009-   ', 'artist': 'None'}, {'key': '010|||', 'revenue': 4734.360000000001, 'title': '010-', 'artist': 'None'}, {'key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer heilig vuur', 'revenue': 4132.27, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg'}, {'key': '002|||', 'revenue': 4119.89, 'title': '002-', 'artist': ' '}, {'key': 'luke bryan|||all my friends say album version', 'revenue': 4110.55, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}], 'var_function-call-7264091150168437329': [{'key': '004|||', 'revenue': 7249.700000000001, 'title': '004- ', 'artist': ' '}, {'key': '003|||', 'revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'key': 'rich matteson|||groovey', 'revenue': 5417.34, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'key': '005|||', 'revenue': 5222.0, 'title': '005-', 'artist': 'None'}, {'key': '009|||', 'revenue': 5045.7, 'title': '009-   ', 'artist': 'None'}, {'key': '010|||', 'revenue': 4734.360000000001, 'title': '010-', 'artist': 'None'}, {'key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer heilig vuur', 'revenue': 4132.27, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg'}, {'key': '002|||', 'revenue': 4119.89, 'title': '002-', 'artist': ' '}, {'key': 'luke bryan|||all my friends say album version', 'revenue': 4110.55, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}, {'key': 'kerstin gier|||kapitel 01', 'revenue': 4091.12, 'title': 'Kapitel 01', 'artist': 'Kerstin Gier'}, {'key': 'damian marley|||beautiful instrumental', 'revenue': 4004.42, 'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley'}, {'key': 'matthew barber|||the story of your life', 'revenue': 3962.97, 'title': 'Matthew Barber - The Story of Your Life', 'artist': 'None'}, {'key': '006|||', 'revenue': 3946.7799999999997, 'title': '006- ', 'artist': ' '}, {'key': 'candido|||thousand finger man salsoul 30th', 'revenue': 3934.83, 'title': 'Thousand Finger Man - Salsoul 30th', 'artist': 'Candido'}, {'key': 'sir william gilbert sir arthur sullivan|||a wandring minstrel i from the mikado', 'revenue': 3877.43, 'title': 'Sir William Gilbert & Sir Arthur Sullivan - A Wand\'ring Minstrel I, From "The Mikado"', 'artist': 'None'}, {'key': 'ugly winner|||fret one grow old inside your wave', 'revenue': 3844.09, 'title': 'Fret One (Grow Old) (Inside Your Wave)', 'artist': 'Ugly Winner'}, {'key': 'russ ballard|||the fire still burns', 'revenue': 3807.4, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'key': 'craig padilla|||vostok', 'revenue': 3767.95, 'title': 'Vostok', 'artist': 'Craig Padilla'}, {'key': 'byzantine|||oblivion beckons', 'revenue': 3759.01, 'title': 'Byzantine - Oblivion Beckons', 'artist': 'None'}, {'key': '放課後ティータイム|||キーボードイントロダクション tvアニメけいおんオフィシャル バンドやろーよ バンドスコア付', 'revenue': 3758.99, 'title': 'キーボード・イントロダクション (TVアニメ「けいおん!」オフィシャル バンドやろーよ!! (バンドスコア付))', 'artist': '放課後ティータイム'}]}

exec(code, env_args)
