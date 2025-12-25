code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-8306236312507333947'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8306236312507331086'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['revenue'] = pd.to_numeric(df_sales['revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

merged = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

def clean_title(title):
    if not title: return ""
    title = str(title).lower()
    title = re.sub(r'\s*[\(\[].*?[\)\]]', '', title)
    return title.strip()

def normalize_row(row):
    title = row['title']
    artist = row['artist']
    if title is None: title = ""
    if artist is None: artist = ""
    if str(artist).lower() in ['none', '', 'unknown', '[unknown]'] and ' - ' in str(title):
        parts = str(title).split(' - ', 1)
        artist = parts[0]
        title = parts[1]
    clean_t = clean_title(title)
    clean_a = str(artist).lower().strip()
    return pd.Series([clean_a, clean_t])

merged[['norm_artist', 'norm_title']] = merged.apply(normalize_row, axis=1)

# Inspect Groovey
groovey_rows = merged[(merged['norm_artist'] == 'rich matteson') & (merged['norm_title'] == 'groovey')]
print("__RESULT__:")
print("GROOVEY ROWS:")
print(groovey_rows[['title', 'artist', 'album', 'revenue']].to_json(orient='records'))

# Inspect Zo gaat...
zo_rows = merged[(merged['norm_artist'] == 'syb van der ploeg') & (merged['norm_title'] == 'zo gaat het leven aan je voor')]
print("ZO ROWS:")
print(zo_rows[['title', 'artist', 'album', 'revenue']].to_json(orient='records'))"""

env_args = {'var_function-call-7702967746608488128': ['tracks'], 'var_function-call-7702967746608485357': ['sales'], 'var_function-call-8306236312507333947': 'file_storage/function-call-8306236312507333947.json', 'var_function-call-8306236312507331086': 'file_storage/function-call-8306236312507331086.json', 'var_function-call-6625596137426329529': {'title': 'None', 'artist': 'None', 'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}, 'var_function-call-18314145224782860741': [{'title': 'Groovey', 'artist': 'Rich Matteson', 'inferred_artist': 'rich matteson', 'inferred_title': 'groovey', 'total_revenue': 5417.34}, {'title': '010-', 'artist': 'None', 'inferred_artist': 'none', 'inferred_title': '010-', 'total_revenue': 4163.48}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'inferred_artist': 'luke bryan', 'inferred_title': 'all my friends say (album version)', 'total_revenue': 4110.55}, {'title': 'Kapitel 01', 'artist': 'Kerstin Gier', 'inferred_artist': 'kerstin gier', 'inferred_title': 'kapitel 01', 'total_revenue': 4091.12}, {'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'inferred_artist': 'damian marley', 'inferred_title': 'beautiful (instrumental)', 'total_revenue': 4004.42}], 'var_function-call-13059951677184271040': [{'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'revenue': 5417.34}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue': 5256.43}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'revenue': 4981.38}, {'norm_artist': 'none', 'norm_title': '001-', 'revenue': 4927.17}, {'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'revenue': 4896.24}, {'norm_artist': 'hans zimmer', 'norm_title': 'best friends', 'revenue': 4806.24}, {'norm_artist': 'none', 'norm_title': '003-', 'revenue': 4773.37}, {'norm_artist': 'vrisak generacije', 'norm_title': 'ne veruj', 'revenue': 4693.26}, {'norm_artist': '服部隆之', 'norm_title': 'lifework', 'revenue': 4663.91}, {'norm_artist': 'guts pie earshot', 'norm_title': 'travel', 'revenue': 4595.34}]}

exec(code, env_args)
