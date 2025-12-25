code = """import json
import pandas as pd
import re

# Load data
sales_path = locals()['var_function-call-571140759892803866']
with open(sales_path, 'r') as f:
    sales_data = json.load(f)
df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0)
df_sales['track_id'] = df_sales['track_id'].astype(str)

tracks_path = locals()['var_function-call-7555422285547670374']
with open(tracks_path, 'r') as f:
    tracks_data = json.load(f)
df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_track(row):
    title = str(row.get('title', ''))
    artist = str(row.get('artist', ''))
    
    # Check if artist is missing or placeholder
    artist_missing = artist in ['None', '[unknown]', 'nan', '']
    
    # Remove leading track numbers from title (e.g. "011-Title", "01. Title")
    # Pattern: start of string, one or more digits, followed by separator (-, .)
    title = re.sub(r'^\d+[-.]\s*', '', title)
    
    # Try to extract artist from title if missing
    if artist_missing and ' - ' in title:
        parts = title.split(' - ', 1)
        # Assuming "Artist - Title"
        artist_candidate = parts[0].strip()
        title_candidate = parts[1].strip()
        # Sanity check: if the split result looks reasonable (not too long, etc)
        # For now, just take it.
        artist = artist_candidate
        title = title_candidate
        
    # Clean text
    title_clean = title.strip().lower()
    artist_clean = artist.strip().lower()
    
    # Remove metadata in parens from title for grouping?
    # e.g. "(live)", "(remix)". But keep meaningful parts?
    # To be safe, let's keep it first, but maybe remove common suffixes if needed.
    # For entity resolution, usually we want to group "Song" and "Song (Live)" if asking for "Which song".
    # Let's try removing content in parens at the end.
    title_clean_core = re.sub(r'\s*\(.*\)$', '', title_clean)
    
    return pd.Series([title_clean, artist_clean, title_clean_core, title, artist])

cleaned = df.apply(clean_track, axis=1)
cleaned.columns = ['title_clean', 'artist_clean', 'title_clean_core', 'original_title', 'original_artist']

df_final = pd.concat([df, cleaned], axis=1)

# Group by core title and artist
# Using core title (without parens) to catch duplicates like "Song" and "Song (Live)"
group_cols = ['artist_clean', 'title_clean_core']
grouped = df_final.groupby(group_cols)['total_revenue'].sum().reset_index()

# Sort
top_songs = grouped.sort_values('total_revenue', ascending=False).head(10)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-571140759892803866': 'file_storage/function-call-571140759892803866.json', 'var_function-call-7555422285547670374': 'file_storage/function-call-7555422285547670374.json', 'var_function-call-7889678482353499176': 'file_storage/function-call-7889678482353499176.json'}

exec(code, env_args)
