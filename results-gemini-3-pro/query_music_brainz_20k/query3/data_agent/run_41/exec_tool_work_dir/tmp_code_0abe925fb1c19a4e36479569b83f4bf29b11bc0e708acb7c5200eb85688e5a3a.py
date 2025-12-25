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
    # Remove text in parentheses or brackets
    title = re.sub(r'\s*[\(\[].*?[\)\]]', '', title)
    # Remove special chars
    # title = re.sub(r'[^\w\s]', '', title) # This might be too aggressive (e.g. "Don't" -> "Dont")
    return title.strip()

def normalize_row(row):
    title = row['title']
    artist = row['artist']
    
    if title is None: title = ""
    if artist is None: artist = ""
    
    # Handle "None" artist in title
    if str(artist).lower() in ['none', '', 'unknown', '[unknown]'] and ' - ' in str(title):
        parts = str(title).split(' - ', 1)
        artist = parts[0]
        title = parts[1]
    
    clean_t = clean_title(title)
    clean_a = str(artist).lower().strip()
    
    return pd.Series([clean_a, clean_t])

merged[['norm_artist', 'norm_title']] = merged.apply(normalize_row, axis=1)

# Filter garbage
merged = merged[~merged['norm_title'].isin(['none', '', 'null', '010-', 'track'])]
merged = merged[~merged['norm_title'].str.startswith('010-')]

# Group
grouped = merged.groupby(['norm_artist', 'norm_title'])['revenue'].sum().reset_index()

# Sort
top_songs = grouped.sort_values(by='revenue', ascending=False).head(10)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-7702967746608488128': ['tracks'], 'var_function-call-7702967746608485357': ['sales'], 'var_function-call-8306236312507333947': 'file_storage/function-call-8306236312507333947.json', 'var_function-call-8306236312507331086': 'file_storage/function-call-8306236312507331086.json', 'var_function-call-6625596137426329529': {'title': 'None', 'artist': 'None', 'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}, 'var_function-call-18314145224782860741': [{'title': 'Groovey', 'artist': 'Rich Matteson', 'inferred_artist': 'rich matteson', 'inferred_title': 'groovey', 'total_revenue': 5417.34}, {'title': '010-', 'artist': 'None', 'inferred_artist': 'none', 'inferred_title': '010-', 'total_revenue': 4163.48}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'inferred_artist': 'luke bryan', 'inferred_title': 'all my friends say (album version)', 'total_revenue': 4110.55}, {'title': 'Kapitel 01', 'artist': 'Kerstin Gier', 'inferred_artist': 'kerstin gier', 'inferred_title': 'kapitel 01', 'total_revenue': 4091.12}, {'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'inferred_artist': 'damian marley', 'inferred_title': 'beautiful (instrumental)', 'total_revenue': 4004.42}]}

exec(code, env_args)
