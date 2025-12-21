code = """import json
import pandas as pd
import re

# Load data using the file paths from variables
# Accessing variables with hyphens via locals()
sales_file_path = locals()['var_function-call-17703763520691558553']
tracks_file_path = locals()['var_function-call-17703763520691559746']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
if df_sales.empty:
    print("__RESULT__:")
    print(json.dumps([]))
    exit()

df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

def normalize(s):
    if not isinstance(s, str):
        return ""
    return re.sub(r'[^a-z0-9]', '', s.lower())

def extract_artist_title(row):
    title = row.get('title')
    artist = row.get('artist')
    
    if title is None: title = ""
    if artist is None: artist = ""
    
    # Check for artist in title if artist is missing or placeholder
    if artist.lower() in ['none', '[unknown]', '', 'null'] or artist is None:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist_cand = parts[0]
            title_cand = parts[1]
            return artist_cand, title_cand
        return "", title
    
    return artist, title

cleaned_data = []
for _, row in df_tracks.iterrows():
    raw_artist, raw_title = extract_artist_title(row)
    norm_artist = normalize(raw_artist)
    norm_title = normalize(raw_title)
    
    key = norm_artist + "|" + norm_title
    
    cleaned_data.append({
        'track_id': row['track_id'],
        'original_title': row['title'],
        'original_artist': row['artist'],
        'norm_artist': norm_artist,
        'norm_title': norm_title,
        'merge_key': key
    })

df_clean = pd.DataFrame(cleaned_data)

df_merged = pd.merge(df_clean, df_sales, on='track_id', how='inner')

df_grouped = df_merged.groupby('merge_key').agg({
    'revenue_usd': 'sum',
    'original_title': 'first', 
    'original_artist': 'first'
}).reset_index()

df_sorted = df_grouped.sort_values('revenue_usd', ascending=False)
top_songs = df_sorted.head(10).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_songs))"""

env_args = {'var_function-call-17703763520691558553': 'file_storage/function-call-17703763520691558553.json', 'var_function-call-17703763520691559746': 'file_storage/function-call-17703763520691559746.json'}

exec(code, env_args)
