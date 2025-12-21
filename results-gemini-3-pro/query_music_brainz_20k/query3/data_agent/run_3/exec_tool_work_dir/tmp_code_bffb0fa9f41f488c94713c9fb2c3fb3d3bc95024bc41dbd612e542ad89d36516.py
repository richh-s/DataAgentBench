code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-4743792908613703522'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-12334345703939438194'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_tracks, df_sales, on='track_id', how='left')
df['total_revenue'] = df['total_revenue'].fillna(0.0)

# Improved normalization
def clean_string(s):
    if not isinstance(s, str):
        return ""
    s = s.lower().strip()
    if s in ['none', 'unknown', '[unknown]', '']:
        return ""
    return s

def extract_info(row):
    title = clean_string(row['title'])
    artist = clean_string(row['artist'])
    
    # Heuristic: if artist is empty, check if title is "Artist - Title"
    if not artist and ' - ' in title:
        parts = title.split(' - ', 1)
        # Assume first part is artist if it looks like a name (not a track number)
        if not re.match(r'^\d+$', parts[0]) and not re.match(r'^\d+[\.-]$', parts[0]):
            possible_artist = parts[0].strip()
            possible_title = parts[1].strip()
            if len(possible_artist) > 1:
                artist = possible_artist
                title = possible_title

    # Remove track numbers from start of title e.g. "01 - Title", "001-Title"
    title = re.sub(r'^\d+[\s\.\-]+', '', title)
    
    # Remove metadata in brackets e.g. (live), (remix), [2011 remaster]
    # We replace with empty string
    title = re.sub(r'\s*\(.*?\)', '', title)
    title = re.sub(r'\s*\[.*?\]', '', title)
    
    return pd.Series([title.strip(), artist.strip()])

df[['clean_title', 'clean_artist']] = df.apply(extract_info, axis=1)

# Filter out invalid entries
# We need at least a title.
df_valid = df[df['clean_title'].str.len() > 1].copy()

# Group
grouped = df_valid.groupby(['clean_title', 'clean_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-4743792908613703522': 'file_storage/function-call-4743792908613703522.json', 'var_function-call-12334345703939438194': 'file_storage/function-call-12334345703939438194.json', 'var_function-call-3492472198412527286': [{'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}, {'norm_title': '010-', 'norm_artist': 'none', 'total_revenue': 4163.48}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': '001-', 'norm_artist': 'none', 'total_revenue': 3742.44}, {'norm_title': '003-', 'norm_artist': 'none', 'total_revenue': 3446.78}, {'norm_title': '003-', 'norm_artist': '', 'total_revenue': 3394.4}, {'norm_title': '005-', 'norm_artist': 'none', 'total_revenue': 3347.89}, {'norm_title': '002-', 'norm_artist': 'none', 'total_revenue': 3343.61}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'total_revenue': 3228.62}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63}, {'norm_title': 'unknown', 'norm_artist': 'none', 'total_revenue': 3218.35}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'total_revenue': 3171.7}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'total_revenue': 3052.75}, {'norm_title': 'al stewart - year of the cat', 'norm_artist': 'none', 'total_revenue': 3049.93}, {'norm_title': 'skin', 'norm_artist': 'westworld', 'total_revenue': 3008.01}, {'norm_title': 'christmas in my heart', 'norm_artist': 'candi staton', 'total_revenue': 2969.33}]}

exec(code, env_args)
