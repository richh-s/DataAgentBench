code = """import json
import pandas as pd

with open(locals()['var_function-call-3835480464136415484'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6188791716186405650'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Re-apply cleaning to reproduce the key '004|||'
# Logic: artist=' ', title='004- '
# normalize_text(' ') -> '' -> artist="unknown" (Wait, my logic sets invalid to unknown)
# If artist="unknown" and title="004", key="unknown|||004"
# But result was "004|||" -> implies artist="004", title=""
# This happens if title="004- ". split('-') -> p1="004", p2=" ".
# Artist="004", Title=" ".
# So I want tracks where title starts with "004-" and artist is empty/none.

def is_suspicious(row):
    t = str(row['title'])
    a = str(row['artist'])
    if (a.lower() in ['none', 'unknown', '', ' ']) and t.startswith('004-'):
        return True
    return False

suspicious_tracks = df_tracks[df_tracks.apply(is_suspicious, axis=1)]
ids = suspicious_tracks['track_id'].tolist()
print("__RESULT__:")
print(json.dumps(suspicious_tracks[['track_id', 'title', 'artist', 'album']].head(10).to_dict(orient='records')))"""

env_args = {'var_function-call-3835480464136415484': 'file_storage/function-call-3835480464136415484.json', 'var_function-call-6188791716186405650': 'file_storage/function-call-6188791716186405650.json', 'var_function-call-8554056373783831330': {'top_song_key': 'unknown|', 'revenue': 207955.01, 'sample_title': '妥協', 'sample_artist': '蔡依林', 'top_5': [{'match_key': 'unknown|', 'total_revenue': 207955.01}, {'match_key': 'unknown|none', 'total_revenue': 17150.55}, {'match_key': '004|', 'total_revenue': 7249.700000000001}, {'match_key': '003|', 'total_revenue': 7090.13}, {'match_key': 'richmatteson|groovey', 'total_revenue': 5417.34}]}, 'var_function-call-16098740597880241896': [{'key': 'unknown|||none', 'revenue': 14647.52, 'title': 'None', 'artist': 'None'}, {'key': '004|||', 'revenue': 7249.700000000001, 'title': '004- ', 'artist': ' '}, {'key': '003|||', 'revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'key': 'rich matteson|||groovey', 'revenue': 5417.34, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'key': '005|||', 'revenue': 5222.0, 'title': '005-', 'artist': 'None'}, {'key': '009|||', 'revenue': 5045.7, 'title': '009-   ', 'artist': 'None'}, {'key': '010|||', 'revenue': 4734.360000000001, 'title': '010-', 'artist': 'None'}, {'key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer heilig vuur', 'revenue': 4132.27, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg'}, {'key': '002|||', 'revenue': 4119.89, 'title': '002-', 'artist': ' '}, {'key': 'luke bryan|||all my friends say album version', 'revenue': 4110.55, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}], 'var_function-call-7264091150168437329': [{'key': '004|||', 'revenue': 7249.700000000001, 'title': '004- ', 'artist': ' '}, {'key': '003|||', 'revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'key': 'rich matteson|||groovey', 'revenue': 5417.34, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'key': '005|||', 'revenue': 5222.0, 'title': '005-', 'artist': 'None'}, {'key': '009|||', 'revenue': 5045.7, 'title': '009-   ', 'artist': 'None'}, {'key': '010|||', 'revenue': 4734.360000000001, 'title': '010-', 'artist': 'None'}, {'key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer heilig vuur', 'revenue': 4132.27, 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg'}, {'key': '002|||', 'revenue': 4119.89, 'title': '002-', 'artist': ' '}, {'key': 'luke bryan|||all my friends say album version', 'revenue': 4110.55, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}, {'key': 'kerstin gier|||kapitel 01', 'revenue': 4091.12, 'title': 'Kapitel 01', 'artist': 'Kerstin Gier'}, {'key': 'damian marley|||beautiful instrumental', 'revenue': 4004.42, 'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley'}, {'key': 'matthew barber|||the story of your life', 'revenue': 3962.97, 'title': 'Matthew Barber - The Story of Your Life', 'artist': 'None'}, {'key': '006|||', 'revenue': 3946.7799999999997, 'title': '006- ', 'artist': ' '}, {'key': 'candido|||thousand finger man salsoul 30th', 'revenue': 3934.83, 'title': 'Thousand Finger Man - Salsoul 30th', 'artist': 'Candido'}, {'key': 'sir william gilbert sir arthur sullivan|||a wandring minstrel i from the mikado', 'revenue': 3877.43, 'title': 'Sir William Gilbert & Sir Arthur Sullivan - A Wand\'ring Minstrel I, From "The Mikado"', 'artist': 'None'}, {'key': 'ugly winner|||fret one grow old inside your wave', 'revenue': 3844.09, 'title': 'Fret One (Grow Old) (Inside Your Wave)', 'artist': 'Ugly Winner'}, {'key': 'russ ballard|||the fire still burns', 'revenue': 3807.4, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'key': 'craig padilla|||vostok', 'revenue': 3767.95, 'title': 'Vostok', 'artist': 'Craig Padilla'}, {'key': 'byzantine|||oblivion beckons', 'revenue': 3759.01, 'title': 'Byzantine - Oblivion Beckons', 'artist': 'None'}, {'key': '放課後ティータイム|||キーボードイントロダクション tvアニメけいおんオフィシャル バンドやろーよ バンドスコア付', 'revenue': 3758.99, 'title': 'キーボード・イントロダクション (TVアニメ「けいおん!」オフィシャル バンドやろーよ!! (バンドスコア付))', 'artist': '放課後ティータイム'}], 'var_function-call-14812217205519143356': [{'match_key': 'rich matteson|||006groovey', 'total_revenue': 251.16}, {'match_key': 'rich matteson|||groovey', 'total_revenue': 5417.34}, {'match_key': 'luke bryan|||002all my friends say album version', 'total_revenue': 1070.38}, {'match_key': 'luke bryan|||all my friends say album version', 'total_revenue': 4110.55}, {'match_key': 'syb van der ploeg|||006zo gaat het leven aan je voor', 'total_revenue': 1379.6699999999998}, {'match_key': 'syb van der ploeg|||zo gaat het leven aan je voor', 'total_revenue': 3501.75}, {'match_key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer heilig vuur', 'total_revenue': 4132.27}, {'match_key': 'bruno mars feat damian marley|||liquor store blues doowops hooligans', 'total_revenue': 845.96}, {'match_key': 'damian marley|||beautiful instrumental', 'total_revenue': 4004.42}, {'match_key': 'nas damian marley|||011patience', 'total_revenue': 97.35}, {'match_key': 'nas damian marley|||patience distant relatives', 'total_revenue': 2349.33}, {'match_key': 'kerstin gier|||kapitel 01', 'total_revenue': 4091.12}, {'match_key': 'kerstin gier|||kapitel 01 lügen die von herzen kommen feat narrator mirja bös', 'total_revenue': 492.78}, {'match_key': 'kerstin gier|||kapitel 35 lügen die von herzen kommen feat narrator mirja bös', 'total_revenue': 1437.87}, {'match_key': 'kerstin gier|||lugen die von herzen kommen feat narrator mirja bos 2008', 'total_revenue': 641.26}]}

exec(code, env_args)
