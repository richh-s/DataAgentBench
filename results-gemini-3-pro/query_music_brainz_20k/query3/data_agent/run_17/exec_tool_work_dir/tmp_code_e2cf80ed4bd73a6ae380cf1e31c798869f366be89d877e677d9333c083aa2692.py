code = """import pandas as pd
import json
import re

sales_file_path = locals()['var_function-call-17358517250979617377']
tracks_file_path = locals()['var_function-call-17358517250979616604']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_entry(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    
    # Handle "None" or "Unknown"
    if artist.lower() in ['none', 'unknown', '[unknown]']:
        artist = ""
    if title.lower() in ['none', 'unknown', '[unknown]']:
        title = ""
        
    # Try to split "Artist - Title" if artist is missing
    if not artist and ' - ' in title:
        parts = title.split(' - ', 1)
        potential_artist = parts[0].strip()
        potential_title = parts[1].strip()
        # Heuristic: if artist part is not too long/short
        if len(potential_artist) < 50:
            artist = potential_artist
            title = potential_title

    # Remove generic prefixes like "001-" if they don't look like part of the title
    # Regex: start with digits then hyphen or space
    title = re.sub(r'^\d+[\s-]*', '', title)
    
    # Clean text
    title = title.lower().strip()
    artist = artist.lower().strip()
    
    # Remove things in brackets for title normalization (simple version)
    # E.g. "song (live)" -> "song"
    title_base = re.sub(r'\s*[\(\[].*?[\)\]]', '', title).strip()
    
    return pd.Series([title_base if title_base else title, artist])

df[['norm_title', 'norm_artist']] = df.apply(clean_entry, axis=1)

# Filter out empty titles
df_clean = df[df['norm_title'] != ""]

# Group
grouped = df_clean.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print('__RESULT__:')
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-17358517250979617377': 'file_storage/function-call-17358517250979617377.json', 'var_function-call-17358517250979616604': 'file_storage/function-call-17358517250979616604.json', 'var_function-call-14405160276735663835': [{'clean_title': 'none', 'clean_artist': 'none', 'total_revenue': 14647.52}, {'clean_title': '010-', 'clean_artist': 'none', 'total_revenue': 4163.48}, {'clean_title': 'groovey', 'clean_artist': 'rich matteson', 'total_revenue': 4128.59}, {'clean_title': 'the fire still burns', 'clean_artist': 'russ ballard', 'total_revenue': 3807.4}, {'clean_title': 'vostok', 'clean_artist': 'craig padilla', 'total_revenue': 3767.95}, {'clean_title': '001-', 'clean_artist': 'none', 'total_revenue': 3742.44}, {'clean_title': '003-', 'clean_artist': 'none', 'total_revenue': 3446.78}, {'clean_title': '003-', 'clean_artist': '', 'total_revenue': 3394.4}, {'clean_title': '005-', 'clean_artist': 'none', 'total_revenue': 3347.89}, {'clean_title': '002-', 'clean_artist': 'none', 'total_revenue': 3343.61}, {'clean_title': 'all my friends say (album version)', 'clean_artist': 'luke bryan', 'total_revenue': 3241.21}, {'clean_title': 'beautiful (instrumental)', 'clean_artist': 'damian marley', 'total_revenue': 3228.62}, {'clean_title': 'private soul security', 'clean_artist': 'down below', 'total_revenue': 3218.63}, {'clean_title': 'unknown', 'clean_artist': 'none', 'total_revenue': 3218.35}, {'clean_title': 'bring back the love (spaced out dub)', 'clean_artist': 'laura harris', 'total_revenue': 3171.7}, {'clean_title': 'chi to rome (broke one edit)', 'clean_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}, {'clean_title': 'bad hearts', 'clean_artist': 'tights', 'total_revenue': 3052.75}, {'clean_title': 'al stewart - year of the cat', 'clean_artist': 'none', 'total_revenue': 3049.93}, {'clean_title': 'skin', 'clean_artist': 'westworld', 'total_revenue': 3008.01}, {'clean_title': 'christmas in my heart', 'clean_artist': 'candi staton', 'total_revenue': 2969.33}]}

exec(code, env_args)
