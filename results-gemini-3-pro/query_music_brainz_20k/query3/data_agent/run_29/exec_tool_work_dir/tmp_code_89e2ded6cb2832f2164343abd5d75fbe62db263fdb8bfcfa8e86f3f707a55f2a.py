code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-2517101731408743361'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6464260199203399189'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_string(s):
    if not isinstance(s, str):
        return ""
    # Remove "001-" prefix
    s = re.sub(r'^\d{2,3}-', '', s)
    # Remove text in parentheses/brackets
    s = re.sub(r'\s*\(.*?\)\s*', '', s)
    s = re.sub(r'\s*\[.*?\]\s*', '', s)
    return s.strip()

def clean_track(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    
    missing_vals = ['None', 'null', '[unknown]', '', 'nan', 'Unknown Artist']
    
    # Try splitting if artist is missing
    if artist in missing_vals:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist = parts[0].strip()
            title = parts[1].strip()
    
    # Clean both
    clean_t = clean_string(title)
    clean_a = clean_string(artist)
    
    # If cleaned title is empty (e.g. was just numbers or parens), keep original
    if not clean_t:
        clean_t = title
        
    # Consistency check: if clean_a is still empty/None, set to "Unknown"
    if clean_a in missing_vals or not clean_a:
        clean_a = "Unknown"
        
    return pd.Series([clean_t, clean_a])

merged[['clean_title', 'clean_artist']] = merged.apply(clean_track, axis=1)

grouped = merged.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values(by='total_revenue', ascending=False)

# Exclude Unknown artist if title is also vague, but usually we just want the top one
print("__RESULT__:")
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-9032484242444107887': ['sales'], 'var_function-call-9032484242444109838': ['tracks'], 'var_function-call-2517101731408743361': 'file_storage/function-call-2517101731408743361.json', 'var_function-call-5327854219375283823': [{'COUNT(*)': '19375'}], 'var_function-call-6464260199203399189': 'file_storage/function-call-6464260199203399189.json', 'var_function-call-6131387658296098835': [{'clean_artist': 'None', 'clean_title': 'None', 'total_revenue': 14647.52}, {'clean_artist': 'Rich Matteson', 'clean_title': 'Groovey', 'total_revenue': 5417.34}, {'clean_artist': 'None', 'clean_title': '010-', 'total_revenue': 4163.48}, {'clean_artist': 'Luke Bryan', 'clean_title': 'All My Friends Say (album version)', 'total_revenue': 4110.55}, {'clean_artist': 'Kerstin Gier', 'clean_title': 'Kapitel 01', 'total_revenue': 4091.12}, {'clean_artist': 'Damian Marley', 'clean_title': 'Beautiful (instrumental)', 'total_revenue': 4004.42}, {'clean_artist': 'Matthew Barber', 'clean_title': 'The Story of Your Life', 'total_revenue': 3962.97}, {'clean_artist': 'Sir William Gilbert & Sir Arthur Sullivan', 'clean_title': 'A Wand\'ring Minstrel I, From "The Mikado"', 'total_revenue': 3877.43}, {'clean_artist': 'Russ Ballard', 'clean_title': 'The Fire Still Burns', 'total_revenue': 3807.4}, {'clean_artist': 'Craig Padilla', 'clean_title': 'Vostok', 'total_revenue': 3767.95}], 'var_function-call-14644405490884938180': [{'clean_artist': 'Rich Matteson', 'clean_title': 'Groovey', 'total_revenue': 5417.34}, {'clean_artist': 'Syb van der Ploeg', 'clean_title': 'Zo gaat het leven aan je voor', 'total_revenue': 5256.43}, {'clean_artist': 'Ske', 'clean_title': 'Vagga', 'total_revenue': 4981.38}, {'clean_artist': 'None', 'clean_title': '001-', 'total_revenue': 4927.17}, {'clean_artist': 'Fischerspooner', 'clean_title': 'Emerge', 'total_revenue': 4896.24}, {'clean_artist': 'Hans Zimmer', 'clean_title': 'Best Friends', 'total_revenue': 4806.24}, {'clean_artist': 'None', 'clean_title': '003-', 'total_revenue': 4773.37}, {'clean_artist': 'Vrisak generacije', 'clean_title': 'Ne veruj', 'total_revenue': 4693.26}, {'clean_artist': '服部隆之', 'clean_title': 'Lifework', 'total_revenue': 4663.91}, {'clean_artist': 'Guts Pie Earshot', 'clean_title': 'Travel', 'total_revenue': 4595.34}, {'clean_artist': 'Tété', 'clean_title': 'Rotor', 'total_revenue': 4520.89}, {'clean_artist': 'Fausto Papetti', 'clean_title': 'Lovers', 'total_revenue': 4516.66}, {'clean_artist': 'Love Amongst Ruin', 'clean_title': 'Truth', 'total_revenue': 4491.11}, {'clean_artist': 'Neil Biggin', 'clean_title': 'Chile', 'total_revenue': 4456.97}, {'clean_artist': 'Forte Apache', 'clean_title': 'Colete', 'total_revenue': 4347.57}], 'var_function-call-3957616372872170677': [{'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers'}, {'track_id': '5050', 'title': "Chilliwack - Who's Winning", 'artist': 'None'}, {'track_id': '17757', 'title': '008-FanFanFanatic', 'artist': 'Rheingold'}, {'track_id': '2516', 'title': '006-Osm', 'artist': 'Ourson'}, {'track_id': '6326', 'title': 'Clara Ponty - The Paths to Wisdom', 'artist': 'None'}, {'track_id': '5836', 'title': '002-Karma', 'artist': 'The Waterboys'}, {'track_id': '10760', 'title': 'Eichenschild - Armer Sünder', 'artist': 'None'}, {'track_id': '9002', 'title': 'Gong - New Age Transformation Try: No More Sages', 'artist': 'None'}, {'track_id': '9649', 'title': '004-I Forgot That Love Existed', 'artist': 'Van Morrison'}, {'track_id': '10856', 'title': 'The Amenta - Mictlan', 'artist': 'None'}, {'track_id': '16084', 'title': '007-Cosmic Carousel (full mix)', 'artist': 'Blair Bootqh & Doug Boyle'}, {'track_id': '9652', 'title': 'Jim Norman/Grafite - Antares', 'artist': 'None'}, {'track_id': '3412', 'title': 'Fausto Papetti - Lovers', 'artist': 'None'}, {'track_id': '12207', 'title': 'SDMS - Un Deux Trois', 'artist': 'None'}, {'track_id': '2029', 'title': "Bunny Sigler - Girl Don't Make Me Wait", 'artist': 'None'}, {'track_id': '17669', 'title': "006-Don't Want Fight", 'artist': 'None'}, {'track_id': '12969', 'title': 'Dementia Simplex - Testicle Crack', 'artist': 'None'}, {'track_id': '17840', 'title': 'Metallica - Master of Puppets', 'artist': 'None'}, {'track_id': '17958', 'title': 'Wolfgang Amadeus Mozart - Concerto for Bassoon in B-flat major, K. 186e/191: III. Rondeau. Tempo di menuetto', 'artist': 'None'}, {'track_id': '4528', 'title': '008-iNkomo?', 'artist': 'Mafikizolo'}]}

exec(code, env_args)
