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
    
    # Normalize null-like strings
    if title.lower() in ['none', 'null', 'nan', '']:
        title = ''
    if artist.lower() in ['none', 'null', 'nan', '[unknown]', '']:
        artist = ''

    # Remove leading track numbers from title
    # e.g. "011-Title", "01 Title", "01. Title"
    title_sub = re.sub(r'^\d+[-.\s]+', '', title)
    # If the substitution removed everything (e.g. title was "01"), revert or keep empty
    if not title_sub.strip():
        # It was just a number?
        pass
    else:
        title = title_sub

    # Try to extract artist from title if artist is missing
    if not artist and ' - ' in title:
        parts = title.split(' - ', 1)
        artist_cand = parts[0].strip()
        title_cand = parts[1].strip()
        if artist_cand and title_cand:
            artist = artist_cand
            title = title_cand
    
    # Lowercase and strip
    title_clean = title.strip().lower()
    artist_clean = artist.strip().lower()
    
    # Core title: remove text in parentheses/brackets
    # e.g. "song (live)" -> "song"
    title_clean_core = re.sub(r'\s*[\(\[].*?[\)\]]', '', title_clean).strip()
    
    return pd.Series([artist_clean, title_clean_core, title, artist])

cleaned = df.apply(clean_track, axis=1)
cleaned.columns = ['artist_clean', 'title_clean_core', 'original_title', 'original_artist']

df_final = pd.concat([df, cleaned], axis=1)

# Filter out garbage
# Title must be present
mask = (df_final['title_clean_core'] != '') & (df_final['title_clean_core'] != 'none')
df_filtered = df_final[mask]

# Group
grouped = df_filtered.groupby(['artist_clean', 'title_clean_core'])['total_revenue'].sum().reset_index()

# Sort
top_songs = grouped.sort_values('total_revenue', ascending=False).head(20)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-571140759892803866': 'file_storage/function-call-571140759892803866.json', 'var_function-call-7555422285547670374': 'file_storage/function-call-7555422285547670374.json', 'var_function-call-7889678482353499176': 'file_storage/function-call-7889678482353499176.json', 'var_function-call-18009921770386681425': [{'artist_clean': 'none', 'title_clean_core': '', 'total_revenue': 41667.5}, {'artist_clean': '', 'title_clean_core': '', 'total_revenue': 19264.52}, {'artist_clean': 'none', 'title_clean_core': 'none', 'total_revenue': 14647.52}, {'artist_clean': 'fischerspooner', 'title_clean_core': 'emerge', 'total_revenue': 6665.27}, {'artist_clean': 'syb van der ploeg', 'title_clean_core': 'zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'artist_clean': 'ske', 'title_clean_core': 'vagga', 'total_revenue': 6611.56}, {'artist_clean': 'fausto papetti', 'title_clean_core': 'lovers', 'total_revenue': 6259.3}, {'artist_clean': 'vrisak generacije', 'title_clean_core': 'ne veruj', 'total_revenue': 6125.34}, {'artist_clean': 'neil biggin', 'title_clean_core': 'chile', 'total_revenue': 6008.71}, {'artist_clean': 'guts pie earshot', 'title_clean_core': 'travel', 'total_revenue': 5825.26}]}

exec(code, env_args)
