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
    if not artist and ' - ' in title:
        parts = title.split(' - ', 1)
        if not re.match(r'^\d+$', parts[0]) and not re.match(r'^\d+[\.-]$', parts[0]):
            possible_artist = parts[0].strip()
            possible_title = parts[1].strip()
            if len(possible_artist) > 1:
                artist = possible_artist
                title = possible_title
    title = re.sub(r'^\d+[\s\.\-]+', '', title)
    title = re.sub(r'\s*\(.*?\)', '', title)
    title = re.sub(r'\s*\[.*?\]', '', title)
    return pd.Series([title.strip(), artist.strip()])

df[['clean_title', 'clean_artist']] = df.apply(extract_info, axis=1)
df_valid = df[df['clean_title'].str.len() > 1].copy()

grouped = df_valid.groupby(['clean_title', 'clean_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

top_candidates = grouped.head(5)
result = {}
result['top_groups'] = top_candidates.to_dict(orient='records')

details_1 = df_valid[(df_valid['clean_title'] == 'emerge') & (df_valid['clean_artist'] == 'fischerspooner')]
result['details_1'] = details_1[['track_id', 'title', 'artist', 'total_revenue']].to_dict(orient='records')

details_2 = df_valid[(df_valid['clean_title'] == 'zo gaat het leven aan je voor') & (df_valid['clean_artist'] == 'syb van der ploeg')]
result['details_2'] = details_2[['track_id', 'title', 'artist', 'total_revenue']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4743792908613703522': 'file_storage/function-call-4743792908613703522.json', 'var_function-call-12334345703939438194': 'file_storage/function-call-12334345703939438194.json', 'var_function-call-3492472198412527286': [{'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}, {'norm_title': '010-', 'norm_artist': 'none', 'total_revenue': 4163.48}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': '001-', 'norm_artist': 'none', 'total_revenue': 3742.44}, {'norm_title': '003-', 'norm_artist': 'none', 'total_revenue': 3446.78}, {'norm_title': '003-', 'norm_artist': '', 'total_revenue': 3394.4}, {'norm_title': '005-', 'norm_artist': 'none', 'total_revenue': 3347.89}, {'norm_title': '002-', 'norm_artist': 'none', 'total_revenue': 3343.61}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'total_revenue': 3228.62}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63}, {'norm_title': 'unknown', 'norm_artist': 'none', 'total_revenue': 3218.35}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'total_revenue': 3171.7}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'total_revenue': 3052.75}, {'norm_title': 'al stewart - year of the cat', 'norm_artist': 'none', 'total_revenue': 3049.93}, {'norm_title': 'skin', 'norm_artist': 'westworld', 'total_revenue': 3008.01}, {'norm_title': 'christmas in my heart', 'norm_artist': 'candi staton', 'total_revenue': 2969.33}], 'var_function-call-11322175899281157860': [{'clean_title': 'emerge', 'clean_artist': 'fischerspooner', 'total_revenue': 6665.27}, {'clean_title': 'zo gaat het leven aan je voor', 'clean_artist': 'syb van der ploeg', 'total_revenue': 6636.1}, {'clean_title': 'vagga', 'clean_artist': 'ske', 'total_revenue': 6611.56}, {'clean_title': 'lovers', 'clean_artist': 'fausto papetti', 'total_revenue': 6259.3}, {'clean_title': 'ne veruj', 'clean_artist': 'vrisak generacije', 'total_revenue': 6125.34}, {'clean_title': 'chile', 'clean_artist': 'neil biggin', 'total_revenue': 6008.71}, {'clean_title': 'travel', 'clean_artist': 'guts pie earshot', 'total_revenue': 5825.26}, {'clean_title': 'lookin boy', 'clean_artist': 'hotstylz', 'total_revenue': 5712.89}, {'clean_title': 'groovey', 'clean_artist': 'rich matteson', 'total_revenue': 5668.5}, {'clean_title': 'ghetto supastar', 'clean_artist': 'pras', 'total_revenue': 5514.57}, {'clean_title': 'to be free', 'clean_artist': 'mike oldfield', 'total_revenue': 5432.46}, {'clean_title': 'sex', 'clean_artist': 'berlin', 'total_revenue': 5420.8}, {'clean_title': 'truth', 'clean_artist': 'love amongst ruin', 'total_revenue': 5379.11}, {'clean_title': 'mother forest', 'clean_artist': 'wotan', 'total_revenue': 5277.67}, {'clean_title': 'faded', 'clean_artist': 'suzanne de bussac', 'total_revenue': 5251.56}, {'clean_title': 'let u go', 'clean_artist': 'atb', 'total_revenue': 5227.45}, {'clean_title': 'all my friends say', 'clean_artist': 'luke bryan', 'total_revenue': 5180.93}, {'clean_title': 'jah love', 'clean_artist': 'lemon d', 'total_revenue': 5168.45}, {'clean_title': 'sky', 'clean_artist': 'power of dreams', 'total_revenue': 5087.81}, {'clean_title': 'too beautiful', 'clean_artist': 'will kimbrough', 'total_revenue': 4996.46}]}

exec(code, env_args)
