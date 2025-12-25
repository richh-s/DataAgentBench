code = """import json
import pandas as pd

# Load sales data
with open(locals()['var_function-call-18145844648055813096'], 'r') as f:
    sales_data = json.load(f)

# Load tracks data
with open(locals()['var_function-call-16557127791975595763'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_tracks['norm_title'] = df_tracks['title'].apply(lambda x: str(x).lower().strip() if x else "")
df_tracks['norm_artist'] = df_tracks['artist'].apply(lambda x: str(x).lower().strip() if x else "")

# Merge
merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Grouping
grouped = merged.groupby(['norm_title', 'norm_artist']).agg({
    'revenue_usd': 'sum',
    'album': lambda x: list(x.unique()),
    'title': lambda x: list(x.unique()),
    'artist': lambda x: list(x.unique())
}).reset_index()

grouped = grouped.sort_values('revenue_usd', ascending=False)

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-18145844648055813096': 'file_storage/function-call-18145844648055813096.json', 'var_function-call-16557127791975595763': 'file_storage/function-call-16557127791975595763.json', 'var_function-call-4354660084992028470': [{'norm_title': 'none', 'norm_artist': 'none', 'revenue_usd': 14647.52}, {'norm_title': '010-', 'norm_artist': 'none', 'revenue_usd': 4163.48}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue_usd': 4128.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'revenue_usd': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'revenue_usd': 3767.95}, {'norm_title': '001-', 'norm_artist': 'none', 'revenue_usd': 3742.44}, {'norm_title': '003-', 'norm_artist': 'none', 'revenue_usd': 3446.78}, {'norm_title': '003-', 'norm_artist': '', 'revenue_usd': 3394.4}, {'norm_title': '005-', 'norm_artist': 'none', 'revenue_usd': 3347.89}, {'norm_title': '002-', 'norm_artist': 'none', 'revenue_usd': 3343.61}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'revenue_usd': 3241.21}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'revenue_usd': 3228.62}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'revenue_usd': 3218.63}, {'norm_title': 'unknown', 'norm_artist': 'none', 'revenue_usd': 3218.35}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'revenue_usd': 3171.7}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'revenue_usd': 3091.77}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'revenue_usd': 3052.75}, {'norm_title': 'al stewart - year of the cat', 'norm_artist': 'none', 'revenue_usd': 3049.93}, {'norm_title': 'skin', 'norm_artist': 'westworld', 'revenue_usd': 3008.01}, {'norm_title': 'christmas in my heart', 'norm_artist': 'candi staton', 'revenue_usd': 2969.33}]}

exec(code, env_args)
