code = """import pandas as pd
import json
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

def normalize(s):
    if s is None: return ""
    s = str(s).lower().strip()
    s = s.translate(str.maketrans('', '', string.punctuation))
    return s

df['title_norm'] = df['title'].apply(normalize)
df['artist_norm'] = df['artist'].apply(normalize)

groovey_mask = df['title_norm'].str.contains('groovey', na=False) | df['artist_norm'].str.contains('matteson', na=False)
russ_mask = df['title_norm'].str.contains('fire still burns', na=False) | df['artist_norm'].str.contains('ballard', na=False)

res = {
    "groovey_matches": json.loads(df[groovey_mask][['title', 'artist', 'total_revenue']].to_json(orient='records')),
    "russ_matches": json.loads(df[russ_mask][['title', 'artist', 'total_revenue']].to_json(orient='records'))
}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-712639782687319237': 'file_storage/function-call-712639782687319237.json', 'var_function-call-712639782687319000': 'file_storage/function-call-712639782687319000.json', 'var_function-call-5270781572036163336': [{'title_norm': 'none', 'artist_norm': 'none', 'total_revenue': 14647.52}, {'title_norm': '010-', 'artist_norm': 'none', 'total_revenue': 4163.48}, {'title_norm': 'groovey', 'artist_norm': 'rich matteson', 'total_revenue': 4128.59}, {'title_norm': 'the fire still burns', 'artist_norm': 'russ ballard', 'total_revenue': 3807.4}, {'title_norm': 'vostok', 'artist_norm': 'craig padilla', 'total_revenue': 3767.95}, {'title_norm': '001-', 'artist_norm': 'none', 'total_revenue': 3742.44}, {'title_norm': '003-', 'artist_norm': 'none', 'total_revenue': 3446.78}, {'title_norm': '003-', 'artist_norm': '', 'total_revenue': 3394.4}, {'title_norm': '005-', 'artist_norm': 'none', 'total_revenue': 3347.89}, {'title_norm': '002-', 'artist_norm': 'none', 'total_revenue': 3343.61}], 'var_function-call-11273542440502140139': [{'title_norm': 'groovey', 'artist_norm': 'rich matteson', 'total_revenue': 4128.59}, {'title_norm': 'the fire still burns', 'artist_norm': 'russ ballard', 'total_revenue': 3807.4}, {'title_norm': 'vostok', 'artist_norm': 'craig padilla', 'total_revenue': 3767.95}, {'title_norm': 'all my friends say album version', 'artist_norm': 'luke bryan', 'total_revenue': 3241.21}, {'title_norm': 'beautiful instrumental', 'artist_norm': 'damian marley', 'total_revenue': 3228.62}, {'title_norm': 'private soul security', 'artist_norm': 'down below', 'total_revenue': 3218.63}, {'title_norm': 'unknown', 'artist_norm': 'none', 'total_revenue': 3218.35}, {'title_norm': 'bring back the love spaced out dub', 'artist_norm': 'laura harris', 'total_revenue': 3171.7}, {'title_norm': 'chi to rome broke one edit', 'artist_norm': 'lazy ants  rob threezy', 'total_revenue': 3091.77}, {'title_norm': 'bad hearts', 'artist_norm': 'tights', 'total_revenue': 3052.75}]}

exec(code, env_args)
