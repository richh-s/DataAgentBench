code = """import json
import pandas as pd
import re

# Load data
with open('var_function-call-17703763520691558553.json', 'r') as f:
    sales_data = json.load(f)
with open('var_function-call-17703763520691559746.json', 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Normalization function
def normalize(s):
    if not isinstance(s, str):
        return ""
    # Remove non-alphanumeric
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
        # specialized check for "ArtistTitle" concatenation? Hard without dictionary.
        # Track 42 example: "CharlyGarcíaNobombardeenBuenosAires" -> "None"
        # We will just treat the whole thing as title if we can't split.
        return "", title
    
    return artist, title

# Apply extraction
cleaned_data = []
for _, row in df_tracks.iterrows():
    raw_artist, raw_title = extract_artist_title(row)
    norm_artist = normalize(raw_artist)
    norm_title = normalize(raw_title)
    
    # Combined key
    # If artist is empty, we just use title. 
    # But for "Endless Love", we expect an artist.
    # We will use the normalized concatenation as the merge key.
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

# Join with sales
# sales has track_id
df_merged = pd.merge(df_clean, df_sales, on='track_id', how='inner')

# Aggregate revenue
df_grouped = df_merged.groupby('merge_key').agg({
    'revenue_usd': 'sum',
    'original_title': 'first', # just pick one for display
    'original_artist': 'first',
    'norm_artist': 'first',
    'norm_title': 'first'
}).reset_index()

# Sort
df_sorted = df_grouped.sort_values('revenue_usd', ascending=False)

# Get top result
top_song = df_sorted.iloc[0].to_dict()

print("__RESULT__:")
print(json.dumps(top_song))"""

env_args = {'var_function-call-17703763520691558553': 'file_storage/function-call-17703763520691558553.json', 'var_function-call-17703763520691559746': 'file_storage/function-call-17703763520691559746.json'}

exec(code, env_args)
