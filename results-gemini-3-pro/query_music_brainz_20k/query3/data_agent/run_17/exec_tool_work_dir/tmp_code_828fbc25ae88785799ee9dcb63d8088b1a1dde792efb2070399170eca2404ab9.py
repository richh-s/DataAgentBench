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
    if artist.lower() in ['none', 'unknown', '[unknown]']:
        artist = ""
    if title.lower() in ['none', 'unknown', '[unknown]']:
        title = ""
    if not artist and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts[0]) < 50:
            artist = parts[0].strip()
            title = parts[1].strip()
    title = re.sub(r'^\d+[\s-]*', '', title)
    title_norm = title.lower().strip()
    artist_norm = artist.lower().strip()
    title_base = re.sub(r'\s*[\(\[].*?[\)\]]', '', title_norm).strip()
    if not title_base: title_base = title_norm
    return pd.Series([title_base, artist_norm, title, artist])

df[['norm_title', 'norm_artist', 'orig_title_clean', 'orig_artist_clean']] = df.apply(clean_entry, axis=1)

# Check top candidates details
candidates = [
    ('emerge', 'fischerspooner'),
    ('zo gaat het leven aan je voor', 'syb van der ploeg'),
    ('vagga', 'ske')
]

for t, a in candidates:
    print(f"--- {t} by {a} ---")
    subset = df[(df['norm_title'] == t) & (df['norm_artist'] == a)]
    print(subset[['track_id', 'title', 'artist', 'total_revenue']].to_string())"""

env_args = {'var_function-call-17358517250979617377': 'file_storage/function-call-17358517250979617377.json', 'var_function-call-17358517250979616604': 'file_storage/function-call-17358517250979616604.json', 'var_function-call-14405160276735663835': [{'clean_title': 'none', 'clean_artist': 'none', 'total_revenue': 14647.52}, {'clean_title': '010-', 'clean_artist': 'none', 'total_revenue': 4163.48}, {'clean_title': 'groovey', 'clean_artist': 'rich matteson', 'total_revenue': 4128.59}, {'clean_title': 'the fire still burns', 'clean_artist': 'russ ballard', 'total_revenue': 3807.4}, {'clean_title': 'vostok', 'clean_artist': 'craig padilla', 'total_revenue': 3767.95}, {'clean_title': '001-', 'clean_artist': 'none', 'total_revenue': 3742.44}, {'clean_title': '003-', 'clean_artist': 'none', 'total_revenue': 3446.78}, {'clean_title': '003-', 'clean_artist': '', 'total_revenue': 3394.4}, {'clean_title': '005-', 'clean_artist': 'none', 'total_revenue': 3347.89}, {'clean_title': '002-', 'clean_artist': 'none', 'total_revenue': 3343.61}, {'clean_title': 'all my friends say (album version)', 'clean_artist': 'luke bryan', 'total_revenue': 3241.21}, {'clean_title': 'beautiful (instrumental)', 'clean_artist': 'damian marley', 'total_revenue': 3228.62}, {'clean_title': 'private soul security', 'clean_artist': 'down below', 'total_revenue': 3218.63}, {'clean_title': 'unknown', 'clean_artist': 'none', 'total_revenue': 3218.35}, {'clean_title': 'bring back the love (spaced out dub)', 'clean_artist': 'laura harris', 'total_revenue': 3171.7}, {'clean_title': 'chi to rome (broke one edit)', 'clean_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}, {'clean_title': 'bad hearts', 'clean_artist': 'tights', 'total_revenue': 3052.75}, {'clean_title': 'al stewart - year of the cat', 'clean_artist': 'none', 'total_revenue': 3049.93}, {'clean_title': 'skin', 'clean_artist': 'westworld', 'total_revenue': 3008.01}, {'clean_title': 'christmas in my heart', 'clean_artist': 'candi staton', 'total_revenue': 2969.33}], 'var_function-call-10564647232742443246': [{'norm_title': 'emerge', 'norm_artist': 'fischerspooner', 'total_revenue': 6665.27}, {'norm_title': 'zo gaat het leven aan je voor', 'norm_artist': 'syb van der ploeg', 'total_revenue': 6636.1}, {'norm_title': 'vagga', 'norm_artist': 'ske', 'total_revenue': 6611.56}, {'norm_title': 'lovers', 'norm_artist': 'fausto papetti', 'total_revenue': 6259.3}, {'norm_title': 'ne veruj', 'norm_artist': 'vrisak generacije', 'total_revenue': 6125.34}, {'norm_title': 'chile', 'norm_artist': 'neil biggin', 'total_revenue': 6008.71}, {'norm_title': 'travel', 'norm_artist': 'guts pie earshot', 'total_revenue': 5825.26}, {'norm_title': 'lookin boy', 'norm_artist': 'hotstylz', 'total_revenue': 5712.89}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 5668.5}, {'norm_title': 'ghetto supastar', 'norm_artist': 'pras', 'total_revenue': 5514.57}, {'norm_title': 'to be free', 'norm_artist': 'mike oldfield', 'total_revenue': 5432.46}, {'norm_title': 'sex', 'norm_artist': 'berlin', 'total_revenue': 5420.8}, {'norm_title': 'truth', 'norm_artist': 'love amongst ruin', 'total_revenue': 5379.11}, {'norm_title': 'mother forest', 'norm_artist': 'wotan', 'total_revenue': 5277.67}, {'norm_title': 'faded', 'norm_artist': 'suzanne de bussac', 'total_revenue': 5251.56}, {'norm_title': 'let u go', 'norm_artist': 'atb', 'total_revenue': 5227.45}, {'norm_title': 'all my friends say', 'norm_artist': 'luke bryan', 'total_revenue': 5180.93}, {'norm_title': 'jah love', 'norm_artist': 'lemon d', 'total_revenue': 5168.45}, {'norm_title': 'sky', 'norm_artist': 'power of dreams', 'total_revenue': 5087.81}, {'norm_title': 'too beautiful', 'norm_artist': 'will kimbrough', 'total_revenue': 4996.46}]}

exec(code, env_args)
