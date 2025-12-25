code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-5570592498162877174'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-5570592498162876679'], 'r') as f:
    tracks_data = json.load(f)

# Create DataFrames
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert total_revenue to float
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0.0)

# Merge
# Ensure track_id is same type
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Entity Resolution Function
def resolve_song(row):
    artist_raw = str(row['artist']) if row['artist'] is not None else "none"
    title_raw = str(row['title']) if row['title'] is not None else ""
    
    # Basic normalization
    artist_norm = artist_raw.lower().strip()
    title_norm = title_raw.lower().strip()
    
    # Handle missing artist
    if artist_norm in ["none", "[unknown]", "unknown", "null", ""]:
        # Try to extract from title
        if " - " in title_norm:
            parts = title_norm.split(" - ", 1)
            artist_norm = parts[0].strip()
            title_norm = parts[1].strip()
        else:
            artist_norm = "unknown_artist"
            
    # Clean title
    # Remove (...) and [...]
    title_cleaned = re.sub(r'\(.*?\)', '', title_norm)
    title_cleaned = re.sub(r'\[.*?\]', '', title_cleaned)
    
    # Remove 'feat.' or 'ft.' and everything after
    title_cleaned = re.split(r'\bfeat\.|\bft\.', title_cleaned)[0]
    
    # If " - " remains in title (e.g. "Song - Remastered" or "Song - Live"), take first part
    # Be careful not to cut "Song - Subtitle" if it's part of the name, but usually for grouping "Song" is safer.
    # Given the previous logic (extracting artist), " - " usually separates metadata now.
    if " - " in title_cleaned:
        title_cleaned = title_cleaned.split(" - ")[0]
        
    return artist_norm.strip(), title_cleaned.strip()

# Apply resolution
resolved = merged.apply(resolve_song, axis=1)
merged['clean_artist'] = resolved.apply(lambda x: x[0])
merged['clean_title'] = resolved.apply(lambda x: x[1])

# Group by cleaned attributes
grouped = merged.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()

# Sort descending
top_songs = grouped.sort_values(by='total_revenue', ascending=False).head(10)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-5570592498162877174': 'file_storage/function-call-5570592498162877174.json', 'var_function-call-5570592498162876679': 'file_storage/function-call-5570592498162876679.json'}

exec(code, env_args)
