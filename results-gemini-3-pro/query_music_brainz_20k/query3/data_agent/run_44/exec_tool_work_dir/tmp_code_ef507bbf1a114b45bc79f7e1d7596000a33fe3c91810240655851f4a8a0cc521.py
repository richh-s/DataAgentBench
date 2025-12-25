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

def normalize(s):
    if s is None: return ""
    s = str(s).lower().strip()
    # Remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    return s

df['title_norm'] = df['title'].apply(normalize)
df['artist_norm'] = df['artist'].apply(normalize)

# Filter garbage
df_clean = df[df['title_norm'] != 'none']
# Filter out titles that are just digits
df_clean = df_clean[~df_clean['title_norm'].str.match(r'^\d+$')]
df_clean = df_clean[df_clean['title_norm'] != '']

grouped = df_clean.groupby(['title_norm', 'artist_norm'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-712639782687319237': 'file_storage/function-call-712639782687319237.json', 'var_function-call-712639782687319000': 'file_storage/function-call-712639782687319000.json', 'var_function-call-5270781572036163336': [{'title_norm': 'none', 'artist_norm': 'none', 'total_revenue': 14647.52}, {'title_norm': '010-', 'artist_norm': 'none', 'total_revenue': 4163.48}, {'title_norm': 'groovey', 'artist_norm': 'rich matteson', 'total_revenue': 4128.59}, {'title_norm': 'the fire still burns', 'artist_norm': 'russ ballard', 'total_revenue': 3807.4}, {'title_norm': 'vostok', 'artist_norm': 'craig padilla', 'total_revenue': 3767.95}, {'title_norm': '001-', 'artist_norm': 'none', 'total_revenue': 3742.44}, {'title_norm': '003-', 'artist_norm': 'none', 'total_revenue': 3446.78}, {'title_norm': '003-', 'artist_norm': '', 'total_revenue': 3394.4}, {'title_norm': '005-', 'artist_norm': 'none', 'total_revenue': 3347.89}, {'title_norm': '002-', 'artist_norm': 'none', 'total_revenue': 3343.61}]}

exec(code, env_args)
