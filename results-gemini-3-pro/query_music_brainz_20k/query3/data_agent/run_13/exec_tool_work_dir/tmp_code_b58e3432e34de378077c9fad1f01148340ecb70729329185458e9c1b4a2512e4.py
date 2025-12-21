code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-7603886357055213310'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-3062453601885258613'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Join
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Fill NA
df_merged['title'] = df_merged['title'].fillna('None').astype(str)
df_merged['artist'] = df_merged['artist'].fillna('None').astype(str)

def clean_record(row):
    title = row['title'].strip()
    artist = row['artist'].strip()
    
    # Lowercase for comparison
    title_lower = title.lower()
    artist_lower = artist.lower()
    
    # Clean Title prefixes
    title_cleaned = re.sub(r'^\d+[-\s]+', '', title)
    if not title_cleaned.strip(): 
        title_cleaned = title
    
    # Handle Artist = None
    bad_artists = ['none', 'unknown', 'n/a', 'n.a.', '', '[unknown]']
    
    final_artist = artist
    final_title = title_cleaned
    
    if artist_lower in bad_artists:
        if ' - ' in title_cleaned:
            parts = title_cleaned.split(' - ', 1)
            final_artist = parts[0]
            final_title = parts[1]
        else:
            final_artist = "Unknown"
            
    return pd.Series([final_title, final_artist])

df_merged[['clean_title', 'clean_artist']] = df_merged.apply(clean_record, axis=1)

# Normalize
df_merged['norm_title'] = df_merged['clean_title'].apply(lambda x: x.lower().strip())
df_merged['norm_artist'] = df_merged['clean_artist'].apply(lambda x: x.lower().strip())

# Filter valid titles: must contain at least one letter
def is_valid_title(s):
    if s in ['none', 'n.a.', 'unknown', '', 'null', 'track']:
        return False
    if not re.search('[a-z]', s): # must have at least one letter
        return False
    return True

df_valid = df_merged[df_merged['norm_title'].apply(is_valid_title)]

# Group
grouped = df_valid.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

top_5 = grouped.head(5)

result_list = []
for index, row in top_5.iterrows():
    # Find a representative
    original_rec = df_valid[
        (df_valid['norm_title'] == row['norm_title']) & 
        (df_valid['norm_artist'] == row['norm_artist'])
    ].iloc[0]
    
    result_list.append({
        'clean_title': original_rec['clean_title'],
        'clean_artist': original_rec['clean_artist'],
        'total_revenue': row['total_revenue']
    })

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-7603886357055213310': 'file_storage/function-call-7603886357055213310.json', 'var_function-call-3062453601885258613': 'file_storage/function-call-3062453601885258613.json', 'var_function-call-9915776680240783115': [{'title': 'None', 'artist': 'None', 'total_revenue': 14647.52}, {'title': '010-', 'artist': 'None', 'total_revenue': 4163.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 4128.59}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'total_revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'total_revenue': 3767.95}], 'var_function-call-11307769233160746123': [{'title': '010-', 'artist': 'None', 'total_revenue': 4163.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 4128.59}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'total_revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'total_revenue': 3767.95}, {'title': '001-', 'artist': 'None', 'total_revenue': 3742.4399999999996}], 'var_function-call-12878792246621240414': [{'track_id': '14719', 'title': 'Systemisch bled', 'artist': 'Stüngö', 'total_revenue': 2522.82}, {'track_id': '5124', 'title': "011-I'll Tell You", 'artist': 'The BGeau Brummels', 'total_revenue': 2503.1899999999996}, {'track_id': '1344', 'title': 'Life CycUles', 'artist': 'Chosen', 'total_revenue': 2500.72}, {'track_id': '6725', 'title': '005-Passion Flower', 'artist': 'The Heath Brothers', 'total_revenue': 2489.81}, {'track_id': '10377', 'title': 'Another Room - Null Hour', 'artist': 'Snken Seas', 'total_revenue': 2466.71}, {'track_id': '5050', 'title': "Chilliwack - Who's Winning", 'artist': 'None', 'total_revenue': 2466.3100000000004}, {'track_id': '6667', 'title': 'n.a.', 'artist': 'Ludwig van Beethoven', 'total_revenue': 2452.7000000000003}, {'track_id': '7245', 'title': 'Nem érdekel, ki énekel (Indul a boksz)', 'artist': 'Moby Dick', 'total_revenue': 2436.9700000000003}, {'track_id': '11641', 'title': 'So in Love With You', 'artist': 'Kenny Rogers', 'total_revenue': 2428.2200000000003}, {'track_id': '964', 'title': 'Correct Spellings: Minor Sevenths - The Relative Pitch Ear Training SuperCourse - Level 3 - Lesson 18', 'artist': 'David Lucas Burge', 'total_revenue': 2425.61}, {'track_id': '12984', 'title': "The Goblin's Trail - Tales Fom a Forgotten World", 'artist': 'Tempus Fugit', 'total_revenue': 2401.71}, {'track_id': '6208', 'title': 'World Down Under (Helloween, Part 2: The Rise of Satan)', 'artist': 'II Tone feat. Satan, Big Cheese, $lim Money & Mac Montese', 'total_revenue': 2385.0299999999997}, {'track_id': '666', 'title': 'Emblem G - G of the Planets - Original Soundtrack', 'artist': 'Hoyt S. Curtin', 'total_revenue': 2382.74}, {'track_id': '12620', 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'total_revenue': 2377.59}, {'track_id': '19232', 'title': 'Misfortunes - From Horizon to Horizon: Singles 1983-92', 'artist': 'And Also The Trees', 'total_revenue': 2368.7499999999995}, {'track_id': '17757', 'title': '008-FanFanFanatic', 'artist': 'Rheingold', 'total_revenue': 2365.59}, {'track_id': '3462', 'title': 'Word (15 second) - Electronica', 'artist': 'Thomas Foyer', 'total_revenue': 2359.23}, {'track_id': '9639', 'title': 'Traces of Paganea', 'artist': 'Furious', 'total_revenue': 2351.68}, {'track_id': '18760', 'title': 'Patience - Distant Relatives', 'artist': 'Nas & Damian Marley', 'total_revenue': 2349.33}, {'track_id': '2516', 'title': '006-Osm', 'artist': 'Ourson', 'total_revenue': 2346.18}], 'var_function-call-9850685959955189276': [{'clean_title': '003-', 'clean_artist': 'Unknown', 'original_title': '003-', 'original_artist': 'None', 'total_revenue': 7979.77}, {'clean_title': 'Groovey', 'clean_artist': 'Rich Matteson', 'original_title': 'Groovey', 'original_artist': 'Rich Matteson', 'total_revenue': 5668.5}, {'clean_title': '005-', 'clean_artist': 'Unknown', 'original_title': '005-', 'original_artist': 'None', 'total_revenue': 5222.0}, {'clean_title': 'All My Friends Say (album version)', 'clean_artist': 'Luke Bryan', 'original_title': 'All My Friends Say (album version)', 'original_artist': 'Luke Bryan', 'total_revenue': 5180.93}, {'clean_title': '009-', 'clean_artist': 'Unknown', 'original_title': '009-  ', 'original_artist': ' ', 'total_revenue': 5045.700000000001}]}

exec(code, env_args)
