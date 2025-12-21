code = """import json
import pandas as pd
import re
import unicodedata

# ... (Same setup)
with open(locals()['var_function-call-3835480464136415484'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6188791716186405650'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

def normalize_text(text):
    if not text: return ""
    text = str(text).lower()
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'[^\w\s]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_track_info(row):
    title = row['title']
    artist = row['artist']
    invalid = ['none', 'unknown', '[unknown]', '', 'null', ' ']
    
    if title:
        m = re.match(r'^(\d+)\s*-\s*(.*)', title)
        if m: title = m.group(2)
            
    norm_artist_check = str(artist).lower().strip()
    artist_missing = norm_artist_check in invalid

    if artist_missing and title and ('-' in title):
        parts = title.split('-', 1)
        if len(parts) == 2:
            p1 = parts[0].strip()
            p2 = parts[1].strip()
            if not p1.isdigit() and len(p1) < 50:
                artist = p1
                title = p2
    return pd.Series([normalize_text(title), normalize_text(artist)])

df_tracks[['clean_title', 'clean_artist']] = df_tracks.apply(clean_track_info, axis=1)
df_tracks['match_key'] = df_tracks['clean_artist'] + "|||" + df_tracks['clean_title']

merged = df_sales.merge(df_tracks, on='track_id', how='left')
grouped = merged.groupby('match_key')['total_revenue'].sum().reset_index()

# Check Pras variants
pras_matches = grouped[grouped['match_key'].str.contains('pras', na=False) | grouped['match_key'].str.contains('ghetto', na=False)]
# Check Groovy variants
groovy_matches = grouped[grouped['match_key'].str.contains('matteson', na=False) | grouped['match_key'].str.contains('groov', na=False)]

print("__RESULT__:")
print(json.dumps({
    "pras": pras_matches.to_dict(orient='records'),
    "groovy": groovy_matches.to_dict(orient='records')
}))"""

