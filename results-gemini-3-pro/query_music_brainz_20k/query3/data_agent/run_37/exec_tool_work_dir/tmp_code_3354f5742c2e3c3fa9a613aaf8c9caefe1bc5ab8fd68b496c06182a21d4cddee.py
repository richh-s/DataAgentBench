code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-5828808762132496056'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8680221993785875883'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_string(s):
    if s is None:
        return ""
    return str(s).lower().strip()

def normalize_track(row):
    title = clean_string(row['title'])
    artist = clean_string(row['artist'])
    
    # Handle "None" or unknown artists
    if artist in ["none", "[unknown]", ""]:
        artist = ""
        # Try to extract artist from title if it looks like "Artist - Title"
        # But be careful about "Title - Subtitle"
        if " - " in title:
            parts = title.split(" - ", 1)
            # Heuristic: assume first part is artist if artist is missing
            artist_candidate = parts[0].strip()
            title_candidate = parts[1].strip()
            # if the first part is short and looks like a track number, ignore it
            if not re.match(r'^\d+$', artist_candidate):
                 artist = artist_candidate
                 title = title_candidate

    # Remove leading numbering from title (e.g. "01 - ", "001-", "1. ")
    title = re.sub(r'^\d+[\.\-]\s*', '', title)
    title = re.sub(r'^\d+\s+', '', title) # Leading numbers followed by space

    # Remove junk in parenthesis/brackets
    # Examples: "(live)", "(remix)", "(acoustic)", "[video]", "(2008 remaster)"
    # We want to keep the main song title.
    # However, sometimes essential info is in brackets. But for aggregation "Which song", we usually want the core song.
    title = re.sub(r'\(.*?\)', '', title)
    title = re.sub(r'\[.*?\]', '', title)
    
    # Remove text after " - " if it looks like extra info (e.g. " - Live at...")
    # But earlier we used " - " to split artist. Now we check for suffixes.
    if " - " in title:
        title = title.split(" - ")[0]

    # Final cleanup
    title = title.strip()
    artist = artist.strip()
    
    # Special fix for specific patterns if needed, but generic should work.
    
    return pd.Series([artist, title])

# Apply normalization
df[['norm_artist', 'norm_title']] = df.apply(normalize_track, axis=1)

# Group by normalized keys
df_grouped = df.groupby(['norm_artist', 'norm_title'])['revenue_usd'].sum().reset_index()

# Sort
df_sorted = df_grouped.sort_values(by='revenue_usd', ascending=False)

# Get top results
top_song = df_sorted.iloc[0]

print("__RESULT__:")
print(json.dumps({
    "top_song": {
        "artist": top_song['norm_artist'],
        "title": top_song['norm_title'],
        "total_revenue": top_song['revenue_usd']
    },
    "top_5": df_sorted.head(5).to_dict(orient='records')
}))"""

env_args = {'var_function-call-5828808762132496056': 'file_storage/function-call-5828808762132496056.json', 'var_function-call-8680221993785875883': 'file_storage/function-call-8680221993785875883.json'}

exec(code, env_args)
