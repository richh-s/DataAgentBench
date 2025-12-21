code = """import json
import pandas as pd

# Load data (re-loading to be safe, though locals persist)
with open(locals()['var_function-call-16438138636169770779'], 'r') as f:
    revenue_data = json.load(f)
with open(locals()['var_function-call-17040196689853941222'], 'r') as f:
    track_data = json.load(f)

df_revenue = pd.DataFrame(revenue_data)
df_tracks = pd.DataFrame(track_data)

df_revenue['track_id'] = df_revenue['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_revenue['total_revenue'] = pd.to_numeric(df_revenue['total_revenue'])

df = pd.merge(df_revenue, df_tracks, on='track_id', how='inner')

def normalize_string(s):
    if not s or s == 'None' or s == '[unknown]':
        return ''
    s = str(s).lower().strip()
    return s

df['norm_title'] = df['title'].apply(normalize_string)
df['norm_artist'] = df['artist'].apply(normalize_string)

grouped = df.groupby(['norm_title', 'norm_artist'])
result_list = []

for name, group in grouped:
    total_rev = group['total_revenue'].sum()
    # Get a sample of original titles/artists
    sample_titles = group['title'].unique().tolist()[:3]
    sample_artists = group['artist'].unique().tolist()[:3]
    result_list.append({
        "norm_title": name[0],
        "norm_artist": name[1],
        "total_revenue": total_rev,
        "original_titles": sample_titles,
        "original_artists": sample_artists
    })

df_res = pd.DataFrame(result_list).sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(df_res.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-16438138636169770779': 'file_storage/function-call-16438138636169770779.json', 'var_function-call-17040196689853941222': 'file_storage/function-call-17040196689853941222.json', 'var_function-call-2203332676551410598': [{'norm_title': '', 'norm_artist': '', 'total_revenue': 14647.52}, {'norm_title': '003-', 'norm_artist': '', 'total_revenue': 6841.18}, {'norm_title': '005-', 'norm_artist': '', 'total_revenue': 5222.0}, {'norm_title': '009-', 'norm_artist': '', 'total_revenue': 5045.7}, {'norm_title': '004-', 'norm_artist': '', 'total_revenue': 4868.47}, {'norm_title': '010-', 'norm_artist': '', 'total_revenue': 4734.36}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'norm_title': '002-', 'norm_artist': '', 'total_revenue': 4119.89}, {'norm_title': '006-', 'norm_artist': '', 'total_revenue': 3946.78}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': '001-', 'norm_artist': '', 'total_revenue': 3742.44}, {'norm_title': '012-', 'norm_artist': '', 'total_revenue': 3635.13}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'total_revenue': 3228.62}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63}, {'norm_title': 'unknown', 'norm_artist': '', 'total_revenue': 3218.35}, {'norm_title': '020-', 'norm_artist': '', 'total_revenue': 3202.16}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'total_revenue': 3171.7}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}]}

exec(code, env_args)
