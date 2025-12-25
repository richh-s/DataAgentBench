code = """import pandas as pd
import json
import re
import string

with open(locals()['var_function-call-712639782687319237'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-712639782687319000'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

def clean_row(row):
    title = str(row['title'])
    artist = str(row['artist'])
    if artist.lower() in ['none', 'nan', ''] or artist == '[unknown]':
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist = parts[0]
            title = parts[1]
    title = re.sub(r'^\d+-\s*', '', title)
    t_norm = title.lower().strip().translate(str.maketrans('', '', string.punctuation))
    a_norm = artist.lower().strip().translate(str.maketrans('', '', string.punctuation))
    return pd.Series([t_norm, a_norm, title, artist])

cleaned = df.apply(clean_row, axis=1)
cleaned.columns = ['title_norm', 'artist_norm', 'clean_title', 'clean_artist']
df_final = pd.concat([df, cleaned], axis=1)

ghetto_mask = df_final['title_norm'].str.contains('ghetto', na=False)
happy_mask = df_final['title_norm'].str.contains('happy together', na=False)

res = {
    "ghetto": df_final[ghetto_mask][['clean_title', 'clean_artist', 'total_revenue']].to_dict(orient='records'),
    "happy": df_final[happy_mask][['clean_title', 'clean_artist', 'total_revenue']].to_dict(orient='records')
}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-712639782687319237': 'file_storage/function-call-712639782687319237.json', 'var_function-call-712639782687319000': 'file_storage/function-call-712639782687319000.json', 'var_function-call-5270781572036163336': [{'title_norm': 'none', 'artist_norm': 'none', 'total_revenue': 14647.52}, {'title_norm': '010-', 'artist_norm': 'none', 'total_revenue': 4163.48}, {'title_norm': 'groovey', 'artist_norm': 'rich matteson', 'total_revenue': 4128.59}, {'title_norm': 'the fire still burns', 'artist_norm': 'russ ballard', 'total_revenue': 3807.4}, {'title_norm': 'vostok', 'artist_norm': 'craig padilla', 'total_revenue': 3767.95}, {'title_norm': '001-', 'artist_norm': 'none', 'total_revenue': 3742.44}, {'title_norm': '003-', 'artist_norm': 'none', 'total_revenue': 3446.78}, {'title_norm': '003-', 'artist_norm': '', 'total_revenue': 3394.4}, {'title_norm': '005-', 'artist_norm': 'none', 'total_revenue': 3347.89}, {'title_norm': '002-', 'artist_norm': 'none', 'total_revenue': 3343.61}], 'var_function-call-11273542440502140139': [{'title_norm': 'groovey', 'artist_norm': 'rich matteson', 'total_revenue': 4128.59}, {'title_norm': 'the fire still burns', 'artist_norm': 'russ ballard', 'total_revenue': 3807.4}, {'title_norm': 'vostok', 'artist_norm': 'craig padilla', 'total_revenue': 3767.95}, {'title_norm': 'all my friends say album version', 'artist_norm': 'luke bryan', 'total_revenue': 3241.21}, {'title_norm': 'beautiful instrumental', 'artist_norm': 'damian marley', 'total_revenue': 3228.62}, {'title_norm': 'private soul security', 'artist_norm': 'down below', 'total_revenue': 3218.63}, {'title_norm': 'unknown', 'artist_norm': 'none', 'total_revenue': 3218.35}, {'title_norm': 'bring back the love spaced out dub', 'artist_norm': 'laura harris', 'total_revenue': 3171.7}, {'title_norm': 'chi to rome broke one edit', 'artist_norm': 'lazy ants  rob threezy', 'total_revenue': 3091.77}, {'title_norm': 'bad hearts', 'artist_norm': 'tights', 'total_revenue': 3052.75}], 'var_function-call-5796698080928854843': {'groovey_matches': [{'title': '006-Groovey', 'artist': 'Rich Matteson', 'total_revenue': 251.16}, {'title': 'Rich Matteson - Groovey', 'artist': 'None', 'total_revenue': 1288.75}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 949.82}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 2142.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 1036.29}], 'russ_matches': [{'title': 'Come on and Get It - Nothing but Good: 1952-1962', 'artist': 'Hank Ballard and The Midnighters', 'total_revenue': 507.27}, {'title': '015-Come on and Get It', 'artist': 'Hank Ballard and The Midnighters', 'total_revenue': 814.92}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'total_revenue': 1815.43}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'total_revenue': 1991.97}, {'title': '008-The Fire Still Burns', 'artist': 'Russ Ballard', 'total_revenue': 295.05}]}, 'var_function-call-8347770475251035569': {'title': '', 'artist': 'None', 'revenue': 39995.87, 'debug_top_5': [{'title_norm': '', 'artist_norm': 'none', 'total_revenue': 39995.87}, {'title_norm': '', 'artist_norm': '', 'total_revenue': 20898.67}, {'title_norm': 'none', 'artist_norm': 'none', 'total_revenue': 14647.52}, {'title_norm': 'groovey', 'artist_norm': 'rich matteson', 'total_revenue': 5668.5}, {'title_norm': 'all my friends say album version', 'artist_norm': 'luke bryan', 'total_revenue': 5180.93}]}}

exec(code, env_args)