env_args = {'var_function-call-3835480464136415484': 'file_storage/function-call-3835480464136415484.json', 'var_function-call-6188791716186405650': 'file_storage/function-call-6188791716186405650.json', 'var_function-call-8554056373783831330': {'top_song_key': 'unknown|', 'revenue': 207955.01, 'sample_title': '妥協', 'sample_artist': '蔡依林', 'top_5': [{'match_key': 'unknown|', 'total_revenue': 207955.01}, {'match_key': 'unknown|none', 'total_revenue': 17150.55}, {'match_key': '004|', 'total_revenue': 7249.700000000001}, {'match_key': '003|', 'total_revenue': 7090.13}, {'match_key': 'richmatteson|groovey', 'total_revenue': 5417.34}]}, 'var_function-call-16098740597880241896': [{'key': 'unknown|||none', 'revenue': 14647.52, 'title': 'None', 'artist': 'None'}, {'key': '004|||', 'revenue': 7249.700000000001, 'title': '004- ', 'artist': ' '}, {'key': '003|||', 'revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'key': 'rich matteson|||groovey', 'revenue': 5417.34, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'key': '005|||', 'revenue': 5222.0, 'title': '005-', 'artist': 'None'}, {'key': '009|||', 'revenue': 5045.7, 'title': '009-   ', 'artist': 'None'}, {'key': '010|||', 'revenue': 4734.360000000001, 'title': '010-', 'artist': 'None'}, {'key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer heilig vuur', 'revenue': 4132.27, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg'}, {'key': '002|||', 'revenue': 4119.89, 'title': '002-', 'artist': ' '}, {'key': 'luke bryan|||all my friends say album version', 'revenue': 4110.55, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}], 'var_function-call-7264091150168437329': [{'key': '004|||', 'revenue': 7249.700000000001, 'title': '004- ', 'artist': ' '}, {'key': '003|||', 'revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'key': 'rich matteson|||groovey', 'revenue': 5417.34, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'key': '005|||', 'revenue': 5222.0, 'title': '005-', 'artist': 'None'}, {'key': '009|||', 'revenue': 5045.7, 'title': '009-   ', 'artist': 'None'}, {'key': '010|||', 'revenue': 4734.360000000001, 'title': '010-', 'artist': 'None'}, {'key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer heilig vuur', 'revenue': 4132.27, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg'}, {'key': '002|||', 'revenue': 4119.89, 'title': '002-', 'artist': ' '}, {'key': 'luke bryan|||all my friends say album version', 'revenue': 4110.55, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}, {'key': 'kerstin gier|||kapitel 01', 'revenue': 4091.12, 'title': 'Kapitel 01', 'artist': 'Kerstin Gier'}, {'key': 'damian marley|||beautiful instrumental', 'revenue': 4004.42, 'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley'}, {'key': 'matthew barber|||the story of your life', 'revenue': 3962.97, 'title': 'Matthew Barber - The Story of Your Life', 'artist': 'None'}, {'key': '006|||', 'revenue': 3946.7799999999997, 'title': '006- ', 'artist': ' '}, {'key': 'candido|||thousand finger man salsoul 30th', 'revenue': 3934.83, 'title': 'Thousand Finger Man - Salsoul 30th', 'artist': 'Candido'}, {'key': 'sir william gilbert sir arthur sullivan|||a wandring minstrel i from the mikado', 'revenue': 3877.43, 'title': 'Sir William Gilbert & Sir Arthur Sullivan - A Wand\'ring Minstrel I, From "The Mikado"', 'artist': 'None'}, {'key': 'ugly winner|||fret one grow old inside your wave', 'revenue': 3844.09, 'title': 'Fret One (Grow Old) (Inside Your Wave)', 'artist': 'Ugly Winner'}, {'key': 'russ ballard|||the fire still burns', 'revenue': 3807.4, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'key': 'craig padilla|||vostok', 'revenue': 3767.95, 'title': 'Vostok', 'artist': 'Craig Padilla'}, {'key': 'byzantine|||oblivion beckons', 'revenue': 3759.01, 'title': 'Byzantine - Oblivion Beckons', 'artist': 'None'}, {'key': '放課後ティータイム|||キーボードイントロダクション tvアニメけいおんオフィシャル バンドやろーよ バンドスコア付', 'revenue': 3758.99, 'title': 'キーボード・イントロダクション (TVアニメ「けいおん!」オフィシャル バンドやろーよ!! (バンドスコア付))', 'artist': '放課後ティータイム'}], 'var_function-call-14812217205519143356': [{'match_key': 'rich matteson|||006groovey', 'total_revenue': 251.16}, {'match_key': 'rich matteson|||groovey', 'total_revenue': 5417.34}, {'match_key': 'luke bryan|||002all my friends say album version', 'total_revenue': 1070.38}, {'match_key': 'luke bryan|||all my friends say album version', 'total_revenue': 4110.55}, {'match_key': 'syb van der ploeg|||006zo gaat het leven aan je voor', 'total_revenue': 1379.6699999999998}, {'match_key': 'syb van der ploeg|||zo gaat het leven aan je voor', 'total_revenue': 3501.75}, {'match_key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer heilig vuur', 'total_revenue': 4132.27}, {'match_key': 'bruno mars feat damian marley|||liquor store blues doowops hooligans', 'total_revenue': 845.96}, {'match_key': 'damian marley|||beautiful instrumental', 'total_revenue': 4004.42}, {'match_key': 'nas damian marley|||011patience', 'total_revenue': 97.35}, {'match_key': 'nas damian marley|||patience distant relatives', 'total_revenue': 2349.33}, {'match_key': 'kerstin gier|||kapitel 01', 'total_revenue': 4091.12}, {'match_key': 'kerstin gier|||kapitel 01 lügen die von herzen kommen feat narrator mirja bös', 'total_revenue': 492.78}, {'match_key': 'kerstin gier|||kapitel 35 lügen die von herzen kommen feat narrator mirja bös', 'total_revenue': 1437.87}, {'match_key': 'kerstin gier|||lugen die von herzen kommen feat narrator mirja bos 2008', 'total_revenue': 641.26}], 'var_function-call-4470112519927535430': [{'track_id': '403', 'title': '004-Love & Peace = ', 'artist': 'None', 'album': 'BEST FRIENDS (2013)'}, {'track_id': '5742', 'title': '004-/', 'artist': 'None', 'album': 'Initial J (2005)'}, {'track_id': '5999', 'title': '004-"" (, , , )', 'artist': ' ', 'album': '  -    (2004)'}, {'track_id': '7471', 'title': '004- ', 'artist': ' ', 'album': ' , 22:   (1997)'}, {'track_id': '7659', 'title': '004-', 'artist': 'None', 'album': ' (1997)'}, {'track_id': '9198', 'title': '004-Kimiwotsureteiku', 'artist': 'None', 'album': 'Wishes (2003)'}, {'track_id': '11048', 'title': '004-', 'artist': 'None', 'album': ' (2009)'}, {'track_id': '11349', 'title': '004- -off vocal ver.-', 'artist': 'None', 'album': 'Winter Kiss (2013)'}, {'track_id': '12273', 'title': '004-Konayuki Maifuru Kouen de * karaoke', 'artist': 'None', 'album': 'Mamoru-kun ni Megami no Shukufuku wo! OP Single  MA MO RU! (2006)'}, {'track_id': '12562', 'title': '004- ', 'artist': ' ', 'album': '   (2002)'}], 'var_function-call-8985187738768142923': [{'key': 'unknown|||', 'revenue': 65286.36, 'sample_title': '020-', 'sample_artist': 'None'}, {'key': 'unknown|||none', 'revenue': 14647.52, 'sample_title': 'None', 'sample_artist': 'None'}, {'key': 'rich matteson|||groovey', 'revenue': 5668.5, 'sample_title': 'Groovey', 'sample_artist': 'Rich Matteson'}, {'key': 'luke bryan|||all my friends say album version', 'revenue': 5180.93, 'sample_title': 'All My Friends Say (album version)', 'sample_artist': 'Luke Bryan'}, {'key': 'pras|||ghetto supastar that is what you are', 'revenue': 4933.98, 'sample_title': 'Ghetto Supastar (That Is What You Are)', 'sample_artist': 'Pras'}, {'key': 'frankie goes to hollywood|||the power of love rob searle club mix', 'revenue': 4909.04, 'sample_title': 'The Power of Love (Rob Searle club mix)', 'sample_artist': 'Frankie Goes to Hollywood'}, {'key': 'syb van der ploeg|||zo gaat het leven aan je voor', 'revenue': 4881.42, 'sample_title': '006-Zo gaat het leven aan je voor', 'sample_artist': 'Syb van der Ploeg'}, {'key': 'fausto papetti|||lovers', 'revenue': 4770.54, 'sample_title': 'Lovers', 'sample_artist': 'Fausto Papetti'}, {'key': 'the turtles|||happy together', 'revenue': 4747.049999999999, 'sample_title': 'The Turtles - Happy Together', 'sample_artist': 'None'}, {'key': 'lemon d|||jah love vip remix', 'revenue': 4645.110000000001, 'sample_title': 'Lemon D - Jah Love (VIP Remix)', 'sample_artist': 'None'}], 'var_function-call-3713187450884790204': [{'match_key': 'pras|||ghetto supastar that is what you are', 'total_revenue': 4933.98}, {'match_key': 'pras|||ghetto supastar that is whatt you are', 'total_revenue': 580.59}, {'match_key': 'frankie goes to hollywood|||orgasm discussion', 'total_revenue': 1680.89}, {'match_key': 'frankie goes to hollywood|||the power of love rob searle club mix', 'total_revenue': 4909.04}, {'match_key': 'frankie goes to hollywood|||two tribes', 'total_revenue': 599.3199999999999}, {'match_key': 'frankie goes to hollywood|||two tribes welcome to the pleasuredome', 'total_revenue': 509.0799999999999}, {'match_key': 'frankie goes to hollywood|||two tribess', 'total_revenue': 462.17}, {'match_key': 'the turtles|||happy together', 'total_revenue': 4747.049999999999}, {'match_key': 'turtles|||happy together sixties', 'total_revenue': 435.69}, {'match_key': 'the turtles|||happy together', 'total_revenue': 4747.049999999999}, {'match_key': 'turtles|||happy together sixties', 'total_revenue': 435.69}, {'match_key': 'pras|||ghetto supastar that is what you are', 'total_revenue': 4933.98}, {'match_key': 'pras|||ghetto supastar that is whatt you are', 'total_revenue': 580.59}, {'match_key': 'frankie goes to hollywood|||the power of love rob searle club mix', 'total_revenue': 4909.04}, {'match_key': 'jennifer rush|||the power of love', 'total_revenue': 674.88}, {'match_key': 'jennifer rush|||the power of love simply the best ballads', 'total_revenue': 1184.99}, {'match_key': 'nicola|||power of love', 'total_revenue': 880.9599999999999}, {'match_key': 'phil collins|||against all odds the power of love', 'total_revenue': 1176.71}, {'match_key': 'rich matteson|||groovey', 'total_revenue': 5668.5}, {'match_key': 'grooveyard|||gator whale', 'total_revenue': 294.01}, {'match_key': 'rich matteson|||groovey', 'total_revenue': 5668.5}]}

exec(code, env_args)
