code = """import json
import pandas as pd
import re

sales_file_path = locals()['var_function-call-647087583900672662']
tracks_file_path = locals()['var_function-call-7759510096737382327']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_track_info_aggressive(row):
    title = str(row['title']) if row['title'] is not None else ""
    artist = str(row['artist']) if row['artist'] is not None else ""
    
    # Handle artist "None"
    if artist.lower() in ['none', 'unknown', '[unknown]', ''] and ' - ' in title:
        parts = title.split(' - ', 1)
        potential_artist = parts[0]
        potential_title = parts[1]
        if len(potential_artist) > 0 and len(potential_title) > 0:
            artist = potential_artist
            title = potential_title

    # Remove leading numbering
    title = re.sub(r'^\d+[\.\-\s]+', '', title)
    
    # Remove text in parentheses and brackets (e.g., (live), [remix])
    title = re.sub(r'\s*[\(\[].*?[\)\]]', '', title)
    
    # Clean up whitespace and lower case
    title = title.strip().lower()
    artist = artist.strip().lower()
    
    return pd.Series([title, artist])

df[['clean_title', 'clean_artist']] = df.apply(clean_track_info_aggressive, axis=1)

valid_df = df[
    (df['clean_title'] != "") & 
    (df['clean_title'] != "none") & 
    (df['clean_artist'] != "") & 
    (df['clean_artist'] != "none")
]

grouped = valid_df.groupby(['clean_title', 'clean_artist'])['total_revenue'].sum().reset_index()
top_songs = grouped.sort_values(by='total_revenue', ascending=False).head(5)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-647087583900672662': 'file_storage/function-call-647087583900672662.json', 'var_function-call-7759510096737382327': 'file_storage/function-call-7759510096737382327.json', 'var_function-call-16962190421532214928': [{'clean_title': '', 'clean_artist': 'none', 'total_revenue': 38736.14}, {'clean_title': '', 'clean_artist': '', 'total_revenue': 19324.28}, {'clean_title': 'none', 'clean_artist': 'none', 'total_revenue': 14647.52}, {'clean_title': 'groovey', 'clean_artist': 'rich matteson', 'total_revenue': 5668.5}, {'clean_title': 'all my friends say (album version)', 'clean_artist': 'luke bryan', 'total_revenue': 5180.93}, {'clean_title': 'ghetto supastar (that is what you are)', 'clean_artist': 'pras', 'total_revenue': 4933.98}, {'clean_title': 'the power of love (rob searle club mix)', 'clean_artist': 'frankie goes to hollywood', 'total_revenue': 4909.04}, {'clean_title': 'zo gaat het leven aan je voor', 'clean_artist': 'syb van der ploeg', 'total_revenue': 4881.42}, {'clean_title': 'lovers', 'clean_artist': 'fausto papetti', 'total_revenue': 4770.54}, {'clean_title': 'happy together', 'clean_artist': 'the turtles', 'total_revenue': 4747.05}, {'clean_title': 'jah love (vip remix)', 'clean_artist': 'lemon d', 'total_revenue': 4645.11}, {'clean_title': 'alona', 'clean_artist': 'madbones', 'total_revenue': 4615.9}, {'clean_title': 'passion flower', 'clean_artist': 'the heath brothers', 'total_revenue': 4533.34}, {'clean_title': 'letters: a short essay', 'clean_artist': 'echolyn', 'total_revenue': 4484.08}, {'clean_title': 'remedy (numan remix)', 'clean_artist': 'crookers feat. miike snow', 'total_revenue': 4482.8}, {'clean_title': 'something', 'clean_artist': 'lasgo', 'total_revenue': 4461.79}, {'clean_title': 'ne veruj', 'clean_artist': 'vrisak generacije', 'total_revenue': 4450.29}, {'clean_title': 'vagga', 'clean_artist': 'ske', 'total_revenue': 4447.87}, {'clean_title': 'call me mr tibbs (main title)', 'clean_artist': 'quincy jones', 'total_revenue': 4442.71}, {'clean_title': 'intruder alert', 'clean_artist': 'lupe fiasco', 'total_revenue': 4401.09}], 'var_function-call-5833101839576106743': {'top_songs': [{'clean_title': 'groovey', 'clean_artist': 'rich matteson', 'total_revenue': 5668.5}, {'clean_title': 'all my friends say (album version)', 'clean_artist': 'luke bryan', 'total_revenue': 5180.93}, {'clean_title': 'ghetto supastar (that is what you are)', 'clean_artist': 'pras', 'total_revenue': 4933.98}, {'clean_title': 'the power of love (rob searle club mix)', 'clean_artist': 'frankie goes to hollywood', 'total_revenue': 4909.04}, {'clean_title': 'zo gaat het leven aan je voor', 'clean_artist': 'syb van der ploeg', 'total_revenue': 4881.42}], 'top_song_constituents': [{'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 1036.29}, {'track_id': '7710', 'title': '006-Groovey', 'artist': 'Rich Matteson', 'total_revenue': 251.16}, {'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'total_revenue': 1288.75}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 949.82}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 2142.48}]}}

exec(code, env_args)
